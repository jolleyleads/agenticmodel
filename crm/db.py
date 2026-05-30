import sqlite3, json, os

os.makedirs('data', exist_ok=True)
DB = 'data/agent.db'

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS companies (
        id TEXT PRIMARY KEY,
        data TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS queue (
        id TEXT,
        type TEXT,
        payload TEXT,
        status TEXT
    )''')

    conn.commit()
    conn.close()

def enqueue(task_id, task_type, payload):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("INSERT INTO queue VALUES (?, ?, ?, ?)",
              (task_id, task_type, json.dumps(payload), "pending"))

    conn.commit()
    conn.close()
