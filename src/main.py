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
    print(" [*] Importing Module...")
    print(" [*] Mungkin agak lama karena kami harus mengimpor file logo.txt ini juga berpengaruh tergantung kecepatan device kalian!")
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
        from rembg import remove, new_session
        from PIL import Image
        from PIL import ImageEnhance
        import numpy as np
        import io
        import ffmpeg
        import glob
        import shutil
        from multiprocessing import Pool, cpu_count
        from tqdm import tqdm
    except Exception as e:
        print(e)
        print(" [!] Coba install module ini: pillow, numpy, rembg, ffmpeg, onnxruntime(opsional)");sys.exit()
except KeyboardInterrupt: print(" [!] Dibatalkan...");sys.exit()

os.system('cls || clear')
def image_eraser(media, output, model, url):
    if model is None or model == "":
        print(kelabu+" ["+banmerah+"!"+reset+kelabu+"]"+putih+" Masukkan model untuk pemrosesan!"+reset);sys.exit()
    default_path = media.split("/")[-1]
    os.makedirs('hasil', exist_ok=True)
    if url:
        os.makedirs('cache', exist_ok=True)
        try:
            import socket, requests
            socket.create_connection(('8.8.8.8', 53), timeout=5)
        except ImportError: print(kelabu+" ["+banorange+"!"+reset+kelabu+"]"+putih+" Module Requests tidak ditemukan, silakan install: pip install requests");sys.exit()
        print(kelabu+" ["+orange+"*"+reset+kelabu+"]"+putih+" Mengunduh gambar..."+reset)
        req = requests.get(url)
        dirr = url.split("/")[-1]
        caches = os.path.join('cache', dirr)
        with open (caches, 'wb') as ca:
            ca.write(req.content)
        print(kelabu+" ["+banhijau+"✔️"+reset+kelabu+"]"+hijau+" Pengunduhan Selesai"+reset)

    if media == "":
        media = 'cache/'+dirr
    if default_path == "":
        default_path = dirr
    else:
        pass
    print(kelabu+" ["+banorange+"!"+reset+kelabu+"]"+putih+" Memproses...."+reset)

    if output == '':
        with open(media, 'rb') as imag:
            imaga = imag.read()
        session = new_session(model)
        imagee = Image.open(io.BytesIO(imaga)).convert("RGBA")
        imagee_np = np.array(imagee)
        med = remove(imagee_np, session=session, alpha_matting=True, alpha_matting_foreground_threshold=250, alpha_matting_background_threshold=5, alpha_matting_erode_size=5)
        outd = Image.fromarray(med)
        with open(output+"/eraser-"+default_path, 'wb') as outs:
            with io.BytesIO() as byte_io:
                outd.save(byte_io, format='PNG')
                byte_io.seek(0)
                outs.write(byte_io.read())
        print(putih+" ["+banorange+"✔️"+reset+putih+"] Pemrosesan gambar Berhasil!"+reset)
        print(putih+" ["+banhijau+"#"+reset+putih+"] Gambar disimpan di "+a+reset);sys.exit()
    else:
        os.makedirs(output, exist_ok=True)
        with open(media, 'rb') as imag:
            imaga = imag.read()
        session = new_session(model)
        imagee = Image.open(io.BytesIO(imaga)).convert("RGBA")
        imagee_np = np.array(imagee)
        med = remove(imagee_np, session=session, alpha_matting=True, alpha_matting_foreground_threshold=250, alpha_matting_background_threshold=5, alpha_matting_erode_size=5)
        outd = Image.fromarray(med)
        with open(output+"/eraser-"+default_path, 'wb') as outs:
            with io.BytesIO() as byte_io:
                outd.save(byte_io, format='PNG')
                byte_io.seek(0)
                outs.write(byte_io.read())
        print(putih+" ["+banorange+"✔️"+reset+putih+"] Pemrosesan gambar Berhasil!"+reset)
        print(putih+" ["+banhijau+"#"+reset+putih+"] Gambar disimpan di "+output+"eraser-"+default_path+reset);sys.exit()

def remove_background(args):
    model, frame_raw = args
    with open(frame_raw, 'rb') as imag:
        imaga = imag.read()
    session = new_session(model)
    imagee = Image.open(io.BytesIO(imaga)).convert("RGBA")
    imagee_np = np.array(imagee)
    med = remove(imagee_np, session=session, alpha_matting=True, alpha_matting_foreground_threshold=250, alpha_matting_background_threshold=5, alpha_matting_erode_size=5)
    outd = Image.fromarray(med)
    output_path = os.path.join("cache/frame_eraser/", os.path.basename(frame_raw))
    outd.save(output_path)

def video_background_eraser(media, output, model):
    name = media.split("/")[-1]
    probe = ffmpeg.probe(media)
    video_stream = next((stream for stream in probe["streams"] if stream["codec_type"] == "video"), None)
    if video_stream:
        width = int(video_stream["width"])
        height = int(video_stream["height"])
        fps = eval(video_stream["r_frame_rate"])
    if output is None or output == "":
        output = "hasil"
    os.makedirs('cache', exist_ok=True)
    os.makedirs('cache/frame', exist_ok=True)
    os.makedirs(output, exist_ok=True)

    #Extract Frame
    print(kelabu+" ["+hijau+"..."+reset+kelabu+"]"+putih+" Mengekstrak frame..."+reset)
    ffmpeg.input(media).output("cache/frame/animation_%01d.png", format="image2", vcodec="png").run(quiet=True)

    #Eraser
    os.makedirs('cache/frame_eraser', exist_ok=True)
    out = 'cache/frame_eraser'

    print(kelabu+" ["+orange+"~"+kelabu+"]"+putih+" Membersihkan Background...")
    frame_list = sorted(glob.glob("cache/frame/*.png"))
    total_frame = len(frame_list)
    task_list = [(model, frame) for frame in frame_list]
    num_workers = cpu_count()
    optimal_chunksize = max(4, len(task_list) // (num_workers * 4))
    with Pool(num_workers) as p, tqdm(total=total_frame, unit="frame"):
        for _ in p.imap_unordered(remove_background, task_list, chunksize=optimal_chunksize):
            pass
    # Penyatuan Frame
    outsd = output+name
    print(kelabu+" ["+orange+"~"+kelabu+"]"+putih+" Memproses hingga menjadi video kembali...")
    ffmpeg.input("cache/frame_eraser/animation_%01d.png").output(outsd, vcodec="libx264", crf=23, s=f"{width}x{height}").run(quiet=True)
    shutil.rmtree("cache/frame")
    shutil.rmtree("cache/frame_eraser")
    print(putih+" ["+banorange+"✔️"+reset+putih+"] Pemrosesan penghapusan background video Berhasil!"+reset)
    print(putih+" ["+banhijau+"#"+reset+putih+"] Video disimpan di "+hijau+output+name+reset);sys.exit()

def help(hh):
    banner()
    if hh == 'indonesia':
        with open("color/tutorial-id.txt", 'r') as tut:
            c = tut.read()
        print(c);sys.exit()
    if hh == 'english':
        with open("color/tutorial-en.txt", 'r') as tut:
            c = tut.read()
        print(c);sys.exit()
    else:
        print(putih+' ['+banmerah+'!'+reset+putih+'] Mohon masukkan input! --hh');sys.exit()

#Menggunakan ArgumentParser karena jika penggunakan OptionParser input spasi tidak dapat ditangkap dengan benar
menu = ArgumentParser()
menu.add_argument('--mode', dest='mode', default='', help='Tentukan mode')
menu.add_argument('--media', dest='media', default='', help='Masukkan media gambar atau video yang akan di bersihkan background nya')
menu.add_argument('--easy-mode', dest='easy_mode', action="store_true", default=False, help='Masuk ke easy mode aja kalo mode option parser terasa sulit')
menu.add_argument('--hh', dest='hh', help='Menu bantuan')
menu.add_argument('-o', '--output', dest='output', default='', help='Lokasi file akan disimpan')
menu.add_argument('--update', dest='update', action='store_true', default=False, help='Hanya mengupdate script utama')
menu.add_argument('--update-all', dest='updated', action='store_true', default=False, help='Untuk mengupdate semua module script bahkan mengupdate script utama')
menu.add_argument('--url', dest='url', default='', help='Unduh dan hapus latar belakang gambar secara langsung!')
menu.add_argument('--model', dest='model', help='Pilih Model untuk proses')
menu.add_argument('--multi', dest='multi', action='store_true', default=False, help='masukkan input berapa gambar yang akan di gunakan (int)')
option = menu.parse_args()

mode = option.mode
easy_mode = option.easy_mode
hh = option.hh
media = str(option.media).strip()
output = str(option.output).strip()
update = option.update
update_all = option.updated
model = option.model
url = option.url
multi = option.multi

if mode == "image-background-eraser":
    bannerd()
    print(kelabu+" ["+banhijau+"#"+reset+kelabu+"]"+putih+" Mode Image Background Eraser...."+reset)
    print(kelabu+" ["+banhijau+"!"+reset+kelabu+"]"+putih+" Mungkin proses akan sedikit lambat tergantung deivce"+reset)
    image_eraser(media, output, model, url)
if mode == "video-background-eraser":
    bannerd()
    print(kelabu+" ["+banhijau+"#"+reset+kelabu+"]"+putih+" Mode Video Background Eraser...."+reset)
    print(kelabu+" ["+banhijau+"!"+reset+kelabu+"]"+putih+" Mungkin proses akan sedikit lambat tergantung deivce"+reset)
    print(putih+" ["+banorange+"!"+reset+putih+"]"+kelabu+" Memproses..."+reset)
    video_background_eraser(media, output, model)
if hh:
    help(hh)
if update_all:
    try:
        import socket, requests
        socket.create_connection(('8.8.8.8', 53), timeout=3)
    except ImportError: print(kelabu+" ["+banorange+"!"+reset+kelabu+"]"+putih+" Module Requests tidak ditemukan, silakan install: pip install requests");sys.exit()
    print(kelabu+" ["+banorange+"UPDATE"+reset+kelabu+"]"+putih+" Checking Update..."+reset);time.sleep(0.2)
    maind = requests.get("https://raw.githubusercontent.com/Sreetx/Eraser/refs/heads/master/src/main.py")
    colorr = requests.get("https://raw.githubusercontent.com/Sreetx/Eraser/refs/heads/master/src/color/warna.py")
    logoo = requests.get("https://raw.githubusercontent.com/Sreetx/Eraser/refs/heads/master/src/color/logo.txt")
    tutor_id = requests.get("https://raw.githubusercontent.com/Sreetx/Eraser/refs/heads/master/src/color/tutorial-id.txt")
    tutor_en = requests.get("https://raw.githubusercontent.com/Sreetx/Eraser/refs/heads/master/src/color/tutorial-id.txt")
    maind_byte = maind.content.decode("utf-8")
    tutor_id_byte = tutor_id.content.decode("utf-8")
    tutor_en_byte = tutor_en.content.decode("utf-8")
    colorr_byte = colorr.content.decode("utf-8")
    logoo_byte = logoo.content.decode("utf-8")
    os.makedirs('color', exist_ok=True)
    print(kelabu+" ["+banorange+"UPDATE"+reset+kelabu+"]"+putih+" Installing Main Script..."+reset);time.sleep(0.2)
    with open("main.py", "w", encoding="utf-8") as a:
        a.write(maind_byte)
    print(kelabu+" ["+banorange+"UPDATE"+reset+kelabu+"]"+putih+" Installing Color Script..."+reset);time.sleep(0.2)
    with open("color/warna.py", "w", encoding="utf-8") as b:
        b.write(colorr_byte)
    print(kelabu+" ["+banorange+"UPDATE"+reset+kelabu+"]"+putih+" Updating Logo/Banner..."+reset);time.sleep(0.2)
    with open("color/logo.txt", "w", encoding="utf-8") as c:
        c.write(logoo_byte)
    print(kelabu+" ["+banorange+"UPDATE"+reset+kelabu+"]"+putih+" Installing Guide text..."+reset);time.sleep(0.2)
    with open("color/tutorial-id.txt", "w", encoding="utf-8") as d:
        d.write(tutor_id_byte)
    with open("color/tutorial-id.txt", "w", encoding="utf-8") as e:
        e.write(tutor_en_byte)
    print(putih+" ["+banhijau+"UPDATE"+reset+putih+"] Update Succed!"+reset);sys.exit()

if update:
    try:
        import socket, requests
    except ImportError: print(kelabu+" ["+banorange+"!"+reset+kelabu+"]"+putih+" Module Requests tidak ditemukan, silakan install: pip install requests");sys.exit()
    maind = requests.get("https://raw.githubusercontent.com/Sreetx/Eraser/refs/heads/master/src/main.py")
    maind_byte = maind.content.decode("utf-8")
    print(kelabu+" ["+banorange+"UPDATE"+reset+kelabu+"]"+putih+" Installing Main Script..."+reset);time.sleep(0.2)
    with open("main.py", "w", encoding="utf-8") as a:
        a.write(maind_byte)
    print(putih+" ["+banhijau+"UPDATE"+reset+putih+"] Update Succed!"+reset);sys.exit()
if easy_mode:
    bannerd()
    print(kelabu+" ["+banhijau+"#"+reset+kelabu+"]"+putih+" Easy Mode...."+reset)
    mode = input(kelabu+" ["+orange+">"+kelabu+"]"+putih+" Pilih Mode, [image-background-eraser] or [video-background-eraser]: ")
    if mode == "image-background-eraser":
        media = str(input(kelabu+" ["+orange+">"+reset+kelabu+"]"+putih+" Masukan path file gambar [lewatkan jika menggunakan link(enter)] (.jpg; .png; .jpeg;): "+reset).strip())
        if media == "":
            url = str(input(kelabu+" ["+orange+">"+reset+kelabu+"]"+putih+" Masukkan link gambar: "+reset).strip())
        output = str(input(kelabu+" ["+orange+">"+reset+kelabu+"]"+putih+" Masukan path output: "+reset).strip())
        model = str(input(kelabu+" ["+orange+">"+reset+kelabu+"]"+putih+" Masukan model ('u2net'; 'u2net_human_seg'; 'silueta'; 'isnet-general-use'; isnet-anime', etc.): "+reset).strip())
        print(kelabu+" ["+banhijau+"!"+reset+kelabu+"]"+putih+" Mungkin proses akan sedikit lambat tergantung deivce"+reset)
        image_eraser(media, output, model, url)
    if mode == "video-background-eraser":
        bannerd()
        print(kelabu+" ["+banorange+"!"+reset+kelabu+"]"+putih+" Fitur belum tersedia, Nantikan update selanjutnya"+reset)
        pass
else:
    print(" [*] Importing Module...")
    print(" [*] Mungkin agak lama karena kami harus mengimpor file logo.txt ini juga berpengaruh tergantung kecepatan device kalian!")
    banner()
    print(kelabu+" ["+banorange+"!"+reset+kelabu+"]"+putih+" Wajib menggunakan BackSlash di semua sistem!")
    print(kelabu+" ["+orange+"*"+reset+kelabu+"]"+putih+" coba ketik python3 main.py --hh indonesia | english");sys.exit()
    print(kelabu+" ["+orange+"*"+reset+kelabu+"]"+putih+" Untuk panduan lengkap");sys.exit()
