import random

#definimos el diccionario
departamentos=[]

def agregar_departamento(nombre, capital):
    departamento={
        "nombre": nombre,
        "capital": capital
    }
    departamentos.append(departamento)
    
def mostrar_departamentos():
    for departamento in departamentos:
        print(f"Departamento: {departamento['nombre'].upper()}")
        print(f"Capital: {departamento['capital'].upper()}")        
        print("-"*40)
        
        
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

        


while True:
        print("="*40)
        print("Menu:")
        print("1. Agregar Departamento:")
        print("2. Consultar Departamentos:")
        print("3. Jugar:")
        print("4. Salir:")
        print("="*40)
        
        opcion = input("Seleccione una opción: ").upper()
        
        if opcion=="1":
            nombre= input("Ingrese El Departamento: ").upper()
            capital= input("Ingrese La Capital Del Departamento: ").upper()

            agregar_departamento(nombre,capital)
        
        if opcion=="2":
            if departamentos:
                print("Lista De Departamentos: ")
                print("-"*40)
                mostrar_departamentos()
            else:
                print("No Hay Departamentos Registrados")
        
        if opcion=="3":
            jugar()

            
        elif opcion == "4" or opcion.upper() == "SALIR":
            print("Gracias Por Usar El Sistema")
            break   

        else:
            print("Opcion Invalida")
            
        
        
