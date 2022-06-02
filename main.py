import telebot
import os
import threading
import requests 
import time

token = os.environ['TOKEN']
chatID = os.environ['CHAT']
print(token, chatID)

def request_forever():
    r = requests.get("https://google.com")
    time.sleep(1)

bot = telebot.TeleBot(token)
@bot.message_handler()
def repeat_all_messages(message): # Название функции не играет никакой роли
    print(message.message_id)
    bot.forward_message(chatID, message.chat.id, message.message_id)

if __name__ == '__main__':
    threading.Thread(target=request_forever).start()
    bot.infinity_polling()
