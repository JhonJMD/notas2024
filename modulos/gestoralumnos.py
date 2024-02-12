from tabulate import tabulate
import ui.title as t
import ui.menu as m
import os
alumno = {
    'id':'',
    'nombre':'',
    'edad':'',
    'email':''
}

def AddStudents(alumnos:dict):
    os.system('cls')
    t.headerRegAlumno()
    id = input('Ingrese el id : ')
    nombre = input('Ingrese el nombre: ')
    edad = int(input(f'Ingrese la edad de {nombre}: '))
    email = input(f'Ingrese el email de {nombre}: ')
    alumno = {
        'id':id,
        'nombre':nombre,
        'edad':edad,
        'email':email 
    }
    #update actualiza y agrega
    alumnos.update({id:alumno})

def SearchStudent(alumnos:dict):
    os.system('cls')
    t.headerSearchSt()
    id = input('Ingrese el numero de id del Estudiante: ')
    #get busca el valor de la llave
    data  = alumnos.get(id,False)
    if(type(data) == dict):
        print(data)
        os.system('pause')
    elif((type(data) == bool) and (data == False)):
        print('El Estudiante no se encuentra registrado')
        os.system('pause')

def ListData(alumnos:dict):
    os.system('cls')
    if len(alumnos) > 0:
        info = []
        for key, value in alumnos.items():
            info.append(value)
        print(tabulate(info,headers="keys", tablefmt='grid'))
        os.system('pause')
    else:
        print('No se encuentra ningun alumno registrado')
        os.system('pause')

def ValidateStudent(alumnos:dict, id) -> bool:
    return bool(alumnos.get(id,''))
    

def DelStudent(alumnos: dict):
    os.system('cls')
    t.headerDelAlumno()
    id = input('Ingrese el numero de id del Estudiante: ')
    if ValidateStudent(alumnos,id) == True:
        alumnos.pop(id)
    else:
        print('El Estudiante no se encuentra registrado')
        os.system('pause')

def DelByName(alumnos : dict):
    os.system('cls')
    t.headerDelNameAlumno()
    nombre = input('Ingrese el nombre del Estudiante: ')
    exist = False
    for llave, valor in alumnos.items():
        if (nombre in valor['nombre']):
            alumnos.pop(llave)
            exist = True
            break
    if exist == False:
        print('El nombre ingresado no se encuentra')
        os.system('pause')

def AddGrades(alumnos: dict):
    os.system('cls')
    t.headerRegNotas()
    id = input('Ingrese el ID del Estudiante: ')
    if id in alumnos:
        alumno = alumnos[id]
        notas = alumno.get('calificaciones', {'parciales': [], 'quices': [], 'trabajos': []})
        while True:
            os.system('cls')
            m.menuNotas()
            try:
                opcion = input(': ')
            except ValueError:
                print('Dato invalido')
            else:
                if opcion == '1':
                    tipoNota = 'parciales'
                elif opcion == '2':
                    tipoNota = 'quices'
                elif opcion == '3':
                    tipoNota = 'trabajos'
                elif opcion == '4':
                    break
                else:
                    print('Opción no válida')
                    os.system('pause')
                    continue
                rta = True
                while rta:
                    try:
                        nota = float(input(f"Ingrese la nota {(len(notas[tipoNota])) + 1} de {tipoNota}: "))
                    except ValueError:
                        print('Dato invalido')
                    else:
                        notas[tipoNota].append(nota)
                        rta = bool(input(f'Desea ingresar otra nota {tipoNota} (S(Si)/Enter(No)): '))
        alumno['calificaciones'] = notas
    else:
        print('El ID ingresado no se encuentra')
        os.system('pause')
