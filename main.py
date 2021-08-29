from pathlib import Path
import os
import shutil

originPathString = "/Users/cleeryy/Downloads/"
originPath = Path(originPathString)
paths = {
    "Images": "images/",
    ".png": "images/png/",
    ".jpg": "images/jpg/",
    ".jpeg": "images/jpg/",
    ".gif": "images/gif/",
    ".webp": "images/webp/",
    ".psd": "images/photoshop/",
    ".heic": "images/heic/",

    "Videos": "videos/",
    ".mp4": "videos/mp4/",
    ".mkv": "videos/mkv/",
    ".avi": "videos/avi/",

    "Compressed": "compressed/",
    ".zip": "compressed/zip/",
    ".rar": "compressed/rar/",
    ".7z": "compressed/7z/",

    "Documents": "documents/",
    ".pdf": "documents/pdf/",
    ".xlsx": "documents/xlsx/",
    ".txt": "documents/txt/",
    ".torrent": "documents/torrents/",

    "Development": "development/",
    ".py": "development/python/",
    ".pyw": "development/python/",
    ".js": "development/javascript/",
    ".java": "development/java/",
    ".html": "development/html/",
    ".css": "development/css/",
    ".env": "development/env/",
    ".json": "development/json/",
    ".yml": "development/yml/",
    ".pkg": "development/pkg/",
    ".ovpn": "development/open-vpn/",

    "Others": "others/",
    ".ttf": "others/fonts/",
    ".otf": "others/fonts/",
    ".jar": "others/minecraft-plugins/",
    ".dmg": "others/setups/",
    ".bz2": "others/bz2/",

    ".avi": "videos/avi/"

}

def makeDir(dirname):
    try:
        os.mkdir(originPathString + dirname.lower())
    except:
        print(f'The directory {dirname.lower()} exists already.')
    return (originPathString + dirname.lower())

for dir in paths:
    print(makeDir(paths[dir]))

filesToSort = originPath.iterdir()
for file in filesToSort:
    if file.is_file():
        if file.suffix.lower() in paths:
            shutil.move(originPathString + file.name, originPathString + paths[file.suffix.lower()] + file.name)
        else:
            newDir = makeDir("others/" + file.suffix[1:] + "/")
            print(newDir)
            shutil.move(originPathString + file.name, newDir + file.name)
    else:
        pass