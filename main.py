import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from os import system, name
import os
from colorama import *
import ctypes

"""
Sneaky Sneaky, looking at my code!

            Best video ever!!
                VVVVVVVV
https://www.youtube.com/watch?v=dQw4w9WgXcQ
"""

os.system('mode con: cols=150 lines=50')
ctypes.windll.kernel32.SetConsoleTitleW("Gravity TikTok Bot")
init()

likes = 0


def print_title():
    print(Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX, "  ▄████  ██▀███   ▄▄▄    ██▒   █▓ ██▓▄▄▄█████▓▓██   ██▓")
    print(" ██▒ ▀█▒▓██ ▒ ██▒▒████▄ ▓██░   █▒▓██▒▓  ██▒ ▓▒ ▒██  ██▒")
    print("▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄▓██  █▒░▒██▒▒ ▓██░ ▒░  ▒██ ██░")
    print("░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██▒██ █░░░██░░ ▓██▓ ░   ░ ▐██▓░")
    print("░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒▒▀█░  ░██░  ▒██▒ ░   ░ ██▒▓░")
    print(" ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▐░  ░▓    ▒ ░░      ██▒▒▒ ")
    print("  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ▒ ░    ░     ▓██ ░▒░ ")
    print("░ ░   ░   ░░   ░   ░   ▒     ░░   ▒ ░  ░       ▒ ▒ ░░  ")
    print("      ░    ░           ░  ░   ░   ░            ░ ░     ")
    print("                             ░                 ░ ░     ")
    print(Style.RESET_ALL, "\n\n")


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    elif name == 'posix':
        _ = system('clear')
    else:
        print("YOU ARE FAGGOT MONKEY, HAVE A GREAT DAY")
        _ = system('cls')
        _ = system('clear')


def comment_likes():
    comment_button = driver.find_element_by_xpath('//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button')
    comment_button.click()
    sleep(2)
    comment_send_likes = driver.find_element_by_xpath(
        '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9r"]/form[1]/ul/li/div/button')
    comment_send_likes.click()


def views():
    views_button = driver.find_element_by_xpath('//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9V"]/div[1]/div/form/button')
    views_button.click()


def views_enter_video():
    global field
    field = driver.find_element_by_xpath('//*[@id="sid4"]/div/div/div/form/div/input')
    field.send_keys(video)


def views_press_button():
    global button
    button = driver.find_element_by_xpath('//*[@id="sid4"]/div/div/div/form/div/div/button')
    button.click()


def comment_likes_press_button():
    global button
    button = driver.find_element_by_xpath('//*[@id="sid3"]/div/div/div/form/div/div/button')
    button.click()


def comment_likes_enter_video():
    global field
    field = driver.find_element_by_xpath('//*[@id="sid3"]/div/div/div/form/div/input')
    field.send_keys(video)


def followers_enter_video():
    global field
    field = driver.find_element_by_xpath('//*[@id="sid"]/div/div/div/form/div/input')
    field.send_keys(video)


def followers_press_button():
    global button
    button = driver.find_element_by_xpath('//*[@id="sid"]/div/div/div/form/div/div/button')
    button.click()


def followers():
    followers_button = driver.find_element_by_xpath('//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9V"]/div[1]/div/form/button')
    followers_button.click()


def shares_enter_video():
    global field
    field = driver.find_element_by_xpath('//*[@id="sid7"]/div/div/div/form/div/input')
    field.send_keys(video)


def shares_press_button():
    global button
    button = driver.find_element_by_xpath('//*[@id="sid7"]/div/div/div/form/div/div/button')
    button.click()


def shares():
    shares_button = driver.find_element_by_xpath('//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9s"]/div[1]/div/form/button')
    shares_button.click()

def check_status(status):
    if "danger" in status:
        print(Fore.RED, "[Not Working!]")
    else:
        print(Fore.GREEN, "[Working!]")


print_title()
PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://zefoy.com")
try:
    clear()
    print_title()

    print(Fore.BLUE, "[+]Captcha")
    sleep(3)
    clear()
    print_title()
    def get_status():
        global followers_status, hearts_status, comments_hearts_status, views_status, shares_status
        try:
            followers_status = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div/p/small[@class]').get_attribute('class')
            hearts_status = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/p/small[@class]').get_attribute('class')
            comments_hearts_status = driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/p/small[@class]').get_attribute('class')
            views_status = driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div/p/small[@class]').get_attribute('class')
            shares_status = driver.find_element_by_xpath('//*[@id="main"]/div/div[5]/div/p/small[@class]').get_attribute('class')
        except:
            clear()
            print_title()

            print(Fore.BLUE, "[+]Captcha")
            sleep(3)
            get_status()
    get_status()


    print(Fore.BLUE, "[1]Followers", end="")
    check_status(followers_status)
    print(Fore.BLUE, "[2]Hearts", end="")
    check_status(hearts_status)
    print(Fore.BLUE, "[3]Comments Hearts", end="")
    check_status(comments_hearts_status)
    print(Fore.BLUE, "[4]Views", end="")
    check_status(views_status)
    print(Fore.BLUE, "[5]Shares", end="")
    check_status(shares_status)

    mode = input("\n\nWhat mode do you want to use?: ")
    driver.set_window_position(-10000, 0)

    row = driver.find_elements_by_css_selector("div.row > div")
    row[int(mode) - 1].click()
    clear()
    print_title()

    video = input("Video URL: ")

    if int(mode) == 1:
        followers_enter_video()
    if int(mode) == 3:
        comment_likes_enter_video()
    if int(mode) == 4:
        views_enter_video()
    clear()
    print_title()
    while True:
        if int(mode) == 1:
            followers_press_button()
        if int(mode) == 3:
            comment_likes_press_button()
        elif int(mode) == 4:
            views_press_button()
        sleep(2)

        try:
            if int(mode) == 1:
                followers()
            if int(mode) == 3:
                comment_likes()
            if int(mode) == 4:
                views()
            for i in range(60):
                sleep(1)
            clear()
            print_title()
            print(Fore.MAGENTA, "[+]Sent the things\n")
            if int(mode) == 1:
                likes += 25
                ctypes.windll.kernel32.SetConsoleTitleW("Gravity TikTok Bot | followers: {0}".format(str(likes)))
            if int(mode) == 3:
                likes += 30
                ctypes.windll.kernel32.SetConsoleTitleW("Gravity TikTok Bot | likes: {0}".format(str(likes)))
            if int(mode) == 4:
                likes += 1000
                ctypes.windll.kernel32.SetConsoleTitleW("Gravity TikTok Bot | views: {0}".format(str(likes)))
            print(Fore.MAGENTA, "[+]", str(likes), "\n")
            print(Fore.MAGENTA, "[+]Cooldown")
        except:
            for i in range(20):
                sleep(20)
            clear()
            print_title()
            print(Fore.MAGENTA, "[+]Cooldown")

finally:
    driver.quit()
    print("Bye Bye")
