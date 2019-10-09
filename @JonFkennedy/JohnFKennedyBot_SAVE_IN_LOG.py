# -*- coding: utf-8 -*-



import telebot # Librería de la API del bot.

from telebot import types # Tipos para la API del bot.

import time # Librería para hacer que el programa que controla el bot no se acabe.





# Aqui definiremos aparte del Token, por ejemplo los ids de los grupos y pondríamos grupo= -XXXXX



TOKEN = "891479632:AAEMeE7Ca15mkC0sVoY7g8F3I5F2MSktUxE"
  # Nuestro token del bot.



AYUDA = 'Puedes utilizar los siguientes comandos : \n\n/ayuda - Guia para utilizar el bot. \n/info - Informacion De interes \n/hola - Saludo del Bot \n/piensa3D - Informacion sobre Piensa3D \n\n'



GRUPO = "XXXXXX" #Definimos que cuando pongamos la palabra grupo lo vincule con el Id del grupo donde nos encontremos.  Al meter el bot en un grupo, en la propia consola nos saldrá


JohnFKennedyBot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.

#############################################
#Listener

def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.

    for m in messages: # Por cada dato 'm' en el dato 'messages'

        cid = m.chat.id # El Cid es el identificador del chat los negativos son grupos y positivos los usuarios
        print cid
        if cid > 0:

            mensaje = str(m.chat.first_name) + " [" + str(cid) + "]: " + m.text # Si 'cid' es positivo, usaremos 'm.chat.first_name' para el nombre.

        else:

            mensaje = str(m.from_user.first_name) + "[" + str(cid) + "]: " + m.text # Si 'cid' es negativo, usaremos 'm.from_user.first_name' para el nombre.

        f = open( 'JohnFKennedyBotlog.txt', 'a') # Abrimos nuestro fichero log en modo 'Añadir'.

        f.write(mensaje + "\n") # Escribimos la linea de log en el fichero.

        f.close() # Cerramos el fichero para que se guarde.

        JohnFKennedyBot.send_message(cid, "Que pasa bro")

        #print mensaje # Imprimimos el mensaje en la terminal, que nunca viene mal :)



JohnFKennedyBot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
JohnFKennedyBot.polling()
