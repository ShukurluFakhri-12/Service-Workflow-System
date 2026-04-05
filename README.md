# Service Workflow System

A lightweight workflow and operations dashboard designed for small service-based businesses.

Originally inspired by jewelry store operations, the system is built to support any service workflow involving task tracking, status management, and payment visibility.

---

## Overview

This project provides a structured way to manage:

- Custom service workflows (e.g., Consultation → Design → Production → Completion)
- Repair / service job tracking
- Deposit and remaining balance monitoring
- Job status progression
- Basic operational analytics

The system helps businesses move from unstructured tracking (notes, spreadsheets) to a more organized and visible workflow.

---

## Features

- Add and manage custom jobs
- Track repair/service tasks
- Editable job tables
- Status-based workflow tracking
- Deposit & remaining balance calculation
- Basic analytics (open jobs, revenue, outstanding balance)
- Filtering and search functionality

---

## System Design

The application follows a simple layered structure:

- **UI Layer** — Streamlit interface for interaction
- **Data Layer** — Currently CSV-based storage (planned upgrade to SQLite)
- **Logic Layer** — Handles calculations (balances, status, filters)

Future versions will extend this into a more structured backend system.

---

## Tech Stack

- Python
- Streamlit
- Pandas

(Currently using CSV storage, transitioning to SQLite)

---

## Project Direction

This project is being actively developed toward a more advanced system with:

- SQLite-based database backend
- Improved business logic (status rules, priority detection)
- Enhanced analytics
- AI-assisted features (e.g., message classification, summaries)
- Cleaner modular architecture

---

## Use Case

While initially inspired by jewelry businesses, this system can be adapted for:

- Repair services
- Custom manufacturing
- Small workshops
- Freelance service operations
- Any task-based workflow environment

---

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
