import psycopg2

try:
    conn = psycopg2.connect(
        host="mgg.vps.webdock.cloud",
        port=5432,
        user="usr_ro_dmc_rrhh_estudiantes",
        password=r"fZp!jHt0j6%89^B4I*L*29bz4b^",
        database="dmc"
    )
    print("Conexión exitosa!")
    conn.close()
except Exception as e:
    print("Error al conectar:", e)
