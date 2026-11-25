from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Business, Event, EventBooking, Notice, Place, Service, ServiceBooking, ServiceSlot
from .serializers import (BusinessSerializer, EventBookingRequestSerializer, EventBookingSerializer,
                          EventSerializer, NoticeSerializer, PlaceSerializer, ServiceBookingRequestSerializer,
                          ServiceBookingSerializer, ServiceSerializer, SlotSerializer)

@api_view(["GET"])
@permission_classes([AllowAny])
def health(request):
    return Response({"status": "ok", "project": "City Main API", "city": "Kochi"})

@api_view(["GET"])
@permission_classes([AllowAny])
def places(request):
    qs = Place.objects.filter(is_published=True, city__slug="kochi").select_related("city")
    query = request.query_params.get("q", "").strip()
    category = request.query_params.get("category", "").strip()
    if query:
        qs = qs.filter(Q(name__icontains=query) | Q(description__icontains=query))
    if category:
        qs = qs.filter(category=category)
    return Response(PlaceSerializer(qs.order_by("name"), many=True).data)

@api_view(["GET"])
@permission_classes([AllowAny])
def businesses(request):
    qs = Business.objects.filter(is_published=True, is_approved=True, city__slug="kochi").select_related("city")
    category = request.query_params.get("category", "").strip()
    query = request.query_params.get("q", "").strip()
    if category:
        qs = qs.filter(category=category)
    if query:
        qs = qs.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return Response(BusinessSerializer(qs.order_by("name"), many=True).data)

@api_view(["GET"])
@permission_classes([AllowAny])
def events(request):
    qs = Event.objects.filter(is_published=True, city__slug="kochi", starts_at__gt=timezone.now()).select_related("city")
    return Response(EventSerializer(qs.order_by("starts_at"), many=True).data)

@api_view(["GET"])
@permission_classes([AllowAny])
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk, is_published=True, city__slug="kochi")
    return Response(EventSerializer(event).data)

@api_view(["GET"])
@permission_classes([AllowAny])
def services(request):
    qs = Service.objects.filter(is_active=True, business__is_approved=True, business__is_published=True,
                                business__category__in=["salon", "store"], business__city__slug="kochi")
    category = request.query_params.get("category", "").strip()
    if category:
        qs = qs.filter(business__category=category)
    return Response(ServiceSerializer(qs.select_related("business").order_by("name"), many=True).data)

@api_view(["GET"])
@permission_classes([AllowAny])
def slots(request):
    service = request.query_params.get("service", "").strip()
    if not service.isdigit():
        raise ValidationError({"service": "Provide a valid numeric service ID."})
    qs = ServiceSlot.objects.filter(service_id=int(service), starts_at__gt=timezone.now(), is_available=True,
                                    service__is_active=True, service__business__is_approved=True,
                                    service__business__is_published=True, service__business__city__slug="kochi",
                                    service__business__category__in=["salon", "store"])
    return Response(SlotSerializer(qs.order_by("starts_at"), many=True).data)

@api_view(["GET"])
@permission_classes([AllowAny])
def notices(request):
    qs = Notice.objects.filter(is_published=True, city__slug="kochi", published_at__lte=timezone.now()).filter(
        Q(expires_at__isnull=True) | Q(expires_at__gt=timezone.now()))
    return Response(NoticeSerializer(qs.order_by("-published_at"), many=True).data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def my_bookings(request):
    event_qs = EventBooking.objects.filter(user=request.user).select_related("event").order_by("-created_at")
    service_qs = ServiceBooking.objects.filter(user=request.user).select_related("slot__service").order_by("-created_at")
    return Response({"events": EventBookingSerializer(event_qs, many=True).data,
                     "services": ServiceBookingSerializer(service_qs, many=True).data})

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def book_event(request):
    serializer = EventBookingRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    event_id, quantity = serializer.validated_data["event"], serializer.validated_data["quantity"]
    # Lock the event row: all bookings for one event are serialized under PostgreSQL.
    with transaction.atomic():
        event = get_object_or_404(Event.objects.select_for_update(), pk=event_id, is_published=True,
                                  city__slug="kochi", is_free=True)
        if event.starts_at <= timezone.now():
            raise ValidationError({"event": "This event has already started."})
        if quantity > event.max_tickets_per_user:
            raise ValidationError({"quantity": f"Maximum {event.max_tickets_per_user} tickets per user."})
        if EventBooking.objects.filter(event=event, user=request.user, status="confirmed").exists():
            raise ValidationError({"event": "You already have a booking for this event."})
        if quantity > event.remaining:
            raise ValidationError({"quantity": "Not enough seats available."})
        booking = EventBooking.objects.create(event=event, user=request.user, quantity=quantity)
    return Response(EventBookingSerializer(booking).data, status=status.HTTP_201_CREATED)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def book_service(request):
    serializer = ServiceBookingRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    slot_id = serializer.validated_data["slot"]
    with transaction.atomic():
        slot = get_object_or_404(ServiceSlot.objects.select_for_update(), pk=slot_id, is_available=True,
                                 service__is_active=True, service__business__is_published=True,
                                 service__business__is_approved=True, service__business__city__slug="kochi",
                                 service__business__category__in=["salon", "store"])
        if slot.starts_at <= timezone.now():
            raise ValidationError({"slot": "This appointment has already started."})
        if ServiceBooking.objects.filter(slot=slot, user=request.user, status="confirmed").exists():
            raise ValidationError({"slot": "You already have this appointment."})
        if slot.remaining < 1:
            raise ValidationError({"slot": "This appointment slot is full."})
        booking = ServiceBooking.objects.create(slot=slot, user=request.user)
    return Response(ServiceBookingSerializer(booking).data, status=status.HTTP_201_CREATED)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def cancel_event(request, pk):
    with transaction.atomic():
        booking = get_object_or_404(EventBooking.objects.select_for_update().select_related("event"), pk=pk, user=request.user)
        if booking.status == "cancelled":
            raise ValidationError({"booking": "Booking is already cancelled."})
        if booking.event.starts_at <= timezone.now():
            raise ValidationError({"booking": "Cannot cancel after the event starts."})
        booking.status = "cancelled"
        booking.save(update_fields=["status"])
    return Response(EventBookingSerializer(booking).data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def cancel_service(request, pk):
    with transaction.atomic():
        booking = get_object_or_404(ServiceBooking.objects.select_for_update().select_related("slot"), pk=pk, user=request.user)
        if booking.status == "cancelled":
            raise ValidationError({"booking": "Booking is already cancelled."})
        if booking.slot.starts_at <= timezone.now():
            raise ValidationError({"booking": "Cannot cancel after the appointment starts."})
        booking.status = "cancelled"
        booking.save(update_fields=["status"])
    return Response(ServiceBookingSerializer(booking).data)
