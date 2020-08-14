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

# Built-in --------------------------------------------------------------------
# Installed -------------------------------------------------------------------
from kivy.app import App
from kivy.properties import StringProperty, DictProperty
# Coded -----------------------------------------------------------------------
from . import logapp
from .container import GuiContainer
from ..utils import get_modes
# Program ---------------------------------------------------------------------
LOG = 'APP:'


class GuiApp(App):
    mode = StringProperty('')
    params = DictProperty('')
    alarms = DictProperty('')

    def build(self):
        return GuiContainer()

    def on_start(self):
        # TODO: get all supported modes
        modes = get_modes()
        # TODO: load enables modes
        self.root.load_modes(modes)
        # display UI Modes
        self.on_mode(self.mode, '')

    def on_mode(self, instance: StringProperty, value: str):
        if self.mode:
            self.root.ui_loading()
            # TODO: get params and alarms for selected mode
            # TODO: store params
            # TODO: store alarms
            # display UI Params
            self.root.ui_params()
        # Display UI Modes
        else:
            self.root.ui_modes()


if __name__ == "__main__":
    GuiApp().run()
