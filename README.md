Script que lee de la lista de dominios y consulta en Shodan los puertos que ha visto abiertos. Si esos puertos no están registrados en los ficheros de cada host alerta por Telegram.

# REQUISITOS.
-Instalar telebot. --> pip install pyTelegramBotAPI
-En el fichero "Verifica_ips_publicas.py" dar de alta los dominios a verificar.
-Por cada dominio creado en el fichero anterior deberá existir un fichero con el mismo nombre en el mismo directorio con los puertos marcados como conocidos.
-En el fichero "Verifica_ips_publicas.py" configurar el Token de la API de Shodan.
-En el fichero "EnvioConVariables.py" configurar el Token y el chatID para el bot de Telegram.

# Recomendable configurar en Cron para que se ejecute periodicamente.