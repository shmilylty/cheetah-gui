# coding=utf-8
import sys
from os import path

if sys.version_info.major == 2:
    from ConfigParser import ConfigParser
else:
    from configparser import ConfigParser

config_path = path.join(path.abspath(__file__), path.pardir, "cheetah_config.ini")


def read_config(section, key, types):
    config = ConfigParser()
    config.read(config_path)
    if types == "str":
        return config.get(section, key)
    if types == "int":
        return config.getint(section, key)
    if types == "float":
        return config.getfloat(section, key)
    if types == "boolean":
        return config.getboolean(section, key)


def write_config(section, key, value):
    config = ConfigParser()
    config.read(config_path)
    config.set(section, key, str(value))
    config.write(open(config_path, mode='w', encoding='utf-8'))
