import uuid
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Q
from django.utils import timezone


class City(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    class Category(models.TextChoices):
        BEACH = "beach", "Beach"
        PARK = "park", "Park"
        HERITAGE = "heritage", "Heritage"
        OTHER = "other", "Other"

    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name="places")
    name = models.CharField(max_length=160)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.OTHER)
    address = models.CharField(max_length=255, blank=True)
    image_url = models.URLField(blank=True)
    is_published = models.BooleanField(default=False)
    is_demo = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Business(models.Model):
    class Category(models.TextChoices):
        SALON = "salon", "Salon"
        STORE = "store", "Local store"
        RESTAURANT = "restaurant", "Restaurant"
        HOTEL = "hotel", "Hotel"

    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name="businesses")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=160)
    category = models.CharField(max_length=20, choices=Category.choices)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    image_url = models.URLField(blank=True)
    is_published = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_demo = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Event(models.Model):
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name="events")
    title = models.CharField(max_length=180)
    description = models.TextField(blank=True)
    venue = models.CharField(max_length=200)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    capacity = models.PositiveIntegerField(default=20, validators=[MinValueValidator(1)])
    max_tickets_per_user = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])
    is_free = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)
    is_demo = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def remaining(self):
        reserved = self.bookings.filter(status=EventBooking.Status.CONFIRMED).aggregate(
            total=models.Sum("quantity")
        )["total"] or 0
        return max(0, self.capacity - reserved)


class EventBooking(models.Model):
    class Status(models.TextChoices):
        CONFIRMED = "confirmed", "Confirmed"
        CANCELLED = "cancelled", "Cancelled"

    reference = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name="bookings")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="event_bookings")
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.CONFIRMED)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["event", "user"], condition=Q(status="confirmed"), name="unique_active_event_booking_per_user"
        )]


class Service(models.Model):
    business = models.ForeignKey(Business, on_delete=models.PROTECT, related_name="services")
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    duration_minutes = models.PositiveIntegerField(default=30, validators=[MinValueValidator(5)])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.business.name}: {self.name}"


class ServiceSlot(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="slots")
    starts_at = models.DateTimeField()
    capacity = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])
    is_available = models.BooleanField(default=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["service", "starts_at"], name="unique_service_start")]

    @property
    def remaining(self):
        reserved = self.bookings.filter(status=ServiceBooking.Status.CONFIRMED).count()
        return max(0, self.capacity - reserved)

    def __str__(self):
        return f"{self.service} - {self.starts_at}"


class ServiceBooking(models.Model):
    class Status(models.TextChoices):
        CONFIRMED = "confirmed", "Confirmed"
        CANCELLED = "cancelled", "Cancelled"

    reference = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    slot = models.ForeignKey(ServiceSlot, on_delete=models.PROTECT, related_name="bookings")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="service_bookings")
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.CONFIRMED)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["slot", "user"], condition=Q(status="confirmed"), name="unique_active_service_slot_per_user"
        )]


class Notice(models.Model):
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name="notices")
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=160)
    message = models.TextField()
    source_url = models.URLField(blank=True)
    published_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    is_demo = models.BooleanField(default=False)

    def __str__(self):
        return self.title
