# TechFlow Portal - Quick Start Guide

## Starting the Portal

From the project root directory:

```bash
# Start all services (PostgreSQL, Redis, Portal)
docker compose -f docker-compose.infrastructure.yml up -d

# View logs
docker compose -f docker-compose.infrastructure.yml logs -f portal

# Stop all services
docker compose -f docker-compose.infrastructure.yml down
```

## Accessing the Portal

Once started, visit: **http://localhost:3000**

## What's Running

- **PostgreSQL (port 5432)** - Database + Vector storage (pgvector)
- **Redis (port 6379)** - Cache and session store
- **Portal (port 3000)** - TechFlow Operations Portal (Next.js)

## Experience the Manual Workflows

### Support Dashboard
Navigate to **Support Dashboard** to experience:
- Manual ticket processing (45 min avg response time)
- Tedious knowledge base searching (500+ articles)
- Manual response composition (no templates)
- Error-prone ticket routing (40% misrouted)

### Other Modules (Coming Soon)
- Sales Hub - Manual prospect research (6+ hours per prospect)
- Developer Portal - Manual code reviews (2-3 days)
- HR Portal - Repetitive policy questions (50+ daily)
- Finance Dashboard - Manual invoice processing (80 hours/month)

## Development Mode

To run the portal in development mode (with hot reload):

```bash
cd portal
npm install
npm run dev
```

Visit http://localhost:3000

## Troubleshooting

**Portal won't start:**
```bash
# Rebuild the portal image
docker compose -f docker-compose.infrastructure.yml build portal
docker compose -f docker-compose.infrastructure.yml up -d
```

**Database connection issues:**
```bash
# Check PostgreSQL is healthy
docker ps --filter "name=techflow-postgres"

# View PostgreSQL logs
docker logs techflow-postgres
```

**Clear all data and start fresh:**
```bash
docker compose -f docker-compose.infrastructure.yml down -v
docker compose -f docker-compose.infrastructure.yml up -d
```
