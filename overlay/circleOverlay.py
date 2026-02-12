# Circle's Overlay

from logging import root
import tkinter as tk
import win32gui
import win32con
from core.appState import app_state
from PIL import Image, ImageTk
import win32gui
import win32con


class CircleOverlay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-transparentcolor", "black")
        self.image = None


        self.canvas = tk.Canvas(
            self.root,
            bg="black",
            highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)

        self.root.withdraw()

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
            self.root.withdraw()
            return

        if win32gui.GetForegroundWindow() != hwnd:
            self.root.withdraw()
            return

        x1, y1, x2, y2 = win32gui.GetWindowRect(hwnd)
        width = x2 - x1
        height = y2 - y1

        if app_state.mode == "circle":
            w = h = app_state.circle_size

        elif app_state.mode == "image" and self.image:
            w = self.image.width()
            h = self.image.height()

        else:
            return

        cx = x1 + width // 2 - w // 2
        cy = y1 + height // 2 - h // 2

        self.root.geometry(f"{w}x{h}+{cx}+{cy}")
        if app_state.mode == "circle":
            self.root.attributes("-alpha", app_state.opacity)
        self.root.deiconify()


    def update_loop(self):
        if app_state.running:
            self.draw_reticle()
            self.update_position()

        self.root.after(30, self.update_loop)