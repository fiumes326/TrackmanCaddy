import pyautogui
import keyboard
import threading
import time
import pyttsx3

class TrackmanCaddy:
    def __init__(self):
        self.total_clicks = 0
        self.confidence = .85

        self.watch_thread_object = None

        self.speech_engine = pyttsx3.init()

    def set_hotkeys():
        keyboard.add_hotkey("r", nudge_right, surpress=True)
        keyboard.add_hotkey("shift+r", aim_right, surpress=True)

        keyboard.add_hotkey("l", nudge_left, surpress=True)
        keyboard.add_hotkey("shift+l", aim_left, surpress=True)

        keyboard.add_hotkey("m", take_mulligan, surpress=True)
        

    def next_shot(self):
        location = pyautogui.locateOnScreen("../images/next_shot.png", confidence = self.confidence)
        if not location:
            return
        print("Heading to next shot...")
        center = pyautogui.center(location)
        pyautogui.click(center)
        self.total_clicks += 1

    def nudge_right(self):
        print("Nudging Right...")
        screen_width, screen_height = pyautogui.size()
        center_x = screen_width // 2
        center_y = screen_height // 2
        
        right_edge_x = screen_width - 1

        right_quater_x = (center_x + right_edge_x) // 4
        right_center_y = center_y

        pyautogui.click(right_quater_x, right_center_y)
        self.total_clicks += 1

    def nudge_left(self):
        print("Nudging Left...")
        screen_width, screen_height = pyautogui.size()
        center_x = screen_width // 2
        center_y = screen_height // 2
        
        left_edge_x = 0

        left_quater_x = (center_x + left_edge_x) // 4
        left_center_y = center_y

        pyautogui.click(left_center_x, left_center_y)
        self.total_clicks += 1


    def aim_right(self):
        print("Aiming Right...")
        screen_width, screen_height = pyautogui.size()
        center_x = screen_width // 2
        center_y = screen_height // 2
        
        right_edge_x = screen_width - 1

        right_center_x = (center_x + right_edge_x) // 2
        right_center_y = center_y

        pyautogui.click(right_center_x, right_center_y)
        self.total_clicks += 1

    def aim_left(self):
        print("Aiming Left...")
        screen_width, screen_height = pyautogui.size()
        center_x = screen_width // 2
        center_y = screen_height // 2
        
        left_edge_x = 0

        left_center_x = (center_x + left_edge_x) // 2
        left_center_y = center_y

        pyautogui.click(left_center_x, left_center_y)
        total_clicks += 1

    def take_mulligan(self):
        print("Taking A mulligan...")
        location = pyautogui.locateOnScreen("../images/mulligan.png", confidence = self.confidence)
        if not location:
            return

    def calculate_yardage():
        ground_yardage = 0
        calculated_yardage = ground_yardage
        elavation = 0
        x_wind = 0
        y_wind = 0
       
        #tailwind
        if y_wind > 0:
            affected_yards = y_wind * .5
            calculated_yardage -= affected_yards
       
        #tailwind
        else if y_wind < 0:
            calculated_yardage += y_wind
        
        #add elavation
        calculated_yardage += elavation
        
        output = [f"{ground_yardage} yards playing {calculated_yardage}"]
        self.speek(output)
        print(f"{ouput[0]}\n")
        
    
    def watch_loop(self):
        while True:
            self.next_shot()
            time.sleep(.2)
    

    def start_wacther_thread(self):
        self.wacth_thread_object = threading.Thread(target=self.watch_loop, daemon = True)
        self.wacth_thread_object.start()
    
    def stop_watcher_thread(self):
        self.watch_thread_object.stop()

    def speek(self, text: list[str]):
        for phrase in text:
            self.speech_engine.say(phrase)

        self.speech_engine.runAndWait()
        
    def shutdown(self):
        keyboard.unhook_all()
        self.stop_watcher_thread()


