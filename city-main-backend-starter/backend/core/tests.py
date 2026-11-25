from datetime import timedelta
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient
from .models import Business, City, Event, EventBooking, Service, ServiceBooking, ServiceSlot

class BookingApiTests(TestCase):
    def setUp(self):
        self.city = City.objects.create(name="Kochi", slug="kochi")
        self.user = get_user_model().objects.create_user(username="testmember", password="StrongDemoPass908!")
        self.other = get_user_model().objects.create_user(username="othermember", password="StrongDemoPass908!")
        start = timezone.now() + timedelta(days=2)
        self.event = Event.objects.create(city=self.city, title="Demo Event", venue="Test venue",
                                          starts_at=start, ends_at=start + timedelta(hours=2),
                                          capacity=2, is_published=True)
        self.business = Business.objects.create(city=self.city, name="Test Salon", category="salon",
                                                is_published=True, is_approved=True)
        self.service = Service.objects.create(business=self.business, name="Haircut")
        self.slot = ServiceSlot.objects.create(service=self.service, starts_at=start, capacity=1)
        self.client = APIClient()

    def test_public_health_and_events(self):
        self.assertEqual(self.client.get("/api/health/").status_code, 200)
        self.assertEqual(self.client.get("/api/events/").status_code, 200)

    def test_anonymous_user_cannot_book(self):
        self.assertIn(self.client.post("/api/bookings/events/", {"event": self.event.pk, "quantity": 1}).status_code, [401, 403])

    def test_event_capacity_duplicate_and_cancel(self):
        self.client.force_authenticate(user=self.user)
        first = self.client.post("/api/bookings/events/", {"event": self.event.pk, "quantity": 2})
        self.assertEqual(first.status_code, 201)
        duplicate = self.client.post("/api/bookings/events/", {"event": self.event.pk, "quantity": 1})
        self.assertEqual(duplicate.status_code, 400)
        booking_id = first.data["id"]
        self.client.force_authenticate(user=self.other)
        self.assertEqual(self.client.post("/api/bookings/events/", {"event": self.event.pk, "quantity": 1}).status_code, 400)
        self.assertEqual(self.client.post(f"/api/bookings/events/{booking_id}/cancel/").status_code, 404)
        self.client.force_authenticate(user=self.user)
        self.assertEqual(self.client.post(f"/api/bookings/events/{booking_id}/cancel/").status_code, 200)
        self.client.force_authenticate(user=self.other)
        self.assertEqual(self.client.post("/api/bookings/events/", {"event": self.event.pk, "quantity": 1}).status_code, 201)
        self.assertEqual(EventBooking.objects.filter(status="confirmed").count(), 1)

    def test_service_slot_capacity(self):
        self.client.force_authenticate(user=self.user)
        self.assertEqual(self.client.post("/api/bookings/services/", {"slot": self.slot.pk}).status_code, 201)
        self.client.force_authenticate(user=self.other)
        self.assertEqual(self.client.post("/api/bookings/services/", {"slot": self.slot.pk}).status_code, 400)
        self.assertEqual(ServiceBooking.objects.filter(status="confirmed").count(), 1)

    def test_non_salon_store_cannot_book(self):
        restaurant = Business.objects.create(city=self.city, name="Demo Restaurant", category="restaurant",
                                             is_published=True, is_approved=True)
        service = Service.objects.create(business=restaurant, name="Table")
        slot = ServiceSlot.objects.create(service=service, starts_at=timezone.now()+timedelta(days=2))
        self.client.force_authenticate(user=self.user)
        self.assertEqual(self.client.post("/api/bookings/services/", {"slot": slot.pk}).status_code, 404)
