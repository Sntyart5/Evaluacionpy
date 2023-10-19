import random

departamentos = []

def agregar_departamento(nombre, capital):
    departamento = {
        "nombre": nombre,
        "capital": capital
    }
    departamentos.append(departamento)

def consultar_departamentos():
    if not departamentos:
        print("No hay departamentos registrados.")
    else:
        for departamento in departamentos:
            print(f"Departamento: {departamento['nombre']}")
            print(f"Capital: {departamento['capital']}")
            print("-" * 40)

def jugar():
    if not departamentos:
        print("No hay departamentos registrados para jugar.")
        return

    departamento_aleatorio = random.choice(departamentos)
    nombre_departamento = departamento_aleatorio["nombre"]
    capital_correcta = departamento_aleatorio["capital"]

    print(f"\n¡Adivina la capital de {nombre_departamento}!")

    intentos = 0
    while True:
        intentos += 1
        capital_usuario = input("Ingresa la capital: ").upper()

        if capital_usuario == capital_correcta:
            print(f"¡Correcto! La capital de {nombre_departamento} es {capital_correcta}.")
            break
        else:
            print("Incorrecto. ¡Inténtalo de nuevo!")

    print(f"¡Lo lograste en {intentos} intentos!")

def menu():
    while True:
        print("=" * 40)
        print("Menu:")
        print("1. Agregar Departamento")
        print("2. Consultar Departamentos")
        print("3. Jugar")
        print("4. Salir")
        print("=" * 40)

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            nombre = input("Ingrese el nombre del departamento: ").capitalize()
            capital = input("Ingrese la capital del departamento: ").capitalize()

            agregar_departamento(nombre, capital)
        elif opcion == 2:
            consultar_departamentos()
        elif opcion == 3:
            jugar()
        elif opcion == 4:
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()
