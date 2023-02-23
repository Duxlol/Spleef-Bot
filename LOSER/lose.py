from PIL import Image
import pyautogui as pag
from python_imagesearch.imagesearch import imagesearch
from time import sleep
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import sys
sys.setrecursionlimit(10000)
keyboard = KeyboardController()
mouse = MouseController()

lobby = Image.open('./screenshots/lobby.png')
inventory = Image.open('./screenshots/inventory.png')


def requeue():
    #print("RE QUEUEING")
    # if paper is in inventory, right click
    # if ...: pag.click(button='right')
    pos = imagesearch('./screenshots/paper.png')
    if pos[0] != -1:
        mouse.click(Button.right, 1)
        sleep(1)
        game_start()
    else:
        requeue()


def join_game():
    print('Player status: Joining Game')
    # joins game from lobby
    join = imagesearch('./screenshots/lobby.png')
    if join[0] != -1:
        keyboard.press('1')
        keyboard.release('1')
        pag.rightClick()
        sleep(0.3)
        pag.moveTo(889, 450)
        sleep(0.3)
        pag.leftClick()
        pag.moveTo(1036, 484)
        sleep(0.3)
        pag.leftClick()
        sleep(1)
        game_start()


def death():
    #print("STARTING DEATH FUNCTION")
    width, height = pag.size()
    for i in range(11):
        pag.click(width / 2, height)
    requeue()


def compare_images():
    #print("COMPARING IMAGES")
    pag.screenshot('./screenshots/hotbar.png', region=(786, 1005, 29, 30))
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
        #print('Status Player: Lobby')
        join_game()

    else:
        #print('Status player: In-Game')
        game_start()


def game_start():
    # checks for game start
    #print("CHECKING FOR GAME START")
    pos = imagesearch('./screenshots/start.png')
    pos2 = imagesearch('./screenshots/start2.png')
    if pos[0] != -1 or pos2[0] != -1:
        #print('game has started')
        death()
    else:
        compare_images()


sleep(2)
compare_images()
