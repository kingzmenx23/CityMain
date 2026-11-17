# City Main — User Flows (Version 1)

**Status:** Approved frontend prototype flows; server-backed production flows planned.

## User roles

- **Visitor:** Explore Kochi, places, events and local businesses without signing in.
- **Registered user:** Make bookings, check status and cancel eligible bookings.
- **Provider/organizer:** Manage their own offerings, slots, capacity and bookings.
- **Administrator:** Approve listings, publish notices, moderate reviews and investigate issues.

## 1. Dashboard discovery

`Dashboard → Search / category → Directory → Listing details → (Book or view information)`

The four booking/discovery gateways share prominence: **Events**, **Salons**, **Local Stores**, **Restaurants & Hotels**. Additional services: places, weather, transport, advisories.

## 2. Event reservation

`Dashboard → Events → Event detail → Ticket quantity → Sign in → Availability recheck → Confirm → My Bookings`

Production system must lock/recheck remaining capacity, enforce per-user ticket caps and generate unique server-issued references. Frontend prototype: creates a clearly labeled **demo** entry in browser storage only.

## 3. Salon appointment

`Dashboard → Salons → Provider → Service → Date/time → Sign in → Availability recheck → Confirm or request approval → My Bookings`

Provider may accept/decline manual requests. Protect against overlapping reservations and respect blackout windows.

## 4. Local store reservation

`Dashboard → Local Stores → Provider → Visit / consultation / pickup → Date/time → Sign in → Confirm or request approval → My Bookings`

Store visits must not imply product stock reservation.

## 5. Restaurant or hotel

- Restaurant: `Dashboard → Restaurants & Hotels → Restaurant → Party size + time → Submit table request → Provider responds → My Bookings`.
- Hotel: `Dashboard → Restaurants & Hotels → Hotel → Details / contact`. Hotel room booking is deferred to a later phase.

## 6. My Bookings

`Sign in → My Bookings → Choose booking → Read status → Cancel if policy allows`

In the current prototype, bookings are stored only on the browser and have no real effect. Production bookings need authentication, permission checks and an audit trail.

## 7. Administrator / provider

`Sign in → Assigned dashboard → Manage listings, hours/slots or event capacity → Review bookings → Accept/decline/cancel with audit log`

## Failure and edge cases

- Event sold out: show unavailable state; never oversell.
- Slot unavailable: ask user to pick a different slot.
- Duplicate submission: make server endpoint idempotent.
- Unauthorized booking access: return 403/404; never expose other customers' personal details.
- Unknown weather/notice freshness: show last-updated and verified source, not fabricated live data.
