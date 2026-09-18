# 🤝 SahyogSetu

**Cooperative Gig Services Platform for Household & Community Services**

SahyogSetu is a Django-based full-stack platform that connects households with **verified cooperative members** for household and community services. It includes role-based workflows for customers, workers, and cooperative administrators, along with an explainable worker-matching system designed to balance service suitability and workload fairness.

## 🌟 Why SahyogSetu?

Many service platforms can naturally concentrate opportunities among workers who already have strong ratings or visibility. SahyogSetu introduces a simple, transparent matching score that considers **skills, availability, location, rating, and recent workload**.

This makes the matching process easier to understand and gives the project a clear business-logic component beyond basic CRUD operations.

## ✨ Key Features

### 👤 Customer
- Browse and search available services
- Find eligible verified workers
- View worker matching results
- Create and track bookings
- Simulate payment
- Rate completed services

### 👷 Worker
- View incoming service requests
- Accept or reject bookings
- Start and complete assigned jobs
- Track earnings
- View cooperative welfare information

### 🛡️ Cooperative Admin
- Verify cooperative members
- Monitor bookings and worker records
- Review service activity
- View service-demand analytics

### ⚖️ Fair Worker Matching
The platform calculates a score out of 100 using:

| Factor | Weight |
|---|---:|
| Skill match | 40 |
| Availability | 20 |
| Location | 15 |
| Rating | 15 |
| Workload fairness | 10 |
| **Total** | **100** |

Only workers who are **verified, available, and suitable for the requested service** are considered. A lower recent workload improves the fairness component.

## 🔄 Core Workflow

```text
Customer selects service
        ↓
Enters location + date/time
        ↓
Eligible workers are identified
        ↓
Workers are ranked using matching score
        ↓
Customer creates booking
        ↓
Worker accepts / rejects
        ↓
Service is completed
        ↓
Payment is simulated
        ↓
Customer rates service
        ↓
Cooperative dashboard reflects activity
```

## 🏗️ Architecture

```text
┌─────────────────────────────┐
│     Django Templates        │
│      HTML + CSS + JS        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       Django Backend        │
│ Views + Business Logic      │
│ Authentication + Workflows  │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│          SQLite             │
│ Users + Workers + Bookings  │
│ Services + Activity Data    │
└─────────────────────────────┘
```

## 📸 Application Preview

Screenshots of the customer, worker, admin, booking, and matching workflows will be added here.

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript, Django Templates |
| Backend | Python, Django |
| Database | SQLite |
| Static Files | WhiteNoise |
| Server | Gunicorn |
| Deployment | Render-compatible configuration |

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/anshull-rajput/SahyogSetu.git
cd SahyogSetu
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

**Windows**
```bash
venv\\Scripts\\activate
```

**macOS/Linux**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Load demo data

```bash
python manage.py seed_demo
```

The demo seed creates **15 cooperative workers** across multiple locations, including verified and pending members, along with bookings in different states such as pending, confirmed, completed, and rejected.

### 6. Start the server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## 🚢 Deployment

The repository includes a **Render-compatible configuration**, Gunicorn startup configuration, and WhiteNoise static-file handling.

The current prototype uses SQLite for simplicity. A persistent production database can be introduced for a larger deployment.

## 🔐 Security & Scope

- Role-based workflows separate customer, worker, and cooperative-admin actions.
- Authentication and application permissions control access to workflows.
- Production deployments should use secure secrets, HTTPS, restricted access, and a persistent production database.

## 🔮 Future Improvements

- Add a production-grade PostgreSQL database
- Add real payment integration
- Add notifications for booking updates
- Add richer worker profiles and service history
- Add automated tests
- Add production monitoring and logging
- Improve mobile responsiveness and accessibility

## 📌 Project Status

SahyogSetu is a portfolio/prototype project demonstrating **Django development, role-based workflows, database-backed business logic, service booking, and explainable fair worker matching**.

---

⭐ If you find the project interesting, feel free to explore the code and follow the project.
