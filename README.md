# Chrome Dinosaur Game Automator
### (DISCLAIMER: Usually works )
This Python script automates the Chrome dinosaur game by detecting obstacles and reacting accordingly. It uses PyAutoGUI
and PIL libraries to capture screenshots and interact with the game window.

## Requirements

- Python 3.x
- PyAutoGUI
- PIL (Python Imaging Library)

## Installation

1. Install Python if you haven't already. You can download it from the official
   website: https://www.python.org/downloads/
2. Install the required libraries by running:
    ```bash
    pip install pyautogui pillow

## Usage

1. Open the Chrome browser and navigate to the dinosaur game.
2. Run the script using the following command:
    ```bash
   python dinosaur_game_automator.py

3. Switch to the Chrome window where the game is running.
4. The script will automatically start playing the game.

## Customization

You can customize the script by adjusting the following parameters in the code:

- `OBSTACLE_HEIGHTS`: Heights at which the script should check for obstacles.
- `SPACE_INTERVAL`: Interval between pressing the space key and the down key (adjust as needed).
- `GAME_REGION`: Define the region of the screen where the game is located.

## Notes

- Ensure that the game window is visible and not obstructed by any other windows.
- Adjust the parameters and thresholds based on your screen resolution and game settings for optimal performance.

## Disclaimer

This script is for educational purposes only. Use it responsibly and respect the terms of service of the game you are
automating.

## License

This project is licensed under the [MIT License](LICENSE).