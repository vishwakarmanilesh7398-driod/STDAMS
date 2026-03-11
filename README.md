# STDAMS (Satellite Threat Detection & Autonomous Monitoring System)

## Project Overview
STDAMS is an AI-driven autonomous monitoring system for real-time satellite threat detection. It continuously analyzes satellite telemetry (altitude, velocity, signal strength, orbital drift) to detect anomalies, classify threats, and generate alerts—without human intervention. The system features a premium, futuristic dashboard for live monitoring and alert visualization.

## Problem Statement Mapping
- **Goal:** Build an AI-driven autonomous monitoring system for satellite threat detection.
- **How STDAMS Solves It:**
  - Simulates and ingests real-time satellite telemetry.
  - Uses machine learning (Isolation Forest) for anomaly detection.
  - Classifies threats and assigns risk scores.
  - Generates and displays alerts on a live dashboard.

## System Architecture
```
[simulator.py] --(telemetry)--> [model.py] --(anomaly)--> [threat_engine.py] --(threat)--> [alerts.py] --(alerts)--> [app.py] --(API/UI)--> [dashboard.html]
```
- **simulator.py:** Generates live telemetry with random anomalies.
- **model.py:** Detects anomalies using Isolation Forest.
- **threat_engine.py:** Classifies threat type and risk.
- **alerts.py:** Triggers and manages alerts.
- **app.py:** Flask API and dashboard server.
- **dashboard.html:** Premium real-time UI.

## How Anomaly Detection Works
- The system learns what "normal" satellite data looks like.
- When new data arrives, it checks if it looks unusual (anomaly) using Isolation Forest.
- If something is off (e.g., sudden drop in signal), it flags it as an anomaly.
- The threat engine then classifies the type and risk.

## How to Run the Project
1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
2. **Start the Flask server:**
   ```
   python app.py
   ```
   python simulator.py
   
3. **Open your browser:**
   - Go to `http://localhost:5000` to view the live dashboard.

## Future Scope
- Integrate with real satellite data feeds.
- Add user authentication and alert history.
- Deploy to cloud for global access.
- Enhance ML models for more threat types.
- Add notification integrations (email/SMS).
pradeep ary nilesh nikhil