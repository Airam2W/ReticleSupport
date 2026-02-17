# Main program

from ui.configWindow import ConfigWindow
from core.appState import app_state
from overlay.circleOverlay import CircleOverlay
from core.configManager import load_config



def start_application():
    app_state.running = True
    overlay = CircleOverlay()
    overlay.root.mainloop()


if __name__ == "__main__":
    config_ui = ConfigWindow(start_application)
    config_ui.run()
