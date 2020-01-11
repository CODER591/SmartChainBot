from telegram.ext import *
from cached_text  import *

# Type: Command
# Name: /start
#
# Arguments: doc_default
#
# Functional: 
#   Providing basic tutorial for user
#
# Return value: None
#
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=start_text);
# Type: Command
#
# Name: /help
#
# Arguments: doc_default
#
# Functional: 
#   Providing tutorial for user to particular bot Functional
#
# Return value: None
#
def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=help_text);

# Type: Command
#
# Name: /get_info
#
# Arguments: doc_default
#
# Functional: 
#   Providing tutorial for user to particular bot Functional
#
# Return value: None
#
''' Here is simple one line function '''


# Type: Command
#
# Name: /test
#
# Arguments:
#
# Functional: 
#   Test functionality for developer =) me actioly
#
# Return value: None
#
def test(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="");

                             #in field "text" should be function that return value 
