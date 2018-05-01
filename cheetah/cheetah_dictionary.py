# coding=utf-8
import sys
import cheetah_dictionary_support

if sys.version_info.major == 2:
    from Tkinter import *
    import ttk
else:
    from tkinter import *
    import tkinter.ttk as ttk


def vp_start_gui():
    """Starting point when module is the main routine."""
    global val, w, root
    root = Tk()
    cheetah_dictionary_support.set_tk_var()
    top = CheetahDictionarySetting(root)
    cheetah_dictionary_support.init(root, top)
    root.mainloop()


w = None


def create_cheetah_dictionary_setting(root):
    """Starting point when module is imported by another program."""
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    cheetah_dictionary_support.set_tk_var()
    top = CheetahDictionarySetting(w)
    cheetah_dictionary_support.init(w, top)
    return w, top


def destroy_cheetah_dictionary_setting():
    global w
    w.destroy()
    w = None


class CheetahDictionarySetting:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])

        top.geometry("398x150+490+300")
        top.title("Cheetah Dictionary Setting")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.resizable(0, 0)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.05, rely=0.27, height=27, width=36)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Path :''')

        self.Button1 = Button(top)
        self.Button1.place(relx=0.89, rely=0.27, height=24, width=24)
        self.Button1.configure(takefocus="")
        self.Button1.configure(text='''...''')
        self.Button1.configure(command=cheetah_dictionary_support.set_pwd_file)

        self.TButton2 = ttk.Button(top)
        self.TButton2.place(relx=0.21, rely=0.6, height=27, width=98)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Dereplicat''')
        self.TButton2.configure(command=cheetah_dictionary_support.dereplicat_pwd_file)

        self.TButton3 = ttk.Button(top)
        self.TButton3.place(relx=0.54, rely=0.6, height=27, width=98)
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''OK''')
        self.TButton3.configure(command=cheetah_dictionary_support.exit_dict_setting)

        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1.place(relx=0.15, rely=0.27, relheight=0.18, relwidth=0.74)
        self.TCombobox1.configure(values=cheetah_dictionary_support.dict_list)
        self.TCombobox1.configure(textvariable=cheetah_dictionary_support.dict_path_var)
        self.TCombobox1.configure(takefocus="")
        # self.TCombobox1.set(cheetah_dictionary_support.dict_path)


if __name__ == '__main__':
    vp_start_gui()
