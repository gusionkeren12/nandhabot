from telegram import user,Chat


def user_can_changeinfo(chat: Chat, user: User, bot_id: int) -> bool:
    return chat.get_member(user.id).can_change_info
