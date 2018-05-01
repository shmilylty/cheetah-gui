# coding=utf-8
import sys
from os import path
import cheetah_proxy_support

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
    cheetah_proxy_support.set_tk_var()
    top = CheetahProxySetting(root)
    cheetah_proxy_support.init(root, top)
    root.mainloop()


w = None


def create_cheetah_proxy_setting(root):
    """Starting point when module is imported by another program."""

    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    cheetah_proxy_support.set_tk_var()
    top = CheetahProxySetting(w)
    cheetah_proxy_support.init(w, top)
    return w, top


def destroy_cheetah_proxy_setting():
    global w
    w.destroy()
    w = None


class CheetahProxySetting:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _font9 = "-family Consolas -size 12 -weight normal -slant roman" \
                " -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        # self.style.configure('.',font=_font9)
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana1color)])

        top.geometry("600x490+393+110")
        top.title("Cheetah Proxy Setting")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.resizable(0, 0)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.07, rely=0.31, height=23, width=62)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Address :''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.08, rely=0.39, height=23, width=37)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Port :''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.07, rely=0.47, height=23, width=62)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Protocol :''')

        self.TEntry1 = ttk.Entry(top)
        self.TEntry1.place(relx=0.18, rely=0.31, relheight=0.05, relwidth=0.19)
        self.TEntry1.configure(textvariable=cheetah_proxy_support.address)
        self.TEntry1.configure(takefocus="")

        self.TCombobox5 = ttk.Combobox(top)
        self.TCombobox5.place(relx=0.18, rely=0.39, relheight=0.05, relwidth=0.19)
        self.value_list = [i for i in range(65536)]
        self.TCombobox5.configure(values=self.value_list)
        self.TCombobox5.configure(textvariable=cheetah_proxy_support.port)
        self.TCombobox5.configure(takefocus="")

        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1.place(relx=0.18, rely=0.47, relheight=0.05, relwidth=0.19)
        self.value_list = ["http", "https", "socks4", "socks4a", "socks5", "socks5h", ]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(state="readonly")
        self.TCombobox1.configure(textvariable=cheetah_proxy_support.protocol)
        self.TCombobox1.configure(takefocus="")

        self.Label4 = Label(top)
        self.Label4.place(relx=0.07, rely=0.55, height=21, width=68)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(text='''Username:''')

        self.TEntry3 = ttk.Entry(top)
        self.TEntry3.place(relx=0.18, rely=0.55, relheight=0.05, relwidth=0.19)
        self.TEntry3.configure(textvariable=cheetah_proxy_support.username)
        self.TEntry3.configure(takefocus="")
        # self.TEntry3.configure(cursor="ibeam")

        self.Label5 = Label(top)
        self.Label5.place(relx=0.07, rely=0.63, height=21, width=68)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(text='''Password:''')

        self.TEntry4 = ttk.Entry(top)
        self.TEntry4.place(relx=0.18, rely=0.63, relheight=0.05, relwidth=0.19)
        self.TEntry4.configure(textvariable=cheetah_proxy_support.password)
        self.TEntry4.configure(takefocus="")
        # self.TEntry4.configure(cursor="ibeam")

        self.Scrolledlistbox1 = ScrolledListBox(top)
        self.Scrolledlistbox1.place(relx=0.4, rely=0.31, relheight=0.47, relwidth=0.52)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1.configure(font=_font9)
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(selectforeground="black")
        self.Scrolledlistbox1.configure(width=10)

        self.TButton2 = ttk.Button(top)
        self.TButton2.place(relx=0.18, rely=0.71, height=27, width=77)
        self.TButton2.configure(command=cheetah_proxy_support.add_custom_proxy)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Add''')

        self.Label6 = Label(top)
        self.Label6.place(relx=0.07, rely=0.12, height=21, width=65)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(text='''Proxy list :''')

        self.data_dir = path.abspath(path.join(path.dirname(__file__), path.pardir, 'data'))
        self.proxy_path = path.join(self.data_dir, "proxy.txt")
        self.value_list = [self.proxy_path, ]
        self.TCombobox2 = ttk.Combobox(top)
        self.TCombobox2.place(relx=0.18, rely=0.12, relheight=0.05, relwidth=0.61)
        self.TCombobox2.configure(values=self.value_list)
        self.TCombobox2.configure(textvariable=cheetah_proxy_support.proxy_path_var)
        self.TCombobox2.configure(width=360)
        self.TCombobox2.configure(takefocus="")

        self.TButton3 = ttk.Button(top)
        self.TButton3.place(relx=0.82, rely=0.12, height=27, width=74)
        self.TButton3.configure(command=cheetah_proxy_support.import_proxy_list)
        # self.TButton3.configure(font="TkDefaultFont")
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''Import''')

        self.Label7 = Label(top)
        self.Label7.place(relx=0.07, rely=0.2, height=21, width=65)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(text='''Proxy api :''')

        self.TCombobox3 = ttk.Combobox(top)
        self.TCombobox3.place(relx=0.18, rely=0.2, relheight=0.05, relwidth=0.61)
        self.value_list = ["https://api.getproxylist.com/proxy",
                           "https://gimmeproxy.com/api/getProxy",
                           "http://pubproxy.com/api/proxy"]
        self.TCombobox3.configure(values=self.value_list)
        self.TCombobox3.configure(textvariable=cheetah_proxy_support.proxy_api)
        self.TCombobox3.configure(width=360)
        self.TCombobox3.configure(takefocus="")

        self.TButton4 = ttk.Button(top)
        self.TButton4.place(relx=0.82, rely=0.2, height=27, width=74)
        self.TButton4.configure(command=cheetah_proxy_support.get_proxy_list)
        self.TButton4.configure(takefocus="")
        self.TButton4.configure(text='''Get''')

        self.Label8 = Label(top)
        self.Label8.place(relx=0.08, rely=0.84, height=21, width=86)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(text='''Test address :''')

        self.TCombobox4 = ttk.Combobox(top)
        self.value_list = ["http://www.example.com",
                           "http://www.google.com",
                           "http://www.bing.com",
                           "http://www.baidu.com",
                           "http://www.yandex.com",
                           "http://www.naver.com",
                           "http://www.goo.ne.jp"]
        self.TCombobox4.place(relx=0.25, rely=0.84, relheight=0.05, relwidth=0.53)
        self.TCombobox4.configure(values=self.value_list)
        self.TCombobox4.configure(textvariable=cheetah_proxy_support.test_address)
        self.TCombobox4.configure(width=323)
        self.TCombobox4.configure(takefocus="")

        self.TButton5 = ttk.Button(top)
        self.TButton5.place(relx=0.8, rely=0.84, height=27, width=83)
        self.TButton5.configure(command=cheetah_proxy_support.validate_proxy)
        self.TButton5.configure(takefocus="")
        self.TButton5.configure(text='''Validate''')

        self.Checkbutton1 = Checkbutton(top)
        self.Checkbutton1.place(relx=0.07, rely=0.04, relwidth=0.14, relheight=0.0, height=23)
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(variable=cheetah_proxy_support.use_proxy)
        self.Checkbutton1.configure(text='''Use Proxy''')

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.43, rely=0.92, height=27, width=80)
        self.TButton1.configure(command=cheetah_proxy_support.exit_proxy_setting)
        self.TButton1.configure(text='''OK''')


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


if __name__ == '__main__':
    vp_start_gui()
