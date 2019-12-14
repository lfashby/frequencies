import os
import requests
import tarfile
import time

from matches import MATCHES

def download():
    os.mkdir("tars")
    for language in MATCHES:
        url = MATCHES[language]["data_url"]
        with requests.get(url, stream=True) as response:
            target_path = url.split("/")[-1]
            print("Downloading:", target_path)
            print(response.status_code)
            if response.status_code == 200:
                with open(f"tars/{target_path}", "wb") as f:
                    f.write(response.raw.read())
            else:
                print("ERROR DOWNLOADING", target_path)
        time.sleep(60)


def unzip():
    os.mkdir("freq_tsvs")
    for tarball in os.listdir("tars"):
        print(tarball)
        with tarfile.open(name=f"tars/{tarball}", mode="r:gz") as data:
            for entry in data.getnames():
                # print(entry)
                if entry.endswith("words.txt"):
                    data.extract(entry, "freq_tsvs")

download()
# unzip()




# Attempting to do everything in one step didn't work.
# StreamError, seeking backwards...too much work to fix that.
# data = response.raw
# with tarfile.open(fileobj=data, mode="r|gz") as dataum:
#     for entry in dataum.getnames():
#         # print(entry)
#         if entry.endswith("words.txt"):
#             dataum.extract(entry, "freq_tsvs")