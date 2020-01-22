from getpass import getpass
import os
import sys
import pickle
import subprocess
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
wikipedia.set_lang('es')
engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
print(voices[2].id)
engine.setProperty('voices', voices[0].id)
r= sr.Recognizer()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0  and hour<12:
        speak("Buenos días")
    elif hour>=12 and hour<18:
        speak("Buenas tardes")
    else:
        speak("Buenas noches")
wishMe()
print('                   Morgan v1.0                    ')
print()
# AQUI SE AUTENTICA EL USUARIO Y BASE DE DATOS
# DEBE SER EDITADO CON EL ARCHIVO MORGAN 2.0.PY
# PARA ASI PODER ACCEDER AL REGISTRO DE ESTE
# DEBE EDITAR EL URL DE LOS ARCHIVOS PARA ENTRAR AL PROGRAMA
with open("/Users/dk34p/Desktop/data/user.pckl",'r') as usera:
    user=usera.read()
    usera.close()
with open("/Users/dk34p/Desktop/data/pass.pckl",'r') as passa:
    pas=passa.read()
    passa.close()
print("Por favor, Ingrese el usuario")
speak('Por favor,Ingrese el usuario')
a=input()
#autenticacion de usuario y pass
while a!=user:
    print("Usuario no registrado o incorrecto")
    speak('Usuario no registrado o incorrecto')
    print("Ingrese nuevamente por favor.")
    speak('Ingrese nuevamente por favor')
    a=input()
    if a!=user:
        print("Usuario incorrecto. el programa se cerrará")
        speak('Usuario incorrecto. el programa se cerrará')
        x=input()
        os.system('cls')
        sys.exit()
print("Ingrese contraseña:")
speak('Ingrese contraseña')
pasx=getpass()
while pasx!=pas:
    print("Contraseña incorrecta, por favor intente nuevamente")
    speak('Contraseña incorrecta.. por favor intente nuevamente')
    pasx=input()
    if pasx!=pas:
        print("Contraseña incorrecta. El programa se cerrará")
        speak('Contraseña incorecta. El programa se cerrará')
        x=input()
        os.system('cls')
        sys.exit()
os.system('cls')
os.system('C:/Users/dk34p/AppData/Local/Programs/Python/Python38-32/pythonw.exe')
#inicio del programa
print ("-----------------------------------------------")
print (f"               Bienvenido {user}            ")
print ("-----------------------------------------------")
speak(f'Bienvenido{user}')
print("Dime, ¿qué puedo hacer por tí?")
speak('Dime,¿Qué puedo hacer por ti?')
def tomarcomando():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='es-mx')
        print(query)
    except Exception as e: #U KNOW PRINT E WAS A REPLY?
        #print (e)
        print('Por favor dilo de nuevo')
        return "none"
    return query
if __name__ == "__main__":
    while True:
        query=tomarcomando().lower()
        if 'qué sabes sobre' in query:
            print (query)
            speak(f'Buscando en Wikipedia... por favor espere')
            query= query.replace('qué sabes sobre', '')
            results= wikipedia.summary(query, sentences=2)
            speak("Según Wikipedia")
            print(results)
            speak(results)
        elif 'abre youtube' in query:
            print (query)
            webbrowser.open('www.youtube.com')
            speak("Accediendo a Youtube")
        elif 'abre facebook' in query:
            webbrowser.open('www.facebook.com')
            speak("Accediendo a Facebook")
        elif 'abre spotify' in query:
            print (query)
            subprocess.Popen(['Spotify'])
            print("Accediendo a Spotify")
            speak('Accediendo a Spotify')
        elif 'abre league of legends' in query:
            print (query)
            subprocess.Popen(['C:/Riot Games/League of Legends/LeagueClient.exe'])
            print("Accediendo a League of legends")
            speak('Accediendo a Lig of legends')
        elif 'qué hora es' in query:
            print (query)
            strTime= datetime.datetime.now().strftime("%H:%M")
            print(strTime)
            speak(f"La hora es {strTime}")
        elif 'dime la hora' in query:
            print (query)
            strTime= datetime.datetime.now().strftime("%H:%M")
            print(strTime)
            speak(f"La hora es {strTime}")
        elif 'gracias' in query:
            print (query)
            speak('No hay de qué')
        elif 'abre visual code' in query:
            print (query)
            subprocess.Popen(['C:/Users/dk34p/AppData/Local/Programs/Microsoft VS Code/code.exe'])
            print("Accediendo a Visual Code")
            speak('Accediendo a visual code')
        elif 'abre whatsapp' in query:
            print(query)
            webbrowser.open('https://web.whatsapp.com/')
            print("Accediendo a WhatsApp")
            speak('Accediendo a WhatsApp')
        elif 'abre netflix' in query:
            print(query)
            webbrowser.open('www.netflix.com')
            print('Accediendo a Netflix')
            speak('Accediendo a Netflix')
        elif 'cierra sesión' in query:
            speak('Cerrando sesión')
            os.system('shutdown -l')
        elif 'limpia el terminal' in query:
            speak('Terminal Limpiado.')
            os.system('cls')
        elif 'quién soy' in query:
            with open('/Users/dk34p/desktop/data/nc.pckl', 'rb') as nc:
                nca=pickle.load(nc)
                nc.close()
            with open('/Users/dk34p/desktop/data/ed.pckl','rb') as ed:
                eda=pickle.load(ed)
                ed.close()
            with open('/Users/dk34p/desktop/data/fdn.pckl','rb') as fn:
                fdn=pickle.load(fn)
                fn.close()
            with open('/Users/dk34p/desktop/data/rut.pckl','rb') as ru:
                rut=pickle.load(ru)
                ru.close()
            with open('/Users/dk34p/desktop/data/city.pckl','rb') as cit:
                city=pickle.load(cit)
                cit.close()
            with open('/Users/dk34p/desktop/data/celn.pckl','rb') as celn:
                celna=pickle.load(celn)
                celn.close()
            print('--------------------------------')
            print('           Tus datos son:       ')
            print('--------------------------------')
            print()
            print("Nombre : ",nca)
            speak(f'Su nombre es {nca}')
            print("Edad:",eda)
            speak(f'Tiene {eda} años')
            print("Fecha de nacimiento: " ,fdn)
            speak(f'Nació el {fdn}')
            print('Rut:',rut)
            speak(f'Su rut es {rut}')
            print('Ciudad:',city)
            speak(f'Vive en la ciudad de {city} ')
            print(f'Número de teléfono:',celna)
            speak(f'Su número de teléfono es {celna}')
        elif 'apaga el equipo' in query:
            speak('Apagando el equipo')
            os.system('shutdown')
        elif 'apaga el computador' in query:
            speak('Apagando el computador')
            os.system('shutdown ')    
        elif 'reinicia el computador' in query:
            speak('Reiniciando el computador')
            os.system('shutdown -r -t 1')
        elif 'suspende el equipo' in query:
            speak('Suspendiendo el equipo')
            os.system('rundll32.exe powrprof.dll, SetSuspendState 0,1,0')
        elif 'suspender equipo' in query:
            speak('Suspendiendo el equipo')
            os.system('rundll32.exe powrprof.dll, SetSuspendState 0,1,0')
        elif 'abrir gato' in query:
            print("-----------------------")
            print("    Hackeando NASA     ")
            speak('Hackeando NASA')
            print("-----------------------")
            print()
            print()
            print("Inicio de Hackeo, espere")
            speak('Inicio de hackeo, espere')
            print('Hackeo al 10%')
            speak('Hackeo al 10%')
            print("Hackeo al 20%")
            speak('Hackeo al 20%')
            print('Hackeo al 30%')
            speak('Hackeo al 30%')
            print("Hackeo al 40%")
            speak('Hackeo al 40%')
            print('Hackeo al 50%')
            speak('Hackeo al 50%')
            print("Hackeo al 60%")
            speak('Hackeo al 60%')
            print('Hackeo al 70%')
            speak('Hackeo al 70%')
            print("Hackeo al 80%")
            speak('Hackeo al 80%')
            print('Hackeo al 90%')
            speak('Hackeo al 90%')
            print("Hackeo al 100%")
            speak('Hackeo al 100%')
            print('Hackeo completo')
            speak('Hackeo completo')
            speak(f'{user}... Según los documentos obtenidos. Hector es el ser mas wueón del universo')
        elif 'te odio' in query:
            speak('No.. yo, yo, yo te amo no te vaaayaaaaaas. -muere-')
        elif 'establece alarma' in query:
            speak('A que hora quiere establecer alarma?')
            tomarcomando()
        elif 'cierra Spotify' in query:
            os.system('TASKKILL /F /IM Spotify.exe')
            speak('Cerrando Spotify')
        elif 'cierre visual code' in query:
            os.system('TASKKILL /F /IM code.exe')
            speak('Cerrando Visual Code')
        elif 'close visual code' in query:
            os.system('TASKKILL /F /IM code.exe')
            speak('Cerrando Visual Code')
        elif 'cierra torrent' in query:
            os.system('TASKKILL /F /IM uTorrent.exe')
        elif '+' in query:
            query=query.replace("+", ' ')
            query=query.split()
            a=int(query[0])
            b=int(query[1])
            re=a+b
            print(re)
            speak(f'El resultado es {re}')
        elif 'por' in query:
            query=query.replace("por", ' ')
            query=query.split()
            a=int(query[0])
            b=int(query[1])
            re=a*b
            print(f'El resultado es {re}')
            speak(f'El resultado es {re}')
        elif '*' in query:
            query=query.replace("*", ' ')
            query=query.split()
            a=int(query[0])
            b=int(query[1])
            re=a*b
            print(f'El resultado es {re}')
            speak(f'El resultado es {re}')
        elif 'menos' in query:
            query=query.replace("menos", ' ')
            query=query.split()
            a=int(query[0])
            b=int(query[1])
            re=a-b
            print(f'El resultado es {re}')
            speak(f'El resultado es {re}')
        elif 'dividido' in query:
            query=query.replace("dividido", ' ')
            query=query.split()
            a=int(query[0])
            b=int(query[1])
            re=a/b
            int(re)
            print(f'El resultado es {re}')
            speak(f'El resultado es {re}')
        elif 'raíz cuadrada de' in query:
            import math
            query=query.replace('raíz cuadrada de', '')
            query=query.split()
            a=int(query[0])
            b=math.sqrt(a)
            print('El resultado es : ' ,b)
            speak(f'El resultado es: {b}')
        elif 'cuál es la raiz cuadrada de' in query:
            import math
            query=query.replace('cuál es la raiz cuadrada de','')
            query.query.split()
            a=int(query[0])
            b=math.sqrt(a)
            print("El resultado es :",b)
            speak(f"El resultado es: {b}")
        elif 'Abre Telegram' in query:
            subprocess.Popen(['C:/Users/dk34p/AppData/Roaming/Telegram Desktop/Telegram.exe'])
            print("Abriendo Telegram")
            speak("Abriendo Telegram")


        
