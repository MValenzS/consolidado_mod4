from vehiculo import Automovil, Vehiculo, Carga, Particular, Bicicleta, Motocicleta, guardar_vehiculos_csv, leer_vehiculos_csv
import csv

def main():
    # creamos una lista para almacenar los vehiculos
    vehiculos = []

    num_vehiculos = int(input("¿Cuántos vehiculos desea ingresar? "))

    # ciclo para pedir los datos
    for i in range(num_vehiculos):
        print(f"\nDatos del automovil {i + 1}")
        marca = input("Ingrese la marca del automovil: ")
        modelo = input("Ingrese el modelo: ")
        nro_ruedas = int(input("Ingrese el numero de ruedas: "))
        velocidad = int(input("Ingrese la velocidad en km/h: "))
        cilindrada = int(input("Ingrese el cilindraje en cc: "))

        # creamos la instancia
        automovil = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)

        # agregamos a la lista
        vehiculos.append(automovil)

    # imprimimos todos los vehiculos
    print("\nImprimiendo por pantalla los Vehiculos:")
    for i, vehiculo in enumerate(vehiculos, start=1):
        print(f"Datos del automóvil {i}: {vehiculo}")

    # creamos los vehiculos segun el enunciado
    particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    # creaos la lista para guardar los vehiculos
    vehiculos = [particular, carga, bicicleta, motocicleta]
    
    # Imprimir las instancias creadas
    print('\nLista de vehiculos parte 2')
    for vehiculo in vehiculos:
        print(vehiculo)
        
    #
    def verificar_instancias(motocicleta):
        print(f"\nVerificando la relacion de la instancia motocicleta:")

        print(f"Motocicleta es instancia con relación a Vehiculo: {isinstance(motocicleta, Vehiculo)}")
        print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}")
        print(f"Motocicleta es instancia con relación a Particular: {isinstance(motocicleta, Particular)}")
        print(f"Motocicleta es instancia con relación a Carga: {isinstance(motocicleta, Carga)}")
        print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
        print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}")    
    
    # Verificamos instancias de la motocicleta
    verificar_instancias(motocicleta) 
    
    #parte 3   
    # Guardar los vehículos en un archivo CSV
    guardar_vehiculos_csv(vehiculos, "vehiculos.csv")

    # Leer los vehículos desde el archivo CSV
    print("\nLeyendo vehículos del archivo CSV:")
    leer_vehiculos_csv("vehiculos.csv")    

if __name__ == "__main__":
    main()
