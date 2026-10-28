import sqlite3
from datetime import datetime

DB_NAME = "propinas.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS predicciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            total_bill REAL,
            size INTEGER,
            day TEXT,
            time TEXT,
            propina_estimada REAL,
            r2 REAL,
            fecha TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()
    print("DB propinas.db creada")

def guardar_prediccion(total_bill, size, day, time, propina, r2=0.4675):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        INSERT INTO predicciones (total_bill, size, day, time, propina_estimada, r2, fecha)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (total_bill, size, day, time, propina, r2, datetime.now().isoformat()))
    conn.commit()
    conn.close()
    print(f"Guardado: ${propina} para bill ${total_bill}")

def ver_historial():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM predicciones ORDER BY id DESC LIMIT 10")
    rows = c.fetchall()
    for r in rows:
        print(r)
    conn.close()

if __name__ == "__main__":
    init_db()
    guardar_prediccion(20, 2, "Fri", "Dinner", 2.97)
    ver_historial()
