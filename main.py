import logging.config
import keyboard
from myrecorder.core.recorder import WindowRecorder
from myrecorder.config.settings import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

def main():
    recorder = WindowRecorder()
    logger.info("Starting recorder application")
    print("Press 'F9' to start recording")
    print("Press 'F10' to stop recording")
    
    keyboard.wait('F9')
    logger.info("Recording started")
    print("Recording started...")
    recorder.start_recording()
    
    keyboard.wait('F10')
    logger.info("Recording stopped")
    print("Recording stopped...")
    recorder.stop_recording()

if __name__ == "__main__":
    main()
