from django.urls import path
from . import views

urlpatterns = [
    path("places/", views.places, name="places"),
    path("businesses/", views.businesses, name="businesses"),
    path("events/", views.events, name="events"),
    path("events/<int:pk>/", views.event_detail, name="event-detail"),
    path("services/", views.services, name="services"),
    path("slots/", views.slots, name="slots"),
    path("notices/", views.notices, name="notices"),
    path("bookings/me/", views.my_bookings, name="my-bookings"),
    path("bookings/events/", views.book_event, name="book-event"),
    path("bookings/services/", views.book_service, name="book-service"),
    path("bookings/events/<int:pk>/cancel/", views.cancel_event, name="cancel-event"),
    path("bookings/services/<int:pk>/cancel/", views.cancel_service, name="cancel-service"),
]
