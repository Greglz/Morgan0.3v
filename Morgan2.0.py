import pickle
def a (str):
    pass
def b (str):
    pass

#DEFINIDAS VARIABLES E IMPORTACION DE LIBRERIA PICKLE

with open("/Users/dk34p/Desktop/data/user.pckl",'r') as b:
    user=b.read()
    b.close()
with open("/Users/dk34p/Desktop/data/pass.pckl",'r') as k:
    pas=k.read()
    k.close()

print ("1)Inicio de sesión")
print("2)Registro")
c=input()
if c=="1":
    print("Ingrese nombre de usuario")
    a=input()
    if a==user:
        print("Ingrese contraseña")
        n=input()
        j=0
        if n==pas:
            print("Bienvenido",user)
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
#INGRESAR DATOS Y EDITAR EL URL PARA GUARDAR LOS DATOS EN ARCHIVOS 
if c=="2":
    print("Buenas, Por favor ingrese un nombre de usuario a registrar")
    user2=input()
    with open("/Users/dk34p/Desktop/data/user.pckl",'w') as u:
        u.write(user2)
        u.close()
    print ("Ingrese su nueva contraseña")
    pas2=input()
    with open("/Users/dk34p/Desktop/data/pass.pckl",'w') as p:
        p.write(pas2)
        p.close()

