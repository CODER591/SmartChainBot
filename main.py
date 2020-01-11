import telegram
from commands import *

from telegram.ext import Updater
from telegram.ext import CommandHandler
#commands

updater = Updater(token='1033505337:AAFVOVB4Ksf5vYJtOw5gh3IlMVqJ5RC2pNQ', use_context=True);
#print(updater.get_me());
dispatcher = updater.dispatcher;
start_handler = CommandHandler('start', start);
kek_handler = CommandHandler('help', help);
kek_handler = CommandHandler('test', test);
dispatcher.add_handler(start_handler);
dispatcher.add_handler(kek_handler);
dispatcher.add_handler(test_handler);
updater.start_polling();
#updater.stop();
