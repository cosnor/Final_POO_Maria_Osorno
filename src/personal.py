from multipledispatch import dispatch

class RegistroPersonal: 
    def __init__(self) -> None:
        self.conductores = []
        self.ayudantes = []
    
    #Polimorfismo para agregar ayudante o conductor
    @dispatch (int)
    def agregar_trabajador(self, id:int):
        self.ayudantes.append(Ayudante(id))
    
    @dispatch (int, int)
    def agregar_trabajador(self, id: int, licencia: int):
        self.conductores.append(Conductor(id, licencia))
    
class Persona: 
    def __init__(self) -> None:
        self.estado = "Sin asignar"
    
    def establecer_asignado(self): 
        self.estado = "Asignado" 
    
    
class Conductor(Persona): 
    def __init__(self, id: int, licencia: int) -> None:
        super().__init__()
        self.licencia = licencia
        self.__id = id
    
    @property
    def id(self):
        return self.__id
    

class Ayudante(Persona): 
    def __init__(self, id: int) -> None:
        super().__init__()
        self.__id = id
    
    @property
    def id(self):
        return self.__id

class Equipo: 
    def __init__(self, conductor, ayudantes: list) -> None:
        self.conductor = conductor
        self.ayudantes = ayudantes