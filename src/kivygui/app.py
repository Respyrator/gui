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
from pathlib import Path
# Installed -------------------------------------------------------------------
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, NoTransition
# Coded -----------------------------------------------------------------------
from kivygui.kivyconfig import KIVY_DIR
# Program ---------------------------------------------------------------------

#polla = Path(__name__).resolve().stem + '.kv'
#print(f'File = {polla}, type = {type(polla)}')
pene = Path(__file__).resolve().parents[0] / 'app.kv'

Builder.load_file(str(pene))


class GuiManager(ScreenManager):
    pass


class GuiApp(App):

    def build(self):
        return GuiManager()


if __name__ == "__main__":
    GuiApp().run()
