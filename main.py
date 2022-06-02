import os

from flask import Flask, request

import telebot

TOKEN = os.environ['TOKEN']
chatID = os.environ['CHAT']

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler()
def repeat_all_messages(message): 
    print(message.message_id)
    bot.forward_message(chatID, message.chat.id, message.message_id)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://loh-s-cti.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
