import tkinter as tk
import win32gui
from core.appState import app_state
from PIL import Image, ImageTk
import os



ICON_RUTE = os.path.join(os.path.dirname(__file__), "../utils/working.ico")

class CircleOverlay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Reticle Support - Overlay")
        self.root.geometry("1x1+0+0")
        self.root.attributes("-alpha", 0.0)
        
        self.root.iconbitmap(ICON_RUTE)

        # Create a transparent overlay window
        self.overlay = tk.Toplevel(self.root)
        self.overlay.overrideredirect(True)
        self.overlay.attributes("-topmost", True)
        self.overlay.attributes("-transparentcolor", "black")

        self.image = None
        self.canvas = tk.Canvas(self.overlay, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.overlay.withdraw()
        self.update_loop()

    def draw_reticle(self):
        self.canvas.delete("all")
        size = app_state.circle_size

        if app_state.mode == "circle":
            self.canvas.create_oval(
                0, 0, size, size,
                fill=app_state.circle_color,
                outline=""
            )
        elif app_state.mode == "image" and app_state.image_path:
            img = Image.open(app_state.image_path).convert("RGBA")
            self.image = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, image=self.image, anchor="nw")

    def update_position(self):
        hwnd = app_state.target_hwnd
        if not hwnd:
            self.overlay.withdraw()
            return

        if win32gui.GetForegroundWindow() != hwnd:
            self.overlay.withdraw()
            return

        x1, y1, x2, y2 = win32gui.GetWindowRect(hwnd)
        width, height = x2 - x1, y2 - y1

        if app_state.mode == "circle":
            w = h = app_state.circle_size
        elif app_state.mode == "image" and self.image:
            w, h = self.image.width(), self.image.height()
        else:
            return

        cx = x1 + width // 2 - w // 2
        cy = y1 + height // 2 - h // 2

        self.overlay.geometry(f"{w}x{h}+{cx}+{cy}")
        if app_state.mode == "circle":
            self.overlay.attributes("-alpha", app_state.opacity)
        self.overlay.deiconify()

    def update_loop(self):
        if app_state.running:
            self.draw_reticle()
            self.update_position()
        self.overlay.after(30, self.update_loop)
