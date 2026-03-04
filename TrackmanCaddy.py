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

    def set_hotkeys(self):
        keyboard.add_hotkey("r", self.nudge_right, suppress=True)
        keyboard.add_hotkey("shift+r", self.aim_right, suppress=True)

        keyboard.add_hotkey("l", self.nudge_left, suppress=True)
        keyboard.add_hotkey("shift+l", self.aim_left, suppress=True)

        keyboard.add_hotkey("m", self.take_mulligan, suppress=True)
        

    def next_shot(self):
        location = pyautogui.locateOnScreen("../images/next.jpeg", confidence = self.confidence)
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

        pyautogui.click(left_quater_x, left_center_y)
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
        self.total_clicks += 1

    def take_mulligan(self):
        print("Taking A mulligan...")
        location = pyautogui.locateOnScreen("../images/mulligan.png", confidence = self.confidence)
        if not location:
            return

    def get_shot_info(self):
        ground_yardage = 0
        calculated_yardage = ground_yardage
        elevation = 0
        x_wind = 0
        y_wind = 0

        return (ground_yardage, calculated_yardage, elevation, x_wind, y_wind)           

    def calculate_yardage(self):
        ground_yardage, calculated_yardage, elevation, x_wind, y_wind = self.get_shot_info() 

        #tailwind
        if y_wind > 0:
            affected_yards = y_wind * .5
            calculated_yardage -= affected_yards
        
        #headwind
        elif y_wind < 0:
            affected_yards = y_wind 
            calculated_yardage -= affected_yards
        
        #add elevation
        calculated_yardage += elevation
        
        output = [f"{ground_yardage} yards playing {calculated_yardage}"]
        self.speek(output)
        print(f"{output[0]}\n")
        
    
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
        print(f"Total Clicks: {self.total_clicks}")


