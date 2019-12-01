
# Name: /start
#
# Functional: 
#   Providing basic tutorial for user
#
#


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!");
    update.message.reply_text("kek");


# Name: /help
#
# Functional: 
#   Providing basic tutorial for user to particular bot Functional
#
#


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="kek");
