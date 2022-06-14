import telebot
import requests
import schedule
import json
import webservice.web_service_empresa as wse
import webservice.web_service_personas as wsp

bot = telebot.TeleBot("5423228670:AAFgJSwGYkE2NBfaupJcpbYqdxmXjB-oAYA")

#Funciones que calculan el mensaje correspondiente a los comandos y peticiones del cliente

def recopilar_todos_comandos_help():

    mensaje = "Ayuda de todos los comandos disponibles para el bot\n"
    mensaje += "\n CUENTA"
    mensaje += "\n ---------------------------------------------------------------------------"
    mensaje += "\n /IniciarSesion: Te enseñaré a iniciar sesión"
    mensaje += "\n /CrearCuenta: Te enseñaré a crearte una cuenta"
    mensaje += "\n ---------------------------------------------------------------------------"
    mensaje += "\n COMO USAR LA APLICACIÓN"
    mensaje += "\n ---------------------------------------------------------------------------"
    mensaje += "\n /DescargarAplicacion: Te diré donde descargarte la apk para el móvil"
    mensaje += "\n /UsarDesktop: Te diré la URL para usar Meetfever Desktop"
    mensaje += "\n ---------------------------------------------------------------------------"
    mensaje += "\n FUNCIONALIDADES INTERESANTES DE LA APP"
    mensaje += "\n ---------------------------------------------------------------------------"
    mensaje += "\n /Opinion: Te diré como crear una opinión desde la aplicación móvil"
    mensaje += "\n /GenerarQR: Te diré como generar el código QR de tu perfil, y como escanear ese QR para seguir a alguien"
    mensaje += "\n ---------------------------------------------------------------------------"
    mensaje += "\n ESTADISTICAS DE LA APLICACION"
    mensaje += "\n ---------------------------------------------------------------------------"
    mensaje += "\n /PersonasRegistradas: Te diré cuantas personas se han registrado en la aplicación"
    mensaje += "\n /PersonasActivas: Te diré cuantas personas usan la aplicación a día de hoy"
    mensaje += "\n /EmpresasRegistradas: Te diré cuantas empresas se han registrado en la aplicación"
    mensaje += "\n /EmpresasActivas: Te diré cuantas empesas se usan la aplicación a día de hoy"
    
    return str(mensaje)
  
def comoIniciarSesion():
    mensaje = "Para iniciar sesión tenemos dos formas, una desde la aplicación móvil y la otra desde la aplicación web, "
    mensaje += "para obtener ambos puedes irte al siguiente enlace:\nhttps://edu-meetfever.odoo.com/descargas\nLo primero que "
    mensaje += "te vas a encontrar es la pantalla de crear cuenta o inicio de sesión. Pulsas el botón de Iniciar Sesión"
    mensaje += "\nEspero haberte ayudado y gracias por usar MeetFever!"
    
    return mensaje

def comoCrearteUnCuenta():
    mensaje = "Para crearte una cuenta tenemos dos formas, una desde la aplicación móvil y la otra desde la aplicación web, "
    mensaje += "para obtener ambos puedes irte al siguiente enlace:\nhttps://edu-meetfever.odoo.com/descargas\nLo primero que "
    mensaje += "te vas a encontrar es la pantalla de crear cuenta o inicio de sesión. Pulsas el botón de crear cuenta"
    mensaje += "\nEspero haberte ayudado y gracias por usar MeetFever!"
    
    return mensaje

def dondeDescargarAplicacion():
    mensaje = "Para descargarte la apliación de móvil solo tienes que acceder al siguiente enlace:"
    mensaje += "\n https://drive.google.com/file/d/1qUOYR4GWusBGq-vbe7aVleWeSajRFkTe/view?usp=sharing"
    mensaje += "\nEspero haberte ayudado y gracias por usar MeetFever!"
        
    return mensaje

def UrlDesktop():
    mensaje = "El enlace a seguir para usar la aplicación web es el siguiente:"
    mensaje += "\n     https://meetfever.eu/app/login"
    mensaje += "\nEspero haberte ayudado y gracias por usar MeetFever!"
    return mensaje

def comoHacerUnaOpinion():
    mensaje = "Para poder crear una opinión, desde la apliación para móviles:\n\n1: Hay que pulsar el botón "
    mensaje += "que nos acompaña continuamente abajo a la derecha en las tres pantallas principales, donde puedes ver la parte "
    mensaje += "de personas, locales y experiencias y opiniones.\n\n2: Al abrirse el despliegue con varias opciones, hay que "
    mensaje += "pulsar el donde pone publicar Feev! con el símbolo de una pluma al lado.\n\n3: Rellenar los datos que nos piden.\n"
    mensaje += "\n4: Pulsar el botón de publicar Feev!"
    mensaje += "\nEspero haberte ayudado y gracias por usar MeetFever!"
    return mensaje

def ComoGenerarElQR():
    mensaje = "Para generar el QR para que otro usuario nos pueda seguir:\n\n1: En nuestro perfil, arriba a la derecha nos aparecerá "
    mensaje += "una pequeña imagen de un pequeño QR, pulsando ahí se generará el QR para que otros usuarios te puedan seguir."
    mensaje += "\n\n2: El scanner se abre en la aplicación móvil desde el botón de + que aparece en la pantalla del móvil "
    mensaje += "seleccionando la opción de Meet follower scanner."
    mensaje += "\nEspero haberte ayudado y gracias por usar MeetFever!"
    return mensaje


def personasRegistradas():
    
    personas_registradas = str(wsp.get_personas_registradas()[0])
    caracteres = ["d","i","c","t","_","v","a","l","u","e","s","(","[","]",")"]
    personas_registradas = ''.join(x for x in personas_registradas if x not in caracteres)
    mensaje = "Actualmente hay un total de " + personas_registradas + " personas registradas, no te quedes atrás." 
    mensaje += "\nEspero haberte ayudado y gracias por usar MeetFever!"
    return mensaje

def personasActivas():
    personas_activas = str(wsp.get_personas_activas()[0])
    caracteres = ["d","i","c","t","_","v","a","l","u","e","s","(","[","]",")"]
    personas_activas = ''.join(x for x in personas_activas if x not in caracteres)
    mensaje = "Actualmente hay un total de " + personas_activas + " personas activas, sé el primero en ver sus opiniones." 
    mensaje += "\nEspero haberte ayudado y gracias por usar MeetFever!"
    return mensaje

def empresasRegistradas():
    empresas_registradas = str(wse.get_empresas_registradas()[0])
    caracteres = ["d","i","c","t","_","v","a","l","u","e","s","(","[","]",")"]
    empresas_registradas = ''.join(x for x in empresas_registradas if x not in caracteres)
    mensaje = "Actualmente hay un total de " + empresas_registradas + " empresas registradas." 
    mensaje += "\nEspero haberte ayudado y gracias por usar MeetFever!"
    return mensaje

def empresasActivas():
    empresas_activas = str(wse.get_empresas_activas()[0])
    caracteres = ["d","i","c","t","_","v","a","l","u","e","s","(","[","]",")"]
    empresas_activas = ''.join(x for x in empresas_activas if x not in caracteres)
    mensaje = "Actualmente hay un total de " + empresas_activas + " empresas activas, sé el primero en comprar sus experiencias." 
    mensaje += "\nEspero haberte ayudado y gracias por usar MeetFever!"
    return mensaje


#Leer y entender los comandos que manda el cliente al BOT para poder llamar a las funciones anteriores y devolver el 
#Correspondiente mensaje a cada comando


@bot.message_handler(commands=['start','Start'])
def send_welcome(message):
    bot.reply_to(message, recopilar_todos_comandos_help())

@bot.message_handler(commands=['help','Help','HELP'])
def send_welcome(message):
    bot.reply_to(message, recopilar_todos_comandos_help())
 
@bot.message_handler(commands=['IniciarSesion','Iniciarsesion','iniciarsesion','iniciarSesion'])
def respuestaInicioSesion(message):
        bot.reply_to(message, comoIniciarSesion())
        
@bot.message_handler(commands=['CrearCuenta','Crearcuenta','crearcuenta','crearCuenta'])
def respuestaCrearCuenta(message):
        bot.reply_to(message, comoCrearteUnCuenta())

@bot.message_handler(commands=['DescargarAplicacion','Descargaraplicacion','descargarAplicacion','descargaraplicacion'])
def RespuestaDescargarApp(message):
        bot.reply_to(message, dondeDescargarAplicacion())
        
@bot.message_handler(commands=['UsarDesktop','Usardesktop','usarDesktop','usardesktop'])
def RespuestaUrlDekstop(message):
        bot.reply_to(message, UrlDesktop())
        
@bot.message_handler(commands=['Opinion','opinion'])
def RespuestaUrlDekstop(message):
        bot.reply_to(message, comoHacerUnaOpinion())

@bot.message_handler(commands=['GenerarQR','generarQR','Generarqr','generarqr','GenerarQr', 'generarQr'])
def RespuestaUrlDekstop(message):
        bot.reply_to(message, ComoGenerarElQR())

@bot.message_handler(commands=['PersonasRegistradas','Personasregistradas','personasRegistradas','personasregistradas'])
def respuestaInicioSesion(message):
        bot.reply_to(message, personasRegistradas())


@bot.message_handler(commands=['PersonasActivas','Personasactivas','personasActivas','personasactivas'])
def respuestaInicioSesion(message):
        bot.reply_to(message, personasActivas())

@bot.message_handler(commands=['EmpresasRegistradas','Empresasregistradas','empresasRegistradas','empresasregistradas'])
def respuestaInicioSesion(message):
        bot.reply_to(message, empresasRegistradas())

@bot.message_handler(commands=['EmpresasActivas','Empresasactivas','empresasActivas','empresasactivas'])
def respuestaInicioSesion(message):
        bot.reply_to(message, empresasActivas())


bot.polling()