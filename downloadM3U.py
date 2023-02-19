import urllib.request
import os

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

    if (os.path.exists(f"{file_name_m3u}.m3u")):
        i = 1
        while os.path.exists(f"{file_name_m3u}_{i}.m3u"):
            i += 1
        file_name_m3u = f"{file_name_m3u}_{i}.m3u"
    else:
        file_name_m3u = f"{file_name_m3u}.m3u"

    with open(file_name_m3u, mode="w", encoding="utf-8") as f:
        f.write(content_m3u)