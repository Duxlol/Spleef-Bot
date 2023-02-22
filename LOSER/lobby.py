from PIL import Image
import pyautogui as pag
from python_imagesearch.imagesearch import imagesearch
import time

pag.screenshot('./screenshots/hotbar.png', region=(305, 369, 29, 30))
hotbar = Image.open('./screenshots/hotbar.png')
lobby = Image.open('./screenshots/lobby.png')
inventory = Image.open('./screenshots/inventory.png')


def requeue():
    # TODO: requeue (click paper)
    # if paper is in inventory, right click
    # if ...: pag.click(button='right')
    game_start()


def join_game():
    print('Player status: Joining Game')
    # TODO: add join game features
    # joins game from lobby
    death()


def death():
    width, height = pag.size()
    for i in range(8):
        pag.click(width / 2, height)
    requeue()


def compare_images():
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
        print('Status Player: Lobby')
        join_game()

    else:
        print('Status player: In-Game')
        game_start()


def game_start():
    # TODO: check for game start
    # checks for game start
    pos = imagesearch('...')
    if pos[0] != -1:
        print('game has started')
        death()
    else:
        time.sleep(2)
        compare_images()
