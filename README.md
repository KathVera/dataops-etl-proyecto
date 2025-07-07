# Proyecto Final - DataOps con CI/CD

## Nombre del Proyecto
**Implementación de DataOps con CI/CD para un proceso ETL automatizado**

## Curso
DE–ED12 – Módulo DataOps

## Alumna
Katherine Vera Huarhua


## Objetivo del Proyecto
Diseñar e implementar un pipeline automatizado que:
- Integre datos desde una fuente relacional PostgreSQL y un archivo CSV.
- Procese los datos mediante un flujo ETL en Python.
- Consolide la información de empleados con sus departamentos.
- Automatice la ejecución en distintos entornos (desarrollo, pruebas, producción) usando herramientas de CI/CD bajo prácticas de DataOps.


## Tecnologías y Herramientas Utilizadas

| Categoría        | Herramienta                      |
|------------------|----------------------------------|
| Lenguaje         | Python 3.10                      |
| Librerías        | pandas, SQLAlchemy, psycopg2     |
| Contenedores     | Docker                           |
| CI/CD            | Jenkins                          |
| Control de versiones | Git y GitHub                 |


## Estructura del Proyecto

dataops-etl/
    data/
      departamentos.csv
      resultado_etl.csv
    etl/
      init.py
      config.py
      extract.py
      load.py
      transform.py
      test_conn.py
    Dockerfile
	Dockerfile.jenkins
	docker-entrypoint
	gitignore
    Jenkinsfile
    main.py
    requirements.txt
	testfile.txt
    README.md


## Flujo ETL

1. **Extracción**:  
   - Se conecta a una base de datos PostgreSQL para extraer la información de empleados.
   - Se lee un archivo CSV con datos de departamentos.

2. **Transformación**:  
   - Unión de empleados con sus departamentos.
   - Cálculo del promedio del tope de comisiones por departamento.

3. **Carga**:  
   - Se guarda el resultado transformado como un nuevo archivo CSV (`resultado_etl.csv`).


## CI/CD con Jenkins

- Jenkins clona el repositorio desde GitHub.
- Construye la imagen Docker usando el `Dockerfile`.
- Ejecuta el contenedor que lanza el script `main.py`.
- Verifica que los archivos generados estén presentes en `/app/data/`.

**Pipeline exitoso** con evidencias de ejecución:
- Columnas procesadas correctamente.
- Archivo final `resultado_etl.csv` generado y validado.


## Repositorio
https://github.com/KathVera/dataops-etl-proyecto