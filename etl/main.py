from transform import transformar_datos

df = transformar_datos()

# Mostrar en pantalla (para el pantallazo)
print(df)

# Guardar salida como CSV
df.to_csv("data/salida_transformada.csv", index=False)
print("\n✅ Archivo 'salida_transformada.csv' generado correctamente.")
