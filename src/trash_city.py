from multipledispatch import dispatch
import random

class TrashCity: 
    pass

class CentroAcopio: 
    pass


    
class Camion: 
    def __init__(self, placa: str, ruta) -> None:
        self.placa = placa
        self.conductor = None
        self.ayudantes = []
        self.ruta = ruta

class RegistroPersonal: 
    def __init__(self) -> None:
        self.conductores = []
        self.ayudantes = []
    
    @dispatch (int)
    def agregar_trabajador(self, id:int):
        self.ayudantes.append(Ayudante(id))
    
    @dispatch (int, int)
    def agregar_trabajador(self, id: int, licencia: int):
        self.conductores.append(Conductor(id, licencia))
    
    def asignar_trabajadores(self): 
        pass
    
    
class Persona: 
    def __init__(self, id) -> None:
        self.id = id
        self.estado = "Sin asignar"
    
    def establecer_asignado(self): 
        self.estado = "Asignado" 
    
class Conductor(Persona): 
    def __init__(self, id: int, licencia: int) -> None:
        super.__init__(id)
        self.licencia = licencia

class Ayudante: 
    def __init__(self, id) -> None:
        super.__init__(id)
    

class Turno: 
    pass

class Ruta: 
    def __init__(self, numero_puntos) -> None:
        self.puntos = []
        self.numero_puntos = numero_puntos
    
    def crear_rutas(self): 
        for i in range (0, self.numero_puntos): 
            latitud = random.randit(0,100) 
            longitud = random.randit(0,100) 
            self.puntos.append(PuntoGeografico(latitud, longitud))
        
class PuntoGeografico: 
    def __init__(self, latitud, longitud) -> None:
        self.punto = (latitud, longitud)