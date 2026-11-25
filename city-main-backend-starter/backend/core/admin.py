from django.contrib import admin
from .models import Business, City, Event, EventBooking, Notice, Place, Service, ServiceBooking, ServiceSlot

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "category", "is_published", "is_demo")
    list_filter = ("city", "category", "is_published")

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "city", "is_published", "is_approved", "is_demo")
    list_filter = ("category", "is_published", "is_approved")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "city", "starts_at", "capacity", "is_free", "is_published")
    list_filter = ("city", "is_free", "is_published")

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "business", "duration_minutes", "is_active")

@admin.register(ServiceSlot)
class ServiceSlotAdmin(admin.ModelAdmin):
    list_display = ("service", "starts_at", "capacity", "is_available")

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ("title", "city", "published_at", "expires_at", "is_published")

@admin.register(EventBooking)
class EventBookingAdmin(admin.ModelAdmin):
    list_display = ("reference", "event", "user", "quantity", "status", "created_at")
    readonly_fields = ("reference", "created_at")

@admin.register(ServiceBooking)
class ServiceBookingAdmin(admin.ModelAdmin):
    list_display = ("reference", "slot", "user", "status", "created_at")
    readonly_fields = ("reference", "created_at")
