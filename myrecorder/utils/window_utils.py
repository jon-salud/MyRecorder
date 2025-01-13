import platform

if platform.system() == "Windows":
    import win32gui
elif platform.system() == "Darwin":
    from AppKit import NSWorkspace
else:
    import Xlib
    import Xlib.display

def get_active_window_title():
    """Get active window title across different platforms."""
    if platform.system() == "Windows":
        window = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(window)
    elif platform.system() == "Darwin":
        return NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    else:
        display = Xlib.display.Display()
        window = display.get_input_focus().focus
        return window.get_wm_name()
