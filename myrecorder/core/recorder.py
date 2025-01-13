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

    # ...existing code for other methods...
