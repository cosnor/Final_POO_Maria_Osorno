from __future__ import annotations
from src.trash_city import *
from src.personal import *
from src.turno_horario import *
from src.reciclaje import *

# Se crea el objeto empresa
trashCity = Empresa()
print("----------------------------------")
print("Bienvenido a Trash City")
print("----------------------------------")

#Se crea el objeto registro de turnos que funciona de observable
registro_turnos = RegistroTurnos()

#Se agregan los camiones a la empresa y sus rutas
for i in range (0,5):
    numero_placa = random.randint(100, 999)
    trashCity.agregar_camion(f"TC{numero_placa}", 6, registro_turnos)

# Se agregan los observadores al registro de turnos
registro_turnos.set_observadores(trashCity.camiones)

# Se agrega personal a la empresa 
print("\nInformación de los camiones: \n")
print("----------------------------------")

for i in range(0, 5): 
    id = random.randint(1000000, 2000000)
    #Se agregan al registro personal y a la empresa los ayudantes
    trashCity.personal.agregar_trabajador(id)
    id = random.randint(1000000, 2000000)
    trashCity.personal.agregar_trabajador(id)
    #Se agregan al registro personal y a la empresa los conductores
    id = random.randint(1000000, 2000000)
    licencia = random.randint(1000000, 2000000)
    trashCity.personal.agregar_trabajador(id, licencia)
    
    
print("----------------------------------")

#Se instancia el centro de acopio
tc_acopio = CentroAcopio()
    
#Se asignan los turnos y con ello, los horarios y el equipo de trabajo
for indice, camion in enumerate(trashCity.camiones):
    
    HORARIOS = [["6:00", "12:00"], ["12:00", "18:00"], ["18:00", "24:00"]]
    indice_elegido = random.randint(0, 2)
    nuevo_horario = Horario(HORARIOS[indice_elegido][0], HORARIOS[indice_elegido][1])
    camion.asignar_turno(nuevo_horario, tc_acopio)
    LISTA_AYUDANTES = []
    i = 0
    for ayudante in trashCity.personal.ayudantes:
        #Validación para no asignar a alguien ya asignado a otro camión
        if ayudante.estado == "Sin asignar":
            ayudante.estado = "Asignado"
            ayudante.establecer_asignado()
            LISTA_AYUDANTES.append(ayudante)
            i+=1
            # Se asignan dos ayudantes por camión
            if i == 2:
                break

    camion.turno.asignar_equipo(trashCity.personal.conductores[indice], LISTA_AYUDANTES)
    trashCity.personal.conductores[indice].establecer_asignado()
    #Output
    print("|")
    print(f"Se ha agregado el turno al camión con placa {camion.placa}")
    print(f"El equipo de trabajo está conformado por: Conductor ID {trashCity.personal.conductores[indice].id} y los ayudantes ID {LISTA_AYUDANTES[0].id} y {LISTA_AYUDANTES[1].id}")
    print(f"El horario del turno va de {camion.turno.horario.hora_inicio} a {camion.turno.horario.hora_fin}")
    print("|")
    
print("----------------------------------")
print("Asignación de rutas")
print("----------------------------------")

#Se crean las rutas de los camiones
for camion in trashCity.camiones:
    camion.ruta.crear_rutas()
    print(f"El camión con placa {camion.placa} tiene la siguiente ruta: ")
    for numero, punto in enumerate(camion.ruta.puntos):
        print(f"Punto {numero +1 }: {punto.latitud}, {punto.longitud} ")
    print("")

print("----------------------------------")
print("Cargas por punto de los camiones en su turno")
print("----------------------------------")

#Se cargan los camiones en cada punto de su ruta
for camion in trashCity.camiones: 
    print("")
    print(f"Para el camión con placa {camion.placa} :")
    print(f"_______________________________")
    
    for punto in camion.ruta.puntos:
        carga = random.randint(1, 50)
        camion.cargar(carga)
        print(f"El camión con placa {camion.placa} ha cargado {carga} ton de basura en el punto {punto.latitud}, {punto.longitud}")
    

print("----------------------------------")
print("Descarga de los camiones en el centro de acopio por cambio de turno")
print("----------------------------------")

#Fin de turno
#Se descargan los camiones en el centro de acopio
registro_turnos.cambio_diario()
tc_acopio.reciclar()


#Consulta de la cantidad de vidrio por día: 
#Ejemplo con día 1

print("----------------------------------")
print(tc_acopio.buscar_vidrio(1))
print("----------------------------------")
print("Gracias por usar Trash City :)")
print("----------------------------------")