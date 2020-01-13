
import os

TGTOKEN = os.environ['TGTOKEN']

import telegram
from commands import *

from telegram.ext import Updater
from telegram.ext import CommandHandler
#commands

updater = Updater(token=TGTOKEN, use_context=True);
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
