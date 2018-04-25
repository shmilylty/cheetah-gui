# coding=utf-8
import sys
import time
import requests
from os import path, rename
from cheetah_config_operation import read_config, write_config
from cheetah_validator import is_host

if sys.version_info.major == 2:
    from tkFileDialog import askopenfilename
    from tkMessageBox import showinfo, showerror
    from Tkinter import StringVar, IntVar, BooleanVar
else:
    from tkinter.filedialog import askopenfilename
    from tkinter.messagebox import showinfo, showerror
    from tkinter import StringVar, IntVar, BooleanVar


data_dir = path.abspath(path.join(path.dirname(__file__), path.pardir, 'data'))


def set_tk_var():
    global address
    address = StringVar()
    address.set(read_config("Proxy", "Address", "str"))
    global port
    port = IntVar()
    port.set(read_config("Proxy", "Port", "int"))
    global protocol
    protocol = StringVar()
    protocol.set(read_config("Proxy", "Protocol", "str"))
    global username
    username = StringVar()
    username.set(read_config("Proxy", "Username", "str"))
    global password
    password = StringVar()
    password.set(read_config("Proxy", "Password", "str"))
    global proxy_list
    proxy_list = StringVar()
    proxy_list.set(path.abspath(read_config("Proxy", "List", "str")))
    global proxy_api
    proxy_api = StringVar()
    proxy_api.set(read_config("Proxy", "API", "str"))
    global test_address
    test_address = StringVar()
    test_address.set(read_config("Proxy", "TestAddress", "str"))
    global use_proxy
    use_proxy = BooleanVar()
    use_proxy.set(read_config("Proxy", "Proxy", "boolean"))


def add_custom_proxy():
    host = address.get()
    if len(host) != 0:
        if is_host(host):
            proxy_protocol = protocol.get()
            proxy_ip = address.get()
            proxy_port = port.get()
            proxy_user = username.get()
            proxy_pass = password.get()
            if len(proxy_user) != 0 and len(proxy_pass):
                proxy_user_pass = "{}:{}@".format(proxy_user, proxy_pass)
                proxy_data = '{}://{}{}:{}'.format(proxy_protocol, proxy_user_pass, proxy_ip, proxy_port)
                add_proxy(proxy_data)
                return
            proxy_data = '{}://{}:{}'.format(proxy_protocol, proxy_ip, proxy_port)
            add_proxy(proxy_data)


def save_config():
    write_config("Proxy", "Address", address.get())
    write_config("Proxy", "Port", port.get())
    write_config("Proxy", "Protocol", protocol.get())
    write_config("Proxy", "Username", username.get())
    write_config("Proxy", "Password", password.get())
    write_config("Proxy", "List", proxy_list.get())
    write_config("Proxy", "API", proxy_api.get())
    write_config("Proxy", "TestAddress", test_address.get())
    write_config("Proxy", "Proxy", use_proxy.get())


def exit_proxy_setting():
    save_config()
    save_proxy()
    destroy_window()


def add_proxy(data):
    w.Scrolledlistbox1.insert('end', data)
    root.update()
    w.Scrolledlistbox1.see('end')


def save_proxy():
    proxys = w.Scrolledlistbox1.get(0, 'end')
    proxy_path = path.abspath(path.join(path.dirname(__file__), path.pardir, 'data', 'proxy.txt'))
    with open(proxy_path, mode='a', encoding='utf-8') as proxy_file:
        proxy_file.write("\n".join(proxys))


def save_validated_proxy():
    proxys = w.Scrolledlistbox1.get(0, 'end')
    proxy_path = path.abspath(path.join(path.dirname(__file__), path.pardir, 'data', 'proxy.txt'))
    if path.exists(proxy_path):
        time_stamp = int(time.time())
        proxy_bak_path = '{}.{}.bak'.format(proxy_path, time_stamp)
        rename(proxy_path, proxy_bak_path)
    with open(proxy_path, mode='w', encoding='utf-8') as proxy_file:
        proxy_file.write("\n".join(proxys))


def get_proxy_list():
    w.TButton4.configure(state='disable')
    url = proxy_api.get()

    if "getproxylist" in url:
        for x in range(15):
            try:
                r = requests.get(url, timeout=(3, 10), verify=False)
            except:
                continue
            proxy_info = r.json()
            if 'error' in proxy_info.keys():
                title = "Cheetah Error"
                message = proxy_info['error']
                showerror(title, message, parent=root)
                break
            if 'protocol' in proxy_info.keys() and 'ip' in proxy_info.keys() and 'port' in proxy_info.keys():
                proxy_protocol = proxy_info['protocol']
                proxy_ip = proxy_info['ip']
                proxy_port = proxy_info['port']
                proxy_data = '{}://{}:{}'.format(proxy_protocol, proxy_ip, proxy_port)
                add_proxy(proxy_data)

    if "gimmeproxy" in url:
        for x in range(15):
            try:
                r = requests.get(url, timeout=(3, 10), verify=False)
            except:
                continue
            proxy_info = r.json()
            if 'error' in proxy_info.keys():
                title = "Cheetah Error"
                message = proxy_info['error']
                showerror(title, message, parent=root)
                break
            if 'curl' in proxy_info.keys():
                proxy_data = proxy_info['curl']
                add_proxy(proxy_data)

    if "pubproxy" in url:
        for x in range(15):
            try:
                r = requests.get(url, timeout=(3, 10), verify=False)
            except:
                continue
            if '100' in r.text:
                title = "Cheetah Error"
                message = r.text
                showerror(title, message)
                break
            proxy_info = r.json()
            if 'count' in proxy_info.keys():
                count = int(proxy_info['count'])
                for i in range(count):
                    proxy_protocol = proxy_info['data'][i]['type']
                    proxy_ip = proxy_info['data'][i]['ip']
                    proxy_port = proxy_info['data'][i]['port']
                    proxy_data = '{}://{}:{}'.format(proxy_protocol, proxy_ip, proxy_port)
                    add_proxy(proxy_data)
    save_proxy()
    w.TButton4.configure(state='normal')


def import_proxy_list():
    proxy_path = askopenfilename(initialdir=data_dir, initialfile="proxy.txt",
                                 parent=root, filetypes=[("text files", "*.txt")])
    if path.isfile(proxy_path):
        w.TCombobox2.delete(0, 'end')
        w.TCombobox2.insert(0, proxy_path)
        w.TCombobox2.set(proxy_path)
        write_config("Proxy", "List", proxy_path)

        with open(proxy_path, encoding='utf-8') as proxy_file:
            for proxy_line in proxy_file:
                proxys_data = proxy_line.strip()
                add_proxy(proxys_data)


def remove_invalid_proxys():
    print('cheetah_proxy_support.remove_invalid_proxys')
    sys.stdout.flush()


def validate_proxy():
    w.TButton5.configure(state='disable')
    proxys = w.Scrolledlistbox1.get(0, 'end')
    del_index = 0
    for index, proxy in enumerate(proxys):
        w.Scrolledlistbox1.see(index)
        proxy = proxy.strip()
        scheme = proxy.split('://', 1)
        proxies = {}
        if scheme == 'http':
            proxies['http'] = proxy
        elif scheme == 'https':
            proxies['https'] = proxy
        else:
            proxies['http'] = proxy
            proxies['https'] = proxy
        url = test_address.get()
        try:
            r = requests.get(url, proxies=proxies, timeout=(3, 10), verify=False)
        except:
            w.Scrolledlistbox1.delete(del_index)
            root.update()
            continue
        else:
            if r.status_code == 200:
                del_index += 1
            else:
                w.Scrolledlistbox1.delete(del_index)
                root.update()

    title = 'Cheetah Info'
    message = 'Validation has been completed.'
    showinfo(title, message, parent=root)
    save_validated_proxy()
    w.TButton5.configure(state='normal')


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
    import cheetah_proxy

    cheetah_proxy.vp_start_gui()
