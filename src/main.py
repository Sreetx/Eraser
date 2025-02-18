# main.py
#
# Copyright 2025 Programmer
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import os, sys, time
from argparse import ArgumentParser

try:
    try:
        import sys, os, time, webbrowser
        from color.warna import orange
        from color.warna import putih
        from color.warna import merah
        from color.warna import banner
        from color.warna import bannerd
        from color.warna import hijau
        from color.warna import biru
        from color.warna import borange
        from color.warna import bputih
        from color.warna import bhijau
        from color.warna import bbiru
        from color.warna import bmerah
        from color.warna import kelabu
        from color.warna import borangekelip
        from color.warna import banmerah
        from color.warna import banhijau
        from color.warna import banorange
        from color.warna import reset
    except ImportError:
        print(' [!] Harap install ulang script ini dari repository github kami!');sys.exit()
    try:
        from rembg import remove
        from PIL import Image
        from PIL import ImageEnhance
        import numpy as np
        import io
    except Exception as e:
        print(e)
        print(" [!] Coba install module ini: pillow, numpy, rembg, onnxruntime");sys.exit()
except KeyboardInterrupt: print(" [!] Dibatalkan...");sys.exit()

def image_eraser(media, output):
    default_path = media.split("/")[-1]
    if not os.path.exists('hasil'):
        os.makedirs('hasil')
    if output == '':
        with open(media, 'rb') as imag:
            imaga = imag.read()
        imagee = Image.open(io.BytesIO(imaga))
        imagee_np = np.array(imagee)
        med = remove(imagee_np, alpha_matting=True, alpha_matting_foreground_threshold=250, alpha_matting_background_threshold=5, alpha_matting_erode_size=5)
        outd = Image.fromarray(med)
        a = 'hasil/eraser-'+default_path
        with open("hasil/eraser-"+default_path, 'wb') as outs:
            with io.BytesIO() as byte_io:
                outd.save(byte_io, format='PNG')
                byte_io.seek(0)
                outs.write(byte_io.read())
        print(putih+" ["+banorange+"✔️"+reset+putih+"] Pemrosesan gambar Berhasil!"+reset)
        print(putih+" ["+banhijau+"#"+reset+putih+"] Gambar disimpan di "+a+reset)
    else:
        if not os.path.exists(output):
            os.makedirs(output)
        with open(media, 'rb') as imag:
            imaga = imag.read()
        imagee = Image.open(io.BytesIO(imaga))
        imagee_np = np.array(imagee)
        med = remove(imagee_np, alpha_matting=True, alpha_matting_foreground_threshold=250, alpha_matting_background_threshold=5, alpha_matting_erode_size=5)
        outd = Image.fromarray(med)
        with open(output+"/eraser-"+default_path, 'wb') as outs:
            with io.BytesIO() as byte_io:
                outd.save(byte_io, format='PNG')
                byte_io.seek(0)
                outs.write(byte_io.read())
        print(putih+" ["+banorange+"✔️"+reset+putih+"] Pemrosesan gambar Berhasil!"+reset)
        print(putih+" ["+banhijau+"#"+reset+putih+"] Gambar disimpan di "+output+"eraser-"+default_path+reset)

def help():
    banner()
    print("""
Options: python3 main.py [option]
    --mode      Buat milih mode "image-background-eraser" atau "video-background-eraser"
    --media     Letakan path media seperti gambar atau video pake opsi ini
    --easy-mode Pake easy mode langsung kalo nggak terbiasa dengan option parser
    --hh        Tampilkan menu bantuan ini!
    -o --output Tentukan lokasi gambar disimpan (default: "hasil")
Usage:
    python3 main.py --mode=image-background-eraser --media="/path/to/you image" -o /folder/destination/
    python3 main.py --mode=video-background-eraser --media=/path/to/video -o /folder/destination/
    python3 main.py --easy-mode
    python3 main.py --hh

 """+kelabu+"""["""+orange+"""*"""+kelabu+"""]"""+putih+""" Tanpa menggunakan opsi output. file akan otomatis di simpan di Eraser/src/hasil/"""+reset)

#Menggunakan ArgumentParser karena jika penggunakan OptionParser input spasi tidak dapat ditangkap dengan benar
menu = ArgumentParser()
menu.add_argument('--mode', dest='mode', help='Tentukan mode')
menu.add_argument('--media', dest='media', help='Masukkan media gambar atau video yang akan di bersihkan background nya')
menu.add_argument('--easy-mode', dest='easy_mode', action="store_true", default=False, help='Masuk ke easy mode aja kalo mode option parser terasa sulit')
menu.add_argument('--hh', dest='hh', action='store_true', default=False, help='Menu bantuan')
menu.add_argument('-o', '--output', dest='output', default='', help='Lokasi file akan disimpan')
option = menu.parse_args()

mode = option.mode
easy_mode = option.easy_mode
hh = option.hh
media = str(option.media).strip()
output = str(option.output).strip()

if mode == "image-background-eraser":
    bannerd()
    print(kelabu+" ["+banhijau+"#"+reset+kelabu+"]"+putih+" Mode Image Background Eraser...."+reset)
    print(kelabu+" ["+banhijau+"!"+reset+kelabu+"]"+putih+" Mungkin proses akan sedikit lambat tergantung deivce"+reset)
    print(kelabu+" ["+banorange+"!"+reset+kelabu+"]"+putih+" Memproses...."+reset)
    image_eraser(media, output)
elif mode == "video-background-eraser":
    bannerd()
    print(kelabu+" ["+banhijau+"#"+reset+kelabu+"]"+putih+" Mode Video Background Eraser...."+reset)
    print(putih+" ["+banmerah+"*"+reset+putih+"] Coming Soon!!..."+reset);sys.exit()
    print(putih+" ["+banmerah+"*"+reset+putih+"] Nantikan Update berikutnya!..."+reset);sys.exit()
elif easy_mode:
    bannerd()
    print(kelabu+" ["+banhijau+"#"+reset+kelabu+"]"+putih+" Masuk ke easy mode!"+reset); time.sleep(1)
elif hh:
    help()
else:
    help()
    print(kelabu+" ["+banorange+"!"+reset+kelabu+"]"+putih+" Input lu salah atau lu gk masukkan input sama sekali!")
