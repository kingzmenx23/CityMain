# CityMain — Stage 1 Software Requirements Specification

**Project:** CityMain
**Initial city:** Kochi, Kerala, India
**Document status:** Approved planning baseline
**Last updated:** 25 November 2026
**Stage:** Stage 1 — Salon service booking

## 1. Purpose

CityMain is a city discovery and service-booking platform. Stage 1 delivers one complete, reliable workflow for booking salon services in Kochi.

The product will allow a customer to discover approved salons, view their services and prices, select an available appointment slot, confirm a booking, and manage that booking. Salon owners will manage their own salon information, services, working hours, and appointments. Administrators will approve businesses and manage platform records.

This stage establishes the account, role, availability, booking, and access-control foundations needed for future CityMain features.

## 2. Problem statement

Customers need a simple way to find a salon and book an appointment without calling or messaging several businesses. Salon owners need a structured way to publish services, define availability, and manage customer appointments. CityMain provides one shared system for both groups.

## 3. Stage 1 goals

1. Let a visitor browse approved Kochi salons and their services.
2. Let a registered customer book an available salon service appointment.
3. Prevent two bookings from using the same unavailable appointment capacity.
4. Let a business owner manage only their own salon, services, schedule, and bookings.
5. Let an administrator review business registrations and manage platform data.
6. Provide clear booking status and feedback across the customer, owner, and administrator experiences.

## 4. Scope

### 4.1 In scope

- Kochi as the only available city.
- Customer, business owner, and administrator accounts.
- Customer registration, sign-in, sign-out, password reset, and profile management.
- Business-owner registration and administrator approval.
- Public salon listing and salon detail pages.
- Salon services with name, description, duration, and price.
- Salon working hours and date-specific unavailable periods.
- Available appointment time slots based on service duration and salon availability.
- Customer appointment creation, booking reference, booking history, and eligible cancellation.
- Business-owner appointment list and booking-status management.
- Administrator management of users, salons, services, business approval, and bookings.
- Responsive frontend and REST API connection between Next.js and Django.

### 4.2 Out of scope for Stage 1

- Payments, refunds, invoices, and Razorpay integration.
- Ratings and reviews.
- Restaurant, hotel, local-store, event, transport, weather, map, trip-planning, notification, and AI recommendation features.
- Multi-city support in the user interface.
- Multiple staff-member scheduling and staff-specific appointments.
- Live third-party business data integrations.

These features may be planned after the Stage 1 salon-booking workflow is complete and tested.

## 5. User roles and permissions

| Role | Capabilities |
| --- | --- |
| Visitor | Browse approved salons and view public service details. |
| Customer | Manage profile, create bookings, view own bookings, and cancel eligible bookings. |
| Business owner | Register a salon, manage assigned salon details, services, working hours, unavailable periods, and own salon bookings. |
| Administrator | Manage users, approve or reject business registrations, manage salons and services, and monitor all bookings. |

Business owners must not see another owner's salons, customer details, schedules, or bookings. Customers must not access another customer's bookings. Administrator actions that change approval or booking status should be recorded for later audit support.

## 6. Functional requirements

### 6.1 Authentication and profiles

- A user can register with name, email address, password, and selected role.
- A customer account becomes active after successful registration.
- A business-owner registration remains pending until an administrator approves it.
- Registered users can sign in, sign out, request a password reset, and update their basic profile.
- The system must enforce role-based access on the backend for every protected operation.

### 6.2 Salon discovery

- Visitors and customers can view a list of approved salons in Kochi.
- A salon card shows salon name, area, short description, and a clear link to details.
- Users can search salons by name or area.
- A salon detail page shows its name, description, address or area, contact details, services, prices, service durations, and booking availability.
- Pending, rejected, archived, or inactive salons are not visible publicly.

### 6.3 Service management

- An approved business owner can create, edit, activate, deactivate, and remove services for their own salon.
- Each service includes a name, optional description, price in INR, duration in minutes, and active status.
- Only active services can be selected for a new booking.
- An administrator can manage any salon and service when support is required.

### 6.4 Availability and time slots

- A business owner can configure regular working hours for each day of the week.
- A business owner can add a date-specific closure or unavailable period.
- The system generates bookable time slots within working hours using the selected service duration.
- A slot must not overlap a closure, unavailable period, or confirmed booking.
- The user interface must show only future available slots in the Asia/Kolkata time zone.
- Stage 1 assumes one shared salon capacity per slot. Staff-specific scheduling will be added later if needed.

### 6.5 Customer booking

- A signed-in customer selects a salon, active service, date, and available time slot.
- Before confirmation, the interface shows salon name, service, price, date, start time, and expected duration.
- The backend checks availability again when the booking request is submitted.
- A successful booking receives a unique booking reference and a `confirmed` status.
- If availability changes before confirmation, the system rejects the request with a clear message and prompts the customer to choose another slot.
- A customer can view their own current and past bookings in the dashboard.
- A customer can cancel a future booking while it is eligible under the configured cancellation rule.

### 6.6 Business-owner booking management

- A business owner can view bookings for their own salon only.
- The booking list shows customer name, service, date, time, booking reference, and status.
- A business owner can mark a booking as completed, cancelled, or no-show when appropriate.
- Owners cannot change bookings belonging to another salon.

### 6.7 Administration

- An administrator can view and manage all users and business-owner registrations.
- An administrator can approve, reject, archive, or reactivate salons.
- An administrator can view all bookings and correct records when needed.
- The system displays clear approval and booking-status feedback to the affected user.

## 7. Booking statuses

| Status | Meaning | Set by |
| --- | --- | --- |
| `confirmed` | The appointment slot has been reserved successfully. | System at booking creation |
| `completed` | The salon service was delivered. | Business owner or administrator |
| `cancelled_by_customer` | The customer cancelled an eligible booking. | Customer |
| `cancelled_by_owner` | The salon owner or administrator cancelled the booking. | Business owner or administrator |
| `no_show` | The customer did not attend the appointment. | Business owner or administrator |

Cancelled and completed bookings never make their former time slot unavailable for a new booking. The system retains them in booking history.

## 8. Main user flows

### 8.1 Customer booking flow

1. Open CityMain and browse Kochi salons.
2. Open a salon and review its services.
3. Select an active service.
4. Select a future date and available time slot.
5. Sign in or create a customer account when prompted.
6. Review the booking details and confirm.
7. Receive a booking reference and see the confirmed booking in My Bookings.

### 8.2 Business-owner flow

1. Register as a business owner and submit salon details.
2. Wait for administrator approval.
3. Add services, prices, durations, working hours, and closures.
4. Review upcoming appointments.
5. Update an appointment to completed, cancelled, or no-show after the scheduled time.

### 8.3 Administrator flow

1. Review business-owner registration and salon information.
2. Approve or reject the salon.
3. Monitor users, salons, and bookings.
4. Correct or archive records when required.

Detailed diagrams and alternate cases will be added in `docs/user-flows.md`.

## 9. User interface requirements

The Stage 1 frontend needs the following screens.

| Screen | Primary content |
| --- | --- |
| Home / Kochi salons | Search field, approved salon cards, and links to salon details. |
| Salon detail | Salon information, service list, and booking entry point. |
| Booking | Service summary, date picker, available slots, confirmation, and error feedback. |
| My Bookings | Customer's upcoming and past bookings with status and cancellation action. |
| Authentication | Registration, sign-in, password reset, and role selection. |
| Owner dashboard | Salon setup, services, working hours, closures, and bookings. |
| Administrator dashboard | User and salon approval, salon records, and booking oversight. |

The interface must work on current mobile and desktop browser sizes, support keyboard form use, and provide loading, empty, validation, and error states.

## 10. Data requirements

The initial database design will cover these concepts.

- `User` for identity, profile, authentication, and role.
- `Salon` for business information, approval status, and ownership.
- `Service` for a salon's bookable offerings.
- `WorkingHours` for recurring weekly hours.
- `AvailabilityException` for closures and unavailable periods.
- `Booking` for customer appointments, time range, price snapshot, status, and reference.
- `BookingStatusHistory` for critical status changes.

The detailed fields, relationships, constraints, indexes, and migration plan will be defined in `docs/database-design.md`.

## 11. Technical requirements

- Frontend uses Next.js App Router, TypeScript, Tailwind CSS, and shadcn/ui where it improves reusable interface components.
- Backend uses Python, Django, and Django REST Framework.
- PostgreSQL stores application data.
- The frontend requests data from Django REST API endpoints over HTTP.
- Django validates the request, checks the user's permissions, reads or changes PostgreSQL data, then returns JSON to the frontend.
- Booking creation uses a database transaction and an availability check so simultaneous requests cannot reserve the same unavailable slot.
- Times are stored consistently and displayed in Asia/Kolkata.
- Secrets such as database credentials and API keys stay in untracked local environment files.

## 12. Quality and security requirements

- Validate all user input on the backend, including ownership, dates, booking status, service activity, and time-slot availability.
- Use secure password handling provided by Django.
- Never expose another customer's bookings or contact details to a customer or unrelated owner.
- Use clear and actionable success and error messages for every booking operation.
- Keep a basic audit record for business approval and booking-status changes.
- Test authentication, role permissions, service management, time-slot conflicts, booking creation, cancellation, and booking visibility.

## 13. Stage 1 acceptance criteria

- [ ] A visitor can browse approved Kochi salons and view their active services.
- [ ] A customer can register, sign in, select a service, choose an available time slot, and receive a confirmed booking reference.
- [ ] A confirmed booking appears in that customer's My Bookings page.
- [ ] A customer cannot view or cancel another customer's booking.
- [ ] A business owner can manage only their own salon, services, hours, closures, and bookings.
- [ ] The system prevents two confirmed bookings from using the same unavailable appointment time.
- [ ] An administrator can approve a business registration and control its public visibility.
- [ ] Booking and permission tests pass against the Django API.
- [ ] The core booking journey works on mobile and desktop layouts.

## 14. Future phases

After Stage 1, CityMain may add payments, service-provider staff schedules, ratings and reviews, restaurant bookings, local-store appointments, events, hotels, weather, maps, transport information, notifications, itinerary tools, AI recommendations, and other cities.

## 15. Decisions recorded for Stage 1

- City: Kochi only.
- Booking category: salons only.
- Booking result: instant confirmation after a successful server-side availability check.
- Payment: no online payment in Stage 1.
- Capacity model: one shared salon appointment capacity per time slot.
- Time zone: Asia/Kolkata.

These decisions keep the first feature focused. Any change affects the later database and API designs and should be recorded before implementation.
