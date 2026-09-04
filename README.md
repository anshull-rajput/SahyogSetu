# 🤝 SahyogSetu

**Cooperative Gig Services Platform for Household & Community Services**

SahyogSetu connects households with **verified cooperative members** and uses a simple, explainable fair-matching score so service opportunities are not concentrated only among the highest-rated workers.

## Core flow
Customer selects service → enters location/date/time → eligible workers are ranked → customer books → worker accepts/rejects → service is completed → customer pays and rates → cooperative dashboard reflects activity.

## Roles
- **Customer:** search services, compare verified members, book, track status, simulate payment and rate.
- **Worker:** receive requests, accept/reject, start/complete jobs, view earnings and cooperative welfare information.
- **Cooperative Admin:** verify members, monitor bookings, review worker records and view service-demand analytics.

## Tech stack
- Frontend: HTML, CSS, JavaScript with Django templates
- Backend: Python + Django
- Database: SQLite
- Static files: WhiteNoise
- Hosting: compatible with Render web services

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
Open `http://127.0.0.1:8000/` and choose a demo role.

## Demo data
The seed command creates 15 cooperative workers across multiple locations, including verified and pending members, plus bookings in pending, confirmed, completed and rejected states.

## Matching logic
**Skill 40 + Availability 20 + Location 15 + Rating 15 + Workload Fairness 10 = 100.** Lower recent workload improves the fairness component. Only verified and available workers matching the requested service are recommended.

## Deployment
The repository includes `render.yaml`, a Gunicorn start command and WhiteNoise static-file configuration. SQLite keeps the prototype simple; a persistent production database can be introduced later if required.
