#Definir cuantos cupos tiene el parqueadero en motos y carros
print('///BIENVENIDO AL SISTEMA DE PARQUEADEROS GALVIS///')
print("-"*50)

camp_cars int(input("Ingrese la cantidad de parqueaderos para carros: "))
camp_motos int(input("Ingrese la cantidad de parqueaderos para motos: "))

name_camp_cars=[]
name_camp_moto=[]

while int(len(name_camp_cars)) < camp_cars:
    name_camp_cars.append({})