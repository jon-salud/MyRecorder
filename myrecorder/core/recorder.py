import os
import logging
from datetime import datetime
from PIL import ImageGrab
from pynput import mouse, keyboard
from ..utils.window_utils import get_active_window_title
from ..config.settings import RECORDINGS_DIR

logger = logging.getLogger(__name__)

class WindowRecorder:
    def __init__(self, output_dir=RECORDINGS_DIR):
        self.output_dir = output_dir
        self.recording = False
        self.screenshots = []
        self.actions = []
        self.current_window = None
        os.makedirs(output_dir, exist_ok=True)
        logger.info(f"Initialized WindowRecorder with output directory: {output_dir}")

    def start(self):
        """Start recording session"""
        if not self.recording:
            self.recording = True
            self.screenshots = []
            self.actions = []
            self.current_window = get_active_window_title()
            logger.info(f"Started recording for window: {self.current_window}")

    def stop(self):
        """Stop recording session and save data"""
        if self.recording:
            self.recording = False
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"recording_{timestamp}.txt"
            filepath = os.path.join(self.output_dir, filename)
            
            with open(filepath, 'w') as f:
                f.write(f"Recording for: {self.current_window}\n")
                f.write(f"Actions: {len(self.actions)}\n")
                f.write(f"Screenshots: {len(self.screenshots)}\n")
            
            logger.info(f"Recording saved to: {filepath}")
            self.screenshots = []
            self.actions = []
            self.current_window = None

    # ...existing code for other methods...
