# Matatu Fleet Tracker

## Overview
A comprehensive informatics solution designed to track maintenance and operational integrity for public transit vehicles (Matatus) in Nairobi. This system aims to improve safety and fleet management efficiency.

## Project Structure
- **backend/**: Contains the server-side logic and API integrations.
- **frontend/**: Built with Vite, React, and TypeScript for a responsive dashboard.
- **database/**: Houses the relational database schema and management scripts.
- **integration/**: Handles the communication layer between the mobile app and backend services.

## Tech Stack
- **Languages**: TypeScript, Python, SQL
- **Frontend**: React, Vite
- **Development Tools**: Git, GitHub, Termux

## Getting Started
1. **Clone the repository**:
   `git clone https://github.com/Matatu-Metrics/matatu-fleet-tracker.git`
2. **Install Dependencies**: Navigate to the `frontend/` or `backend/` folders and run your respective package manager commands (e.g., `npm install`).

## Contributors
- Franklin Obulo Omoding (Mobile Integration Engineer)
Aloyce Dache (Backend developer)
Joseph Ngatia (Frontend Developer)
Anastacia Agumba (Database Designer)
## Setup and Installation

### 1. Frontend (Vite + React + TS)
```bash
cd frontend
npm install
npm run dev

cd ../backend
# Assuming you use Python/pip
pip install -r requirements.txt
python server.py
# Navigate to database folder to run migrations or setup scripts
cd ../database
# Add your specific database startup command here

