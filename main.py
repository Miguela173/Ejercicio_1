import openpyxl

# 1️⃣ Crear un nuevo archivo de Excel
libro = openpyxl.Workbook()
libro.save("mi_primer_excel.xlsx")
print("✅ Archivo Excel creado.")

# 2️⃣ Escribir en la hoja activa
hoja = libro.active
hoja["A1"] = "Hola"
hoja["B1"] = "Mundo"
libro.save("mi_primer_excel.xlsx")
print("✅ Texto agregado al archivo.")

# 3️⃣ Leer lo que escribimos
libro = openpyxl.load_workbook("mi_primer_excel.xlsx")
hoja = libro.active
print("📖 Leyendo el archivo:")
print(f"A1: {hoja['A1'].value}")  # Muestra "Hola"
print(f"B1: {hoja['B1'].value}")  # Muestra "Mundo"

# 4️⃣ Modificar un valor en el archivo
hoja["B1"] = "Amigos"
libro.save("mi_primer_excel.xlsx")
print("✅ Cambio realizado: 'Mundo' → 'Amigos'")
