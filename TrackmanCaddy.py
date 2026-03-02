import pyautogui
import keyboard

class TrackmanCaddy:
    def __init__(self):
        self.total_clicks = 0
        self.confidence = .85

    def set_hotkeys():
        keyboard.add_hotkey("r", nudge_right, surpress=True)
        keyboard.add_hotkey("shift+r", aim_right, surpress=True)

        keyboard.add_hotkey("l", nudge_left, surpress=True)
        keyboard.add_hotkey("shift+l", aim_left, surpress=True)

        keyboard.add_hotkey("m", take_mulligan, surpress=True)
        

    def next_shot(self):
        location = pyautogui.locateOnsScreen("next_shot.png", confidence = self.confidence)
        center = pyautogui.center(location)
        pyautogui.click(center)
        self.total_clicks += 1

    def nudge_right(self):
        screen_width, screen_height = pyautogui.size()
        center_x = screen width // 2
        center_y = screen_height // 2
        
        right_edge_x = screen_width - 1

        right_quater_x = (center_x + right_edge_x) // 4
        right_center_y = center_y

        pyautogui.click(right_quater_x, right_center_y)

    def nudge_left(self):
        screen_width, screen_height = pyautogui.size()
        center_x = screen width // 2
        center_y = screen_height // 2
        
        left_edge_x = 0

        left_quater_x = (center_x + left_edge_x) // 4
        left_center_y = center_y

        pyautogui.click(left_center_x, left_center_y)


    def aim_right(self):
        screen_width, screen_height = pyautogui.size()
        center_x = screen width // 2
        center_y = screen_height // 2
        
        right_edge_x = screen_width - 1

        right_center_x = (center_x + right_edge_x) // 2
        right_center_y = center_y

        pyautogui.click(right_center_x, right_center_y)

    def aim_left(self):
        screen_width, screen_height = pyautogui.size()
        center_x = screen width // 2
        center_y = screen_height // 2
        
        left_edge_x = 0

        left_center_x = (center_x + left_edge_x) // 2
        left_center_y = center_y

        pyautogui.click(left_center_x, left_center_y)

    def take_mulligan(self): 
        pass

    def next_hole():
        pass

