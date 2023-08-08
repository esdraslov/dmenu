import tkinter as win_form
import os

def _open_gameAssets(directory: str):
    return os.system(f"explorer.exe {directory}")

def open_custom_assets(full_path: str):
    try_att = _open_gameAssets(full_path)