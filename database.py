import sqlite3
import pandas as pd

DB_PATH = "data/app.db"

def get_connection():
    """Connection with database."""
    return sqlite3.connect(DB_PATH)

def init_db():
    """Creates tables (If do not exists)."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Custom Jobs table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS custom_jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id TEXT,
        client TEXT,
        item TEXT,
        assigned_to TEXT,
        status TEXT,
        intake_date TEXT,
        due_date TEXT,
        total_price REAL,
        deposit_paid REAL,
        remaining_balance REAL,
        paid TEXT,
        notes TEXT
    )
    """)
    
    # Repair Jobs table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS repair_jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id TEXT,
        client TEXT,
        item TEXT,
        repair_type TEXT,
        assigned_to TEXT,
        status TEXT,
        intake_date TEXT,
        est_completion TEXT,
        total_price REAL,
        deposit_paid REAL,
        remaining_balance REAL,
        paid TEXT,
        notes TEXT
    )
    """)
    
    conn.commit()
    conn.close()