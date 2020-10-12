# (C) SPARKZZZ 2020 @vishnu175
# Kangers plz keep credits
import requests
import asyncio
import random
import re
import time
import sys
import os
from os import remove, execl
from datetime import datetime
from collections import deque
from contextlib import suppress
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon import events
import git
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from userbot import bot, ALIVE_NAME
from userbot.utils import admin_cmd
from heroku_config import Var as Config

# -- Constants -- #
OFFICIAL_UPSTREAM_REPO = "https://github.com/vishnu175/SPARKZZZ"
HEROKU_GIT_REF_SPEC = "HEAD:refs/heads/master"
DELETE_TIMEOUT = 3
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SPARKZZZ user"
# -- Constants End -- #


@sparkzzz.on(admin_cmd("update ?(.*)", outgoing=True))
async def updater(upd):
    "For .update command, check if the bot is up to date, update if specified"
    await upd.edit('**Updation 📲 in progress.....**')

    try:
        repo = git.Repo()
    except git.exc.InvalidGitRepositoryError as e:
        repo = git.Repo.init()
        origin = repo.create_remote('updater', OFFICIAL_UPSTREAM_REPO)
        origin.fetch()
        repo.create_head('master', origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)

    active_branch_name = repo.active_branch.name
    if active_branch_name != 'master':
        await upd.edit(
            f'**[UPDATER]:Oops!!..Looks like you are in a custom branch ** {active_branch_name}.'
            '**is being used:**'
            '**So,updater is not able to identify which branch to be updated.**'
            '**Please check out the official branch and restart updater**')
        repo.__del__()
        return

    try:
        repo.create_remote('updater', OFFICIAL_UPSTREAM_REPO)
    except BaseException as e:
        print(e)
        pass

    upd_rem = repo.remote('updater')
    upd_rem.fetch(active_branch_name)

    changelog = await gen_chlog(repo, f'HEAD..updater/{active_branch_name}')

    if not changelog:
        await upd.edit('**⚡𝕊ℙ𝔸ℝ𝕂ℤℤℤ⚡ is up-to-date..**\n')
        repo.__del__()
        await asyncio.sleep(DELETE_TIMEOUT)
        await upd.delete()
        return

    changelog_str = f'**New 𝐔𝐏𝐃𝐀𝐓𝐄 available for ** {DEFAULTUSER}\n\n**CHANGELOG:**\n {changelog}'
    if len(changelog_str) > 4095:
        await upd.edit('**Changelog is too big, view the file to see it.**')
        file = open("change.txt", "w+")
        file.write(changelog_str)
        file.close()
        await bot.client.send_file(
            upd.chat_id,
            "change.txt",
            reply_to=upd.id,
        )
        os.remove("change.txt")
    else:
        await upd.edit(changelog_str)
        await asyncio.sleep(10)

    upd_rem.fetch(active_branch_name)
    repo.git.reset("--hard", "FETCH_HEAD")

    if Var.HEROKU_API_KEY is not None:
        import heroku3
        heroku = heroku3.from_key(Var.HEROKU_API_KEY)
        heroku_applications = heroku.apps()
        if len(heroku_applications) >= 1:
            if Var.HEROKU_APP_NAME is not None:
                heroku_app = None
                for app in heroku_applications:
                    if app.name == Var.HEROKU_APP_NAME:
                        heroku_app = app
                if heroku_app is None:
                    await upd.edit('**Invalid APP Name.change the value in var `HEROKU_APP_NAME.**')
                    return
                heroku_git_url = heroku_app.git_url.replace(
                    "https://",
                    "https://api:" + Var.HEROKU_API_KEY + "@"
                )
                if "heroku" in repo.remotes:
                    remote = repo.remote("heroku")
                    remote.set_url(heroku_git_url)
                else:
                    remote = repo.create_remote("heroku", heroku_git_url)
                asyncio.get_event_loop().create_task(deploy_start(bot, upd, HEROKU_GIT_REF_SPEC, remote))

            else:
                await upd.edit('**please create the Var `HEROKU_APP_NAME` as the key and the name of your bot in heroku as your value.**')
                return
        else:
            await upd.edit('**No heroku app found**')
    else:
        await upd.edit('**No Heroku api key found in Var `HEROKU_API_KEY**')
        

async def gen_chlog(repo, diff_marker):
    ch_log = ''
    d_form = "%d/%m/%y"
    for c in repo.iter_commits(diff_marker):
        ch_log += f'•[{c.committed_datetime.strftime(d_form)}]: {c.summary} by **{c.author}**\n'
    return ch_log

async def deploy_start(bot, upd, refspec, remote):
    await upd.edit('**Updating⚡𝕊ℙ𝔸ℝ𝕂ℤℤℤ⚡** \n🔷**𝐕𝐞𝐫𝐬𝐢𝐨𝐧** :`𝟙.𝟟` \n🔶**𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧** : `𝟙.𝟙𝟞.𝟜` \n🔷**𝐁𝐫𝐚𝐧𝐜𝐡** :`𝕄𝕒𝕤𝕥𝕖𝕣` \n🔶**𝐒𝐭𝐚𝐭𝐮𝐬**:`𝕌𝕡𝕕𝕒𝕥𝕚𝕟𝕘 & ℝ𝕖𝕤𝕥𝕒𝕣𝕥𝕚𝕟𝕘` \n__Type__ `.𝐚𝐥𝐢𝐯𝐞` __To check 𝐒𝐏𝐀𝐑𝐊𝐙𝐙𝐙 after 6-8 mins !__**\n[**𝕤𝕡𝕒𝕣𝕜𝕫𝕫𝕫𝕓𝕠𝕥𝕙𝕖𝕝𝕡](t.me/sparkzzzbothelp)')
    await remote.push(refspec=refspec)
    await bot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    
   
    
# (C) SPARKZZZ 2020 @vishnu175
