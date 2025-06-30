def cargar_datos(df):
    print("Mostrando los primeros registros transformados:")
    print(df.head())
    
    # Guardar resultado en CSV
    df.to_csv("data/resultado_etl.csv", index=False)
