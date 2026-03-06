
import sqlite3

def init_db():

    conn = sqlite3.connect("threat_logs.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS threats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        result TEXT,
        action TEXT,
        time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def log_threat(url, result, action):

    conn = sqlite3.connect("threat_logs.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO threats (url,result,action) VALUES (?,?,?)",
        (url,result,action)
    )

    conn.commit()
    conn.close()


def get_logs():

    conn = sqlite3.connect("threat_logs.db")
    c = conn.cursor()

    c.execute("SELECT url,result,action,time FROM threats ORDER BY id DESC LIMIT 20")

    rows = c.fetchall()

    conn.close()

    return rows

