
import telebot

TOKEN = "891479632:AAEMeE7Ca15mkC0sVoY7g8F3I5F2MSktUxE"
albondiga = telebot.TeleBot(TOKEN)	#create a new Telegram Bot object
@albondiga.message_handler(commands=['start', 'help'])
def send_welcome(message):
	chatid = message.chat.id

	print(message.chat.id)
	albondiga.send_message(chatid, "Que pasa ")
@albondiga.message_handler(func=lambda message: True)
def echo_all(message):
	chatid = message.chat.id
	audio = ('/home/abosch/Escriptori/ReBoTa.mp3', " ")
	albondiga.send_audio(chatid, audio)

	if message.chat.type == "private":
		albondiga.send_audio(chatid)

albondiga.polling()
