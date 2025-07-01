from etl.config import DB_CONFIG
import sqlalchemy
import pandas as pd
import urllib.parse

def extraer_datos():
    try:
        user = DB_CONFIG['user']
        password = urllib.parse.quote_plus(DB_CONFIG['password'])  # codifica contraseña
        host = DB_CONFIG['host']
        port = DB_CONFIG['port']
        database = DB_CONFIG['database']

        print("Contraseña usada para la conexión:", DB_CONFIG['password'])

        engine = sqlalchemy.create_engine(
            f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
        )
        with engine.connect() as conn:
            query = "SELECT * FROM rrhh.empleado"
            df = pd.read_sql(query, conn)
            print("Columnas disponibles:", df.columns)
        return df
    except Exception as e:
        print("Error al extraer datos:", e)
        return pd.DataFrame()

