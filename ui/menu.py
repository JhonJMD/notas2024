import os
import ui.title as t

def menuPrincipal():
    os.system('cls')
    opciones = ['Agregar Alumno','Elimniar Alumno por ID','Eliminar Alumno por Nombre','Listar Alumnos Registrados','Buscar Alumno','Agregar Notas','Salir']
    t.headerMenuPrincipal()
    for i, item in enumerate(opciones):
        print(f'{i+1}. {item}')

def menuNotas():
    os.system("cls")
    subMenuNotas = ['Parciales', 'Quices', 'Trabajos', 'Regresar al menú']
    t.headerRegNotas()
    for i, item in enumerate(subMenuNotas):
            print(f'{i+1}. {item}')