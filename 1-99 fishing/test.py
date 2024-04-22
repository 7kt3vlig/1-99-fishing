import pyautogui as aut
import time
import cv2 as cv
import numpy as np
import win32, win32api, win32gui, win32con
from PIL import Image
from pathlib import Path

fishingspot_path = Path("fiskebilder/fishingspot.png")
fullinventory_path = Path("fiskebilder/fullinventory.png")
draynorfire_path = Path("fiskebilder/draynorfire.png")



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
max_loc_screen_x = top_left[0] + max_loc_center_x - 5
max_loc_screen_y = top_left[1] + max_loc_center_y +5
if max_val >= threshold:
# Click at the center of the maximum value location in actual screen coordinates
    aut.click(max_loc_screen_x, max_loc_screen_y)
    aut.click(max_loc_screen_x, max_loc_screen_y)
time.sleep(4)
aut.press("space")
time.sleep(20)
aut.moveTo(552,330)
aut.click()
drop


# cv.imshow("1", grayscale)
# cv.imshow("2", template)

# cv.waitKey(0)
# cv.destroyAllWindows()


