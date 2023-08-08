import dmenu
import tkinter
import pytest
import os
import keyboard

tk = dmenu.win_form.Tk()

def test1():
    assert dmenu.win_form == tkinter
def test2():
    dmenu.open_custom_assets(f"C:\\Users\\HP\\Documents\\dmenu\\tests\\assets_fake")
def test3():
    dmenu.OMBK("F1", tk)
