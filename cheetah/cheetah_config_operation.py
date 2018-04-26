# coding=utf-8
import io
import sys
from os import path

if sys.version_info.major == 2:
    from ConfigParser import ConfigParser
else:
    from configparser import ConfigParser

config_path = path.abspath(path.join(path.dirname(__file__), "cheetah_config.ini"))


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
    if sys.version_info.major == 3:
        config.set(section, key, str(value))
    else:
        config.set(section, key, value)
    config.write(open(config_path, mode='w'))
