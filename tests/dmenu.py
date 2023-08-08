import tkinter as win_form
import os, keyboard

def _open_gameAssets(directory: str):
    return os.system(f"explorer.exe {directory}")

def open_custom_assets(full_path: str):
    try_att = _open_gameAssets(full_path)
def _open_menu(Tk: win_form.Tk):
	Tk.mainloop()
def OMBK(key: str, Tk: win_form.Tk):
	if keyboard.is_pressed(key):
		_open_menu(Tk)
