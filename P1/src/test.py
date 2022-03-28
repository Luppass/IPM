from __future__ import annotations

from os import name
from re import S
from ipm import e2e
import os
import textwrap
import sys
import time
import gi

gi.require_version('Atspi', '2.0')
from gi.repository import Atspi


def show_not_passed(e):
    print('\033[91m', "  Not passed",'\033[0m')
    print(textwrap.indent(str(e), "    "))


def show_passed():
    print('\033[92m', "  Passed",'\033[0m')

def show(text):
    print(textwrap.dedent(text))

def hacer_algo(app, name, rolename, action):
    
     all_objs = e2e.find_all_objs(app)
     num_action = -1

     selected_item = None

     for item in all_objs:
        if (item.get_role_name()==rolename and item.get_name()==name):
            selected_item = item

            for it in range(0, item.get_n_actions()):
                if (item.get_action_name(it)==action):
                    num_action = it
    
    
     selected_item.do_action(num_action)    


def buscar_algo(app, name, rolename):
    
     all_objs = e2e.find_all_objs(app)
     selected_item = None

     for item in all_objs:
        if (item.get_role_name()==rolename and item.get_name()==name):
            selected_item = item

     return selected_item

def introduce_text(app, name, rolename, introducir_texto):
    entry = buscar_algo(app, name, rolename)
    assert entry is not None
    entry.set_text_contents(introducir_texto)
    hacer_algo(app, name, rolename, 'activate')


def prueba1(app):
    item = buscar_algo(app, "Rastreo Covid", "frame")
    #print(item.get_name())
    assert (item is not None)


def prueba2(app):
   
    introduce_text(app, "Buscar", "text", "Carla Torres")
    assert buscar_algo(app,"Uuid: f9890a0a-97be-4656-8a0c-b1efc3605253", "label") is not None
    assert buscar_algo(app,"Email: carla.torres@example.com", "label") is not None
    assert buscar_algo(app,"Teléfono: 927-731-605", "label") is not None
    assert buscar_algo(app,"Nombre de usuario: lazypeacock928", "label") is not None
    assert buscar_algo(app,"¿Está vacunado?: Si", "label") is not None
    assert buscar_algo(app,"Apellidos: Torres", "label") is not None
    assert buscar_algo(app,"Nombre: Carla", "label") is not None
    
def prueba3(app):

    action_item = buscar_algo(app, "Rastrear", "push button")
    assert action_item is not None

    start_date_item = buscar_algo(app, "start date", "text")
    end_date_item = buscar_algo(app, "end date", "text")
    
    start_date_item.set_text_contents("05/09/21 11:00")
    end_date_item.set_text_contents("07/09/21 11:00")

    action_item.do_action(0) 
    time.sleep(1)
    
    assert buscar_algo(app, "b09de819-4c9e-4b89-b131-03136e0bba7c", "label") is not None    
    assert buscar_algo(app, "Mario Montero", "label") is not None
    assert buscar_algo(app, "Fecha: 06/09/2021", "label") is not None
    assert buscar_algo(app, "Lugar: Biblioteca Cesar Montero", "label") is not None


def prueba4(app):
   
#Comprobamos el inicio y el final de la ventana que muestra los datos de últimos sitios visitados,
#comprobamos el primero y el último, por lo que damos por hecho que los datos generados en medio también son correctos.

#["Polideportivo Catalina Pastor","5076 Calle de Argumosa","13/08/2021 01:28:13","35.3"],

    item = buscar_algo(app, "FECHAFINAL", "label")
    assert (item.get_text(0,-1) == "13/08/2021 01:28:13")
    item = buscar_algo(app, "DIRECCIONFINAL", "label")
    assert (item.get_text(0,-1) == "5076 Calle de Argumosa")
    item = buscar_algo(app, "NOMBREFINAL", "label")
    assert (item.get_text(0,-1) == "Polideportivo Catalina Pastor")
    item = buscar_algo(app, "TEMPERATURAFINAL", "label")
    assert (item.get_text(0,-1) == "35.3")

#Biblioteca Lorenzo Guerrero","5245 Calle Nebrija","06/09/2021 20:09:52","37.2"
    
    item = buscar_algo(app, "FECHAINICIO", "label")
    assert (item.get_text(0,-1) == "06/09/2021 20:09:52")
    item = buscar_algo(app, "DIRECCIONINICIO", "label")
    assert (item.get_text(0,-1) == "5245 Calle Nebrija")    
    item = buscar_algo(app, "NOMBREINICIO", "label")
    assert (item.get_text(0,-1) == "Biblioteca Lorenzo Guerrero")
    item = buscar_algo(app, "TEMPERATURAINICIO", "label")
    assert (item.get_text(0,-1) == "37.2")


def prueba5(app):

    action_item = buscar_algo(app, "Rastrear", "push button")
    assert action_item is not None

    start_date_item = buscar_algo(app, "start date", "text")
    end_date_item = buscar_algo(app, "end date", "text")

    time.sleep(1)
    start_date_item.set_text_contents("05/09/18 11:00")
    end_date_item.set_text_contents("07/09/18 11:00")
    time.sleep(1)

    action_item.do_action(0)
    time.sleep(1)

    assert (buscar_algo(app, "No se han encontrado contactos cercanos en las \nfechas introducidas, pruebe con otras.", "label")) is not None

# prueba de base de datos mal
# usuario mal introducida

def prueba7(app):
    os.system('sudo systemctl stop docker')
    time.sleep(2)
    os.system('sudo systemctl stop docker.socket')
    time.sleep(1)
    introduce_text(app, "Buscar", "text", "Carla Torres")
    assert (buscar_algo(app, "Problemas con la conexión a la base de datos.", "label")) is not None
    os.system('sudo systemctl start docker')  
    os.system('sudo systemctl start docker.socket')


def prueba6(app):
    introduce_text(app, "Buscar", "text", "Charles Darwin")
    assert (buscar_algo(app, "Persona no encontrada, busque por Uuid o nombre y apellido", "label")) is not None

def prueba8(app: Atspi.Object) -> None:
    Atspi.set_timeout(800,-1)
    assert app.get_name() != "", "La interface no responde"

if __name__== "__main__":
    
    path = sys.argv[1]
    print(path)

    process, app = e2e.run(path)

    if app is None:
        process and process.kill()
        assert False, f"There is no aplication called: {path}"
    
    do, shows = e2e.perform_on(app)

    show("""
        Given the app was launched
        When we introduce the data from name: Carla, username: Torres
        The output of the app is a "track list" of people and a trail 
        of his movements
    """)

    try:
        prueba1(app)
        print('\033[92m', "Passed: Frame rastreo covid detected",'\033[0m')
        prueba2(app)
        print('\033[92m', "Passed: Data of the person introduced is correct",'\033[0m')
        prueba3(app)
        print('\033[92m', "Passed: Data of the person tracked in a expected time is correct",'\033[0m')
        prueba4(app)
        print("\n")
        print('\033[92m', "Passed: We test the whole proccess of tracking a person, we check if the first and the last sites data, this means that the data between them should be correct",'\033[0m')
        prueba5(app)
        print("\n")
        print('\033[92m', "Passed: If we introduce a date range without any results, a message will be displayed to tell the user this problem",'\033[0m')
        prueba6(app)
        print("\n")
        print('\033[92m', "Passed: If we introduce a uuid/name-surname that not exists, an error will be showed about this problem ",'\033[0m')
        
        prueba7(app)
        print("\n")
        print('\033[92m', "Passed: Error of database conexion showed",'\033[0m')
        prueba8(app)
        print("\n")
        print('\033[92m', "Passed: Concurrencia",'\033[0m')


    except Exception as e:
        show_not_passed(e)
        process and process.kill()
    
    process and process.kill()