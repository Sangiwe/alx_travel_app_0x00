# ALX Travel App (0x00)

This is a Django-based travel listing application that allows users to view listings, book stays, and leave reviews.

## 🛠️ Features Implemented

### 1. Models
The following models are defined in `listings/models.py`:
- **Listing**: Represents a property that can be booked.
- **Booking**: Represents a booking made by a user.
- **Review**: Represents a review left by a user on a listing.

### 2. Serializers
The following serializers are defined in `listings/serializers.py`:
- **ListingSerializer**: Serializes Listing model data.
- **BookingSerializer**: Serializes Booking model data.

### 3. Database Seeder
A custom management command is available to seed the database with sample listings:
```bash
python manage.py seed
