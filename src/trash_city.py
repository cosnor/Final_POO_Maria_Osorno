import random
from src.personal import RegistroPersonal
from src.turno_horario import Turno, Horario, Observador


class Empresa: 
    def __init__(self) -> None:
        self.camiones = []
        self.personal = RegistroPersonal()

    
    def agregar_camion(self, placa, numero_puntos, observable): 
        self.camiones.append(Camion(placa, Ruta(numero_puntos), observable))
    
    def mostrar_camiones(self):
        for camion in self.camiones: 
            print(f"Camión con placa {camion.placa}") 



class Camion(Observador): 
    def __init__(self, placa: str, ruta, observable) -> None:
        super().__init__()
        self.placa = placa
        self.ruta = ruta
        self.turno = None
        self.registro_turnos = observable
        self.turno_actual = 0
        
    
    def asignar_turno(self, horario, acopio):
        self.turno = Turno(horario, acopio) 
    
    def cargar(self, carga): 
        self.turno.cargar(carga)
    
        
    def cambio_turno(self, subject):
        self.turno.descargar()
        self.turno_actual = self.registro_turnos.turno_actual
        self.asignar_turno(self.turno.horario, self.turno.centro_acopio)
        

class Ruta: 
    def __init__(self, numero_puntos) -> None:
        self.puntos = []
        self.numero_puntos = numero_puntos
    
    def crear_rutas(self): 
        for i in range (0, self.numero_puntos): 
            latitud = random.randint(0,100) 
            longitud = random.randint(0,100) 
            self.puntos.append(PuntoGeografico(latitud, longitud))
            
        
class PuntoGeografico: 
    def __init__(self, latitud, longitud) -> None:
        self.latitud = latitud
        self.longitud = longitud
