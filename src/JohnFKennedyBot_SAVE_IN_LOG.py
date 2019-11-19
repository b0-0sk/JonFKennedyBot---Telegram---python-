# -*- coding: utf-8 -*-


import telebot # Librería de la API del bot.

from telebot import types # Tipos para la API del bot.

import time # Librería para hacer que el programa que controla el bot no se acabe.

from datetime import datetime, date

import os.path as path
from encodings import undefined

import sys
from atk import Document
from cgitb import text
reload(sys)
sys.setdefaultencoding('utf8')



# Aqui definiremos aparte del Token, por ejemplo los ids de los grupos y pondríamos grupo= -XXXXX



token = "891479632:AAEMeE7Ca15mkC0sVoY7g8F3I5F2MSktUxE" # token del bot.




AYUDA = 'Puedes utilizar los siguientes comandos : \n\n/info - Guia para utilizar el bot \n         · /info [keyword] [date dd/mm/yyyy hh/mm/ss]\n/hola - Saludo del Bot \n/b0_0sk - Informacion sobre b0_0sk \n\n'

SET_KEYWORD = 'Introduiex la paraula que vols que introduiexi.\n'

GRUPO_BOT = "-270997133" #Definimos que cuando pongamos la palabra grupo lo vincule con el Id del grupo donde nos encontremos.  Al meter el bot en un grupo, en la propia consola nos saldrá


JohnFKennedyBot = telebot.TeleBot(token) # Creamos el objeto de nuestro bot.

#############################################
#Listener

@JohnFKennedyBot.message_handler(commands=['start']) # Indicamos que lo siguiente va a controlar el comando '/ayuda'

def welcome(messages): # Definimos una función que resuleva lo que necesitemos.

    
    ###    
    ### MENSAJE DE BIENBENIDA    
    ### 
    
    cid = messages.chat.id # Guardamos el ID de la conversación para poder responder.
         
    JohnFKennedyBot.send_message(cid, "Hola, bienvenido!")
   
   


@JohnFKennedyBot.message_handler(commands=['ayuda']) # Indicamos que lo siguiente va a controlar el comando '/ayuda'

def command_ayuda(messages): # Definimos una función que resuleva lo que necesitemos.

    cid = messages.chat.id # Guardamos el ID de la conversación para poder responder.

    JohnFKennedyBot.send_chat_action(cid, 'typing') # Enviando ...

    time.sleep(1) #La respuesta del bot tarda 1 segundo en ejecutarse

    JohnFKennedyBot.send_message( cid, AYUDA) # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.


@JohnFKennedyBot.message_handler(commands=['search']) # Indicamos que lo siguiente va a controlar el comando '/info'

def command_info(messages): # Definimos una función que resuleva lo que necesitemos.
    
    cid = messages.chat.id # Guardamos el ID de la conversación para poder responder.
    
    keyword = messages.text.split()
    JohnFKennedyBot.send_message(cid, keyword[1])
    documento = open( str(cid) +".txt")
    linea = documento.readline()
    CountLines = 0
    while linea != "":
      if keyword[1] in linea:
          
          InfoWords= linea.split("|")
          InfoWords[3] = InfoWords[3].replace(keyword[1],"*"+keyword[1]+"*")
          
          JohnFKennedyBot.send_message(cid, "    - User: ["+InfoWords[0] +"]\n    - Date: ["+ InfoWords[2]+"]\n    - Message: "+ InfoWords[3],parse_mode= 'Markdown')
          CountLines = CountLines + 1
      linea = documento.readline()

         
           
    #dato = documento.read() 
        
        
    #JohnFKennedyBot.send_message( cid, dato)
    #documento.close()
    
    
    
@JohnFKennedyBot.message_handler(commands=['historial']) # Indicamos que lo siguiente va a controlar el comando '/set_channel' INUTIL

def historial(messages): # Definimos una función que resuleva lo que necesitemos.

    cid = messages.chat.id # Guardamos el ID de la conversación para poder responder.
    
    JohnFKennedyBot.send_chat_action(cid, 'typing') # Enviando ...
    
    JohnFKennedyBot.send_message( cid, SET_KEYWORD) # Nos devolvera el mensaje que previamente hemos escrito en la variable SET_CHANNEL.


@JohnFKennedyBot.message_handler(commands=['search']) # Indicamos que lo siguiente va a controlar el comando '/set_channel'

def search(messages): # Definimos una función que resuleva lo que necesitemos.

    cid = messages.chat.id # Guardamos el ID de la conversación para poder responder.
    
    JohnFKennedyBot.send_chat_action(cid, 'typing') # Enviando ...
    
    JohnFKennedyBot.send_message( cid, SET_CHANNEL) # Nos devolvera el mensaje que previamente hemos escrito en la variable SET_CHANNEL.



def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
  
    now = datetime.now() # Variable para guardar la fecha del mensaje
    for word in messages: # Por cada dato 'm' en el dato 'messages'
             
        cid = word.chat.id # Guardamos el ID de la conversación para poder responder.  
                           
        cid = word.chat.id # El Cid es el identificador del chat los negativos son grupos y positivos los usuarios
        if cid != word.chat.id:
            cid = word.chat.id

        
        clientDatetime = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        clientText = word.text
        if cid > 0: # Conversacion privada

            clientName =  str(word.chat.first_name) # nom del chat

            
            clientChat = str(word.chat)

            nombre_documento = str(cid)

            mensaje = clientName + "|" + str(cid) + "|" + clientDatetime +"|" + clientText+"| "     # Si 'cid' es positivo, usaremos 'm.chat.first_name' para el nombre.
            

        elif cid < 0: # Conversacion grupal


            groupName = str(word.chat.title) # Name group
            clientName = str(word.from_user.first_name) #Name user

            mensaje = clientName + "|" + str(cid) + "|" + clientDatetime +"|" + clientText+"| "
            nombre_documento = str(cid)
            
            #for word in messages:
             #  print (word)
            

        
        
        # si el documento existe escribe debajo
        if path.exists(nombre_documento + '.txt') == True:
            #JohnFKennedyBot.send_message(cid, "Existe") //Chivato para comproba si el fichero existe 
            documentoNuevo = open(nombre_documento + '.txt', 'a') # Abrimos nuestro fichero log en modo 'Añadir'.

        
        # si no existe crearlo y añade la siguiente linia name / cid / datetime / message
        elif path.exists(nombre_documento + '.txt') == False:

            #JohnFKennedyBot.send_message(cid, "No existe")//Chivato para comproba si el fichero no existe 
            documentoNuevo = open(nombre_documento + '.txt', 'a') # Abrimos nuestro fichero log en modo 'Añadir'.
            documentoNuevo.write(" Name  / cid / Datetime / message" + "\n")
           

        documentoNuevo.write(mensaje + "\n") # Escribimos la linea de log en el fichero.
        documentoNuevo.close() # Cerramos el fichero para que se guarde.
        
        
               
        
JohnFKennedyBot.set_update_listener(listener) # Así, le decimos al bot que utilice como función listener nuestra función 'listener' declarada arriba.
JohnFKennedyBot.polling()