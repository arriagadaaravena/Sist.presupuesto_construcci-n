import os
os.system("cls")

IVA = 0.19
PRESUPUESTO_MAXIMO = 50000000

print("SISTEMA DE PRESUPUESTO DE CONSTRUCCIÓN")
nombre_proyecto = input("Escriba el nombre del proyecto\n")

while True:
    try:
        metros = float(input("Ingrese la cantidad de metros cuadrados a contruir: \n"))
        costo_metro = int(input("Ingrese el costo por metro cuadrado: \n"))
        trabajadores = int(input("Ingrese la cantidad de trabajadores: \n"))
        costo_trabajador = int(input("Ingrese el costo por trabajador: \n"))
    
        if metros > 0 and costo_metro > 0 and trabajadores > 0 and costo_trabajador > 0:
            break
        else:
            print("El valor ingresado debe ser mayor que 0. Ingrese nuevamente...")
    except:
        print("ERROR, los datos ingresados no son válidos")
        
costo_materiales = metros * costo_metro
costo_manodeobra = trabajadores * costo_trabajador
costo_neto = costo_materiales + costo_manodeobra
costo_total = costo_neto * (1 + IVA)

if costo_total > PRESUPUESTO_MAXIMO:
    print("El presupuesto excede el máximo permitido")
    
else:
    print("El presupuesto está dentro del límite")
    
print("\n====RESUMEN====")
print(f"Proyecto:{nombre_proyecto}")
print(f"Costo materiales: ${costo_materiales}")
print(f"Costo mano de obra: ${costo_manodeobra}")
print(f"Costo neto: ${costo_neto}")
print(f"Costo total con IVA: ${int(costo_total):,}")
