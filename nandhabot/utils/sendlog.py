from nandhabot import bot, SUPPORT_CHAT


def send_log(err, module):
    bot.send_message(f"@{SUPPORT_CHAT}", f"error in {module}\n\n{err}")
