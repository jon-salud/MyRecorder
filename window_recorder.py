
import os
import time
from datetime import datetime
from PIL import ImageGrab
import mouse
from pynput import mouse as mouse_listener
from pynput import keyboard as keyboard_listener
import platform

if platform.system() == "Windows":
    import win32gui
elif platform.system() == "Darwin":
    from AppKit import NSWorkspace
else:
    import Xlib
    import Xlib.display

class WindowRecorder:
    def __init__(self, output_dir="recordings"):
        self.output_dir = output_dir
        self.recording = False
        self.screenshots = []
        self.actions = []
        self.current_window = None
        os.makedirs(output_dir, exist_ok=True)
        
    def start_recording(self):
        self.recording = True
        self.start_time = datetime.now()
        self.setup_listeners()
        
    def stop_recording(self):
        self.recording = False
        self.mouse_listener.stop()
        self.keyboard_listener.stop()
        self.generate_report()
        
    def setup_listeners(self):
        self.mouse_listener = mouse_listener.Listener(
            on_click=self.on_click)
        self.keyboard_listener = keyboard_listener.Listener(
            on_press=self.on_key_press)
        
        self.mouse_listener.start()
        self.keyboard_listener.start()
        
    def on_click(self, x, y, button, pressed):
        if pressed and self.recording:
            window_title = self.get_active_window_title()
            if window_title != self.current_window:
                self.capture_screenshot()
                self.current_window = window_title
            
            self.actions.append({
                'type': 'click',
                'position': (x, y),
                'window': window_title,
                'timestamp': datetime.now()
            })
            
    def on_key_press(self, key):
        if self.recording:
            window_title = self.get_active_window_title()
            if window_title != self.current_window:
                self.capture_screenshot()
                self.current_window = window_title
                
            self.actions.append({
                'type': 'keypress',
                'key': str(key),
                'window': window_title,
                'timestamp': datetime.now()
            })
            
    def capture_screenshot(self):
        screenshot = ImageGrab.grab()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        filepath = os.path.join(self.output_dir, filename)
        screenshot.save(filepath)
        self.screenshots.append({
            'filepath': filepath,
            'timestamp': datetime.now(),
            'window': self.current_window
        })
        
    def get_active_window_title(self):
        if platform.system() == "Windows":
            window = win32gui.GetForegroundWindow()
            return win32gui.GetWindowText(window)
        elif platform.system() == "Darwin":
            return NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
        else:
            display = Xlib.display.Display()
            window = display.get_input_focus().focus
            return window.get_wm_name()
            
    def generate_report(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = os.path.join(self.output_dir, f"recording_report_{timestamp}.md")
        
        with open(report_path, 'w') as f:
            f.write("# Window Recording Report\n\n")
            f.write(f"Recording started: {self.start_time}\n")
            f.write(f"Recording ended: {datetime.now()}\n\n")
            
            for screenshot in self.screenshots:
                f.write(f"## Window: {screenshot['window']}\n")
                f.write(f"Time: {screenshot['timestamp']}\n")
                f.write(f"![Screenshot]({screenshot['filepath']})\n\n")
                
                related_actions = [
                    action for action in self.actions 
                    if action['window'] == screenshot['window']
                ]
                
                if related_actions:
                    f.write("### Actions:\n")
                    for action in related_actions:
                        f.write(f"- {action['type']}: {action['timestamp']}\n")
                f.write("\n---\n\n")