def command_searchBucle(messages,cont): # Definimos una función que resuleva lo que necesitemos.
    
    cid = messages.chat.id # Guardamos el ID de la conversación para poder responder.
    keyword = messages.text.split()
    
    documento = open( str(cid) +".txt")
    linea = documento.readline()
    
    CountLines = 0
           
    while linea != "":
        if keyword[1] in linea:

            InfoWords= linea.split("|")
            print (keyword[1])
            if cont == 1:
                
                InfoWords[4] = InfoWords[4].replace(keyword[1],"*"+keyword[1]+"*")
               
            
            elif cont == 2:
                InfoWords[2] = InfoWords[2].replace(keyword[1],"*"+keyword[1]+"*")
                
            JohnFKennedyBot.send_message(cid, "    - User: ["+InfoWords[0] +"]\n    - Date: ["+ InfoWords[2] +" "+InfoWords[3]+"]\n    - Message: "+ InfoWords[4], parse_mode = 'Markdown')
            CountLines = CountLines + 1
        linea = documento.readline()
        
    return CountLines

def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.

    now = datetime.now() # Variable para guardar la fecha del mensaje
    
    
    for word in messages: # Por cada dato 'm' en el dato 'messages'
             
        cid = word.chat.id # Guardamos el ID de la conversación para poder responder.  
                           
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
           

        documentoNuevo.write(str(mensaje.encode("utf-8")) + "\n") # Escribimos la linea de log en el fichero.
        documentoNuevo.close() # Cerramos el fichero para que se guarde.
        
        
               
       
JohnFKennedyBot.set_update_listener(listener) # Así, le decimos al bot que utilice como función listener nuestra función 'listener' declarada arriba.
JohnFKennedyBot.polling()