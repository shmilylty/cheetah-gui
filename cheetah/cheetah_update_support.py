# coding=utf-8
import os
import sys
from os import path
import requests


if sys.version_info.major == 2:
    from Tkinter import *
    from tkMessageBox import showinfo, showwarning
else:
    from tkinter import *
    from tkinter.messagebox import showinfo, showwarning


def set_tk_var():
    global check_update
    check_update = StringVar()
    check_update.set("Check")
    global update_msg
    update_msg = StringVar()
    global current_ver
    current_ver = 2.1
    msg = "The current Cheetah version is %.1f, " \
          "do you need to check for updates?" % current_ver
    update_msg.set(msg)


def check_updates():
    if check_update.get() == "OK":
        exit_update()
    if check_update.get() == "Update":
        w.TButton1.configure(state="disable")
        w.TButton2.configure(state="disable")
        process = os.popen("git --version")
        output = process.read()
        process.close()
        par_dir = path.abspath(path.join(path.dirname(__file__), path.pardir))
        if "git version" in output:
            if path.exists(path.join(par_dir, '.git')):
                os.chdir(par_dir)
                os.system('git pull origin master')
                title = "Cheetah Info"
                message = "Cheetah has completed the update."
                showinfo(title, message, parent=root)
                destroy_window()
            else:
                os.chdir(par_dir)
                message = "Cheetah is about to be updated, " \
                          "please do not do anything else during the update!"
                title = "Cheetah Warn"
                showwarning(title, message, parent=root)
                os.system('git clone https://github.com/sunnyelf/cheetah.git new_cheetah')
                title = "Cheetah Info"
                message = "Cheetah has completed the update."
                showinfo(title, message, parent=root)
                destroy_window()
        else:
            url = 'https://github.com/sunnyelf/cheetah/archive/master.zip'
            r = requests.get(url, verify=False)
            with open("cheetah.zip", "wb") as f:
                f.write(r.content)
            zip_path = path.join(par_dir, "cheetah.zip")
            title = "Cheetah Info"
            message = "The latest version of Cheetah has been downloaded.\n" \
                      "File path: %s" % zip_path
            showinfo(title, message, parent=root)
            destroy_window()
    if check_update.get() == "Check":
        w.TButton1.configure(state="disable")
        update_log_url = "https://pastebin.com/raw/n6YYbzri"
        r = requests.get(update_log_url, verify=False)
        update_log_json = r.json()
        update_ver = update_log_json['ver']
        update_log = update_log_json['log']
        if update_ver > current_ver:
            msg = "The latest Cheetah version is %.1f, " \
                  "do you need to update it now?\n" % update_ver
            update_msg.set(msg + 'New version: ' + update_log)
            w.TButton1.configure(state="normal")
            check_update.set("Update")
        else:
            msg = "The current cheetah is already the latest version."
            update_msg.set(msg)
            w.TButton1.configure(state="normal")
            check_update.set("OK")


def exit_update():
    destroy_window()


def init(top, gui):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import cheetah_update

    cheetah_update.vp_start_gui()
