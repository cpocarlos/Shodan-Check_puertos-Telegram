import telebot
import sys

TOKEN = 'xxxxxxxxU19xxxxx2xxxHgnUPYGEW14vKqWGY'
chatid = '-xxxxxxxxx'

tb = telebot.TeleBot(TOKEN)


def enviamensaje(servicio,mensaje):
	tb.send_message(chatid, "[Rock64][" + servicio + "] " + mensaje)


if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("ERROR: Es necesario pasar como argumento el NOMBRE_DE_SERVICIO y luego el TEXTO")
		#sys.exit(1)
	else:
		texto=""
		for i in range (2,len(sys.argv)):
			texto = texto + sys.argv[i] + " "

		enviamensaje( sys.argv[1].upper(), texto)		
