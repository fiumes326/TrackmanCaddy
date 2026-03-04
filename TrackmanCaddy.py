#!/usr/bin/env python3

import os
import pyautogui
from pynput import keyboard
import threading
import time
import pyttsx3

IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

class TrackmanCaddy:
    def __init__(self):
        self.total_clicks = 0
        self.confidence = .80

        self.watch_thread_object = None
        self.stop_watcher_event = threading.Event()

        self.speech_engine = pyttsx3.init()
        self.keyboard_listener = None

    def _on_press(self, key):
        try:
            char = key.char
        except AttributeError:
            return

        if char == 'R':
            self.aim_right()
        elif char == 'r':
            self.nudge_right()
        elif char == 'L':
            self.aim_left()
        elif char == 'l':
            self.nudge_left()
        elif char == 'm':
            self.take_mulligan()

    def set_hotkeys(self):
        self.keyboard_listener = keyboard.Listener(on_press=self._on_press)
        self.keyboard_listener.start()
        

    def next_shot(self):
        try:
            location = pyautogui.locateOnScreen(os.path.join(IMAGES_DIR, "next.png"), confidence = self.confidence)
        except pyautogui.ImageNotFoundException:
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
        try:
            location = pyautogui.locateOnScreen(os.path.join(IMAGES_DIR, "mulligan.png"), confidence = self.confidence)
        except pyautogui.ImageNotFoundException:
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

        #helping wind
        if y_wind > 0:
            affected_yards = y_wind * .5
            calculated_yardage += affected_yards
        
        #hurting wind
        elif y_wind < 0:
            affected_yards = y_wind 
            calculated_yardage += affected_yards
        
        #add elevation
        calculated_yardage += elevation
        
        output = [f"{ground_yardage} yards playing {calculated_yardage}"]
        self.speek(output)
        print(f"{output[0]}\n")
        
    
    def watch_loop(self):
        while not self.stop_watcher_event.is_set():
            try:
                self.next_shot()
            except Exception:
                if self.stop_watcher_event.is_set():
                    break
            time.sleep(.2)
    

    def start_watcher_thread(self):
        if self.watch_thread_object and self.watch_thread_object.is_alive():
            return

        self.stop_watcher_event.clear()
        self.watch_thread_object = threading.Thread(target=self.watch_loop, daemon=True)
        self.watch_thread_object.start()
    
    def stop_watcher_thread(self):
        if not self.watch_thread_object:
            return

        self.stop_watcher_event.set()
        self.watch_thread_object.join(timeout=1)
        self.watch_thread_object = None

    def speek(self, text: list[str]):
        for phrase in text:
            self.speech_engine.say(phrase)

        self.speech_engine.runAndWait()
        
    def shutdown(self):
        if self.keyboard_listener:
            self.keyboard_listener.stop()
        self.stop_watcher_thread()
        print(f"Total Clicks: {self.total_clicks}")


