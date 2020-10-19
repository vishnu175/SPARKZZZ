# (C) SPARKZZZ 2020

import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from userbot import TMP_DOWNLOAD_DIRECTORY


async def chrome(chrome_options=None):
    if chrome_options is None:
        chrome_options = await options()
    if not os.path.isdir(TMP_DOWNLOAD_DIRECTORY):
        os.mkdir(TMP_DOWNLOAD_DIRECTORY)
    prefs = {'download.default_directory': TMP_DOWNLOAD_DIRECTORY}
    chrome_options.add_experimental_option('prefs', prefs)
    return webdriver.Chrome(executable_path=CHROME_DRIVER,
                            options=chrome_options)

async def options():
    chrome_options = Options()
    chrome_options.binary_location = "/app/.apt/usr/bin/google-chrome"
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    return chrome_options
