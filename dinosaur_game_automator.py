import time

import pyautogui
from PIL import ImageGrab

# Constants
GAME_REGION = (0, 540, 1400, 1200)
OBSTACLE_HEIGHTS = [590, 450]
# Adjust according to your needs
SPACE_INTERVAL = 0.1


# Function to check for dark theme
def check_for_dark_theme(img_data):
    return img_data[10, 10] < 50


# Function to check for obstacles
def check_for_obstacle(img_data, dark_theme):
    obstacle_color = 172 if dark_theme else 83
    for x in range(300, 600):
        if img_data[x, OBSTACLE_HEIGHTS[0]] == obstacle_color:
            pyautogui.press('space')
            time.sleep(SPACE_INTERVAL)
            pyautogui.press('down')
            return
        if img_data[x, OBSTACLE_HEIGHTS[1]] == obstacle_color:
            pyautogui.press('down')
            return


# Function to check for loss
def check_for_loss(img_data, dark_theme):
    loss_color = 172 if dark_theme else 83
    if img_data[GAME_REGION[2] - 1, 425] == loss_color:
        return True
    return False


# Main function
def main():
    game_is_on = True
    time.sleep(3)
    pyautogui.press('space')
    while game_is_on:
        img = ImageGrab.grab(bbox=GAME_REGION).convert("L")
        img_data = img.load()
        dark_theme = check_for_dark_theme(img_data)
        check_for_obstacle(img_data, dark_theme)
        if check_for_loss(img_data, dark_theme):
            game_is_on = False


if __name__ == "__main__":
    main()
