# coding=utf-8
import sys
import time
from os import path

if sys.version_info.major == 2:
    from tkFileDialog import askopenfilename
    from tkMessageBox import showinfo, showerror
else:
    from tkinter.filedialog import askopenfilename
    from tkinter.messagebox import showinfo, showerror

from cheetah_config_operation import read_config, write_config

data_dir = path.abspath(path.join(path.dirname(__file__), path.pardir, 'data'))


def set_tk_var():
    global dict_path
    dict_path = path.abspath(read_config("Dictionary", "Path", "str"))
    small_dict_path = path.join(data_dir, "pwd.txt")
    big_dict_path = path.join(data_dir, "big_pwd.txt")
    global dict_list
    dict_list = [small_dict_path, big_dict_path]


def set_pwd_file():
    dict_file = askopenfilename(initialdir=data_dir, initialfile="pwd.txt",
                                parent=root, filetypes=[("text files", "*.txt")])
    if path.isfile(dict_file):
        w.TCombobox1.delete(0, 'end')
        w.TCombobox1.insert(0, dict_file)
        w.TCombobox1.set(dict_file)
        write_config("Dictionary", "Path", dict_file)


def read_chunks(pwd_file):
    with open(pwd_file, encoding='utf-8') as pwd_file:
        while 1:
            chunk_data = pwd_file.read(100 * 1024 * 1024)
            if not chunk_data:
                break
            yield chunk_data


def dereplicat_pwd_file():
    pwd_path = w.TCombobox1.get()
    base_name = path.basename(pwd_path)
    if 'deduplicated' in base_name:
        title = "Cheetah Info"
        message = "The dictionary file has been deduplicated."
        showerror(title, message, parent=root)
        return
    format_str = "_%Y-%m-%d_(%H.%M.%S)_"
    time_str = str(time.strftime(format_str, time.localtime()))
    new_dict_name = 'deduplicated' + time_str + base_name
    new_dict_path = path.join(data_dir, new_dict_name)
    with open(new_dict_path, mode='a', encoding='utf-8') as new_file:
        for chunk in read_chunks(pwd_path):
            new_file.write('\n'.join(set(chunk.split())).lower())
    title = "Cheetah Info"
    message = "Dereplication completed, new dictionary file is %s." % new_dict_name
    showinfo(title, message, parent=root)
    w.TCombobox1.set(new_dict_path)
    write_config("Dictionary", "Path", new_dict_path)


def exit_dict_setting():
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
    import cheetah_dictionary

    cheetah_dictionary.vp_start_gui()
