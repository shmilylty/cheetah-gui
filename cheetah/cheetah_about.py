# coding=utf-8
import sys
import cheetah_about_support

if sys.version_info.major == 2:
    from Tkinter import *
else:
    from tkinter import *


def vp_start_gui():
    """Starting point when module is the main routine."""
    global val, w, root
    root = Tk()
    top = CheetahAbout(root)
    cheetah_about_support.init(root, top)
    root.mainloop()


w = None


def create_cheetah_about(root, *args, **kwargs):
    """Starting point when module is imported by another program."""
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = CheetahAbout(w)
    cheetah_about_support.init(w, top)
    return w, top


def destroy_cheetah_about():
    global w
    w.destroy()
    w = None


class CheetahAbout:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'

        top.geometry("530x388+432+184")
        top.title("Cheetah About")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.resizable(0, 0)

        self.Message1 = Message(top)
        self.Message1.place(relx=0.08, rely=0.08, relheight=0.84, relwidth=0.84)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''
        Cheetah is a very fast brute force webshell password tool.
        Program: cheetah
        Version: 1.0.0
        License: GNU GPLv3
        Author: admin[@hackfun.org]
        Github: https://github.com/sunnyelf/cheetah
        
        Description:
        Cheetah is a dictionary-based webshell password violent cracker
        that runs like a cheetah hunt for prey as swift and violent.
        Cheetah's working principle is that it can submit a large number
        of detection passwords based on different web services at once,
        blasting efficiency is thousands of times other common webshell
        password violent crack tools.''')
        self.Message1.configure(width=447)
        self.menubar = Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)


if __name__ == '__main__':
    vp_start_gui()
