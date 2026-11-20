from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import Business, City, Event, Place, Service, ServiceSlot

class Command(BaseCommand):
    help = "Create explicitly labeled demo-only Kochi listings and sample slots."

    def handle(self, *args, **options):
        city, _ = City.objects.get_or_create(slug="kochi", defaults={"name": "Kochi"})
        for name, category, description in [
            ("Fort Kochi", "heritage", "Example listing; confirm visiting details with official sources."),
            ("Chinese Fishing Nets", "heritage", "Example listing; confirm access details with official sources."),
            ("Mattancherry Palace", "heritage", "Example listing; verify opening information before visiting."),
        ]:
            Place.objects.get_or_create(city=city, name=name, defaults={
                "category": category, "description": description, "is_published": True, "is_demo": True,
            })
        businesses = {}
        for category, name in [
            ("salon", "Demo Harbour Salon"),
            ("store", "Demo Kochi Local Store"),
            ("restaurant", "Demo Coast Restaurant"),
            ("hotel", "Demo Riverside Hotel"),
        ]:
            businesses[category], _ = Business.objects.get_or_create(city=city, name=name, defaults={
                "category": category, "description": "Fictional listing for development only.",
                "is_published": True, "is_approved": True, "is_demo": True,
            })
        start = timezone.now() + timedelta(days=14)
        for title, offset in [("Demo Kochi Art Walk", 0), ("Demo Music Evening", 1)]:
            starts_at = (start + timedelta(days=offset)).replace(hour=17, minute=0, second=0, microsecond=0)
            Event.objects.get_or_create(city=city, title=title, defaults={
                "venue": "Demo venue (not a real reservation)", "starts_at": starts_at,
                "ends_at": starts_at + timedelta(hours=2), "capacity": 25,
                "is_published": True, "is_demo": True, "is_free": True,
            })
        for category, service_name in [("salon", "Demo Haircut"), ("store", "Demo Store Consultation")]:
            service, _ = Service.objects.get_or_create(business=businesses[category], name=service_name, defaults={
                "description": "Demonstration appointment only", "duration_minutes": 30,
            })
            for offset in (14, 15, 16):
                at = (timezone.now() + timedelta(days=offset)).replace(hour=11, minute=0, second=0, microsecond=0)
                ServiceSlot.objects.get_or_create(service=service, starts_at=at, defaults={"capacity": 1})
        self.stdout.write(self.style.SUCCESS("Demo Kochi listings seeded. No real bookings or businesses are connected."))
