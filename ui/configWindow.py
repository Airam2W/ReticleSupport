# Configuration window shown at startup, allowing users to customize the reticle settings.

import tkinter as tk
from tkinter import ttk, colorchooser
from core.appState import app_state
from core.configManager import load_config, save_config
from utils.windowUtils import list_open_windows
from tkinter import filedialog



class ConfigWindow:

    def __init__(self, on_start_callback):
        self.on_start = on_start_callback

        self.root = tk.Tk()
        self.root.title("Reticle Support - Configuration")
        self.root.geometry("400x515")
        self.root.resizable(False, False)
        self.center_window(400, 515)
        self.opacity_var = tk.DoubleVar(value=app_state.opacity)
        
        load_config(app_state)
        
        self._build_ui()

    # ----------------------
    # UI
    # ----------------------
    def _build_ui(self):
        title = ttk.Label(
            self.root,
            text="Reticle Support",
            font=("Segoe UI", 16, "bold")
        )
        title.pack(pady=(0,5))
        
        # ---- Target Window ----
        window_frame = ttk.LabelFrame(self.root, text="Target Window")
        window_frame.pack(fill="x", padx=20, pady=10)

        self.window_list = list_open_windows()
        self.window_titles = [title for _, title in self.window_list]

        self.window_var = tk.StringVar()

        self.window_combo = ttk.Combobox(
            window_frame,
            textvariable=self.window_var,
            values=self.window_titles,
            state="readonly"
        )
        self.window_combo.pack(fill="x", padx=10, pady=5)

        ttk.Button(
            window_frame,
            text="Refresh window list",
            command=self.refresh_window_list
        ).pack(pady=5)

        # ---- Reticle Mode ----
        mode_frame = ttk.LabelFrame(self.root, text="Reticle Mode")
        mode_frame.pack(fill="x", padx=20, pady=10)

        self.mode_var = tk.StringVar(value=app_state.mode)

        ttk.Radiobutton(
            mode_frame,
            text="Circle",
            value="circle",
            variable=self.mode_var,
            command=self.on_mode_change
        ).pack(anchor="w", padx=10, pady=2)

        ttk.Radiobutton(
            mode_frame,
            text="Image",
            value="image",
            variable=self.mode_var,
            command=self.on_mode_change
        ).pack(anchor="w", padx=10, pady=2)


        self.circle_image_frame = ttk.LabelFrame(
            self.root,
            text="Circle Settings"
        )
        self.circle_image_frame.pack(fill="x", padx=20, pady=10)
        
        # ---- Circle widgets ----
        self.circle_widgets = []

        lbl = ttk.Label(self.circle_image_frame, text="Color:")
        lbl.pack(anchor="w", padx=10)
        self.circle_widgets.append(lbl)

        color_row = ttk.Frame(self.circle_image_frame)
        color_row.pack(anchor="w", padx=10, pady=5)

        self.color_preview = tk.Canvas(
            color_row,
            width=20,
            height=20,
            highlightthickness=1,
            highlightbackground="black"
        )
        self.color_preview.pack(side="left", padx=(0, 8))

        self.color_rect = self.color_preview.create_rectangle(
            0, 0, 20, 20,
            fill=app_state.circle_color,
            outline=""
        )

        btn = ttk.Button(
            color_row,
            text="Choose color",
            command=self.choose_color
        )
        btn.pack(side="left")

        self.circle_widgets.extend([color_row])


        lbl = ttk.Label(self.circle_image_frame, text="Size (radius):")
        lbl.pack(anchor="w", padx=10)
        self.circle_widgets.append(lbl)

        self.size_var = tk.IntVar(value=app_state.circle_size)
        spin = ttk.Spinbox(
            self.circle_image_frame,
            from_=5,
            to=200,
            textvariable=self.size_var,
            width=10
        )
        spin.pack(padx=10, pady=5)
        self.circle_widgets.append(spin)

        lbl = ttk.Label(self.circle_image_frame, text="Opacity:")
        lbl.pack(anchor="w", padx=10)
        self.circle_widgets.append(lbl)
        
        opacity_preview_row = ttk.Frame(self.circle_image_frame)
        opacity_preview_row.pack(anchor="w", padx=10, pady=5)

        self.opacity_preview = tk.Canvas(
            opacity_preview_row,
            width=20,
            height=20,
            highlightthickness=1,
            highlightbackground="black"
        )
        self.opacity_preview.pack(side="left", padx=(0, 8))

        self.opacity_rect = self.opacity_preview.create_rectangle(
            0, 0, 20, 20,
            fill=self._color_with_opacity(),
            outline=""
        )
        
        scale = ttk.Scale(
            opacity_preview_row,
            from_=0.1,
            to=1.0,
            orient="horizontal",
            variable=self.opacity_var,
            command=lambda e: self.update_opacity_preview()
        )
        scale.pack(fill="x", padx=10, pady=5)
        self.circle_widgets.append(opacity_preview_row)

        
        
        # ---- Image widgets ----
        self.image_widgets = []

        self.image_label = ttk.Label(
            self.circle_image_frame,
            text=app_state.image_path.split("/")[-1] if app_state.image_path else "No image selected"
        )
        self.image_widgets.append(self.image_label)

        img_btn = ttk.Button(
            self.circle_image_frame,
            text="Choose image",
            command=self.choose_image
        )
        img_btn.pack(padx=10, pady=5)
        self.image_widgets.append(img_btn)

        
        # ---- Start Button ----
        ttk.Button(
            self.root,
            text="Start",
            command=self.start
        ).pack(pady=(0,20))
        
        self.on_mode_change()
        

    def choose_color(self):
        color = colorchooser.askcolor(title="Choose circle color")
        if color[1]:
            app_state.circle_color = color[1]
            self.color_preview.itemconfig(self.color_rect, fill=color[1])
            self.update_opacity_preview()

            
    def _color_with_opacity(self):
        hex_color = app_state.circle_color.lstrip("#")
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)

        opacity = self.opacity_var.get()

        bg = 255  # white background
        r = int(bg + (r - bg) * opacity)
        g = int(bg + (g - bg) * opacity)
        b = int(bg + (b - bg) * opacity)

        return f"#{r:02x}{g:02x}{b:02x}"
    
    def update_opacity_preview(self):
        self.opacity_preview.itemconfig(
            self.opacity_rect,
            fill=self._color_with_opacity()
        )


            
    # -------------------------
    # AUX FUNCTIONS
    # -------------------------
    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
    def refresh_window_list(self):
        self.window_list = list_open_windows()
        self.window_titles = [title for _, title in self.window_list]
        self.window_combo["values"] = self.window_titles


    def save_selected_window(self):
        selected_title = self.window_var.get()
        for hwnd, title in self.window_list:
            if title == selected_title:
                app_state.target_hwnd = hwnd
                app_state.target_window_title = title
                break
            
    def on_mode_change(self):
        mode = self.mode_var.get()
        app_state.mode = mode

        # Ocultar todo
        for w in self.circle_widgets + self.image_widgets:
            w.pack_forget()

        if mode == "circle":
            self.circle_image_frame.config(text="Circle Settings")
            for w in self.circle_widgets:
                w.pack(padx=10, pady=5)
        else:
            self.circle_image_frame.config(text="Image Settings")
            for w in self.image_widgets:
                w.pack(padx=10, pady=5)

            
    def choose_image(self):
        path = filedialog.askopenfilename(
            title="Select reticle image",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.bmp")
            ]
        )

        if path:
            app_state.image_path = path
            self.image_label.config(text=path.split("/")[-1])





    # -------------------------
    # System functions
    # -------------------------
    def start(self):
        if self.window_var.get() == "":
            tk.messagebox.showerror("Error", "Please select a target window")
            return
        app_state.circle_size = self.size_var.get()
        app_state.opacity = self.opacity_var.get()
        app_state.mode = self.mode_var.get()
        app_state.running = True
        self.save_selected_window()
        save_config(app_state)
        self.root.destroy()
        self.on_start()


    def run(self):
        self.root.mainloop()
