# Service Workflow Dashboard

A workflow and operations dashboard designed for small service-based businesses to manage custom orders and repair jobs with real-time tracking, prioritization, and decision support.

📌 Overview

This system helps businesses organize and monitor:

Custom service workflows (Consultation → Design → Production → Pickup)
Repair processes (Intake → Processing → Completion)
Financial tracking (deposits, balances, payments)
Task prioritization and overdue detection

The goal is to transform raw operational data into actionable insights.

🚀 Key Features
Workflow Management
Track custom jobs and repair orders separately
Status-based progression across defined stages
Editable job tables with real-time updates
Financial Tracking
Automatic calculation of:
Remaining balance
Payment status
Revenue and outstanding balance metrics
Smart Logic (Decision Support)
Overdue detection based on deadlines
Priority system:
🔴 High (overdue)
🟡 Medium (due soon)
🟢 Low
Insight messages highlighting critical tasks
Filtering System
Filter by:
Status
Payment state
Search query
Overdue jobs
High-priority jobs
Operational Insights
Workload analysis (jobs per assignee)
Bottleneck detection (stage with highest load)
Pipeline visualization for both workflows
Data Management
SQLite database backend
Persistent storage for all jobs
CSV export functionality
🛠 Tech Stack
Python
Streamlit (UI)
Pandas (data processing)
SQLite3 (database)
🧠 System Design

The system follows a simple layered structure:

UI Layer → Streamlit interface
Logic Layer → priority, overdue, financial calculations
Data Layer → SQLite database

Computed fields (priority, overdue, balances) are dynamically generated rather than stored, ensuring consistency.

📊 Example Use Cases
A repair shop tracking customer devices
A jewelry/custom goods business managing orders
Any small service operation handling staged workflows
▶️ How to Run
Clone the repository

Install dependencies:

pip install streamlit pandas

Run the app:

streamlit run app.py
📈 Future Improvements
Advanced analytics (trend tracking, forecasting)
User authentication / multi-user support
Integration with Google Sheets or external APIs
AI-based task recommendations
📌 Conclusion

This project demonstrates how a simple system can evolve from a basic CRUD app into a decision-support workflow system by adding structured logic, analytics, and user-focused insights.

🧩 Author Note

Built as a learning project to develop:

system design thinking
data handling
practical automation skills
