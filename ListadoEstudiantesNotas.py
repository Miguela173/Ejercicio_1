import openpyxl


estudiantes = {} 

for _ in range(3): 
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    estudiantes[nombre] = nota  


libro = openpyxl.Workbook()  
hoja = libro.active  


hoja["A1"] = "Estudiante"
hoja["B1"] = "Nota"


fila = 2 

for nombre, nota in estudiantes.items():
    hoja[f"A{fila}"] = nombre 
    hoja[f"B{fila}"] = nota  
    fila += 1  

libro.save("ejercicio1.xlsx")

print("¡Ejercicio 1 guardado en ejercicio1.xlsx!")
