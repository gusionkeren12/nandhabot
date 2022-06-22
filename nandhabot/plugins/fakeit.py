from pyrogram import filters
from nandhabot import bot

from faker import Faker

from faker.providers import internet

@bot.on_message(filters.command("fakeit"))
async def fakeit(_, m):
        fake = Faker()
        print("FAKE DETAILS GENERATED\n")
        name = str(fake.name())
        fake.add_provider(internet)
        address = str(fake.address())
        ip = fake.ipv4_private()
        cc = fake.credit_card_full()
        email = fake.ascii_free_email()
        job = fake.job()
        android = fake.android_platform_token()
        pc = fake.chrome()
        await m.reply_text(
        f"<b><u> Fake Information Generated:</b></u>\n<b>Name :-</b><code>{name}</code>\n\n<b>Address:-</b><code>{address}</code>\n\n<b>IP ADDRESS:-</b><code>{ip}</code>\n\n<b>credit card:-</b><code>{cc}</code>\n\n<b>Email Id:-</b><code>{email}</code>\n\n<b>Job:-</b><code>{job}</code>\n\n<b>android user agent:-</b><code>{android}</code>\n\n<b>Pc user agent:-</b><code>{pc}</code>")
