import socket
import requests
import json
from EnvioConVariables import *
import os

# Token de la API de Shodan
querystring = {"key":"xxxxxxxxxxxxxxxxxxDUOkig5kZF7vaW"}

# Obtenemos la ruta del Script
script_dir = os.path.dirname(__file__)

#Dominios a consultar en Shodan. DEBE EXISTIR UN FICHERO AUNQUE ESTÉ VACIO CON EL NOMBRE DEL DOMINIO Y LOS PUERTOS CONOCIDOSS
dominios =	{
  "MK-Coru": "xxxxxx8effef.sn.mynetname.net",
  "MK-xxxxx": "xxxxxxa230b1.sn.mynetname.net"
}

#Consultamos cada dominio
for i in dominios:
    ip = socket.gethostbyname(dominios[i])
    print("\n\nVerificando %s %s" %(i, ip))
    url = "https://api.shodan.io/shodan/host/"+ip
    response = requests.request("GET", url, params=querystring)

    #Si tuvimos respuesta del servidor la procesamos como Json
    if response.status_code == 200:
        #print(response.text)
        salida = json.loads(response.text)
        if len(salida['ports']) > 0:
          puertos_encontrados = ""

          #Cargamos en memoria el fichero de puertos conocidos
          ruta_fichero = os.path.join(script_dir, i)
          file = open(ruta_fichero, "r")
          puertos_conocidos = file.readlines()
          file.close()

          for x in salida['ports']:
              print(x)
              if str(x)+'\n' in puertos_conocidos:
                print("El puerto %s ya estaba reconocido" %x)
              else:
                puertos_encontrados = puertos_encontrados + "\n" + str(x)

          if len(puertos_encontrados) > 0:
            enviamensaje("SHODAN-Script", i+":\nPuertos abiertos:" + puertos_encontrados + "\n\nNOTA: Si algun puerto es conoido añadelo al fichero de puertos del host")
        
        else:
          print("No se encontraron puertos abiertos")
            
    else:
      print("No se ha encontrado nada o hubo algun error en la respuesta del servidor")
