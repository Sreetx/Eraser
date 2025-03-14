# warna.py
#
# Copyright 2024-2025 Programmer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
import sys, os
if sys.platform in ["linux", "linux2", "win32", "win64"]:
    orange = "\033[93m"
    putih = "\033[39m"
    merah = "\033[91m"
    hijau = "\033[92m"
    biru = "\033[94m"
    borange = "\033[1;93m"
    bputih = "\033[1;39m"
    bmerah = "\033[1;91m"
    bhijau = "\033[1;92m"
    bbiru = "\033[1;94m"
    banhijau = "\033[7;92m"
    kelabu = "\033[90m"
    borangekelip = "\033[5;93m"
    banmerah = "\033[7;91m"
    banorange = "\033[7;93m"
    reset = "\033[0m"
else:
    orange = ""
    putih = ""
    merah = ""
    hijau = ""
    biru = ""
    borange = ""
    bputih = ""
    bmerah = ""
    bhijau = ""
    bbiru = ""
    kelabu = ""
    borangekelip = ""
    banhijau = ""
    banmerah = ""
    reset = ""

def bannerd():
    ss = os.path.join("color", "logo.txt")
    with open(ss, "r", encoding="utf-8") as file:
        ini = file.read()
        print('\n')
        print(ini)
def banner():
    ss = os.path.join("color", "logo.txt")
    with open(ss, "r", encoding="utf-8") as file:
        ini = file.read()
        print('\n')
        print(ini)
        print(orange+" ["+banhijau+"*"+reset+orange+"]"+putih+" Atuhor:    "+hijau+"Sreetx"+reset)
        print(orange+" ["+banhijau+"*"+reset+orange+"]"+putih+" Version:    "+hijau+"3.7.11.13032025"+reset)
        print(orange+" ["+banhijau+"*"+reset+orange+"]"+putih+" Language:   "+hijau+"Python"+reset)
        print(orange+" ["+banhijau+"*"+reset+orange+"]"+putih+" License:    "+hijau+"GNU GPL v3"+reset)
        print(orange+" ["+banhijau+"*"+reset+orange+"]"+putih+" YouTube:    "+hijau+"https://youtube.com/@linggachannel4781"+reset)
        print(orange+" ["+banhijau+"*"+reset+orange+"]"+putih+" GitHub:     "+hijau+"https://github.com/Sreetx"+reset)
