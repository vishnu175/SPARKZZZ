import html
import os
import re
from math import ceil
from telethon import Button, custom, events, functions
from telethon.tl.functions.users import GetFullUserRequest
from heroku_config import Var
from userbot import ALIVE_NAME, CMD_LIST, CUSTOM_PMPERMIT, bot
from userbot.plugins import sparkzzzstats

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
TELEPIC = (
    PMPERMIT_PIC
    if PMPERMIT_PIC
    else "https://telegra.ph/file/572a121f67b75f97c7a6a.jpg"
)
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
myid = bot.uid
LOG_ID = Var.PRIVATE_GROUP_ID
MESAG = (
    str(CUSTOM_PMPERMIT)
    if CUSTOM_PMPERMIT
    else "`Dont spam here..else you will be blocked automatically!!!"
)
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SPARKZZZ User"
USER_BOT_WARN_ZERO = "`Hey you,..I have already warned you not to spam inbox ✉️. Now you have been blocked and reported until further notice.`\n\n**GoodBye🙋!**" 
USER_BOT_NO_WARN = (
    f"**Welcome to ⚡SPARKZZZ inbox security 🔐.**\n\nNice to see you here.unfortunately"
    f"[{DEFAULTUSER}](tg://user?id={myid}) is not available right now.This is an automated message from SPARKZZZ-BOT inbox security.kindly wait till my master approves  you..or tag him in group\n\n"
    f"{MESAG}"
    "\n\n Please select Help menu for further appointment..Thank You."
)

if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("`Userbot"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article(
                "© SPARKZZZ Help",
                text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)),
                buttons=buttons,
                link_preview=False,
            )
        elif event.query.user_id == bot.uid and query == "stats":
            result = builder.article(
                title="Stats",
                text=f"**SPARKZZZ Stats For [{DEFAULTUSER}](tg://user?id={myid})**\n\n(c) @sparkzzzbothelp",
                buttons=[
                    [custom.Button.inline("Stats📲", data="enquirestat")],
                    [Button.url("Repo⚙️", "https://github.com/vishnu175/SPARKZZZ")],
                    [
                        Button.url(
                            "Deploy🌀",
                            "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fvishnu175%2FSPARKZZZ&template=https%3A%2F%2Fgithub.com%2Fvishnu175%2FSPARKZZZ",
                        )
                    ],
                ],
            )
        elif event.query.user_id == bot.uid and query.startswith("**PM"):
            WARNTXT = USER_BOT_NO_WARN.format(DEFAULTUSER, myid, MESAG)
            result = builder.photo(
                file=TELEPIC,
                text=TELEBT,
                buttons=[
                    
                        [custom.Button.inline("To ASK 🗣️something", data="ask")],
                        [custom.Button.inline("To get HELP 🙏", data="wanthelp")],
                        [custom.Button.inline("To SPAM inbox 📬 ", data="spaminbox")],
                        [custom.Button.inline("⚡SPARKZZZ USERBOT⚡", data="sparkzzzinfo")],
                ],
            )
        
        await event.answer([result] if result else None)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(rb"helpme_next\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number + 1, CMD_LIST, "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = (
                "Please get your own Userbot from @sparkzzzbothelp , and don't use mine!"
            )
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"sparkzzzinfo")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "You are my master!! Majesty!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"SPARKZZZ userbot is a Telegram Userbot programmed created with python,You can deploy userbot at https://github.com/vishnu175/SPARKZZZ.\n\n visit [SPARKZZZ](t.me/sparkzzzbothelp)"
            )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ask")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "You are my master!! Majesty!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Request accepted, `{DEFAULTUSER}` will contact you soon!\n Kindly wait for my **master** to approve you"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            sendtobot = f"Hi...{DEFAULTUSER}, {first_name} want to ask you something in PM!"
            await tgbot.send_message(LOG_ID, sendtobot)


    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"wanthelp")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "You are my master!! Majesty!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Okay..Okay..👍.cool..{DEFAULTUSER} will help you...\nType your message in **singleline**...about what help you want"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            sendtobot = f"Hey {DEFAULTUSER}, {first_name} want a help from you..in PM!"
            await tgbot.send_message(LOG_ID, sendtobot)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"spaminbox")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "You are my master!! Majesty!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"So you are here to spam my inbox..⚡SPARKZZZ⚡ SECURITY identified you as a spammer🧟\n\nGoodbye...🙋\n."
            )
            await borg(functions.contacts.BlockRequest(event.query.user_id))
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            first_name = html.escape(target.user.first_name)
            await tgbot.send_message(
                LOG_ID,
                f"Hey Master,{first_name} tried to spam your inbox.\n So,I **kicked off** the spammer at the very moment",
            )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await event.edit("Help Menu Closed.")
        else:
            reply_pop_up_alert = "Please get your own userbot from @sparkzzzbothelp "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"enquirestat")))
    async def rip(event):
        text = sparkzzzstats
        await event.answer(text, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(rb"helpme_prev\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1, CMD_LIST, "helpme"  # pylint:disable=E0602
            )
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Please get your own Userbot, and don't use mine!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"us_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            plugin_name = event.data_match.group(1).decode("UTF-8")
            help_string = ""
            try:
                for i in CMD_LIST[plugin_name]:
                    help_string += i
                    help_string += "\n"
            except BaseException:
                pass
            if help_string == "":
                reply_pop_up_alert = "{} is useless".format(plugin_name)
            else:
                reply_pop_up_alert = help_string
            reply_pop_up_alert += "\n Use .unload {} to remove this plugin\n\
                © SPARKZZZ".format(
                plugin_name
            )
            try:
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
            except BaseException:
                halps = "Do .help {} to get the list of commands.".format(plugin_name)
                await event.answer(halps, cache_time=0, alert=True)
        else:
            reply_pop_up_alert = "Please get your own Userbot, and don't use mine!"


def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = 5
    number_of_cols = 2
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        custom.Button.inline("{} {}".format("⚡", x, "⚡"), data="us_plugin_{}".format(x))
        for x in helpable_plugins
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "⏮️ Previous", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline("Close", data="close"),
                custom.Button.inline(
                    "Next ⏭️", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs


async def userinfo(event):
    target = await event.client(GetFullUserRequest(event.query.user_id))
    first_name = html.escape(target.user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    return first_name
