# 🗓️ AI Meeting Scheduling Agent
Discord Bot | Amna Yaseen

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![n8n](https://img.shields.io/badge/n8n-EA4B71?style=flat&logo=n8n&logoColor=white)
![OpenAI](https://img.shields.io/badge/GPT--4o-412991?style=flat&logo=openai&logoColor=white)
![Google Calendar](https://img.shields.io/badge/Google%20Calendar-4285F4?style=flat&logo=googlecalendar&logoColor=white)
![Discord](https://img.shields.io/badge/Discord-5865F2?style=flat&logo=discord&logoColor=white)

An agentic AI workflow that schedules, updates, and manages meetings through a Discord bot using natural language — powered by GPT-4o, n8n, and the Google Calendar API.

---

## 🎮 Demo
Watch a full walkthrough of the agent in action:

[![AI Meeting Scheduling Agent Demo](https://img.youtube.com/vi/ONaJkj-V1ns/0.jpg)](https://youtu.be/ONaJkj-V1ns)

📌 Click the thumbnail or [this link](https://youtu.be/ONaJkj-V1ns) to watch the demo.

---

## 📌 Project Overview

You talk to a Discord bot in plain English. The agent understands your intent, checks your Google Calendar for conflicts, and books (or updates, or cancels) meetings — without you ever opening a calendar app.

**Example interaction:**
> "Schedule a meeting with Ahmad tomorrow at 3 PM for 1 hour"

The agent will:
1. Parse the request using GPT-4o
2. Check Google Calendar for conflicts (with a 15-minute buffer)
3. Book the event and confirm in Discord — or flag the conflict if one exists

---

## 🏗️ Architecture

```
Discord (User Input)
      │
      ▼
Python Bot (discord.py) + ngrok
      │  tunnels to locally hosted n8n
      ▼
n8n Workflow (Orchestration Layer)
      │
      ├── GPT-4o  ──────────────────── intent parsing & response generation
      │
      └── Google Calendar API (5 tools)
            ├── Create Event
            ├── Read / List Events
            ├── Update Event
            ├── Delete Event
            └── Attendee Scheduling
```

---

## ⚙️ Features

- **Natural language scheduling** — no forms, no dropdowns; just type what you need
- **Conflict detection** — automatically checks calendar availability before booking and flags overlapping events with a 15-minute buffer rule
- **Attendee scheduling** — can schedule across multiple attendees' calendars
- **Duplicate message prevention** — bot filters duplicate triggers to avoid double-booking
- **Full CRUD** — create, read, update, and delete calendar events via chat

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| GPT-4o (OpenAI) | Intent parsing & response generation |
| n8n | Workflow orchestration |
| Google Calendar API | Event management (create, read, update, delete) |
| Discord API + Python | Discord bot interface |
| ngrok | Tunnels Discord messages to locally hosted n8n |

---

## 🚀 Setup

### Prerequisites
- n8n instance (self-hosted via Docker)
- OpenAI API key
- Google Cloud project with Calendar API enabled
- Discord bot token
- ngrok account

### 1. Clone the repo

```bash
git clone https://github.com/AmnaaYaseen/ai-meeting-scheduling-agent.git
cd ai-meeting-scheduling-agent
```

### 2. Configure environment variables

Create a `.env` file (use `.env.example` as reference):

```env
DISCORD_BOT_TOKEN=your_discord_bot_token_here
N8N_WEBHOOK_URL=your_n8n_webhook_url_here
```

### 3. Set up Google Calendar credentials

- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Enable the Google Calendar API
- Create OAuth 2.0 credentials
- Connect credentials inside n8n

### 4. Import the n8n workflow

- Open your n8n instance
- Go to **Workflows → Import**
- Upload `AI_Meeting_Schedular.json` from this repo
- Add your OpenAI and Google Calendar credentials in n8n
- Replace all placeholder values (`YOUR_GOOGLE_CRED_ID`, `YOUR_OPENAI_CRED_ID`, etc.) with your actual n8n credential IDs

### 5. Install dependencies and run the bot

```bash
pip install -r requirements.txt
python bot.py
```

---

## 📂 Project Files

```
├── bot.py                    # Discord bot (Python)
├── AI_Meeting_Schedular.json # n8n workflow export
├── requirements.txt
├── .env.example
└── README.md
```

---

## 👩‍💻 Developer

**Amna Yaseen**  
[GitHub](https://github.com/AmnaaYaseen) • [LinkedIn](https://www.linkedin.com/in/amna-yaseen-93a3b2269)

---

## 📄 License

This project is licensed under the MIT License.  
Feel free to use, modify, and share it with credit.

© 2026 Amna Yaseen. All rights reserved.