import telebot
import os

token = os.environ['TOKEN']
chatID = os.environ['CHAT']
print(token, chatID)
bot = telebot.TeleBot(token)


@bot.message_handler()
def repeat_all_messages(message): # Название функции не играет никакой роли
    print(message.message_id)
    bot.forward_message(chatID, message.chat.id, message.message_id)

if __name__ == '__main__':
     bot.infinity_polling()
