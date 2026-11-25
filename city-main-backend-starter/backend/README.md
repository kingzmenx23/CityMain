# City Main — Django backend (Phase 2 starter)

A **development starter**, not a completed production booking system. It provides public listing APIs, an admin panel, and **authenticated** event and salon/store slot bookings. Restaurants and hotels are currently informational listings only. All seeded entries are explicitly marked demo.

## PowerShell quick start (Windows)

From `C:\project_city\city-main`:

```powershell
cd backend
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
# Edit .env to change CITYMAIN_SECRET_KEY (do not commit it)
python manage.py makemigrations core
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_demo
python manage.py runserver 8000
```

If PowerShell blocks the venv activation script, use the venv Python directly instead of changing execution policy, e.g., `.\.venv\Scripts\python.exe manage.py migrate` and `.\.venv\Scripts\python.exe manage.py runserver 8000`.

The starter defaults to **SQLite for fast local setup**. For actual booking concurrency tests, switch to PostgreSQL (below) before treating capacity rules as proven. Both SQLite and PostgreSQL store data on the Django side, unlike the frontend's existing browser-storage demo.

## Check these URLs

- `http://127.0.0.1:8000/api/health/`
- `http://127.0.0.1:8000/api/events/`
- `http://127.0.0.1:8000/api/places/`
- `http://127.0.0.1:8000/api/businesses/?category=salon`
- `http://127.0.0.1:8000/api/businesses/?category=store`
- `http://127.0.0.1:8000/api/businesses/?category=restaurant`
- `http://127.0.0.1:8000/api/businesses/?category=hotel`
- `http://127.0.0.1:8000/api/services/?category=salon`
- `http://127.0.0.1:8000/api/slots/?service=1`
- `http://127.0.0.1:8000/api/notices/`
- `http://127.0.0.1:8000/admin/`

Sign in with the superuser through `http://127.0.0.1:8000/api-auth/login/` to test authenticated API operations from the Django REST Framework browsable API. Booking endpoints require a logged-in session and CSRF protection. Don't disable CSRF for convenience. Use `/api/bookings/events/` POST `{ "event": 1, "quantity": 1 }`, `/api/bookings/services/` POST `{ "slot": 1 }`; `/api/bookings/me/` GET for your reservations. Cancellation URLs: `/api/bookings/events/<id>/cancel/`, `/api/bookings/services/<id>/cancel/` (POST).

## Testing

```powershell
python manage.py test core
python manage.py check
```

## Switch to PostgreSQL when ready

Create a PostgreSQL DB and a least-privilege user for City Main, then configure in `backend/.env`:

```ini
CITYMAIN_USE_POSTGRES=True
CITYMAIN_DB_NAME=citymain
CITYMAIN_DB_USER=citymain
CITYMAIN_DB_PASSWORD=your-local-dev-password
CITYMAIN_DB_HOST=localhost
CITYMAIN_DB_PORT=5432
```

Run `python manage.py migrate` against the new database, then `python manage.py seed_demo`. **Changing DBs does not automatically transfer your SQLite data.** On PostgreSQL, `transaction.atomic()` and `select_for_update()` lock the relevant Event or ServiceSlot row during booking; still perform integration/concurrency testing before launch.

## Important boundaries

- No payment gateway, hotel room reservations, restaurant real table reservations, weather feed, or live transport service is implemented.
- Event bookings support only free events, and appointments currently support salon/store categories, with simple discrete slot availability.
- Provider permissions, self-registration, password reset, full cancellation policies, owner verification, reviews, audit trail, idempotency keys, and production deployment security are **future work**.
- The Next.js UI still uses mock listings/browser-local bookings until explicitly connected to this backend. Nothing in this ZIP changes frontend files.
- `.env`, `.venv/`, `db.sqlite3`, caches and secrets must not be committed. Ensure root `.gitignore` covers them.
- Do not display demo events as real public offerings.
