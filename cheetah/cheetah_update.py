# coding=utf-8
import sys
import cheetah_update_support


if sys.version_info.major == 2:
    from Tkinter import *
    import ttk
    py3 = False
else:
    from tkinter import *
    import tkinter.ttk as ttk
    py3 = True

def vp_start_gui():
    """Starting point when module is the main routine."""
    global val, w, root
    root = Tk()
    cheetah_update_support.set_tk_var()
    top = CheetahUpdate(root)
    cheetah_update_support.init(root, top)
    root.mainloop()


w = None


def create_cheetah_update(root):
    """Starting point when module is imported by another program."""
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    cheetah_update_support.set_tk_var()
    top = CheetahUpdate(w)
    cheetah_update_support.init(w, top)
    return w, top


def destroy_cheetah_update():
    global w
    w.destroy()
    w = None


class CheetahUpdate:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana1color)])

        top.geometry("388x169+474+249")
        top.title("Cheetah Update")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.23, rely=0.71, height=27, width=87)
        self.TButton1.configure(command=cheetah_update_support.check_updates)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(textvariable=cheetah_update_support.check_update)

        self.Message1 = Message(top)
        self.Message1.place(relx=0.05, rely=0.12, relheight=0.44, relwidth=0.87)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(textvariable=cheetah_update_support.update_msg)
        self.Message1.configure(width=337)

        self.TButton2 = ttk.Button(top)
        self.TButton2.place(relx=0.57, rely=0.71, height=27, width=87)
        self.TButton2.configure(command=cheetah_update_support.exit_update)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Cancel''')


if __name__ == '__main__':
    vp_start_gui()
