# Copyright (C) 2020 Respyrator
# This file is part of Respyrator <https://respyrator.github.io>.
#
# Respyrator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Respyrator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Respyrator.  If not, see <http://www.gnu.org/licenses/>.

from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button


from src import logapp
from . import KV_FILES

Builder.load_file(str(KV_FILES / 'loadingscreen.kv'))
# txts: dict = cfg_txt.get('INFOSCREEN', '')
LOG = 'LoadingScreen:'


class LoadingScreen(Screen):
    pass
