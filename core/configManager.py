# Configuration Manager of the application, responsible for saving and loading user settings to/from a JSON file.

import json
import os

CONFIG_PATH = "config/config.json"

def save_config(app_state):
    data = {
        "mode": app_state.mode,
        "circle": {
            "color": app_state.circle_color,
            "size": app_state.circle_size,
            "opacity": app_state.opacity
        },
        "image": {
            "path": app_state.image_path
        }
    }

    os.makedirs("config", exist_ok=True)

    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def load_config(app_state):
    if not os.path.exists(CONFIG_PATH):
        print("No config file found, using default settings.")
        return

    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    app_state.mode = data.get("mode", "circle")

    circle = data.get("circle", {})
    app_state.circle_color = circle.get("color", "#ff0000")
    app_state.circle_size = circle.get("size", 30)
    app_state.opacity = circle.get("opacity", 1.0)

    image = data.get("image", {})
    app_state.image_path = image.get("path", "")
