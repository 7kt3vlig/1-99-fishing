import pyautogui as aut 
import time
import cv2 as cv
import numpy as np
import win32, win32api, win32gui, win32con
from PIL import Image
from pathlib import Path 
from fishingfunctions import checkinventorydraynor, draynorcookinganddropping, check_fishing_status, check_for_fishingspot

fishingspot_path = Path("fiskebilder/fishingspot.png")
fire_path = Path("fiskebilder/fire.png")
shrimp_spot_path = Path("fiskebilder/shrimpspot.png")
fullinventory_path = Path("fiskebilder/fullinventory.png")
not_fishing_path = Path("fiskebilder/notfishing.png")
fishing_path = Path("fiskebilder/fishing.png")
draynorfire_path = Path("fiskebilder/draynorfire.png")

def main():
    while True: 

        if check_fishing_status():
            break
        
        if checkinventorydraynor():
            draynorcookinganddropping()

        if not check_fishing_status():
            time.sleep(1)
            check_for_fishingspot()
            time.sleep(4)


while True:
    main()
