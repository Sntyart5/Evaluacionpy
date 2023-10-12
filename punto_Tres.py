estudiantes = []

agregar_estudiante = lambda nombre, curso, grado, nota1, nota2, nota3: estudiantes.append({
    "nombre": nombre,
    "curso": curso,
    "grado": grado,
    "N1": nota1,
    "N2": nota2,
    "N3": nota3
})

calcular_promedio = lambda nota1, nota2, nota3: (nota1 + nota2 + nota3) / 3

mostrar_estudiantes = lambda: [print(f"{key}: {value}") for estudiante in estudiantes for key, value in estudiante.items()]

actualizar_informacion = lambda: {
    "1": lambda: input("Ingrese el nuevo nombre: "),
    "2": lambda: input("Ingrese el nuevo curso: "),
    "3": lambda: int(input("Ingrese el nuevo grado: ")),
    "4": lambda: float(input("Ingrese la nueva Nota N'1: ")),
    "5": lambda: float(input("Ingrese la nueva Nota N'2: ")),
    "6": lambda: float(input("Ingrese la nueva Nota N'3: "))
}[opcion]()

con_estudiantes = 0

while True:
    print("="*20)
    print("Menu:")
    print("1. Agregar Estudiante")
    print("2. Consultar Estudiantes")
    print("3. Actualizar Información")
    print("0. Salir")
    print("="*20)
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese Su Nombre Completo: ")
        curso = input("Digite Nombre del curso: ")
        grado = int(input("Digite Grado que esta cursando: "))
        nota1 = float(input("Digite la primera Nota: "))
        nota2 = float(input("Digite la segunda Nota: "))
        nota3 = float(input("Digite la tercera Nota: "))
        
        promedio = calcular_promedio(nota1, nota2, nota3)
        agregar_estudiante(nombre, curso, grado, nota1, nota2, nota3)
        
        print("-"*30)
        mostrar_estudiantes()
        
    elif opcion == "2":
        if estudiantes:
            print("Lista de Estudiantes:")
            mostrar_estudiantes()
        else:
            print("No hay estudiantes registrados.")
            
    elif opcion == "3":
        if estudiantes:
            mostrar_estudiantes()
            indice = int(input("Ingrese el número de estudiante que desea actualizar: "))
            if 0 < indice <= len(estudiantes):
                nuevo_valor = actualizar_informacion()
                campo_actualizado = list(estudiantes[indice - 1].keys())[int(opcion) - 1]
                estudiantes[indice - 1][campo_actualizado] = nuevo_valor
                print(f"Información actualizada exitosamente para el campo '{campo_actualizado}'.")
            else:
                print("Número de estudiante inválido.")
        else:
            print("No hay estudiantes registrados.")

    elif opcion == "0":
        print("Gracias por usar el sistema.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
        
    con_estudiantes += 1

print("Numero de estudiantes", con_estudiantes)
