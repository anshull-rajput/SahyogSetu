# 🤝 SahyogSetu

**Cooperative Gig Services Platform for Household & Community Services**  
SIH 2026 — Problem Statement **SIH26089**

SahyogSetu connects households with **verified Labour Cooperative members** and uses a simple, explainable fair-matching score so work is not concentrated only among the highest-rated workers.

## MVP flow
Customer selects service → enters area/date/time → workers are ranked → customer books → worker accepts/rejects → job completed → customer rates → cooperative dashboard updates.

## Tech stack
- Frontend: HTML, CSS, JavaScript-ready Django templates
- Backend: Python + Django
- Database: SQLite
- Admin analytics: Django dashboard

## Run locally
```bash
python -m venv venv
# Windows: venv\\Scripts\\activate
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```
Open `http://127.0.0.1:8000/`.

### Demo pages
- `/` — Customer service search
- `/search/` — Fair worker matching
- `/customer/` — Booking tracker + rating
- `/worker/` — Worker requests and job status
- `/cooperative/` — Cooperative member & activity dashboard
- `/admin/` — Django admin

## Matching logic
The MVP keeps the algorithm transparent: **skill match 40 + availability 20 + location 15 + rating 15 + workload fairness 10**. Lower recent workload improves the fairness component.

> This is a one-day SIH MVP, intentionally kept simple and explainable. Production deployment would add authentication, payments, notifications, stronger location services, audit logs and security hardening.
