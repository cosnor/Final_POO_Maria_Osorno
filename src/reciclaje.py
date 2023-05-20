from __future__ import annotations
import random
    
class CentroAcopio: 
    def __init__(self) -> None:
        self.material_reciente = 0
        self.vidrio_actual = 0
        self.papel_actual = 0
        self.plástico_actual= 0
        self.metal_actual = 0
        self.residuos_orgánicos_actual = 0
        self.registro_diario = []
    
    def buscar_vidrio(self, dia):
        if dia > len(self.registro_diario):
            return "Ingrese un día válido"
        else:
            return f"La cantidad de vidrio recolectada en el día {dia} fue de  {self.registro_diario[dia-1]} toneladas"
        
    def recibir_material(self, carga): 
        self.material_reciente +=  carga
        
        
    def reciclar(self): 
        partes = []
        suma_actual = 0

        # Generar cuatro partes aleatorias
        for _ in range(4):
            parte = random.randint(1, self.material_reciente - suma_actual - 4)
            partes.append(parte)
            suma_actual += parte

        # La quinta parte es el número original menos la suma de las cuatro partes anteriores
        partes.append(self.material_reciente - suma_actual)
        
        self.vidrio_actual += partes[0]
        self.papel_actual += partes[1]
        self.plástico_actual += partes[2]   
        self.metal_actual += partes[3]
        self.residuos_orgánicos_actual += partes[4]
        print (f"Al final del turno, se reciclaron {self.vidrio_actual} ton de vidrio, {self.papel_actual} ton de papel, {self.plástico_actual} ton de plástico, {self.metal_actual} ton de metal y {self.residuos_orgánicos_actual} ton de residuos orgánicos") 
        
        #Se crea el registro del día de vidrio
    
        self.registro_diario.append(self.vidrio_actual)
        
        #Se reinician las cantidades de material reciclado por el día
        self.material_reciente = 0
        self.vidrio_actual = 0
        self.papel_actual = 0
        self.plástico_actual= 0
        self.metal_actual = 0
        self.residuos_orgánicos_actual = 0