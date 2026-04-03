# ReticleSupport

ReticleSupport is a desktop tool for help with motion sickness caused while playing videogames in a PC.
For help with motion sickness, you can put a circle or any image that you want in the screen for rest your eyes.

---

## Why this project (ReticleSupport) was created?

When I was watching gameplays of a shooter 3D videogame or action 3D videogame where Streamer moved the character in third person or moved very fastly the reticle into the game.

Streamer put in the streaming software a orange circle image for specters, specters that get dizzy a lot while watching the streaming.

And also, when I was watching other Streamers, that Streamer once said, "Sorry. Probably I can't to continue this game because I get dizzy a lot. Sorry, I don't want to take motion sickness pills." (Actually that Streamer was the first time that play a 3D videogame in third person and don't like take constatly pills) and probably didn't know any tool for help with motion sickness, I think.

For this reason, I wanted to create a tool for help motion sickness and also support if someone want to play anyvideogame but get dizzy a lot and can't continue to play.

---

## Good things about this project (ReticleSupport)

- Can setting any circle (color, size/radius and opacity) that you want.
- Can setting any image (any format are allows, like: .png, .jpg and more) that you want.
- Can put a circle/image on any window that you want (Full screen videogame, video, etc) for help with motion sickness.
- Can save any configuration without loss it.

---

## Features of MultiCopy

- Easy to use.
- Simple interface.
- Settings persistence.

---

## Preview of MultiCopy

<img width="604" height="822" alt="image" src="https://github.com/user-attachments/assets/92cce51d-d320-439a-9278-a94427eac59a" />
<img width="604" height="827" alt="image" src="https://github.com/user-attachments/assets/6c1d7ec4-f472-4170-a54d-8207a8d8eece" />
<img width="301" height="409" alt="image" src="https://github.com/user-attachments/assets/04e87450-7d0b-40bf-b551-8e37c3e3b5b5" />
<img width="1919" height="962" alt="image" src="https://github.com/user-attachments/assets/a4d3a7bb-83ee-468f-b3ee-a0321a7520b5" />
<img width="1919" height="963" alt="image" src="https://github.com/user-attachments/assets/90c36fbb-63a7-407f-935a-0d815ac41b41" />


---

## Installation

- Step 1. Download *ReticleSupport.exe* located in the folder "dist"
- Step 2. Run *ReticleSupport.exe* and Work with it!

> **If you want to package a python program (MultiCopy) into .exe:**  
> I recommend use this command for it:
```bash
pyinstaller --onefile --windowed --icon=utils/logo.ico --add-data "config/config.json;config" --add-data "utils/working.ico;utils" --add-data "utils/settings.ico;utils" main.py
```

---

## Technologies

- Python (tkinter, win32gui, PIL and others)

---

## Future Improvements

- Add function to return to settings window.
- Improvements UI design.
- Add more functions for help with motion sickness.
