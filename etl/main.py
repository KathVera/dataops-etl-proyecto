# etl/main.py
from etl.extract import extraer_datos
from etl.transform import transformar_datos
from etl.load import cargar_datos

def main():
    # 1. Extraer desde base de datos
    df = extraer_datos()
    if df.empty:
        print("No se pudieron extraer datos.")
        return

    # 2. Transformar
    df_transformado = transformar_datos(df)

    # 3. Guardar
    cargar_datos(df_transformado)

if __name__ == "__main__":
    main()
