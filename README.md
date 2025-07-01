# Proyecto DataOps - ETL con PostgreSQL y CSV

## Descripción

Este proyecto implementa un pipeline ETL que extrae datos de una base de datos PostgreSQL y un archivo CSV, transforma la información de empleados consolidando datos, y finalmente carga los resultados en un archivo CSV. El pipeline está preparado para ser desplegado y automatizado en diferentes entornos con prácticas DataOps.

---

## Estructura del proyecto

- `etl/` - Código fuente ETL (extract, transform, load)
- `data/` - Archivos CSV de entrada y salida
  - `departamento.csv` - Datos complementarios de departamentos
  - `resultado_etl.csv` - Resultado final del pipeline
- `README.md` - Documentación del proyecto

---

## Requisitos

- Python 3.x
- Librerías: pandas, sqlalchemy, psycopg2

Puedes instalar las librerías con:

```bash
pip install pandas sqlalchemy psycopg2-binary
