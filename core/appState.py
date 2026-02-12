# Global application state. This object stores user configuration selected in the UI.

class AppState:
    def __init__(self):
        self.running = False

        # Window
        self.target_hwnd = None
        self.target_window_title = ""

        # Reticle
        self.mode = "circle"   # "circle" or "image"
        self.circle_size = 20
        self.circle_color = "#00FF00"
        self.opacity = 0.7
        self.image_path = ""

        # Shortcut
        self.settings_hotkey = "<ctrl>+<shift>+r"


app_state = AppState()
