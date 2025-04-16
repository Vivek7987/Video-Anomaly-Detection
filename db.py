import sqlite3

def init_db():
    """Initialize the database."""
    conn = sqlite3.connect("anomaly_reports.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            event_details TEXT,
            severity TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_report(timestamp, event_details, severity):
    """Save a report to the database."""
    conn = sqlite3.connect("anomaly_reports.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reports (timestamp, event_details, severity) VALUES (?, ?, ?)",
                   (timestamp, event_details, severity))
    conn.commit()
    conn.close()
