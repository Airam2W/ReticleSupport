# This module provides utility functions for working with windows on the Windows operating system.

import win32gui


def list_open_windows():
    windows = []

    def enum_handler(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title and title.strip():
                windows.append((hwnd, title))

    win32gui.EnumWindows(enum_handler, None)
    return windows
