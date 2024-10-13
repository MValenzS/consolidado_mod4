from abc import ABC, abstractmethod
import csv

class Vehiculo(ABC):
    def __init__(self,marca,modelo,nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas
        
    @abstractmethod
    def __str__(self):
        pass
    @abstractmethod
    def guardar_datos_csv(self, archivo):
        pass

class Automovil(Vehiculo):
    def __init__(self,marca,modelo,nro_ruedas,velocidad,cilindrada):
         super().__init__(marca,modelo,nro_ruedas)
         self.velocidad=velocidad
         self.cilindrada=cilindrada
            
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Num Ruedas: {self.nro_ruedas}, Velocidad: {self.velocidad} km/hr, Cilindrada: {self.cilindrada} cc"  
    
    def guardar_datos_csv(self, archivo):
        archivo.writerow([self.__class__.__name__, self.marca, self.modelo, self.nro_ruedas, self.velocidad, self.cilindrada])
    
class Particular(Automovil):
    def __init__(self,marca,modelo,nro_ruedas,velocidad,cilindrada,nro_puestos): 
        super().__init__(marca,modelo,nro_ruedas,velocidad,cilindrada) 
        self.nro_puestos=nro_puestos
    def __str__(self):
        return f"{super().__str__()}, Puestos: {self.nro_puestos}"
    
    def guardar_datos_csv(self, archivo):
        archivo.writerow([self.__class__.__name__, self.marca, self.modelo, self.nro_ruedas, self.velocidad, self.cilindrada, self.nro_puestos])    

class Carga(Automovil):
    def __init__(self,marca,modelo,nro_ruedas,velocidad,cilindrada,peso_carga): 
        super().__init__(marca,modelo,nro_ruedas,velocidad,cilindrada) 
        self.peso_carga=peso_carga
    def __str__(self):
        return f"{super().__str__()}, Carga: {self.peso_carga} kg"
    
    def guardar_datos_csv(self, archivo):
        archivo.writerow([self.__class__.__name__, self.marca, self.modelo, self.nro_ruedas, self.velocidad, self.cilindrada, self.peso_carga])

class Bicicleta(Vehiculo):
    def __init__(self,marca,modelo,nro_ruedas,tipo_bicicleta):
        super().__init__(marca,modelo,nro_ruedas)
        self.tipo_bicicleta=tipo_bicicleta
        
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Num Ruedas: {self.nro_ruedas}, Tipo Bicicleta: {self.tipo_bicicleta}" 
    
    def guardar_datos_csv(self, archivo):
        archivo.writerow([self.__class__.__name__, self.marca, self.modelo, self.nro_ruedas, self.tipo_bicicleta])
        
class Motocicleta(Bicicleta):
    def __init__(self,marca,modelo,nro_ruedas,tipo_bicicleta,nro_radios,cuadro,motor):
        super().__init__(marca,modelo,nro_ruedas,tipo_bicicleta)    
        self.nro_radios=nro_radios
        self.cuadro=cuadro
        self.motor=motor                     
    
    def __str__(self):
         return f"{super().__str__()}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}" 
     
    def guardar_datos_csv(self, archivo):
        archivo.writerow([self.__class__.__name__, self.marca, self.modelo, self.nro_ruedas, self.tipo_bicicleta, self.motor, self.cuadro, self.nro_radios])    
        
#guardar todos los vehículos en un archivo CSV        
def guardar_vehiculos_csv(vehiculos, nombre_archivo):
    try:
        with open(nombre_archivo, "w", newline='') as archivo:
            writer = csv.writer(archivo)
            for vehiculo in vehiculos:
                vehiculo.guardar_datos_csv(writer)
        print(f"Datos guardados en {nombre_archivo} exitosamente.")
    except Exception as e:
        print(f"Error al guardar los datos en {nombre_archivo}: {e}")
                
def leer_vehiculos_csv(nombre_archivo):
    vehiculos_particular = []
    vehiculos_carga = []
    vehiculos_bicicleta = []
    vehiculos_motocicleta = []
    try:
        with open(nombre_archivo, "r") as archivo:
            reader = csv.reader(archivo)
            for row in reader:
                clase_vehiculo = row[0]
                if clase_vehiculo == "Particular":
                    vehiculos_particular.append(row)
                elif clase_vehiculo == "Carga":
                    vehiculos_carga.append(row)
                elif clase_vehiculo == "Bicicleta":
                    vehiculos_bicicleta.append(row)
                elif clase_vehiculo == "Motocicleta":
                    vehiculos_motocicleta.append(row)         
            
         # Imprimir la lista de vehículos por tipo
        print("\nLista de Vehiculos Particular")
        for v in vehiculos_particular:
            print({
                'marca': v[1],
                'modelo': v[2],
                'nro_ruedas': v[3],
                'velocidad': v[4],
                'cilindrada': v[5],
                'nro_puestos': v[6]
            })   
        print("\nLista de Vehiculos Carga")
        for v in vehiculos_carga:
            print({
                'marca': v[1],
                'modelo': v[2],
                'nro_ruedas': v[3],
                'velocidad': v[4],
                'cilindrada': v[5],
                'carga': v[6]
            })

        print("\nLista de Vehiculos Bicicleta")
        for v in vehiculos_bicicleta:
            print({
                'marca': v[1],
                'modelo': v[2],
                'nro_ruedas': v[3],
                'tipo': v[4]
            })

        print("\nLista de Vehiculos Motocicleta")
        for v in vehiculos_motocicleta:
            print({
                'marca': v[1],
                'modelo': v[2],
                'nro_ruedas': v[3],
                'tipo': v[4],
                'motor': v[5],
                'cuadro': v[6],
                'nro_radios': v[7]
            })

    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no fue encontrado.")
    except Exception as e:
        print(f"Error al leer los datos de {nombre_archivo}: {e}")