from __future__ import annotations
from src.personal import Equipo


class Turno: 
    def __init__(self, horario, centro_acopio) -> None:
        self.horario = horario
        self.equipo = None
        self.carga = 0
        self.centro_acopio = centro_acopio
    
    
    def asignar_equipo(self, conductor, ayudantes): 
        try : 
            if self.equipo is None: 
                self.equipo = Equipo(conductor, ayudantes)      
            else: 
                raise Exception("El turno ya tiene un equipo asignado")
        except Exception as ex: 
            print(f"{ex.__class__.__name__}: {ex}")     
    
    def cargar(self, carga): 
        self.carga += carga
    
    def descargar(self):
        self.centro_acopio.recibir_material(self.carga)

class Horario: 
    def __init__(self, hora_inicio, hora_fin): 
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        

class Observable:
    def __init__(self):
        self.observadores = []
    
    def agregar_observador(self, observador):
        self.observadores.append(observador)
    
    def notificar_cambio_turno(self):
        for observador in self.observadores:
            observador.cambio_turno(self)

class Observador:
    def cambio_turno(self, subject):
        pass
    
class RegistroTurnos(Observable): 
    def __init__(self) -> None:
        super().__init__()
        self.turno_actual = 0
        self.observadores = None
        
    
    def cambio_diario(self):
        self.turno_actual += 1
        self.notificar_cambio_turno()
            
    
    def set_observadores(self, observadores: list):
        self.observadores = observadores
    
    
    




