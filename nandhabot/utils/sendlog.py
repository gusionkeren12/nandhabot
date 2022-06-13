from nandhabot import SUPPORT_CHAT, bot


def send_log(err, module):
    bot.send_message(f"@{SUPPORT_CHAT}", f"error in {module}\n\n{err}")
