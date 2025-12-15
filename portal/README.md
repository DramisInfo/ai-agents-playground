# TechFlow Portal

The interactive operations portal for TechFlow Solutions - experience the AI transformation firsthand.

## Quick Start

### Development Mode

```bash
cd portal
npm install
npm run dev
```

Visit http://localhost:3000

### Production Mode (Docker)

From the root directory:

```bash
docker-compose -f docker-compose.infrastructure.yml up --build
```

The portal will be available at http://localhost:3000 with all backend services running.

## Feature Flags

Toggle AI agents on/off by editing the `.env` file:

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and enable features
ENABLE_SUPPORT_BOT=true
ENABLE_FAQ_EXPERT=true
# etc...
```

Restart the application to see changes.

## Architecture

- **Frontend**: Next.js 14 with TypeScript
- **Styling**: Tailwind CSS
- **Database**: PostgreSQL (via Docker)
- **Cache**: Redis (via Docker)
- **Vector DB**: Qdrant (via Docker)

## Training Workflow

1. Start with **all AI disabled** - experience manual workflows
2. Complete tasks in each portal module
3. Enable **one AI agent** at a time via feature flags
4. Observe the improvement in speed and accuracy
5. Move to the next lesson and agent

## Portal Modules

- **Support Dashboard** - Customer support tickets (Lessons 1-3)
- **Sales Hub** - Prospect research and proposals (Lesson 4)
- **Developer Portal** - Code reviews and onboarding (Lessons 5-6)
- **Finance Dashboard** - Invoice processing (Lesson 7)
- **HR Portal** - Employee self-service (Lesson 9)
- **Research Center** - Market research reports (Lesson 8)
