import pytest
from unittest.mock import patch, MagicMock
from myrecorder.core.recorder import WindowRecorder
from datetime import datetime

def test_window_recorder_init(temp_recording_dir):
    recorder = WindowRecorder(output_dir=temp_recording_dir)
    assert recorder.recording == False
    assert recorder.screenshots == []
    assert recorder.actions == []
    assert recorder.current_window == None

@patch('myrecorder.core.recorder.get_active_window_title')
def test_on_click(mock_get_title, temp_recording_dir, mock_window_title):
    mock_get_title.return_value = mock_window_title
    recorder = WindowRecorder(output_dir=temp_recording_dir)
    recorder.recording = True
    
    with patch('PIL.ImageGrab.grab') as mock_grab:
        mock_grab.return_value = MagicMock()
        recorder.on_click(100, 200, 'left', True)
        
        assert len(recorder.actions) == 1
        action = recorder.actions[0]
        assert action['type'] == 'click'
        assert action['position'] == (100, 200)
        assert action['window'] == mock_window_title

@patch('myrecorder.core.recorder.get_active_window_title')
def test_on_key_press(mock_get_title, temp_recording_dir, mock_window_title):
    mock_get_title.return_value = mock_window_title
    recorder = WindowRecorder(output_dir=temp_recording_dir)
    recorder.recording = True
    
    with patch('PIL.ImageGrab.grab') as mock_grab:
        mock_grab.return_value = MagicMock()
        recorder.on_key_press('a')
        
        assert len(recorder.actions) == 1
        action = recorder.actions[0]
        assert action['type'] == 'keypress'
        assert action['key'] == 'a'
        assert action['window'] == mock_window_title
