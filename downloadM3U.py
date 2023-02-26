import urllib.request
import os
from tkinter import filedialog
from tkinter import *

def downloadM3U(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    file_name, headers = urllib.request.urlretrieve(url)
    return file_name

if __name__ == "__main__":
    url = str(input("\nIntroduce la URL del fichero m3u: "))
    countries = str(input("\nIntroduce los países a filtrar separados por comas: ")).replace(" ", "").upper().split(",")
    file_name_m3u = str(input("\nIntroduce el nombre del fichero m3u que se va a crear: "))

    if(file_name_m3u == ""):
        file_name_m3u = "default_name"

    if(".m3u" in file_name_m3u):
        file_name_m3u = file_name_m3u.split(".m3u")[0]

    tmp_path_m3u_file = downloadM3U(url)
    content_m3u = "#EXTM3U\n"

    with open(tmp_path_m3u_file, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            if any("group-title=\""+country+"\"" in lines[i] for country in countries):
                try:
                    content_m3u += lines[i]
                    content_m3u += lines[i+1]
                except:
                    pass

    folder_selected = os.getcwd()
    select_folder = ""
    while (select_folder  not in  ["NO", "SI"] ):
        select_folder = str(input(f"\nLa ubicación por defecto donde crear el archivo es '{folder_selected}'. ¿Desea cambiarla? [Si/No]: ")).upper()

    if (select_folder == "SI"):
        root = Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory()
        if (folder_selected == ""):
            folder_selected = os.getcwd()

    if (os.path.exists(f"{folder_selected}/{file_name_m3u}.m3u")):
        i = 1
        while os.path.exists(f"{folder_selected}/{file_name_m3u}_{i}.m3u"):
            i += 1
        file_name_m3u = f"{folder_selected}/{file_name_m3u}_{i}.m3u"
    else:
        file_name_m3u = f"{folder_selected}/{file_name_m3u}.m3u"

    with open(file_name_m3u, mode="w", encoding="utf-8") as f:
        f.write(content_m3u)

    print(f"\nArchivo descargado con éxito en {file_name_m3u}")

    input("\nPulsa ENTER para finalizar...")