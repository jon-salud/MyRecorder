import platform

if platform.system() == "Windows":
    import win32gui
else:
    raise NotImplementedError("This application currently only supports Windows")

def get_active_window_title():
    """Get active window title (Windows only)."""
    if platform.system() == "Windows":
        window = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(window)
    else:
        raise NotImplementedError("This application currently only supports Windows")
