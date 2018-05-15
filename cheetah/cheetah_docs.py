# coding=utf-8
import platform

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import cheetah_docs_support


def vp_start_gui():
    """Starting point when module is the main routine."""
    global val, w, root
    root = Tk()
    top = CheetahDocs(root)
    cheetah_docs_support.init(root, top)
    root.mainloop()


w = None


def create_cheetah_docs(root):
    """Starting point when module is imported by another program."""
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = CheetahDocs(w)
    cheetah_docs_support.init(w, top)
    return w, top


def destroy_cheetah_docs():
    global w
    w.destroy()
    w = None


class CheetahDocs:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""
        font9 = "-family Consolas -size 9 -weight normal -slant roman " \
                "-underline 0 -overstrike 0"
        if platform.system() == 'Windows':
            font9 = "-family Consolas -size 9 -weight normal -slant roman " \
                    "-underline 0 -overstrike 0"
        if platform.system() == 'Darwin':
            font9 = "-family Monaco -size 10 -weight normal -slant roman " \
                    "-underline 0 -overstrike 0"
        if platform.system() == 'Linux':
            font9 = "-family SourceCodePro -size 9 -weight normal -slant roman " \
                    "-underline 0 -overstrike 0"
        top.geometry("669x405+360+140")
        top.title("Cheetah Docs")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.resizable(0, 0)

        self.banner = Message(top)
        self.banner.place(relx=0.21, rely=0.02, relheight=0.33, relwidth=0.55)
        self.banner.configure(background="#d9d9d9")
        self.banner.configure(font=font9)
        self.banner.configure(foreground="#000000")
        self.banner.configure(highlightbackground="#d9d9d9")
        self.banner.configure(highlightcolor="black")
        self.banner.configure(justify=CENTER)
        self.banner.configure(text=r'''
_________________________________________________
       ______              _____         ______  
__________  /_ _____ _____ __  /_______ ____  /_ 
_  ___/__  __ \_  _ \_  _ \_  __/_  __ \ __  __ \
/ /__  _  / / //  __//  __// /_  / /_/ / _  / / /
\___/  / / /_/ \___/ \___/ \__/  \____/  / / /_/ 
      /_/                               /_/      

a very fast brute force webshell password tool.''')
        self.banner.configure(width=367)

        self.help = Message(top)
        self.help.place(relx=0.04, rely=0.42, relheight=0.53, relwidth=0.91)
        self.help.configure(background="#d9d9d9")
        self.help.configure(font=font9)

        self.help.configure(foreground="#000000")
        self.help.configure(highlightbackground="#d9d9d9")
        self.help.configure(highlightcolor="black")
        self.help.configure(text='''
Target                  Set the webshell url(s)
Start                   Start brute force
Stop                    Stop brute force
Method                  Select request method(default POST)
Server                  Select web server name(default detect)
Type                    Select webshell type(default detect)
Parameter               Set the number of request parameters(default 0 auto-set)
Thread number           Set the number of request threads(default 1)
Request delay           Set the request delay(default 0s)
Request timeout         Set the request timeout(default 10s)
Random User-Agent       Set the User-Agent field for the HTTP header(default enable)
Connection: close       Set the Connection field for the HTTP header(default enable)
Keep-Alive: 0           Set the Keep-Alive field for the HTTP header(default enable)
Custom request header   Custom the HTTP header of requesting''')
        self.help.configure(width=607)


if __name__ == '__main__':
    vp_start_gui()
