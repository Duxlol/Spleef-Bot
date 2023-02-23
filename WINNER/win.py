from PIL import Image
import pyautogui as pag
from time import sleep
from python_imagesearch.imagesearch import imagesearch
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import sys

sys.setrecursionlimit(10000)
mouse = MouseController()
keyboard = KeyboardController()

lobby = Image.open('./screenshots/lobby.png')
inventory = Image.open('./screenshots/inventory.png')


def join_game():
    # print('Player status: Joining Game')
    # joins game from lobby
    join = imagesearch('./screenshots/lobby.png')
    if join[0] != -1:
        keyboard.press('1')
        keyboard.release('1')
        pag.rightClick()
        sleep(0.5)
        pag.moveTo(889, 450)
        sleep(0.5)
        pag.leftClick()
        pag.moveTo(1036, 484)
        sleep(0.5)
        pag.leftClick()
        sleep(1)
        compare_images()


def compare_images():
    while True:
        pag.screenshot('./screenshots/hotbar.png', region=(786, 1044, 29, 30))
        hotbar = Image.open('./screenshots/hotbar.png')
        # Compare the pixel values of the two images
        pixels1 = hotbar.load()
        pixels2 = lobby.load()
        pixels = hotbar.size[0] * hotbar.size[1]
        identical_pixels = 0
        for i in range(hotbar.size[0]):
            for j in range(hotbar.size[1]):
                if pixels1[i, j] == pixels2[i, j]:
                    identical_pixels += 1
        percentage_identical = identical_pixels / pixels * 100

        # Check if the images are the same for at least 60% of the pixels, or if they are exactly the same
        if percentage_identical >= 35 or hotbar.tobytes() == inventory.tobytes():
            # print('Status Player: Lobby')
            join_game()
            break

        else:
            # print('Status player: In-Game')
            pos = imagesearch('./screenshots/paper.png')
            if pos[0] != -1:
                mouse.click(Button.right, 1)
                webhook()
                continue
            else:
                sleep(0.5)
                continue


def webhook():
    from discordwebhook import Discord
    from configparser import RawConfigParser
    config = RawConfigParser()
    # load webhook url from config
    config.read('config.ini')
    url = config['CONFIG']['webhook']
    discord = Discord(url=url)
    # take screenshot
    pag.screenshot('screen.png', region=(0, 0, 1920, 1080))

    discord.post(file={
        "file1": open("screen.png", "rb"), }, )


sleep(2)
compare_images()
