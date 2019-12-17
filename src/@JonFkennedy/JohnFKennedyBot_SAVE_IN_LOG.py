# -*- coding: utf-8 -*-


import telebot # Librería de la API del bot.

from telebot import types # Tipos para la API del bot.

import time # Librería para hacer que el programa que controla el bot no se acabe.

from datetime import datetime, date

import os.path as path
#from encodings import undefined
#from cgitb import text
#from atk import Document
#import sys
#sys.setdefaultencoding('utf8')

import telebot 
import ast 

import types 




# Aqui definiremos aparte del Token, por ejemplo los ids de los grupos y pondríamos grupo= -XXXXX



token = "891479632:AAEMeE7Ca15mkC0sVoY7g8F3I5F2MSktUxE" # token del bot.




AYUDA = 'Puedes utilizar los siguientes comandos : \n\n/info - Guia para utilizar el bot \n         · /search [keyword] [dd/mm/yyyy hh/mm/ss]\n/hola - Saludo del Bot \n/b0_0sk - Informacion sobre b0_0sk \n\n'


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
   
   


@JohnFKennedyBot.message_handler(commands=['help']) # Indicamos que lo siguiente va a controlar el comando '/ayuda'

def command_ayuda(messages): # Definimos una función que resuleva lo que necesitemos.

    cid = messages.chat.id # Guardamos el ID de la conversación para poder responder.

    JohnFKennedyBot.send_chat_action(cid, 'typing') # Enviando ...

    time.sleep(1) #La respuesta del bot tarda 1 segundo en ejecutarse

    JohnFKennedyBot.send_message( cid, AYUDA) # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.

@JohnFKennedyBot.message_handler(commands=['botones']) # Indicamos que lo siguiente va a controlar el comando '/ayuda'

def command_bt(messages): # Definimos una función que resuleva lo que necesitemos.

    cid = messages.chat.id # Guardamos el ID de la conversación para poder responder.

    
    JohnFKennedyBot.send_message( cid, AYUDA) 



@JohnFKennedyBot.message_handler(commands=['search']) # Indicamos que lo siguiente va a controlar el comando '/info'

def command_search(messages): # Definimos una función que resuleva lo que necesitemos.
    
    cid = messages.chat.id # Guardamos el ID de la conversación para poder responder.
    keyword = messages.text.split()
    
    if len(keyword) > 1:
       
        
        #JohnFKennedyBot.send_message(cid, keyword[1])
        if path.exists(str(cid) +".txt") == True:
            
            documento = open( str(cid) +".txt")
            linea = documento.readline()
            

            CountLines = 0
            
            if len(keyword[1]) == 1:
                JohnFKennedyBot.send_message(cid, "Solamente se pueden buscar palabras, no letras")
            else:
                while linea != "":
                    if keyword[1] in linea:
                        
                        InfoWords= linea.split("|")
                        InfoWords[4] = InfoWords[4].replace(keyword[1],"*"+keyword[1]+"*")
                        print (InfoWords[3])
                        JohnFKennedyBot.send_message(cid, "    - User: ["+InfoWords[0] +"]\n    - Date: ["+ InfoWords[2] +" "+InfoWords[3]+"]\n    - Message: "+ InfoWords[4], parse_mode = 'Markdown')
                        CountLines = CountLines + 1
                                   
                       
                    linea = documento.readline()
                JohnFKennedyBot.send_message(cid, "Ha habido " + str(CountLines) + " ocurrencias")

        else:
                    
            JohnFKennedyBot.send_message(cid, "Porfavor, introduzca algun texto para poder ejecutar correctamente la funcion /search  ")

    else:
        
        JohnFKennedyBot.send_message(cid, "Porfavor, introduzca un argumento :\n  - /search [keyword]\n  - /search [dd/mm/yyyy hh/mm/ss] ")

@JohnFKennedyBot.message_handler(commands=['searchTime']) # Indicamos que lo siguiente va a controlar el comando '/info'

def command_searchTime(messages): # Definimos una función que resuleva lo que necesitemos.
    
    command_search(messages)
    

def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.

    now = datetime.now() # Variable para guardar la fecha del mensaje
    
    
    for word in messages: # Por cada dato 'm' en el dato 'messages'
             
        cid = word.chat.id # Guardamos el ID de la conversación para poder responder.  
                           
        #cid = word.chat.id # El Cid es el identificador del chat los negativos son grupos y positivos los usuarios
        if cid != word.chat.id:
            cid = word.chat.id

        
        clientDayMonthYear= str(now.strftime("%d/%m/%Y"))
        clientHourMinSec = str(now.strftime("%H:%M:%S"))
        clientText = word.text
        if cid > 0: # Conversacion privada

            clientName =  str(word.chat.first_name) # nom del chat
                        
            clientChat = str(word.chat)

            nombre_documento = str(cid)
            if (clientText != None):
            
                mensaje = clientName + "|" + str(cid) + "|" + clientDayMonthYear + "|" + clientHourMinSec + "|" + clientText+"| "     # Si 'cid' es positivo, usaremos 'm.chat.first_name' para el nombre.
            else:
                JohnFKennedyBot.send_message(cid, "Solo se podra guardar el texto")  
                mensaje=""
                

        elif cid < 0: # Conversacion grupal


            groupName = str(word.chat.title) # Name group
            clientName = str(word.from_user.first_name) #Name user

            nombre_documento = str(cid)
            
            if (clientText != None):

                mensaje = clientName + "|" + str(cid) + "|" + clientDayMonthYear + "|" + clientHourMinSec + "|" + clientText+"| "
            
            else:
                JohnFKennedyBot.send_message(cid, "Solo se podra guardar el texto")  
                mensaje=""
            

        
        
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