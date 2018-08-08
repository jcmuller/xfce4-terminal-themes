#!/usr/bin/env python
# -*- coding: utf-8 -*-

# xfce4-terminal-themes.py -- programmatically change the theme of xfce4-terminal.
#
# Copyright © 2018 Juan C. Muller <jcmuller@gmail.com>
#
# License: MIT

from __future__ import print_function
import os
try:
    from configparser import RawConfigParser  # python3
except ImportError:
    from ConfigParser import RawConfigParser  # python2

class Configurator:
    try:
        config_root = os.environ['XDG_CONFIG_HOME']
    except KeyError:
        config_root = os.path.join(os.environ['HOME'], '.config')

    def __init__(self):
        self._config = self._read_config()
        self.theme_names = sorted(self._theme_names())

    def _config_file(self):
        return os.path.join(self.config_root, 'xfce4', 'terminal', 'terminalrc')

    def _themes_file(self):
        return os.path.join(self.config_root, 'xfce4', 'terminal', 'themes')

    def _read_config(self):
        config = RawConfigParser()
        config.optionxform = str  # make keys case-sensitive
        config.read(self._config_file())
        return config

    def _theme_names(self):
        themes = RawConfigParser()
        themes.optionxform = str  # make keys case-sensitive
        themes.read(self._themes_file())
        return themes.sections()

    def _theme(self, theme_name):
        themes = RawConfigParser()
        themes.optionxform = str  # make keys case-sensitive
        themes.read(self._themes_file())
        return themes.items(theme_name)

    def save_config(self):
        with open(self._config_file(), 'w') as f:
            self._config.write(f)

    def set_theme(self, theme_name):
        self._config.set('Configuration', 'ThemeName', theme_name)

        for pair in self._theme(theme_name):
            self._config.set('Configuration', pair[0], pair[1])

    def current_font_name(self):
        f = self._config.get('Configuration', 'FontName').split(" ")
        font = " ".join(f[0:-1])

        return font

    def current_font_size(self):
        f = self._config.get('Configuration', 'FontName').split(" ")
        size = f[-1]

        return size

    def display_config(self):
        print('Theme name:', self._config.get('Configuration', 'ThemeName'))
        print('Font name:', self.current_font_name())
        print('Font size:', self.current_font_size())

    def version(self):
        return '%(prog)s 0.1'
