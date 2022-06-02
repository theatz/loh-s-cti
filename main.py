import telebot
import os

bot = telebot.TeleBot(os.environ['TOKEN'])
chatID = os.environ['CHAT']

@bot.message_handler()
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.forward_message(chatID, message.chat.id, message.message_id)

if __name__ == '__main__':
     bot.infinity_polling()
