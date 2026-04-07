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
    
def insert_custom_job(data):
    """Adds custom jobs to base."""
    conn = get_connection()
    cursor = conn.cursor()
    
    query = """
    INSERT INTO custom_jobs (
        order_id, client, item, assigned_to, status, 
        intake_date, due_date, total_price, deposit_paid, 
        remaining_balance, paid, notes
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    
    values = (
        data["Order_ID"], data["Client"], data["Item"],
        data["Assigned_To"], data["Status"], data["Intake_Date"],
        data["Due_Date"], data["Total_Price"], data["Deposit_Paid"],
        data["Remaining_Balance"], data["Paid"], data["Notes"]
    )
    
    cursor.execute(query, values)
    conn.commit()
    conn.close()

def get_all_custom_jobs():
    """Returns all custom jobs like DataFrame"""
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM custom_jobs" , conn)
    conn.close()
    return df

def insert_repair_job(data):
    """Adds repair jobs to base."""
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO repair_jobs (
        order_id, client, item, repair_type, assigned_to, status, 
        intake_date, est_completion, total_price, deposit_paid, 
        remaining_balance, paid, notes
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    values = (
        data["Order_ID"], data["Client"], data["Item"], data["Repair_Type"],
        data["Assigned_To"], data["Status"], data["Intake_Date"],
        data["Est_Completion"], data["Total_Price"], data["Deposit_Paid"],
        data["Remaining_Balance"], data["Paid"], data["Notes"]
    )
    cursor.execute(query, values)
    conn.commit()
    conn.close()

def get_all_repair_jobs():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM repair_jobs", conn)
    conn.close()
    return df
