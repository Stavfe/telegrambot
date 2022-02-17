import os
import telebot
API_KEY = '5283230920:AAGnp2WPw9KZJst1-USYt_0D5WLqdt4AcHU'
bot = telebot.TeleBot(API_KEY)


def hey_req(message):
  if message.text.isnumeric() & (len(message.text) ==10):
    return True

  elif len(message.text) ==11:
    clean_number =  message.text[:3] +  message.text[4:]
    print(clean_number)
    if clean_number.isnumeric():
      return True
  else:
    return False

@bot.message_handler(func = hey_req)
def greet(message):
  clean_number =  message.text[1:3] +  message.text[4:]
  bot.send_message(message.chat.id,"http://wa.me/972"+str(clean_number))

bot.polling()