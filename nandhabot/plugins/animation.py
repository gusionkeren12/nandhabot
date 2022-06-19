


emoji_ani = [
            "☺️",
            "😞",
            "😀",
            "fuckin",
]

@bot.on_message(filters.command("hack"))
         msg = await message.reply_text("started")
         for x in range(15):
                 await msg.edit_text(hack_ani[x%4])
                 time.sleep(1)
         await msg.edit_text('😎 EMOJI ANIMATION END')
