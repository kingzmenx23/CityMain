# City Main — Product Requirements (Version 1)

**Project:** City Main  
**Initial city:** Kochi, Kerala, India  
**Document status:** Draft for review  
**Last updated:** 16 November 2026  
**Phase:** 1 — Requirements and planning

## 1. Product overview

City Main is a **city discovery and booking platform**. It helps residents and visitors find things to do in a city, see useful and trustworthy local information, and reserve experiences or physical services from one dashboard. The first supported city is **Kochi**; more cities may be added later.

The long-term vision includes attractions, parks, beaches, events, local businesses, hotels, transport information, weather, reviews, advisories and bookable services. **Version 1 is intentionally smaller** so the team can deliver a useful, testable application.

## 2. Problem to solve

People currently use separate apps or websites to discover places, check events, find services, read reviews, and make bookings. City Main brings these activities together in a single Kochi-focused experience. Information about closures or restrictions must be clearly dated and sourced so users do not mistake old information for live advice.

## 3. Goals

1. Help someone discover relevant places, events and services in Kochi.
2. Make it possible to complete a **real booking flow** for a free event or a participating appointment-based service.
3. Offer a clean, responsive dashboard for discovery and booking management.
4. Show useful city context, such as weather and verified location advisories.
5. Give administrators and participating providers a simple way to maintain accurate listings, availability and bookings.

### Non-goals for Version 1

Version 1 will **not** attempt to support every city, every kind of business, live public-transport tracking, hotel-room inventory, payment processing, AI-generated itineraries, or automated scraping of third-party booking sites.

## 4. Target users and permissions

| User type | Needs | Version 1 permissions |
| --- | --- | --- |
| Visitor (not signed in) | Explore Kochi | View public dashboard, listings, event details, reviews, weather and notices |
| Registered user | Book and manage activities | Create bookings, view/cancel eligible bookings, save profile, submit reviews |
| Service provider / event organizer | Manage their offerings | Edit assigned listings, schedule slots or event capacity, view their bookings |
| City Main administrator | Keep platform reliable | Approve providers/listings, manage places, events, notices, users, bookings and reviews |

Providers must not access another provider's private bookings. Administrator actions should be logged.

## 5. Version 1 (MVP) scope

### 5.1 Dashboard and navigation — Must have

- Kochi dashboard with a search bar and clear links to **Explore Places**, **Events**, **Services**, **My Bookings** and **Profile**.
- Sections for featured places, upcoming events, bookable services, latest notices and a weather summary.
- Responsive design for desktop and mobile; helpful loading, empty and error states.
- City is set to Kochi for V1 (no city-switching required yet).

### 5.2 Discover places and local businesses — Must have

- Browse place categories such as parks, beaches, heritage attractions and other points of interest.
- Each place has a title, description, category, address/area, images, location/map link, opening information where known, and relevant notices.
- Browse local business listings (including hotels and shops) with contact/location information and ratings where available.
- Search and filter by keyword and category; distinguish **bookable** from **informational-only** listings.
- Users can view ratings/reviews. Signed-in users can submit reviews subject to moderation and abuse controls.
- No claim that hours, prices, or availability are live unless the source is actually updated.

### 5.3 Events and event reservations — Must have

- Browse upcoming events and open an event detail page with date, time, venue, organizer, description, rules and available capacity.
- Signed-in users can book a specified number of **free** event tickets/seats, up to the configured per-user limit.
- System checks capacity at confirmation time and prevents overselling and duplicate booking requests.
- Confirmed reservations generate a unique booking reference and appear in **My Bookings**.
- Users can cancel eligible reservations according to the organizer's cancellation policy; capacity is released safely.
- Organizers/admins can create events, adjust capacity and review attendee/reservation lists.
- Paid tickets and payment gateways are **out of scope for V1**. Paid events may be displayed as informational-only, clearly labeled as not bookable in City Main.

### 5.4 Appointment-based service bookings — Must have

- Start with **one supported service category (salons)** to validate the booking engine.
- Provider can define services, duration, availability windows, blackout periods and slot capacity.
- User chooses service, date and time, then submits a booking; status is **confirmed** only if the slot is successfully reserved (or **pending** if the provider requires manual acceptance).
- Prevent overlapping bookings beyond actual slot capacity; show booking status and reference in My Bookings.
- Provider can confirm/decline pending requests and manage their appointments.
- Cancellation follows a visible policy; no payments in V1.

### 5.5 Kochi city updates — Must have

- Display weather summary using an external data provider, with source and last-updated time.
- Show admin-published notices for place closures, access restrictions or event changes, including date, affected place/event, source link and validity/expiry where known.
- Clearly label unverified or outdated information. Never imply that all city restrictions are monitored in real time.
- Provide official transport information links for bus/train travel; **live departures, fares and vehicle tracking are later-phase features**.

### 5.6 Accounts and administration — Must have

- Account registration, login, logout and secure password reset.
- User profile and booking history; users can access only their own reservations.
- Admin can create/edit/archive places, businesses, providers, events, services and notices.
- Admin can approve listings and moderate reviews.
- User sees clear success, failure and cancellation feedback for every booking attempt.

## 6. Main user journeys

1. **Explore:** Dashboard → Search/filter places → Place detail → View location and notices.
2. **Book event:** Events → Event detail → Select seats → Sign in (if required) → Confirm reservation → Booking reference → My Bookings.
3. **Book salon:** Services → Salon → Choose service → Choose available date/time → Confirm or request → My Bookings.
4. **Manage booking:** My Bookings → Booking details → Cancel (when allowed) → Updated status.
5. **Admin update:** Admin → Edit place/event or publish advisory → Updated information visible to users with date and source.

These flows will be expanded in `docs/user-flows.md`.

## 7. Planned screens

| Screen | Main elements |
| --- | --- |
| Dashboard | Sidebar/top navigation, location header, search, weather, featured places, event cards, service categories, notices |
| Explore Places | Category filters, result cards, optional map links, place details |
| Events | Event cards, date/category filters, availability indication |
| Event Detail / Booking | Event information, date/venue, tickets quantity, rules, booking confirmation |
| Services / Salon Detail | Service list, prices if provided, availability calendar, appointment form |
| My Bookings | Tabs for events and services, status, reference, cancellation action |
| Sign in / Sign up | Authentication and password recovery |
| Admin / Provider | Manage listings, events, slots, reservations and advisories |

## 8. Initial data entities (draft)

`User`, `City`, `Place`, `Business`, `Category`, `Review`, `Event`, `EventTicketType`, `EventBooking`, `Service`, `ServiceAvailability`, `ServiceBooking`, `Notice` and `BookingAuditLog`.

This is a planning list, not a finalized schema. Detailed fields and relationships belong in `docs/database-design.md`. For V1, City Main stores only Kochi but retains a `City` entity to allow expansion.

## 9. Technical approach (proposed)

- **Frontend:** Next.js with React, TypeScript and Tailwind CSS.
- **Backend:** Django + Django REST Framework (REST API).
- **Database:** PostgreSQL.
- **Authentication:** Secure session/cookie-based authentication or another explicitly designed approach; do not store long-lived credentials in local storage.
- **External services:** Weather API, maps/location links, and official transport links where available.
- **Development:** Git/GitHub, VS Code, PowerShell on Windows; Docker optional later.

Decisions about exact packages, API endpoints and deployment will be recorded during architecture planning.

## 10. Quality, security and data rules

- Mobile-friendly interface and keyboard-accessible forms; aim for WCAG 2.2 AA basics.
- Validate inputs on the server and enforce permission checks on every protected API.
- Safely handle concurrent booking requests using database transactions and capacity checks.
- Store timestamps consistently and display event times in **Asia/Kolkata** for Kochi.
- Protect account/contact data; collect only necessary personal information, never expose attendee lists publicly, and provide a privacy policy before launch.
- Prevent review spam and unauthorized edits; keep an audit trail for critical booking/admin changes.
- Mark notice publication time, source and expiry; allow admins to unpublish inaccurate alerts.
- Include basic automated tests for authentication, access control, event capacity, appointment conflicts and cancellation.

## 11. Version 1 acceptance criteria

The MVP is ready for a limited real-user pilot when:

- [ ] A visitor can open the Kochi dashboard and find a place or event using search/filter.
- [ ] A visitor can see when a place notice was updated and where the information came from.
- [ ] A registered user can book an available free-event seat and receive a unique reservation reference.
- [ ] Multiple users cannot reserve more event seats than capacity.
- [ ] A registered user can book an available salon appointment without exceeding slot capacity.
- [ ] A user can view and, when policy allows, cancel their own booking—but not another user's booking.
- [ ] An organizer/provider can manage only their own listings and bookings.
- [ ] An admin can publish/update places, events, service availability and notices without code changes.
- [ ] Desktop and mobile layouts work and critical booking tests pass.

## 12. Later phases (not part of V1)

- **Phase 2:** Paid event tickets and payment gateway, hotel room booking/inventory, more service categories, email/push notifications, richer maps and trip planning.
- **Phase 3:** Verified live bus/train integrations where permitted, multi-city expansion, personalized recommendations, more complete city itineraries and advanced analytics.

These are ideas, not promised release dates. Priorities will be reviewed after the MVP pilot.

## 13. Open questions before implementation

1. Which **Kochi salons and event organizers** will supply genuine availability for the MVP? Test data may be used in development but must be labeled as demo data.
2. Are salon appointments **instant-confirmation** or **provider-approved** by default?
3. What are the cancellation limits, booking quantity limits and minimum customer details?
4. Which weather and maps providers will be used, and what are their licensing/cost limits?
5. How will admins verify notices, business listings and event organizer ownership?

**Next planning deliverables:** `user-flows.md` → dashboard/event-booking wireframes → `database-design.md` → `api-design.md` → project scaffolding.
