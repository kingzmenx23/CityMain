from rest_framework import serializers
from .models import Business, Event, EventBooking, Notice, Place, Service, ServiceBooking, ServiceSlot

class PlaceSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source="city.name", read_only=True)

    class Meta:
        model = Place
        fields = ("id", "city", "name", "description", "category", "address", "image_url", "updated_at", "is_demo")

class BusinessSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source="city.name", read_only=True)

    class Meta:
        model = Business
        fields = ("id", "city", "name", "category", "description", "address", "image_url", "is_demo")

class EventSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source="city.name", read_only=True)
    remaining = serializers.IntegerField(read_only=True)

    class Meta:
        model = Event
        fields = ("id", "city", "title", "description", "venue", "starts_at", "ends_at", "capacity", "remaining", "max_tickets_per_user", "is_free", "is_demo")

class ServiceSerializer(serializers.ModelSerializer):
    business_name = serializers.CharField(source="business.name", read_only=True)
    business_category = serializers.CharField(source="business.category", read_only=True)
    is_demo = serializers.BooleanField(source="business.is_demo", read_only=True)

    class Meta:
        model = Service
        fields = ("id", "business", "business_name", "business_category", "name", "description", "duration_minutes", "is_demo")

class SlotSerializer(serializers.ModelSerializer):
    remaining = serializers.IntegerField(read_only=True)

    class Meta:
        model = ServiceSlot
        fields = ("id", "service", "starts_at", "remaining", "capacity")

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ("id", "title", "message", "place", "event", "source_url", "published_at", "expires_at", "is_demo")

class EventBookingSerializer(serializers.ModelSerializer):
    event_title = serializers.CharField(source="event.title", read_only=True)

    class Meta:
        model = EventBooking
        fields = ("id", "reference", "event", "event_title", "quantity", "status", "created_at")

class ServiceBookingSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source="slot.service.name", read_only=True)
    starts_at = serializers.DateTimeField(source="slot.starts_at", read_only=True)

    class Meta:
        model = ServiceBooking
        fields = ("id", "reference", "slot", "service_name", "starts_at", "status", "created_at")

class EventBookingRequestSerializer(serializers.Serializer):
    event = serializers.IntegerField(min_value=1)
    quantity = serializers.IntegerField(min_value=1, max_value=10)

class ServiceBookingRequestSerializer(serializers.Serializer):
    slot = serializers.IntegerField(min_value=1)
