# coding=utf-8
import sys
import cheetah
from os import system
from cheetah_config_operation import read_config, write_config

if sys.version_info.major == 2:
    pip = 'pip2'
    from tkMessageBox import showinfo, showwarning
else:
    pip = 'pip3'
    from tkinter.messagebox import showinfo, showwarning


def is_first_run():
    res = read_config('Run', 'first', 'boolean')
    write_config('Run', 'first', False)
    return res


def install_dependent(root):
    title = 'Cheetah Warn'
    message = 'Cheetah is about to install the missing dependencies.'
    showwarning(title, message, parent=root)
    system('{} install -r requirements.txt'.format(pip))
    title = 'Cheetah Info'
    message = 'Cheetah completed the dependent installation,' \
              '\nCheetah will end running, please run again.'
    showinfo(title, message, parent=root)
    exit()


def initialize_cheetah(root):
    if is_first_run():
        install_dependent(root)


if __name__ == '__main__':
    cheetah.main()
