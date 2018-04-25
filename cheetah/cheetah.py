# coding=utf-8
import sys
import cheetah_support
from os import path

if sys.version_info.major == 2:
    from Tkinter import *
    import ttk
    py3 = False
else:
    from tkinter import *
    import tkinter.ttk as ttk
    py3 = True


data_dir = path.abspath(path.join(path.dirname(__file__), path.pardir, 'data'))


def vp_start_gui():
    """Starting point when module is the main routine."""
    global val, w, root
    root = Tk()
    cheetah_support.set_tk_var()
    top = Cheetah(root)
    cheetah_support.init(root, top)
    root.mainloop()


w = None


def create_cheetah(root):
    """Starting point when module is imported by another program."""
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    cheetah_support.set_tk_var()
    top = Cheetah(w)
    cheetah_support.init(w, top)
    return w, top


def destroy_cheetah():
    global w
    w.destroy()
    w = None


class Cheetah:
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
        self.logo_path = path.join(data_dir, 'cheetah.ico')

        if path.exists(self.logo_path):
            top.iconbitmap(default=self.logo_path)
        # top.iconify()
        top.geometry("600x450+393+128")
        top.title("Cheetah")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.resizable(0, 0)

        self.menubar = Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.options = Menu(top, tearoff=0)
        self.menubar.add_cascade(
            menu=self.options,
            activebackground="#d9d9d9",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="Options")
        self.options.add_command(
            activebackground="#d8d8d8",
            activeforeground="#000000",
            background="#d9d9d9",
            command=cheetah_support.set_parameters,
            font="TkMenuFont",
            foreground="#000000",
            label="Configure...")
        self.options.add_command(
            activebackground="#d8d8d8",
            activeforeground="#000000",
            background="#d9d9d9",
            command=cheetah_support.set_dict,
            font="TkMenuFont",
            foreground="#000000",
            label="Dictionary...")
        self.options.add_command(
            activebackground="#d8d8d8",
            activeforeground="#000000",
            background="#d9d9d9",
            command=cheetah_support.set_proxy,
            font="TkMenuFont",
            foreground="#000000",
            label="Proxy...")
        self.help = Menu(top, tearoff=0)
        self.menubar.add_cascade(
            menu=self.help,
            activebackground="#d9d9d9",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="Help")
        self.help.add_command(
            activebackground="#d8d8d8",
            activeforeground="#000000",
            background="#d9d9d9",
            command=cheetah_support.open_about,
            font="TkMenuFont",
            foreground="#000000",
            label="About...")
        self.help.add_command(
            activebackground="#d8d8d8",
            activeforeground="#000000",
            background="#d9d9d9",
            command=cheetah_support.submit_bugs,
            font="TkMenuFont",
            foreground="#000000",
            label="Bugs")
        self.help.add_command(
            activebackground="#d8d8d8",
            activeforeground="#000000",
            background="#d9d9d9",
            command=cheetah_support.open_docs,
            font="TkMenuFont",
            foreground="#000000",
            label="Docs...")
        self.help.add_command(
            activebackground="#d8d8d8",
            activeforeground="#000000",
            background="#d9d9d9",
            command=cheetah_support.check_updates,
            font="TkMenuFont",
            foreground="#000000",
            label="Update...")

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.03, rely=0.04, height=21, width=49)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text='''Target :''')

        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1.place(relx=0.13, rely=0.04, relheight=0.055, relwidth=0.66)
        self.data_dir = path.abspath(path.join(path.dirname(__file__), path.pardir, 'data'))
        self.url_path = path.join(self.data_dir, "url.txt")
        self.value_list = ["http://localhost/post_shell.php", self.url_path]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(textvariable=cheetah_support.target)
        self.TCombobox1.configure(takefocus="")

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.78, rely=0.04, height=25, width=27)
        self.TButton1.configure(command=cheetah_support.set_url_file)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''...''')

        self.TButton2 = ttk.Button(top)
        self.TButton2.place(relx=0.85, rely=0.04, height=27, width=67)
        self.TButton2.configure(command=cheetah_support.start_brute_force)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(textvariable=cheetah_support.state)

        self.Scrolledlistbox1 = ScrolledListBox(top)
        self.Scrolledlistbox1.place(relx=0.03, rely=0.13, relheight=0.8, relwidth=0.94)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(selectforeground="black")
        self.Scrolledlistbox1.configure(width=10)

        self.Message1 = Message(top)
        self.Message1.place(relx=0.02, rely=0.93, relheight=0.06, relwidth=0.26)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(textvariable=cheetah_support.progress_status)
        self.Message1.configure(width=137)


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    """Configure the scrollbars for a widget."""

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        # self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                      | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                      + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        """Hide and show scrollbar as needed."""

        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)

        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    """Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget."""

    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)

    return wrapped


class ScrolledListBox(AutoScroll, Listbox):
    """A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed."""

    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


def main():
    vp_start_gui()


if __name__ == '__main__':
    main()
