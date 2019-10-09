
import telebot

TOKEN = "891479632:AAEMeE7Ca15mkC0sVoY7g8F3I5F2MSktUxE"
JohnFKennedy = telebot.TeleBot(TOKEN)	#create a new Telegram Bot object
@JohnFKennedy.message_handler(commands=['start', 'help'])
def send_welcome(message):
	chatid = message.chat.id

	print(message.chat.id)
	JohnFKennedy.send_message(chatid, "Que pasa ")
@JohnFKennedy.message_handler(func=lambda message: True)
def echo_all(message):
	chatid = message.chat.id
	audio = ('/home/abosch/Escriptori/ReBoTa.mp3', " ")
	JohnFKennedy.send_audio(chatid, audio)

	if message.chat.type == "group":
		JohnFKennedy.send_audio(chatid, audio)

JohnFKennedy.polling()
