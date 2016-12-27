from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import randint

def RunGame():
    Game = browser.find_element_by_class_name("grid-container")
    Game.click()
    for LoopNumber in range(1,500):
        Method2(Game, LoopNumber)
        
def Method1(Game, LoopNumber):
    Move = randint(0,3)
    if Move==0:
        Game.send_keys(Keys.ARROW_LEFT)
    elif Move==1:
        Game.send_keys(Keys.ARROW_RIGHT)
    elif Move==2:
        Game.send_keys(Keys.ARROW_UP)
    elif Move==3:
        Game.send_keys(Keys.ARROW_DOWN)

def Method2(Game, LoopNumber):
    Game.send_keys(Keys.ARROW_LEFT)
    Game.send_keys(Keys.ARROW_LEFT)
    Game.send_keys(Keys.ARROW_UP)
    Game.send_keys(Keys.ARROW_UP)
    if LoopNumber % 25==0:
        Game.send_keys(Keys.ARROW_RIGHT)
        print("Right")
        if LoopNumber % 50==0:
            Game.send_keys(Keys.ARROW_DOWN)
            print("Down")
    
def LoopGame(NumberOfGames):
    RunGame()
    for NumberOfGames in range(1, NumberOfGames):
        time.sleep(1)
        TryAgain = browser.find_element_by_class_name("retry-button")
        type(TryAgain)
        TryAgain.click()
        print("Restart")
        RunGame()

    
browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')

time.sleep(3)
LoopGame(2)


time.sleep(3)
browser.close()
