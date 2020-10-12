"""Update UserBot code
Syntax: .update"""

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
IS_SELECTED_DIFFERENT_BRANCH = (
    "looks like a custom branch {branch_name} "
    "is being used:\n"
    "in this case, Updater is unable to identify the branch to be updated."
    "please check out to an official branch, and re-start the updater."
)
OFFICIAL_UPSTREAM_REPO = "https://github.com/vishnu175/SPARKZZZ"
BOT_IS_UP_TO_DATE = "FriShit UserShit is UpToShit!!!!"
NEW_BOT_UP_DATE_FOUND = (
    "**FriShit Update Found For** {branch_name}\n"
    "\n\n{changelog}\n"
    "Updating !!"
)
NEW_UP_DATE_FOUND = (
    "**New update found for** {branch_name}\n"
    "Updating And Restarting..."
)
REPO_REMOTE_NAME = "temponame"
IFFUCI_ACTIVE_BRANCH_NAME = "master"
DIFF_MARKER = "HEAD..{remote_name}/{branch_name}"
NO_HEROKU_APP_CFGD = "Heroku Api key is required for using this FeaShit"
HEROKU_GIT_REF_SPEC = "HEAD:refs/heads/master"
# -- Constants End -- #

# ---- + ------ + ----- 



@sparkzzz.on(admin_cmd("update ?(.*)", outgoing=True))
async def updater(upd):
    
     try:
        repo = git.Repo()
     except git.exc.InvalidGitRepositoryError as e:
        repo = git.Repo.init()
        origin = repo.create_remote(REPO_REMOTE_NAME, OFFICIAL_UPSTREAM_REPO)
        origin.fetch()
        repo.create_head(IFFUCI_ACTIVE_BRANCH_NAME, origin.refs.master)
        repo.heads.master.checkout(True)

    active_branch_name = repo.active_branch.name
    if active_branch_name != IFFUCI_ACTIVE_BRANCH_NAME:
        await message.edit(IS_SELECTED_DIFFERENT_BRANCH.format(
            branch_name=active_branch_name
        ))
        return False

    try:
        repo.create_remote(REPO_REMOTE_NAME, OFFICIAL_UPSTREAM_REPO)
    except Exception as e:
        print(e)
        pass

    temp_upstream_remote = repo.remote(REPO_REMOTE_NAME)
    temp_upstream_remote.fetch(active_branch_name)

    changelog = await gen_chlog(repo, f'HEAD..updater/{active_branch_name}')
    
    if not changelog:
        await upd.edit(
            f'\n{DEFAULTUSER} **Updating ⚡𝕊ℙ𝔸ℝ𝕂ℤℤℤ⚡**\n')
        repo.__del__()
        await asyncio.sleep(DELETE_TIMEOUT)
        await upd.delete()
        return

    changelog_str = f'**New UPDATE available for ** {DEFAULTUSER}\n\n**CHANGELOG:**\n {changelog}'
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
    else:    
        await upd.edit(changelog_str)     

    temp_upstream_remote.fetch(active_branch_name)
    repo.git.reset("--hard", "FETCH_HEAD")

   if Var.HEROKU_API_KEY is not None:
        import heroku3
        heroku = heroku3.from_key(Var.HEROKU_API_KEY)
        heroku_applications = heroku.apps()
        if len(heroku_applications) >= 1:
            if Var.HEROKU_APP_NAME is not None:
                heroku_app = None
                for i in heroku_applications:
                    if i.name == Var.HEROKU_APP_NAME:
                        heroku_app = i
                if heroku_app is None:
                    await message.edit("Invalid APP Name. Change the value in var HEROKU_APP_NAME.")
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
                asyncio.get_event_loop().create_task(deploy_start(bot, message, HEROKU_GIT_REF_SPEC, remote))

            else:
                await upd.edit("Please create the var HEROKU_APP_NAME as the key and the name of your bot in heroku as your value.")
                return
        else:
            await upd.edit(NO_HEROKU_APP_CFGD)
    else:
        await upd.edit("No heroku api key found in HEROKU_API_KEY var")
        
  async def gen_chlog(repo, diff_marker):
    ch_log = ''
    d_form = "%d/%m/%y"
    for c in repo.iter_commits(diff_marker):
        ch_log += f'•[{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>\n'
    return ch_log
        
        
  async def deploy_start(bot, upd, refspec, remote):
    await upd.edit('**Updating⚡𝕊ℙ𝔸ℝ𝕂ℤℤℤ⚡** \n📱**Version** : `1.7` \n💻**Telethon** : `1.16.4` \n**🛡️Branch** : `Master` \n🔄**Status** : `Updating & Restarting` \n__Type__ `.alive` __To Check If I am Alive after 6-8 mins !__**')
    await remote.push(refspec=refspec)
    await bot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    
    
    # SPARKZZZ 2020 
    
