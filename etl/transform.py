import pandas as pd

def transformar_datos():
    # Leer los datos desde el CSV simulado (en lugar de PostgreSQL)
    empleados = pd.read_csv("data/empleados_pg.csv")

    # Ejemplo simple de transformación: salario promedio por departamento
    resumen = empleados.groupby("departamento").agg(
        cantidad_empleados=("id", "count"),
        salario_promedio=("salario", "mean")
    ).reset_index()

    return resumen
