import json

nombres = []
cursos = []
tarifas = []

def guardar_datos():
    datos = {
        "nombres": nombres,
        "cursos": cursos,
        "tarifas": tarifas,
    }

    with open("estudiantes.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)

def cargar_datos():
    try:
        with open("estudiantes.json","r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        nombres.extend(datos["nombres"])
        cursos.extend(datos["cursos"])
        tarifas.extend(datos["tarifas"])

    except FileNotFoundError:
        pass        

        

def pedir_tarifa (): #def se utiliza para crear una funcion
                     #indica que vamos a crear una funcion
     while True:
        try:
            tarifa = float(input("Tarifa mensual: RD$"))
            if tarifa > 0:
                return tarifa
            print("La tarifa debe ser mayor que cero.")
        except ValueError:
            print("\nErro: introduce un numero válido.")

def registrar():
    nombre = input("Nombre del estudiante: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío")
        for nombre_existente in nombres:
            if nombre_existente.lower() == nombre.lower():
                print("\nEste estudiante ya está registrado.")
                return
    while True:
        curso = input ("Curso: ").strip()

        if curso != "":
            break
        print("\nEl curso no puede estar vacio")
    tarifa = pedir_tarifa()

    nombres.append(nombre)
    cursos.append(curso)
    tarifas.append(tarifa)

    guardar_datos()
    print("\nEstudiante registrado correctamente.")

def mostrar():
    if len(nombres) == 0:
        print("Todavía no hay estudiantes registrados.")
        return
    
    for i in range(len(nombres)):
        print(
            nombres [i],
            "| Cursos: ", cursos[i],
            "| Tarifas: RD$", tarifas[i]
        )

def buscar():
    nombre = input("Nombre del estudiante: ").strip()

    for i in range(len(nombres)):
        if nombres[i].lower() == nombre.lower():
            print("Nombre: ", nombres[i])
            print("Curso: ", cursos[i])
            print("Tarifa: RD$", tarifas[i])
            return
        
    print("\nEstudiante no encontrado.")

def modificar_tarifa():
    nombre = input("Nombre del estudiante: ").strip()
    for i in range(len(nombres)):
        if nombres[i].lower() == nombre.lower():
            print("Tarifa actual: RD$", tarifas[i])
            tarifas[i] = pedir_tarifa()
            guardar_datos()
            print("Tarifa actualizada.")
            return
    print("\nEstudiante no encontrado.")

def editar_estudiante():
    nombre_buscar = input("Nombre del estudiante que desea editar: ").strip()

    for i in range(len(nombres)):
        if nombres[i].lower() == nombre_buscar.lower():

            print("\n Datos actuales: ")
            print("Nombre:", nombres[i])
            print("Curso:", cursos[i])
            print("Tarifa: RD$", tarifas[i])

            nuevo_nombre = input("Nuevo nombre (Enter para conservar): ").strip()
            nuevo_curso = input("Nuevo curso (Enter para convervar): ").strip()
            if nuevo_nombre != "": 
                nombres[i] = nuevo_nombre
            if nuevo_curso != "": 
                cursos[i] = nuevo_curso
            print("Introduce la nueva tarifa.")
            print("Si deseas conservar la tarifa, escribe la actual.")

            tarifas[i] = pedir_tarifa()

            guardar_datos()

            print("\nEstudiante actualizado correctamente.")
            return
    print("\nEstudiante no encontrado.")

def eliminar_estudiante():
    nombre_buscar = input("Nombre del estudiante que deseas eliminar: ").strip()

    for i in range(len(nombres)):
        if nombres[i].lower() == nombre_buscar.lower():
            print("Estudiante encontrado: ", nombres[i])
            confirmar = input("¿Seguro que deseas eliminarlo? (si / no): ").strip().lower()
            if confirmar == "si":
                nombres.pop(i)
                cursos.pop(i)
                tarifas.pop(i)

                guardar_datos()

                print("\n Estudiante eliminado correctamente.")
            else:
                print("Eliminacion cancelada.")
            return
    print("\nEstudiante no encontrado.")
                
    

cargar_datos()

while True:
    print("\n********TRANSPORTE ESCOLAR********")
    print("1. Registrar estudiante")
    print("2. Mostrar lista de estudiante")
    print("3. Buscar estudiante")
    print("4. Modificar tarifa")
    print("5. Calcular ingresos mensuales")
    print("6. Calcular promedio de tarifas")
    print("7. Cantidad de estudiantes")
    print("8. Editar estudiante")
    print("9. Eliminar estudiante")
    print("10. Salir")

    opcion = input("Selecciones una opcion: ")
    if opcion == "1":
        registrar()
    elif opcion == "2":
        mostrar()
    elif opcion == "3":
        buscar()
    elif opcion == "4":
        modificar_tarifa()
    elif opcion == "5":
        total_estudiantes = len(nombres)
        ingresos = sum(tarifas)

        print("Total de estudiantes: ", total_estudiantes)
        print("Ingresos mensuales previstos: RD$ ", ingresos)

    elif opcion == "6":
        if len(tarifas) > 0:
            promedio = sum(tarifas) / len(tarifas)
            print("Promedio de tarifas: RD$ ", promedio)
        else:
            print("No hay estudiantes registrados.")

    elif opcion == "7":
        total_estudiantes = len(nombres)
        print("La cantidad de estudiantes son", total_estudiantes)

    elif opcion == "8":
        editar_estudiante()

    elif opcion == "9":
        eliminar_estudiante()

    elif opcion == "10" :
        print("Gracias por utilizar el sistema.")
        break

    else:
        print("Opcion no valida. Selecciona un número del 1 al 10.")
        