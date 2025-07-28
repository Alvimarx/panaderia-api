from google.cloud.sql.connector import Connector, IPTypes
import pg8000
import os

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
INSTANCE_CONNECTION_NAME = os.getenv("INSTANCE_CONNECTION_NAME")

connector = Connector(ip_type=IPTypes.PRIVATE)

def main():
    try:
        conn = connector.connect(
            INSTANCE_CONNECTION_NAME,
            "pg8000",
            user=DB_USER,
            password=DB_PASS,
            db=DB_NAME,
        )
        print("✅ Conexión exitosa a la base desde el contenedor")
        conn.close()
    except Exception as e:
        print("❌ ERROR desde contenedor:", e)

if __name__ == "__main__":
    main()
