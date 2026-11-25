# CityMain — Stage 1 User Flows

**Project:** CityMain
**Stage:** Stage 1 — Salon service booking in Kochi
**Status:** Planning baseline
**Last updated:** 26 November 2026

## 1. Purpose

This document describes how each user completes the Stage 1 salon-booking tasks. It is the shared reference for wireframes, the database design, API design, and test cases.

All displayed appointment dates and times use the `Asia/Kolkata` time zone.

## 2. Roles

| Role | Starting point | Main outcome |
| --- | --- | --- |
| Visitor | Kochi salons page | Finds an approved salon and its services. |
| Customer | Salon detail page or My Bookings | Creates or manages their own salon appointment. |
| Business owner | Owner dashboard | Manages their own salon and appointments. |
| Administrator | Administrator dashboard | Approves salons and oversees platform records. |

## 3. Customer flows

### 3.1 Browse and find a salon

```text
Home
  → Kochi salons
  → Search by salon name or area (optional)
  → Salon list
  → Salon detail
  → Active service list
```

1. The visitor opens CityMain.
2. The visitor selects the Kochi salon directory.
3. The visitor may search by salon name or Kochi area.
4. The system returns approved salons that match the search.
5. The visitor selects a salon card.
6. The system opens the salon detail page with the salon information and active services.

The public directory never displays a pending, rejected, archived, or inactive salon.

### 3.2 Create a salon booking

```text
Salon detail
  → Select service
  → Select date
  → Select available time slot
  → Sign in / register when required
  → Review booking
  → Confirm booking
  → Booking confirmed
  → My Bookings
```

1. The visitor or customer opens an approved salon detail page.
2. The user selects an active service.
3. The system shows future booking dates and slots that fit the salon's working hours, closures, service duration, and current bookings.
4. The user selects one date and one available start time.
5. If the user is not signed in, CityMain directs them to sign in or create a customer account, then returns them to the selected service and slot.
6. The signed-in customer reviews the salon, service, price, appointment date, start time, and expected duration.
7. The customer selects **Confirm booking**.
8. The backend checks the customer's identity, service status, salon status, and slot availability within a database transaction.
9. If the slot remains available, the system creates a `confirmed` booking with a unique reference.
10. The system shows the confirmation and adds the booking to My Bookings.

The final availability check happens on the backend. A slot shown in the interface can become unavailable before the customer confirms it.

### 3.3 View and cancel a booking

```text
Signed in
  → My Bookings
  → Select booking
  → Review details and cancellation eligibility
  → Cancel booking
  → Cancellation confirmed
```

1. The customer signs in and opens My Bookings.
2. The system shows only that customer's upcoming and past bookings.
3. The customer opens one upcoming booking.
4. The system shows the booking reference, salon, service, date, time, status, and cancellation action when the booking meets the cancellation rule.
5. The customer confirms cancellation.
6. The backend confirms the booking belongs to the signed-in customer and that it remains eligible for cancellation.
7. The system changes the status to `cancelled_by_customer`, records the status change, and releases the appointment time for future availability.
8. My Bookings displays the updated status.

## 4. Business-owner flows

### 4.1 Register a salon business

```text
Register
  → Choose business owner role
  → Enter account and salon details
  → Submit registration
  → Pending review
  → Administrator approval
  → Owner dashboard
```

1. A user opens registration and chooses the business-owner role.
2. The user provides required account details and salon details.
3. The system creates the owner account and salon record with a pending approval status.
4. The system confirms that the registration is awaiting administrator review.
5. An administrator reviews the registration.
6. After approval, the owner can access the owner dashboard and the salon can appear in the public directory.

The owner cannot publish services or accept customer bookings until the salon has been approved.

### 4.2 Configure salon services and schedule

```text
Owner dashboard
  → Salon settings
  → Add or update services
  → Configure weekly working hours
  → Add closure or unavailable period
  → Save
  → Updated public availability
```

1. The approved owner signs in and opens the owner dashboard.
2. The owner updates their salon information when needed.
3. The owner creates or updates services with name, description, price in INR, duration in minutes, and active status.
4. The owner configures working hours for each weekday.
5. The owner adds date-specific closures or unavailable periods when necessary.
6. The backend validates that the owner owns the salon and that dates, times, prices, and durations are valid.
7. The system saves the changes.
8. New booking availability reflects the updated schedule. Existing confirmed bookings remain visible and are handled by the owner if a closure affects them.

### 4.3 Manage appointments

```text
Owner dashboard
  → Bookings
  → Select appointment
  → Review details
  → Mark completed, cancelled, or no-show
  → Updated booking history
```

1. The owner opens the booking list for their salon.
2. The system displays only appointments belonging to that salon.
3. The owner opens an appointment and reviews its customer name, service, date, time, reference, and current status.
4. When appropriate, the owner marks the booking as `completed`, `cancelled_by_owner`, or `no_show`.
5. The backend verifies salon ownership and that the requested state change is valid.
6. The system records the status history and shows the updated status to the customer.

## 5. Administrator flows

### 5.1 Review a business registration

```text
Administrator dashboard
  → Pending salon registrations
  → Review owner and salon details
  → Approve or reject
  → Owner sees updated result
```

1. The administrator opens the pending salon registrations list.
2. The administrator reviews the owner and salon details.
3. The administrator approves or rejects the registration.
4. The backend saves the decision and records the administrator action.
5. The owner sees the updated approval status.
6. An approved salon becomes eligible for public listing and service setup.

### 5.2 Manage platform records

```text
Administrator dashboard
  → Users, salons, services, or bookings
  → Select record
  → Review and update permitted fields
  → Save
  → Audit record created
```

An administrator can review and manage users, salons, services, and bookings. Changes that affect a salon's approval status or booking status must be recorded with the acting administrator and time.

## 6. Alternate and failure flows

| Situation | System behaviour |
| --- | --- |
| Customer selects a slot that becomes unavailable before confirmation | Reject the booking without creating it. Explain that the slot is no longer available and refresh available slots. |
| Customer submits the same booking request twice | Create one booking only. The API handles retries safely and returns the existing or successful booking result. |
| User attempts to access another customer's booking | Deny access without returning booking details. |
| Owner attempts to access another salon's records | Deny access without returning salon or booking details. |
| Customer selects an inactive service | Do not allow booking. Refresh the salon service list. |
| Owner changes working hours or adds a closure | Recalculate availability for new bookings. Show affected confirmed appointments to the owner. |
| Customer cancels an ineligible booking | Keep the booking unchanged and show the cancellation rule or reason. |
| Owner or administrator cancels a booking | Update status to `cancelled_by_owner`, record the reason when supplied, and make the slot available again. |
| Customer is signed out during booking | Preserve the selected service and slot long enough to return after sign-in, then recheck availability. |
| Network error occurs during confirmation | Show a retry message. The customer can safely retry without creating duplicate bookings. |

## 7. State transitions

```text
New booking → confirmed → completed
                 │
                 ├──→ cancelled_by_customer
                 ├──→ cancelled_by_owner
                 └──→ no_show
```

Only a `confirmed` booking can move to a completion, cancellation, or no-show status. A cancelled or completed booking remains in history and cannot be returned to `confirmed`.

## 8. Wireframe inputs

The UI/UX wireframes must visibly support these decisions.

- Salon cards show enough information to choose a salon.
- Salon details show service name, price, duration, and whether booking can begin.
- The booking screen keeps the selected salon and service visible while the customer chooses a date and slot.
- The review step clearly identifies the selected appointment before confirmation.
- My Bookings makes status and eligibility to cancel easy to find.
- Owner screens separate salon details, services, schedule, and appointments.
- Administrator screens provide a clear approval decision and confirmation of the result.

## 9. Related documents

- [Stage 1 requirements](requirements.md)
- `docs/database-design.md` will define the data needed by these flows.
- `docs/api-design.md` will define the requests and responses needed by these flows.
