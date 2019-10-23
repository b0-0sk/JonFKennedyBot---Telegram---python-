# -*- coding: utf-8 -*-



import telebot # Librería de la API del bot.

from telebot import types # Tipos para la API del bot.

import time # Librería para hacer que el programa que controla el bot no se acabe.

from datetime import datetime

import os.path as path




# Aqui definiremos aparte del Token, por ejemplo los ids de los grupos y pondríamos grupo= -XXXXX



TOKEN = "891479632:AAEMeE7Ca15mkC0sVoY7g8F3I5F2MSktUxE" # token del bot.




AYUDA = 'Puedes utilizar los siguientes comandos : \n\n/info - Guia para utilizar el bot\n/hola - Saludo del Bot \n/b0_0sk - Informacion sobre b0_0sk \n\n'

SET_CHANNEL = 'Introduiex el channel que vols que que consulti.\n'

GRUPO_BOT = "-270997133" #Definimos que cuando pongamos la palabra grupo lo vincule con el Id del grupo donde nos encontremos.  Al meter el bot en un grupo, en la propia consola nos saldrá


JohnFKennedyBot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.

#############################################
#Listener

@JohnFKennedyBot.message_handler(commands=['ayuda']) # Indicamos que lo siguiente va a controlar el comando '/ayuda'

def command_ayuda(client): # Definimos una función que resuleva lo que necesitemos.

    cid = client.chat.id # Guardamos el ID de la conversación para poder responder.

    JohnFKennedyBot.send_chat_action(cid, 'typing') # Enviando ...

    time.sleep(1) #La respuesta del bot tarda 1 segundo en ejecutarse

    JohnFKennedyBot.send_message( cid, AYUDA) # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.


@JohnFKennedyBot.message_handler(commands=['info']) # Indicamos que lo siguiente va a controlar el comando '/info'

def command_info(client): # Definimos una función que resuleva lo que necesitemos.

    cid = client.chat.id # Guardamos el ID de la conversación para poder responder.

    JohnFKennedyBot.send_message(cid, "Coming soon...")

@JohnFKennedyBot.message_handler(commands=['set_channel']) # Indicamos que lo siguiente va a controlar el comando '/set_channel'

def set_channel(client): # Definimos una función que resuleva lo que necesitemos.

    cid = client.chat.id # Guardamos el ID de la conversación para poder responder.
    
    JohnFKennedyBot.send_chat_action(cid, 'typing') # Enviando ...
    
    JohnFKennedyBot.send_message( cid, SET_CHANNEL) # Nos devolvera el mensaje que previamente hemos escrito en la variable SET_CHANNEL.


def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.

    now = datetime.now()
    for client in messages: # Por cada dato 'm' en el dato 'messages'

        cid = client.chat.id # El Cid es el identificador del chat los negativos son grupos y positivos los usuarios
        if cid != client.chat.id:
            cid = client.chat.id

        #JohnFKennedyBot.send_message(cid, cid) // Enviar en un mensaje el cid de la conversacion
        if cid > 0: # Conversacion privada

            clientName =  str(client.chat.first_name) # nom del chat
            clientDatetime = str(now.strftime("%d/%m/%Y %H:%M:%S"))

            clientText = str(client.text)
            clientChat = str(client.chat)

            nombre_documento = clientName

            mensaje = clientName + " [" + str(cid) + "|" + clientDatetime +"]: " + clientText     # Si 'cid' es positivo, usaremos 'm.chat.first_name' para el nombre.
            #JohnFKennedyBot.send_message(cid, "Esto es privado") // Enviar un mensaje si el chat es privado
            #JohnFKennedyBot.send_message(cid, messages) // Enviar todo el metadato del mensaje


        elif cid < 0: # Conversacion grupal


            groupName = str(client.chat.title) # Name group
            clientName = str(client.from_user.first_name) #Name user

            JohnFKennedyBot.send_message(cid, "GroupName: " + groupName)
            JohnFKennedyBot.send_message(cid, "clientName: " + clientName)

            JohnFKennedyBot.send_message(cid, "Esto es un grupo")
            #mensaje = clientName + " [" + str(cid) + "]: " + client.text # Si 'cid' es negativo, usaremos 'm.from_user.first_name' para el nombre.
            mensaje = clientName +": " + client.text # Si 'cid' es negativo, usaremos 'm.from_user.first_name' para el nombre.

            nombre_documento = groupName

            #JohnFKennedyBot.send_message(cid, groupName)
            #JohnFKennedyBot.send_message(cid, messages)     
        
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
