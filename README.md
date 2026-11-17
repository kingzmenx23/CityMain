# City Main

**Kochi-first discovery and booking platform.** City Main helps residents and visitors explore places, events, local stores, salons, restaurants, hotels, transport and city information.

## Current milestone

This is a **Next.js frontend prototype**, not a live booking product. Screens use illustrative sample data and browser-only demo bookings. It does not authenticate users, contact real businesses, check real inventory or process payments.

## Project folders

```text
city-main/
  docs/                 Product requirements and architecture drafts
  frontend/             Next.js App Router + TypeScript + Tailwind CSS
  backend/              Reserved for Django REST Framework
  README.md
```

## Run the frontend (PowerShell)

```powershell
cd C:\project_city\city-main\frontend
npm install
npm run dev
```

Open http://localhost:3000 .

## Demo pages

- `/` — Dashboard with four core categories
- `/events`, `/salons`, `/stores`, `/restaurants-hotels` — Categories and demo requests
- `/places` — Explore places
- `/bookings` — Demo bookings in browser localStorage
- `/search?q=...`, `/weather`, `/transport` — Supplemental screens

## What is not yet implemented

Django backend, PostgreSQL schema, real authentication, real provider/event integrations, verified booking capacity, hotel room inventory, payments and live weather/transport.

## Development order

1. Review/update `docs/requirements.md` and `docs/user-flows.md`.
2. Build and review responsive Next.js screens.
3. Design Django models and REST endpoints.
4. Implement auth, booking transactions and provider verification.
5. Add API integration, real data, security and booking tests.

## Git

Use **one Git repository at the project root**, not a separate repository nested inside `frontend/`.
