import pyautogui as aut 
import time
import cv2 as cv
import numpy as np
import win32, win32api, win32gui, win32con
from PIL import Image
from pathlib import Path 



fishingspot_path = Path("fiskebilder/fishingspot.png")
shrimp_spot_path = Path("fiskebilder/shrimpspot.png")
fullinventory_path = Path("fiskebilder/fullinventory.png")
not_fishing_path = Path("fiskebilder/notfishing.png")
fishing_path = Path("fiskebilder/fishing.png")
draynorfire_path = Path("fiskebilder/draynorfire.png")


def check_for_fishingspot():
        
    top_left = 461, 223
    bottom_right = 650, 265

    screenshot = aut.screenshot(region=(top_left[0], top_left[1],
                                        bottom_right[0] - top_left[0],
                                        bottom_right[1] - top_left[1])) 

    screenshot_cv = cv.cvtColor(np.array(screenshot),cv.COLOR_RGB2BGR)

    grayscale = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    template = cv.imread(str(fishingspot_path), cv.IMREAD_GRAYSCALE)

    blur = cv.blur(grayscale, (3,3))
    blur1 = cv.blur(template, (3,3))

    canny = cv.Canny(blur,125, 175)
    canny1 = cv.Canny(blur1, 125, 175)


    result = cv.matchTemplate(canny, canny1, cv.TM_CCOEFF_NORMED )

    threshold = 0.6

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    print(min_val, max_val, min_loc, max_loc)

    # Calculate the center of the maximum value location
    max_loc_center_x = max_loc[0] + (template.shape[1] // 2)
    max_loc_center_y = max_loc[1] + (template.shape[0] // 2)

    # Convert to actual screen coordinates
    max_loc_screen_x = top_left[0] + max_loc_center_x - 5
    max_loc_screen_y = top_left[1] + max_loc_center_y +5
    if max_val >= threshold:
    # Click at the center of the maximum value location in actual screen coordinates
        aut.click(max_loc_screen_x, max_loc_screen_y)
        aut.click(max_loc_screen_x, max_loc_screen_y)

def check_shrimpspot():
    top_left = 299, 32
    bottom_right = 810, 366

    screenshot = aut.screenshot(region=(top_left[0], top_left[1],
                                        bottom_right[0] - top_left[0],
                                        bottom_right[1] - top_left[1])) 

    screenshot_cv = cv.cvtColor(np.array(screenshot),cv.COLOR_RGB2BGR)

    grayscale = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    template = cv.imread(str(shrimp_spot_path), cv.IMREAD_GRAYSCALE)

    blur = cv.blur(grayscale, (3,3))
    blur1 = cv.blur(template, (3,3))

    canny = cv.Canny(blur,125, 175)
    canny1 = cv.Canny(blur1, 125, 175)


    result = cv.matchTemplate(canny, canny1, cv.TM_CCOEFF_NORMED )

    threshold = 0.8

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print("printing shrimp spot values..")
    print(min_val, max_val, min_loc, max_loc)

    # Calculate the center of the maximum value location
    max_loc_center_x = max_loc[0] + (template.shape[1] // 2)
    max_loc_center_y = max_loc[1] + (template.shape[0] // 2)

    # Convert to actual screen coordinates
    max_loc_screen_x = top_left[0] + max_loc_center_x - 5
    max_loc_screen_y = top_left[1] + max_loc_center_y +5
    if max_val >= threshold:
    # Click at the center of the maximum value location in actual screen coordinates
        aut.click(max_loc_screen_x, max_loc_screen_y)
        aut.click(max_loc_screen_x, max_loc_screen_y)
        

def check_full_inventory():
    top_left = 308, 378
    bottom_right = 804, 500

    screenshot = aut.screenshot(region=(top_left[0], top_left[1],
                                        bottom_right[0] - top_left[0],
                                        bottom_right[1] - top_left[1])) 

    screenshot_cv = cv.cvtColor(np.array(screenshot),cv.COLOR_RGB2BGR)

    grayscale = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    template = cv.imread(str(fullinventory_path), cv.IMREAD_GRAYSCALE)

    result = cv.matchTemplate(grayscale, template, cv.TM_CCOEFF_NORMED )

    threshold = 0.8

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print("printing inventory values..")
    print(min_val, max_val, min_loc, max_loc)

    if max_val >= threshold:
        drop_inventory(start_positions, y_offset, num_columns)
    else:
        return False


def drop_inventory(start_positions, y_offset, num_columns):
    for start_x, start_y in start_positions:
        for col in range(num_columns):
            x = start_x
            y = start_y + col * y_offset
            aut.keyDown("shift")
            aut.moveTo(x, y)
            aut.click()
            aut.keyUp("shift")

# Define the starting positions for each row and the y-offset
start_positions = [(872, 331), (916, 331), (957, 331), (1000, 331)]
y_offset = 37  # Adjust this value according to your specific scenario
num_columns = 5

def check_fishing_status():
    top_left = 312, 55
    bottom_right = 412, 75

    screenshot = aut.screenshot(region=(top_left[0], top_left[1],
                                        bottom_right[0] - top_left[0],
                                        bottom_right[1] - top_left[1]))

    screenshot_cv = cv.cvtColor(np.array(screenshot),cv.COLOR_RGB2BGR)
    grayscale = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    template = cv.imread(str(fishing_path), cv.IMREAD_GRAYSCALE)

    result = cv.matchTemplate(grayscale, template, cv.TM_CCOEFF_NORMED )

    threshold = 0.37

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print("printing fishing status values..")
    print(min_val, max_val, min_loc, max_loc)

    if max_val >= threshold:
        return True 
    else:
        return False
    

def checkinventorydraynor():
    top_left = 308, 378
    bottom_right = 804, 500

    screenshot = aut.screenshot(region=(top_left[0], top_left[1],
                                        bottom_right[0] - top_left[0],
                                        bottom_right[1] - top_left[1])) 

    screenshot_cv = cv.cvtColor(np.array(screenshot),cv.COLOR_RGB2BGR)

    grayscale = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    template = cv.imread(str(fullinventory_path), cv.IMREAD_GRAYSCALE)

    result = cv.matchTemplate(grayscale, template, cv.TM_CCOEFF_NORMED )

    threshold = 0.8

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print("printing inventory values..")
    print(min_val, max_val, min_loc, max_loc)

    if max_val >= threshold:
        return True
    else:
        return False


def draynorcookinganddropping():
    top_left = 469, 63
    bottom_right = 572, 93

    screenshot = aut.screenshot(region=(top_left[0], top_left[1],
                                        bottom_right[0] - top_left[0],
                                        bottom_right[1] - top_left[1])) 

    screenshot_cv = cv.cvtColor(np.array(screenshot),cv.COLOR_RGB2BGR)

    grayscale = cv.cvtColor(screenshot_cv, cv.COLOR_BGR2GRAY)

    template = cv.imread(str(draynorfire_path), cv.IMREAD_GRAYSCALE)

    result = cv.matchTemplate(grayscale, template, cv.TM_CCOEFF_NORMED )

    threshold = 0.55

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print("printing inventory values..")
    print(min_val, max_val, min_loc, max_loc)

        
    # Calculate the center of the maximum value location
    max_loc_center_x = max_loc[0] + (template.shape[1] // 2)
    max_loc_center_y = max_loc[1] + (template.shape[0] // 2)

    # Convert to actual screen coordinates
    max_loc_screen_x = top_left[0] + max_loc_center_x - 3
    max_loc_screen_y = top_left[1] + max_loc_center_y - 2
    if max_val >= threshold:
    # Click at the center of the maximum value location in actual screen coordinates
        aut.click(max_loc_screen_x, max_loc_screen_y)
        aut.click(max_loc_screen_x, max_loc_screen_y)
    time.sleep(4)
    aut.press("1")
    time.sleep(25)
    aut.moveTo(519,202)
    aut.click()
    time.sleep(1)
    aut.press("space")
    time.sleep(25)
    aut.moveTo(552,330)
    aut.click()
    dropall()

def dropall():
    aut.keyDown("shift")
    aut.moveTo(996,262)
    aut.click()
    aut.moveTo(996,298)
    aut.click()
    aut.moveTo(996,335)
    aut.click()
    aut.moveTo(996,370)
    aut.click()
    aut.moveTo(996,406)
    aut.click()
    aut.moveTo(996,442)
    aut.click()
    aut.moveTo(996,478)
    aut.click()

    aut.moveTo(956,262)
    aut.click()
    aut.moveTo(956,298)
    aut.click()
    aut.moveTo(956,335)
    aut.click()
    aut.moveTo(956,370)
    aut.click()
    aut.moveTo(956,406)
    aut.click()
    aut.moveTo(956,442)
    aut.click()
    aut.moveTo(956,478)
    aut.click()
    
    aut.moveTo(913,297)
    aut.click()
    aut.moveTo(913,335)
    aut.click()
    aut.moveTo(913,370)
    aut.click()
    aut.moveTo(913,406)
    aut.click()
    aut.moveTo(913,442)
    aut.click()
    aut.moveTo(913,478)
    aut.click()

    aut.moveTo(872,297)
    aut.click()
    aut.moveTo(872,335)
    aut.click()
    aut.moveTo(872,370)
    aut.click()
    aut.moveTo(872,406)
    aut.click()
    aut.moveTo(872,442)
    aut.click()
    aut.moveTo(872,478)
    aut.click()

    aut.keyUp("shift")




# cv.imshow("1",canny )
# cv.imshow("2", canny1)

# cv.waitKey(0)
# cv.destroyAllWindows()

 