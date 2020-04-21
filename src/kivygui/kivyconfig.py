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
from kivy.config import Config
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
# Coded -----------------------------------------------------------------------
from src.settings import LOG_DIR, logapp
from src.guiconfig import gui_colors, gui_imgs, gui_txts
# Program ---------------------------------------------------------------------
LOG = 'KIVYGUI:'

KIVY_DIR = Path(__file__).resolve().parents[0]
KIVY_CONFIG = KIVY_DIR / 'kivyconfig.ini'
if KIVY_CONFIG.exists():
    Config.read(str(KIVY_CONFIG))
    logapp.debug(f'{LOG} Kivy configuration completed')
    # Remove all kivylogs .txt files
    [kvlog.unlink() for kvlog in LOG_DIR.iterdir() if kvlog.suffix == '.txt']
else:
    logapp.error(f'{LOG} Kivy not well configured')
# COLORs
colors = {k: get_color_from_hex(v) for k, v in gui_colors}
print(f'COLORES = {colors}')
# IMGs
imgs = gui_imgs
# TXTs
txts = gui_txts
# Background Window color
Window.clearcolor = colors.get('brand', (0, 1, 0, 1))
logapp.debug(f'{LOG} Window background to {Window.clearcolor}')
# Load .kv files for ScreenManager
'''
if KIVY_DIR:
    from . import loadingscreen, modesscreen, paramsscreen, alarmsscreen, \
        monitoringscreen
    __all__ = [
        'loadingscreen', 'modesscreen', 'paramsscreen', 'alarmsscreen',
        'monitoringscreen'
    ]
'''
logapp.info(f'{LOG} kivy config loaded')
