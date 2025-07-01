import pandas as pd

def transformar_datos(df_empleados):
    # Leer CSV con nombre de departamentos
    df_departamentos = pd.read_csv("data/departamentos.csv")

    # Unir empleados con departamentos por cod_departamento
    df = df_empleados.merge(df_departamentos, how="left", on="cod_departamento")

    # Mostrar columnas disponibles para revisar
    print("Columnas combinadas:", df.columns)

    # Calcular resumen
    resumen = df.groupby("nombre_departamento").agg(
        cantidad_empleados=("empleado_id", "count"),
        salario_promedio=("mnt_salario", "mean"),
        tope_comision_promedio=("mnt_tope_comision", "mean")
    ).reset_index()

    return resumen
