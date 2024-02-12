import modulos.gestoralumnos as st
import ui.menu as m

if __name__ == '__main__':
    alumnos = {}
    isActive = True
    while isActive:
        try:
            m.menuPrincipal()
            op = int(input(': '))
        except ValueError:
            print('Dato Erroneo')
        else:
            if (op == 1):
                st.AddStudents(alumnos)
            elif (op == 2):
                st.DelStudent(alumnos)
            elif (op == 3):
                st.DelByName(alumnos)
            elif (op == 4):
                st.ListData(alumnos)
            elif (op == 5):
                st.SearchStudent(alumnos)
            elif (op == 6):
                st.AddGrades(alumnos)
            elif (op == 7):
                m.os.system('cls')
                print('Gracias por utizar nuestro sistema')
                isActive = False
                m.os.system('pause')
            else: 
                print('Opcion no valido')
                m.os.system('pause')