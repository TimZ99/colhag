# -*- coding: utf-8 -*-
import time
import telepot
import sys
import requests
import re
import logging
import urllib2
import json
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

log = 'false'
def terminal(text, firstname, lastname):
    sys.stderr.write("Message: " + text + "\nSend by:" + firstname + " " + lastname + "\n\n")
    #sys.stderr.write("Message: " + text + "\n")
    #sys.stderr.write("Message: " + message.text + "\nSend by:" + message.chat.first_name + " " + message.chat.last_name + "\n\n")

import getrooster1v
import getrooster2v
import getrooster3v
import getrooster4v
import getrooster5v
import getrooster6v

API_TOKEN = '375453632:AAFzfRoqAbjZB5Q90OnJ45ye3q02tTPmVyU'
def rooster(klas, id):
    if getrooster1v.roosterwijziging == "true" and klas == "1v":
        bot.sendMessage(id, """\
    Er is een roosterwijziging!
    http://hageveld.mwp.nl/rooster/dagrooster/Ver_Kla_1v.htm
    """)
    elif getrooster2v.roosterwijziging == "true":
        bot.sendMessage(id, """\
    Er is een roosterwijziging!
    http://hageveld.mwp.nl/rooster/dagrooster/Ver_Kla_2v.htm
    """)
    elif getrooster3v.roosterwijziging == "true":
        bot.sendMessage(id, """\
    Er is een roosterwijziging!
    http://hageveld.mwp.nl/rooster/dagrooster/Ver_Kla_3v.htm
    """)
    elif getrooster4v.roosterwijziging == "true":
        bot.sendMessage(id, """\
    Er is een roosterwijziging!
    http://hageveld.mwp.nl/rooster/dagrooster/Ver_Kla_4v.htm
    """)
    elif getrooster5v.roosterwijziging == "true":
        bot.sendMessage(id, """\
    Er is een roosterwijziging!
    http://hageveld.mwp.nl/rooster/dagrooster/Ver_Kla_5v.htm
    """)
    elif getrooster6v.roosterwijziging == "true":
        bot.sendMessage(id, """\
    Er is een roosterwijziging!
    http://hageveld.mwp.nl/rooster/dagrooster/Ver_Kla_6v.htm
    """)
    else:
        bot.sendMessage(id, """\
    Er zijn geen roosterwijzigingen!
    """)

# Handle Location
#def handle(location):

# Handle Commands
def handle(msg):
	com = 1
	lo = 1
	try:
		msg['location']['longitude']
	except KeyError:
		lo = None
	try:
		msg['text']
	except KeyError:
		com = None

	if lo is None and com is None:
		command = "Not a location or text"
	elif lo is not None:
		lon = "%.9f" % msg['location']['longitude']
		lat = "%.9f" % msg['location']['latitude']
		command = "Sending locatie lon: "+lon+" Lat: "+lat
	else:
		command = msg['text']

	print 'Got command: %s' % command

	chat_id = msg['chat']['id']

	if(command == '/start'):

        #Mijn hersenen zijn geschreven in Python en draaien op een Raspberry PI 3.
        #Ik ben erg blij dat je mij gestart hebt, want ik wil graag laten zien wat ik kan.

		bot.sendMessage(chat_id, """
Hoi, ik ben Colhag en ik ben een bot.
Ik kan je het weer laten zien en kijken of je klas een roosterwijziging heeft.
Weten hoe het werkt of heb je vragen? Typ '/help'.

Wil je weten door wie ik gemaakt ben? Typ '/credits', doe maar, is leuk ;).
""")
	elif(command == '/help'):
		bot.sendMessage(chat_id, """
Commando's om mij te besturen zijn:
/start Dit heb je al gedaan, maar ik wil je best nog eens begroeten
/help Dit bericht :)
/credits Je moet natuurlijk wel weten door wie ik gemaakt ben
/hoi Gewoon even om hoi te zeggen
/rooster Bekijk of er roosterwijzigingen zijn
/weer Bekijk de weersvoorspelling
""")
	elif(command == '/credits'):
		bot.sendMessage(chat_id, """
En de credits gaaaaan naaaaar... (trommelgeroffel)

Code > Tim
Getest door > Jaxon
Code herschreven door Tim en @hous3m4ster, nu crash ik tenminste niet meer zo vaak :P
""")
    # Handle '/hoi'
	elif(command == '/hoi'):
		bot.sendMessage(chat_id, 'Hoi!')

    # Handle '/rooster'
	elif('/rooster' in command):
		#itembtn6 = inline_keyboard('/rooster 1v')

		if command == "/rooster 6v":
			rooster("6v", chat_id)
		elif command == "/rooster 5v":
			rooster("5v", chat_id)
		elif command == "/rooster 4v":
			rooster("4v", chat_id)
		elif command == "/rooster 3v":
			rooster("3v", chat_id)
		elif command == "/rooster 2v":
			rooster("2v", chat_id)
		elif command == "/rooster 1v":
			print 'test'
			rooster("1v", chat_id)
		else:
			bot.sendMessage(chat_id, "Klas 1v")
			rooster("1v", chat_id)
			bot.sendMessage(chat_id, "Klas 2v")
			rooster("2v", chat_id)
			bot.sendMessage(chat_id, "Klas 3v")
			rooster("3v", chat_id)
			bot.sendMessage(chat_id, "Klas 4v")
			rooster("4v", chat_id)
			bot.sendMessage(chat_id, "Klas 5v")
			rooster("5v", chat_id)
			bot.sendMessage(chat_id, "Klas 6v")
			rooster("6v", chat_id)
			bot.sendMessage(chat_id, "Om voortaan alleen jouw klas te zien dien je '/rooster (jouw klas)' te typen.")
			bot.sendMessage(chat_id, "/mijnklasstaaternietbij")
			#reply_markup=markup)

    # Handle '/mijnklasstaaternietbij'
	elif(command == '/mijnklasstaaternietbij'):
		bot.sendMessage(chat_id, "Deze functie werk momenteel alleen voor VIA klassen. Staat jouw (reguliere) klas er niet bij? Stuur dan even een mail naar Tim@Xervion.nl en misschien voegen we jouw klas wel toe ;).")

    # Handle '/weer'
	elif(command == '/weer'):
		bot.sendMessage(chat_id, """\
Stuur je locatie!
(Dit werkt niet in groepen!)
""")
    #if message.chat.type == "group":
    #    terminal(message.text, message.chat.title, 'Anonymous user')
    #elif message.chat.type == "supergroup":
    #    terminal(message.text, message.chat.title, 'Anonymous user')
    #elif message.chat.type == "private":
    #    terminal(message.text, message.chat.first_name, message.chat.last_name)
    # Handle 'location'
	elif(lo is not None):
		url='http://api.openweathermap.org/data/2.5/weather?lat='+lat+'&lon='+lon+'&appid=d89ab85c7700a2ee6e26475397209c20'
		json_obj=urllib2.urlopen(url)
		data=json.load(json_obj)
		for i in data['weather']:
			if i['main']=='Rain':
			    bot.sendMessage(chat_id, "Kut! Het regent weer!")
		K=data['main']['temp']
		celsius=K-273.15
        #print "Tem:"
        #print celsius
		if celsius>20:
			bot.sendMessage(chat_id, "Het is lekker!")
		elif celsius>5 and celsius<20:
			bot.sendMessage(chat_id, "Het is een beetje matig weer, het is niet warm, het is niet koud!")
		elif celsius<5:
			bot.sendMessage(chat_id, "Het is koud!")
		celsius = "%.1f" % celsius
		bot.sendMessage(chat_id, "Het is "+celsius+" graden.")

'''
# Handle '/logenable'
@bot.message_handler(commands=['logenable'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Log enabled")
    log = 'true'
    logger = telebot.logger
    telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.
    if message.chat.type == "group":
        terminal(message.text, message.chat.title, 'Anonymous user')
    elif message.chat.type == "supergroup":
        terminal(message.text, message.chat.title, 'Anonymous user')
    elif message.chat.type == "private":
        terminal(message.text, message.chat.first_name, message.chat.last_name)

# Handle '/logdisable'
@bot.message_handler(commands=['logdisable'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Log disabled")
    log = 'false'
    logger = telebot.logger
    telebot.logger.setLevel(logging.NOTSET) # Outputs no messages to console.
    if message.chat.type == "group":
        terminal(message.text, message.chat.title, 'Anonymous user')
    elif message.chat.type == "supergroup":
        terminal(message.text, message.chat.title, 'Anonymous user')
    elif message.chat.type == "private":
        terminal(message.text, message.chat.first_name, message.chat.last_name)

# Handle all other messages with content_type 'text'
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    #bot.send_message(message.chat.id, "Ik snap \"" + message.text + "\" niet!")
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('/rooster')
    itembtn2 = types.KeyboardButton('/weer')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, "Sneltoets:", reply_markup=markup)
    if message.chat.type == "group":
        terminal(message.text, message.chat.title, 'Anonymous user')
    elif message.chat.type == "supergroup":
        terminal(message.text, message.chat.title, 'Anonymous user')
    elif message.chat.type == "private":
        terminal(message.text, message.chat.first_name, message.chat.last_name)
'''


if log == 'false':
    print 'Log: %s' % log
elif log == 'true':
    print 'Log: %s' % log
else:
    log = 'false'
    print 'Log: %s' % log

bot = telepot.Bot(API_TOKEN)

MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

while(1):
	time.sleep(10)
