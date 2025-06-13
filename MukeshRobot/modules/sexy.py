import random
import html
from telethon import Button, events
from .. import telethn as asst, SUPPORT_CHAT as c

BUTTON = [[Button.url("🍒 ꜱᴜᴘᴘᴏʀᴛ 🍒", f"https://t.me/{c}")]]
HOT = "https://telegra.ph/file/daad931db960ea40c0fca.gif"
SMEXY = "https://telegra.ph/file/a23e9fd851fb6bc771686.gif"
LEZBIAN = "https://telegra.ph/file/5609b87f0bd461fc36acb.gif"
BIGBALL = "https://i.gifer.com/8ZUg.gif"
LANG = "https://telegra.ph/file/423414459345bf18310f5.gif"
CUTIE = "https://64.media.tumblr.com/d701f53eb5681e87a957a547980371d2/tumblr_nbjmdrQyje1qa94xto1_500.gif"


def make_mention(user_id, user_name):
    return f'<a href="tg://user?id={user_id}">{html.escape(user_name)}</a>'


@asst.on(events.NewMessage(pattern="/horny ?(.*)"))
async def horny(e):
    mention = make_mention(e.sender_id, e.sender.first_name)
    mm = random.randint(1, 100)
    HORNY = f"🔥 {mention} ɪꜱ {mm}% ʜᴏʀɴʏ!"
    await e.reply(HORNY, buttons=BUTTON, file=HOT, parse_mode="html")


@asst.on(events.NewMessage(pattern="/gay ?(.*)"))
async def gay(e):
    mention = make_mention(e.sender_id, e.sender.first_name)
    mm = random.randint(1, 100)
    GAY = f"🍷 {mention} ɪꜱ {mm}% ɢᴀʏ!"
    await e.reply(GAY, buttons=BUTTON, file=SMEXY, parse_mode="html")


@asst.on(events.NewMessage(pattern="/lezbian ?(.*)"))
async def lezbian(e):
    mention = make_mention(e.sender_id, e.sender.first_name)
    mm = random.randint(1, 100)
    FEK = f"💜 {mention} ɪꜱ {mm}% ʟᴇᴢʙɪᴀɴ!"
    await e.reply(FEK, buttons=BUTTON, file=LEZBIAN, parse_mode="html")


@asst.on(events.NewMessage(pattern="/boob ?(.*)"))
async def boob(e):
    mention = make_mention(e.sender_id, e.sender.first_name)
    mm = random.randint(1, 100)
    BOOBS = f"🍒 {mention}'ꜱ ʙᴏᴏʙꜱ ꜱɪᴢᴇ ɪᴢ {mm}!"
    await e.reply(BOOBS, buttons=BUTTON, file=BIGBALL, parse_mode="html")


@asst.on(events.NewMessage(pattern="/cock ?(.*)"))
async def cock(e):
    mention = make_mention(e.sender_id, e.sender.first_name)
    mm = random.randint(1, 100)
    COCK = f"🍆 {mention}'ꜱ ᴄᴏᴄᴋ ꜱɪᴢᴇ ɪᴢ {mm}ᴄᴍ"
    await e.reply(COCK, buttons=BUTTON, file=LANG, parse_mode="html")


@asst.on(events.NewMessage(pattern="/cute ?(.*)"))
async def cute(e):
    mention = make_mention(e.sender_id, e.sender.first_name)
    mm = random.randint(1, 100)
    CUTE = f"🍑 {mention} {mm}% ᴄᴜᴛᴇ"
    await e.reply(CUTE, buttons=BUTTON, file=CUTIE, parse_mode="html")


__help__ = """
➻ /horny - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ʜᴏʀɴʏɴᴇꜱꜱ
➻ /gay - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢᴀʏɴᴇꜱꜱ
➻ /lezbian - ᴄʜᴇᴄᴋ ᴜʀ ʟᴇᴢʙɪᴀɴ ꜱᴛᴀᴛᴜꜱ
➻ /boob - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ʙᴏᴏʙ ꜱɪᴢᴇ
➻ /cock - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴏᴄᴋ ꜱɪᴢᴇ
➻ /cute - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜᴛᴇɴᴇꜱꜱ
"""

__mod_name__ = "Sᴇᴍxʏ"
