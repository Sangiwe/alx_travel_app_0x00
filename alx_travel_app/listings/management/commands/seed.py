from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        sample_listings = [
            {'title': 'Beachfront Villa', 'description': 'A beautiful villa by the beach.', 'location': 'Cape Town', 'price_per_night': 250.00},
            {'title': 'City Apartment', 'description': 'A modern apartment in the city center.', 'location': 'Johannesburg', 'price_per_night': 120.00},
            {'title': 'Mountain Cabin', 'description': 'A cozy cabin in the mountains.', 'location': 'Drakensberg', 'price_per_night': 180.00},
        ]

        for item in sample_listings:
            Listing.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database.'))
