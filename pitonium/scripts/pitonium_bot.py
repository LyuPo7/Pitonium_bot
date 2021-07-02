# This Python file uses the following encoding: utf-8

"""Main file of project."""
import telebot

def main():
    bot = telebot.TeleBot("1688182700:AAHcaPS9PZ9pS29T5TOLXNeC8BqDvCckZVg", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
	    bot.reply_to(message, "Howdy, how are you doing?")
    
    @bot.message_handler(func=lambda m: True)
    def echo_all(message):
	    bot.reply_to(message, message.text)
    
    bot.polling()