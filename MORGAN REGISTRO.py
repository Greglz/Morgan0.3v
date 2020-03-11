import pickle
import time
import pickle
import oss
def a (str):
    pass
def b (str):
    pass

#DEFINIDAS VARIABLES E IMPORTACION DE LIBRERIA PICKLE
def menu():
    try:

        print ("1)Inicio de sesión")
        print("2)Registro")
        c= input("Ingrese una opcion: ")
        os.system("cls")
    except Exception as e:
        print("Hubo un problema eligiendo una opción")
        return "none"
    return c    

if __name__=="__main__":
    while True:
        c= menu()
        if c=="1":
            try:

                with open("user.pckl",'r') as b:
                    user=b.read()
                    b.close()
                with open("pass.pckl",'r') as k:
                    pas=k.read()
                    k.close()
                print("Ingrese nombre de usuario: ")
                a=input()
                if a==user:
                    print("Ingrese contraseña: ")
                    n=input()
                    j=0
                    if n==pas:
                        print("Registrado Exitosamente")
                        exit()

                    else:
                        while j<3:
                            print("Contraseña incorrecta, intente nuevamente")
                            n=input()
                            j+=1
                        if j==3:
                            print("Ha excedido el número máximo de intentos, el programa se cerrará")
                else:
                    i=0
                    while i<3:
                        print("Nombre de usuario incorrecto, intente nuevamente")
                        a=input()
                        i+=1
                    if i==3:
                        print("Ha excedido el numero máximo de intentos, el programa se cerrará")
            except Exception as e:
                print("No hay datos registrados")
                time.sleep(3)



       
        
        #INGRESAR DATOS Y EDITAR EL URL PARA GUARDAR LOS DATOS EN ARCHIVOS 
        elif c=="2":
            print("Buenas, Por favor ingrese un nombre de usuario a registrar")
            user2=input()
            with open("user.pckl",'w') as u:
                u.write(user2)
                u.close()
            print ("Ingrese su nueva contraseña")
            pas2=input()
            with open("pass.pckl",'w') as p:
                p.write(pas2)
                p.close()
            os.system("cls")
            

