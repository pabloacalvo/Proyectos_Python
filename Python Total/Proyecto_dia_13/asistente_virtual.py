import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio

# Escuchar microfono y devolver el audio como texto

def transformar_audio_en_texto():
    # Almacenar el recognizer en variable
    r = sr.Recognizer()
    # Configurar el microfono
    with sr.Microphone() as origen:
        # tiempo de espera
        r.pause_threshold = 0.8
        # informar que ccomenzo la grabacion
        print('Ya podes hablar')
        # Guardar audio
        audio = r.listen(origen)
        try:
            # Buscar en google
            pedido = r.recognize_google(audio, language='es-ar')
            # prueba de que se convirtio la voz en texto
            print('Dijiste:' + pedido)
            # Devolver pedido
            return pedido
        except sr.UnknownValueError:
            #prueba que no comprendio el audio
            print('Ups no entendi')
            #Devolver error
            return 'Sigo esperando'
        # Grabo audio pero no lo pudo transformar
        except sr.RequestError:
            # prueba que no comprendio el audio
            print('Ups no hay servicio')
            # Devolver error
            return 'Sigo esperando'
        # Error inesperado
        except:
            # prueba que no comprendio el audio
            print('Algo salio mal')
            # Devolver error
            return 'Sigo esperando'


# Funcion para que el asistente pueda ser escuchado

def hablar(mensaje):
    # Encender el motor de pyttsx3
    engine = pyttsx3.init()
    # Seleccionar voz
    engine.setProperty('voice',id2)
    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

# Informar dia de la  semana
def pedir_dia():
    #crear variables
    dia = datetime.date.today()
    print(dia)
    #crear variable dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)
    # Diccionario dia
    calendario = {0:'Lunes',
                  1:'Martes',
                  2:'Miércoles',
                  3:'Jueves',
                  6:'Viernes',
                  7:'Sabadp',
                  8:'Domingo'}
    # Decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')



def pedir_hora():
    # Crear variable hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    #decir hora
    hablar(hora)

#funcion saludo inicial
def saludo_inicial():
    # Momento del dia
    hora = datetime.datetime.now()
    if 6 < hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen dia'
    else:
        momento = 'Buenas tardes'
    hablar(f'{momento}, soy rocio, tu asistente personal. Decime en que te puedo ayudar')

def pedir_cosas():
    saludo_inicial()
    # variable de corte
    comenzar = True
    while comenzar:
        #activar el microfono y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()
        if 'abrir youtube' in pedido:
            hablar('Con gusto, voy abrir youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, vamos abrir el navegador')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'qué día es' in pedido:
            pedir_dia()
            continue
        elif 'buscar en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia','')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido,sentences=1)
            hablar('wikipedia dice lo siguiente')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo, estoy en eso')
            pedido = pedido.replace('busca en internet','')
            pywhatkit.search(pedido)
            hablar('esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontre, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdon, no encontre lo que buscabas')
                continue
        elif 'adiós' in pedido:
            hablar('Me voy a descansar, cualquier cosa me avisas')
            break



# Opciones de voz/idioma
"""engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)"""
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
pedir_cosas()



