import unittest
from main import *

class TestTrashCity(unittest.TestCase):
    def setUp(self):
        self.trashCity = Empresa()
    
    #Test 1: Creación de la empresa
    def test_creacion_camiones(self):
        registro_turnos = RegistroTurnos()
        
        for i in range(0, 5):
            numero_placa = random.randint(100, 999)
            self.trashCity.agregar_camion(f"TC{numero_placa}", 6, registro_turnos)
        
        self.assertEqual(len(self.trashCity.camiones), 5)
        
    
    def test_asignacion_personal(self):
        for i in range(0, 5):
            id = random.randint(1000000, 2000000)
            self.trashCity.personal.agregar_trabajador(id)
            id = random.randint(1000000, 2000000)
            self.trashCity.personal.agregar_trabajador(id)
            id = random.randint(1000000, 2000000)
            licencia = random.randint(1000000, 2000000)
            self.trashCity.personal.agregar_trabajador(id, licencia)
        
        #Comprobación de que se agregaron los 15 trabajadores
        self.assertEqual(len(self.trashCity.personal.conductores) + len(self.trashCity.personal.ayudantes)  , 15)
        
        
        for camion in self.trashCity.camiones:
            self.assertIsNotNone(camion.turno.conductor)
            self.assertEqual(len(camion.turno.ayudantes), 2)
    
    def test_creacion_rutas(self):
        for camion in self.trashCity.camiones:
            camion.ruta.crear_rutas()
            self.assertGreater(len(camion.ruta.puntos), 0)
    
    def test_carga_basura(self):
        for camion in self.trashCity.camiones:
            for punto in camion.ruta.puntos:
                carga = random.randint(1, 50)
                camion.cargar(carga)
                self.assertEqual(camion.capacidad_carga, carga)
    
    def test_descarga_camiones_centro_acopio(self):
        tc_acopio = CentroAcopio()
        
        for camion in self.trashCity.camiones:
            camion.ruta.crear_rutas()
            
            for punto in camion.ruta.puntos:
                carga = random.randint(1, 50)
                camion.cargar(carga)
            
            camion.descargar(tc_acopio)
            self.assertEqual(camion.capacidad_carga, 0)
    
    def test_busqueda_vidrio_centro_acopio(self):
        tc_acopio = CentroAcopio()
        
        for dia in range(1, 8):
            cantidad_vidrio = tc_acopio.buscar_vidrio(dia)
            # Realizar las aserciones correspondientes
    
if __name__ == '__main__':
    unittest.main()
    

