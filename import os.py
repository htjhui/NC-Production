import os
import telebot

bot = telebot.Telebot("API Ket Here")

@bot.massage_handler(commands=<"start">)
def send_welcome(massage):
   bot.reply_to(massage,"Hello I'm NC Production Bot")

@bot.massage_handler(commands=<"how">)
def send_welcome(massage):
    bot.send_massage(massage,"https://www.youtube.com/channel/UCTcddQBpMEUf4muPcozu5vg")

bot.polling