# PHISHGaurd
An AI-powered phishing detection system that simulates a SOC environment. It scans URLs using a machine learning model, performs threat intelligence checks, and suggests automated SOAR responses. The web dashboard visualizes scan results, detection statistics, and threat logs using Flask, Scikit-learn, HTML, JavaScript, and Chart.js.
.

🛡️ AI Phishing Detection SOC Dashboard

An AI-driven Phishing Detection System designed to simulate a Security Operations Center (SOC) environment.
This project analyzes URLs to detect potential phishing attacks, performs threat intelligence checks, and automatically suggests response actions through an interactive SOC dashboard.

It demonstrates how Machine Learning, Threat Intelligence, and Security Automation (SOAR) can be integrated to help security analysts identify and respond to phishing threats.

🚀 Project Overview

Phishing attacks are one of the most common cyber threats affecting individuals and organizations.
This project provides a lightweight platform where users can scan URLs and instantly analyze them for potential phishing risks.

The system mimics a SOC workflow where security analysts:

Detect suspicious URLs

Investigate threat intelligence

Respond to potential attacks

The platform provides real-time detection results along with threat logging and visualization.

⚙️ Key Features
🔍 AI-Based URL Phishing Detection

Uses a Machine Learning model (Random Forest) to analyze URLs and classify them as:

Legitimate

Phishing

🌐 Threat Intelligence Lookup

Performs basic threat intelligence analysis to check if the URL appears suspicious or malicious.

🛡️ Automated SOAR Response

Simulates Security Orchestration, Automation, and Response (SOAR) actions such as:

Blocking malicious URLs

Alerting SOC analysts

Initiating security investigation

📊 SOC Dashboard

A simple web-based dashboard that allows analysts to:

Scan URLs

View phishing detection results

Monitor detection statistics

Visualize threat trends using charts

📜 Threat Logging

All scanned URLs are logged with:

URL scanned

Detection result

Recommended response

Timestamp

This helps simulate SOC threat monitoring and incident tracking.

🖥️ Dashboard Capabilities

The dashboard allows users to:

✔ Enter a URL for scanning
✔ Detect phishing threats instantly
✔ View threat intelligence information
✔ Monitor detection statistics
✔ Analyze threat logs
✔ Visualize phishing activity through charts

🏗️ Tech Stack
Backend

Python

Flask

Machine Learning

Scikit-learn

Random Forest Classifier

Frontend

HTML

CSS

JavaScript

Visualization

Chart.js
