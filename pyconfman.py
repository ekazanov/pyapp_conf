"""
TODO: Create validators for cfg data
TODO: Create an add_value method
"""
# -*- coding: utf-8 -*-
__author__ = "Evgeny Kazanov"

import re

class PyConfMan(object):

    def __init__(self, arg=None, config_global=None,
                 config_local=None, env=None):
        self.arg = arg
        self.config_global = config_global
        self.config_local = config_local
        self.env = env
        self.in_data = {}
        # Compile regexps
        self.re_name = re.compile(r'^[0-9a-z][0-9a-z_]+[0-9a-z]$')

    def add_value(self, name, short_key=None, default=None, help=None,
                  required=None, is_key=None):
        cfg_parameter_name = self.validate_name(name)
        data_d = {}
        data_d['short_key'] = short_key
        data_d['long_key'] = cfg_parameter_name
        data_d['default'] = default
        data_d['help'] = help
        data_d['required'] = required
        data_d['is_key'] = is_key
        self.in_data[cfg_parameter_name] = data_d
        return

    def validate_name(self, name):
        if self.re_name.match(name) is None:
            raise RuntimeError('The config parameter name is not right: "{}"'\
                               .format(name))
        return name

    def set_args(self):
        pass

    def read_all(self):
        pass

    def read_args(self):
        pass

    def read_config(self):
        pass

    def read_environment(self):
        pass
