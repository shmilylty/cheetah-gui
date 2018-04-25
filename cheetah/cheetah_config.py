# coding=utf-8
import sys
import cheetah_config_support

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
    cheetah_config_support.set_tk_var()
    top = CheetahConfig(root)
    cheetah_config_support.init(root, top)
    root.mainloop()


w = None


def create_cheetah_config(root):
    """Starting point when module is imported by another program."""
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    cheetah_config_support.set_tk_var()
    top = CheetahConfig(w)
    cheetah_config_support.init(w, top)
    return w, top


def destroy_cheetah_config():
    cheetah_config_support.save_config()
    global w
    w.destroy()
    w = None


class CheetahConfig:
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

        top.geometry("600x420+393+178")
        top.title("Cheetah Configure")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.resizable(0, 0)

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.03, rely=0.05, height=24, width=57)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text='''Method :''')

        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1.place(relx=0.13, rely=0.05, relheight=0.06, relwidth=0.11)
        self.value_list = ["post", "get"]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(state="readonly")
        self.TCombobox1.configure(textvariable=cheetah_config_support.method)
        self.TCombobox1.configure(takefocus="")

        self.TLabel2 = ttk.Label(top)
        self.TLabel2.place(relx=0.27, rely=0.05, height=24, width=48)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief=FLAT)
        self.TLabel2.configure(text='''Server :''')

        self.TCombobox2 = ttk.Combobox(top)
        self.TCombobox2.place(relx=0.35, rely=0.05, relheight=0.06, relwidth=0.12)
        self.value_list = ["detect", "apache", "nginx", "iis", ]
        self.TCombobox2.configure(values=self.value_list)
        self.TCombobox2.configure(state="readonly")
        self.TCombobox2.configure(textvariable=cheetah_config_support.server)
        self.TCombobox2.configure(takefocus="")

        self.TLabel3 = ttk.Label(top)
        self.TLabel3.place(relx=0.5, rely=0.05, height=24, width=39)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief=FLAT)
        self.TLabel3.configure(text='''Type :''')

        self.TCombobox3 = ttk.Combobox(top)
        self.TCombobox3.place(relx=0.57, rely=0.05, relheight=0.06, relwidth=0.12)
        self.value_list = ["detect", "php", "jsp", "asp", "aspx", ]
        self.TCombobox3.configure(values=self.value_list)
        self.TCombobox3.configure(state="readonly")
        self.TCombobox3.configure(textvariable=cheetah_config_support.shelltype)
        self.TCombobox3.configure(takefocus="")

        self.TLabel4 = ttk.Label(top)
        self.TLabel4.place(relx=0.72, rely=0.05, height=24, width=71)
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font="TkDefaultFont")
        self.TLabel4.configure(relief=FLAT)
        self.TLabel4.configure(text='''Parameter :''')

        self.TCombobox4 = ttk.Combobox(top)
        self.TCombobox4.place(relx=0.84, rely=0.05, relheight=0.06, relwidth=0.12)
        self.value_list = ["1000", ]
        self.TCombobox4.configure(values=self.value_list)
        self.TCombobox4.configure(textvariable=cheetah_config_support.parameter)
        self.TCombobox4.configure(takefocus="")

        self.TLabel5 = ttk.Label(top)
        self.TLabel5.place(relx=0.03, rely=0.17, height=21, width=97)
        self.TLabel5.configure(background="#d9d9d9")
        self.TLabel5.configure(foreground="#000000")
        self.TLabel5.configure(font="TkDefaultFont")
        self.TLabel5.configure(relief=FLAT)
        self.TLabel5.configure(text='''Thread number:''')

        self.Spinbox1 = Spinbox(top, from_=1.0, to=100.0)
        self.Spinbox1.place(relx=0.2, rely=0.17, relheight=0.05, relwidth=0.12)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1.configure(foreground="black")
        self.Spinbox1.configure(from_="1.0")
        self.Spinbox1.configure(increment="1.0")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(highlightcolor="black")
        self.Spinbox1.configure(insertbackground="black")
        self.Spinbox1.configure(selectbackground="#c4c4c4")
        self.Spinbox1.configure(selectforeground="black")
        self.Spinbox1.configure(state="disable")
        self.Spinbox1.configure(textvariable=cheetah_config_support.thread_num)
        self.Spinbox1.configure(to="100.0")

        self.TLabel6 = ttk.Label(top)
        self.TLabel6.place(relx=0.35, rely=0.17, height=21, width=93)
        self.TLabel6.configure(background="#d9d9d9")
        self.TLabel6.configure(foreground="#000000")
        self.TLabel6.configure(font="TkDefaultFont")
        self.TLabel6.configure(relief=FLAT)
        self.TLabel6.configure(text='''Request delay :''')

        self.Spinbox2 = Spinbox(top, from_=0.0, to=60.0)
        self.Spinbox2.place(relx=0.52, rely=0.17, relheight=0.05, relwidth=0.12)
        self.Spinbox2.configure(activebackground="#f9f9f9")
        self.Spinbox2.configure(background="white")
        self.Spinbox2.configure(buttonbackground="#d9d9d9")
        self.Spinbox2.configure(disabledforeground="#a3a3a3")
        self.Spinbox2.configure(foreground="black")
        self.Spinbox2.configure(from_="0.0")
        self.Spinbox2.configure(increment="0.5")
        self.Spinbox2.configure(highlightbackground="black")
        self.Spinbox2.configure(highlightcolor="black")
        self.Spinbox2.configure(insertbackground="black")
        self.Spinbox2.configure(selectbackground="#c4c4c4")
        self.Spinbox2.configure(selectforeground="black")
        self.Spinbox2.configure(textvariable=cheetah_config_support.req_delay)
        self.Spinbox2.configure(to="60.0")
        # self.Spinbox2.configure(value="0.0")
        # print(self.Spinbox2.get())

        self.TLabel7 = ttk.Label(top)
        self.TLabel7.place(relx=0.65, rely=0.17, height=21, width=106)
        self.TLabel7.configure(background="#d9d9d9")
        self.TLabel7.configure(foreground="#000000")
        self.TLabel7.configure(font="TkDefaultFont")
        self.TLabel7.configure(relief=FLAT)
        self.TLabel7.configure(text='''Request timeout :''')

        self.Spinbox3 = Spinbox(top, from_=10.0, to=60.0)
        self.Spinbox3.place(relx=0.84, rely=0.17, relheight=0.05, relwidth=0.12)
        self.Spinbox3.configure(activebackground="#f9f9f9")
        self.Spinbox3.configure(background="white")
        self.Spinbox3.configure(buttonbackground="#d9d9d9")
        self.Spinbox3.configure(disabledforeground="#a3a3a3")
        self.Spinbox3.configure(foreground="black")
        self.Spinbox3.configure(from_="10.0")
        self.Spinbox3.configure(increment="0.5")
        self.Spinbox3.configure(highlightbackground="black")
        self.Spinbox3.configure(highlightcolor="black")
        self.Spinbox3.configure(insertbackground="black")
        self.Spinbox3.configure(selectbackground="#c4c4c4")
        self.Spinbox3.configure(selectforeground="black")
        self.Spinbox3.configure(textvariable=cheetah_config_support.time_out)
        self.Spinbox3.configure(to="60.0")

        self.TLabel8 = ttk.Label(top)
        self.TLabel8.place(relx=0.03, rely=0.29, height=21, width=119)
        self.TLabel8.configure(background="#d9d9d9")
        self.TLabel8.configure(foreground="#000000")
        self.TLabel8.configure(font="TkDefaultFont")
        self.TLabel8.configure(relief=FLAT)
        self.TLabel8.configure(text='''Forge HTTP Header''')

        self.style.map('TCheckbutton', background=[('selected', _bgcolor), ('active', _ana1color)])
        self.TCheckbutton1 = ttk.Checkbutton(top)
        self.TCheckbutton1.place(relx=0.1, rely=0.36, relwidth=0.24, relheight=0.0, height=23)
        # self.TCheckbutton1.bind("<ButtonRelease-1>", cheetah_config_support.save_random_ua)
        self.TCheckbutton1.configure(command=cheetah_config_support.save_config)
        self.TCheckbutton1.configure(variable=cheetah_config_support.random_ua)
        self.TCheckbutton1.configure(takefocus="")
        self.TCheckbutton1.configure(text='''Random User-Agent''')

        self.TCheckbutton2 = ttk.Checkbutton(top)
        self.TCheckbutton2.place(relx=0.42, rely=0.36, relwidth=0.21, relheight=0.0, height=23)
        self.TCheckbutton2.configure(command=cheetah_config_support.save_config)
        self.TCheckbutton2.configure(variable=cheetah_config_support.con_close)
        self.TCheckbutton2.configure(takefocus="")
        self.TCheckbutton2.configure(text='''Connection: close''')

        self.TCheckbutton3 = ttk.Checkbutton(top)
        self.TCheckbutton3.place(relx=0.72, rely=0.36, relwidth=0.17, relheight=0.0, height=23)
        self.TCheckbutton3.configure(command=cheetah_config_support.save_config)
        self.TCheckbutton3.configure(variable=cheetah_config_support.keep_alive)
        self.TCheckbutton3.configure(takefocus="")
        self.TCheckbutton3.configure(text='''Keep-Alive: 0''')

        self.TCheckbutton4 = ttk.Checkbutton(top)
        self.TCheckbutton4.place(relx=0.1, rely=0.45, relwidth=0.27, relheight=0.0, height=23)
        # self.TCheckbutton4.configure(command=cheetah_config_support.save_config)
        self.TCheckbutton4.configure(command=cheetah_config_support.custom_req_hdr)
        self.TCheckbutton4.configure(variable=cheetah_config_support.custom_hdr)
        self.TCheckbutton4.configure(takefocus="")
        self.TCheckbutton4.configure(text='''Custom request header''')

        self.Text1 = Text(top)
        self.Text1.place(relx=0.1, rely=0.55, relheight=0.31, relwidth=0.79)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=474)
        # self.Text1.delete(0, END)
        self.Text1.insert('1.0', cheetah_config_support.custom_hdr_data.get())
        self.Text1.configure(state="disabled")
        self.Text1.bind('<KeyRelease>', cheetah_config_support.compare_hdr_data)

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.34, rely=0.9, height=27, width=87)
        self.TButton1.configure(command=cheetah_config_support.exit_config_setting)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''OK''')

        self.TButton2 = ttk.Button(top)
        self.TButton2.place(relx=0.52, rely=0.9, height=27, width=87)
        self.TButton2.configure(command=cheetah_config_support.exit_config_setting)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Cancel''')


if __name__ == '__main__':
    vp_start_gui()
