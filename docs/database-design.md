# City Main — Draft Database Design

**Stack:** PostgreSQL, Django ORM. **Status:** Draft; no migration created.

## Main entities

| Entity | Purpose | Key fields |
| --- | --- | --- |
| City | Multi-city foundation | id, name, state, country, timezone |
| User | Authentication | id, email (unique), password hash, is_active |
| UserProfile | User preferences | user_id, display_name, phone (optional) |
| Business | Verified providers | id, city_id, owner_id, name, type, address, approval_status |
| Place | Tourist attraction | id, city_id, title, category, description, address, coordinates |
| Event | Scheduled event | id, organizer_id, venue, starts_at, ends_at, capacity, per_user_limit, status |
| EventBooking | Free ticket reservation | id, event_id, user_id, quantity, status, reference (unique) |
| Service | Appointment offering | id, business_id, name, duration_minutes, category |
| ServiceSlot | Available time window | id, service_id, start_at, end_at, capacity, is_blocked |
| ServiceBooking | Salon/store appointment | id, slot_id, user_id, party_size, status, reference |
| RestaurantTableRequest | Table reservation request | id, business_id, user_id, starts_at, party_size, status, reference |
| Review | Moderated review | id, author_id, business_id/place_id, rating, text, status |
| Notice | Verified advisory | id, city_id, place_id (nullable), source_url, published_at, expires_at, status |
| BookingAuditLog | Booking state changes | id, booking_type, booking_id, actor_id, action, timestamp |

## Relationships and rules

- `City` 1 → many `Place`, `Business`, `Event`.
- `Business` 1 → many `Service` and `RestaurantTableRequest`.
- `Event` 1 → many `EventBooking`.
- `Service` 1 → many `ServiceSlot`; a `ServiceSlot` has many `ServiceBooking`.
- `User` 1 → many bookings and reviews.
- `EventBooking.reference`, `ServiceBooking.reference`, and `RestaurantTableRequest.reference` are unique.
- Store timestamps in UTC; display Kochi times in `Asia/Kolkata`.
- Enforce capacity under a database transaction using row locking on Event or ServiceSlot.
- Permission-check every booking; providers can access only assigned business records.
- Do not store card details or plaintext passwords.

## Later phase

Hotel rooms, rate plans, inventory, payment intents and refunds are intentionally not part of the initial backend schema.
