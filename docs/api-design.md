# City Main — Draft REST API Design

**Proposed base:** `/api/v1/` · **Backend:** Django REST Framework.
**Status:** Planned only. The included frontend demo does not call these APIs.

## Public read endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| GET | `/api/v1/places/` | Search/filter attractions |
| GET | `/api/v1/places/{id}/` | Place details |
| GET | `/api/v1/events/` | Upcoming events |
| GET | `/api/v1/events/{id}/` | Event details and published capacity |
| GET | `/api/v1/businesses/?type=salon` | Salon directory |
| GET | `/api/v1/businesses/?type=store` | Local store directory |
| GET | `/api/v1/businesses/?type=restaurant` | Restaurants |
| GET | `/api/v1/businesses/?type=hotel` | Hotel discovery |
| GET | `/api/v1/notices/` | Verified city advisories |

## Authenticated user endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| POST | `/api/v1/auth/login/` | Sign in (session/cookie + CSRF protection planned) |
| POST | `/api/v1/auth/logout/` | Sign out |
| GET | `/api/v1/me/` | Current user |
| POST | `/api/v1/event-bookings/` | Reserve free event tickets |
| POST | `/api/v1/service-bookings/` | Request salon/store slot |
| POST | `/api/v1/restaurant-requests/` | Request restaurant table |
| GET | `/api/v1/my-bookings/` | Own bookings only |
| POST | `/api/v1/bookings/{type}/{id}/cancel/` | Cancel with permission/policy check |

## Example: free event reservation

**POST** `/api/v1/event-bookings/`

```json
{"event_id": 15, "quantity": 2}
```

**201 Created**

```json
{"reference":"EVT-000021","status":"confirmed","quantity":2}
```

**409 Conflict:** `{"code":"capacity_unavailable","message":"Not enough seats available."}`

Use an `Idempotency-Key` header for retries. Enforce seat limits server-side under a transaction.

## Rules

- Pagination and query filtering on all directories.
- Consistent error shapes, status codes, validation and rate limits.
- Auth + CSRF protection for write endpoints and object-level authorization on all protected resources.
- No payments, room-inventory APIs, or live transport APIs in V1.
- Bookings never use browser local storage as the authoritative production database.
