# coding=utf-8
import sys
from cheetah_config_operation import read_config, write_config

if sys.version_info.major == 2:
    from Tkinter import StringVar, IntVar, DoubleVar, BooleanVar
else:
    from tkinter import StringVar, IntVar, DoubleVar, BooleanVar


def set_tk_var():
    global method
    method = StringVar()
    method.set(read_config("Config", "Method", "str"))
    global server
    server = StringVar()
    server.set(read_config("Config", "Server", "str"))
    global shelltype
    shelltype = StringVar()
    shelltype.set(read_config("Config", "ShellType", "str"))
    global parameter
    parameter = StringVar()
    parameter.set(read_config("Config", "Parameter", "str"))
    global thread_num
    thread_num = IntVar()
    thread_num.set(read_config("Config", "ThreadNumber", "int"))
    global req_delay
    req_delay = DoubleVar()
    req_delay.set(read_config("Config", "RequestDelay", "float"))
    global time_out
    time_out = DoubleVar()
    time_out.set(read_config("Config", "RequestTimeout", "float"))
    global random_ua
    random_ua = BooleanVar()
    random_ua.set(read_config("Config", "RandomUserAgent", "boolean"))
    global con_close
    con_close = BooleanVar()
    con_close.set(read_config("Config", "ConnectionClose", "boolean"))
    global keep_alive
    keep_alive = BooleanVar()
    keep_alive.set(read_config("Config", "KeepAlive0", "boolean"))
    global custom_hdr
    custom_hdr = BooleanVar()
    custom_hdr.set(read_config("Config", "CustomRequestHeader", "boolean"))
    global custom_hdr_data
    custom_hdr_data = StringVar()
    custom_hdr_data.set(read_config("Config", "CustomRequestHeaderData", "str"))


def save_config():
    write_config("Config", "Method", method.get())
    write_config("Config", "Server", server.get())
    write_config("Config", "ShellType", shelltype.get())
    write_config("Config", "Parameter", parameter.get())
    write_config("Config", "ThreadNumber", thread_num.get())
    write_config("Config", "RequestDelay", req_delay.get())
    write_config("Config", "RequestTimeout", time_out.get())
    write_config("Config", "RandomUserAgent", random_ua.get())
    write_config("Config", "ConnectionClose", con_close.get())
    write_config("Config", "KeepAlive0", keep_alive.get())


def exit_config_setting():
    destroy_window()


def compare_hdr_data(*args):
    if w.Text1.edit_modified():
        hdr_data = w.Text1.get('1.0', 'end-1c')
        write_config("Config", "CustomRequestHeaderData", hdr_data)


def custom_req_hdr():
    curt_custom_hdr = custom_hdr.get()
    # print(curt_custom_hdr)
    write_config("Config", "CustomRequestHeader", curt_custom_hdr)
    if curt_custom_hdr:
        w.Text1.configure(state="normal")
    else:
        w.Text1.configure(state="disabled")


def init(top, gui):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    save_config()
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import cheetah_config

    cheetah_config.vp_start_gui()
