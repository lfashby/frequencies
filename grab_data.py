import os
import requests
import tarfile
import time

from matches import MATCHES

# Downloads the tarballs, roughly 10 GB of data.
def download(data_to_grab):
    to_retry = {}
    os.makedirs("tars", exist_ok=True)        
    for language in data_to_grab:
        url = data_to_grab[language]["data_url"]
        with requests.get(url, stream=True) as response:
            target_path = url.split("/")[-1]
            print("Downloading:", target_path)
            print(response.status_code)
            if response.status_code == 200:
                with open(f"tars/{target_path}", "wb") as f:
                    f.write(response.raw.read())
            else:
                print("ERROR DOWNLOADING", target_path)
                to_retry[language] = data_to_grab[language]
        # 30 seconds appears to not be enough, 60-70 seconds works well
        # but takes a long time.
        time.sleep(45)
    return to_retry


# Unzips word frequency tsvs of tarballs, roughly 1 GB of data.. 
def unzip():
    os.mkdir("freq_tsvs")
    for tarball in os.listdir("tars"):
        print(tarball)
        with tarfile.open(name=f"tars/{tarball}", mode="r:gz") as data:
            for entry in data:
                if entry.name.endswith("words.txt"):
                    # Removes inconsistent path in tarballs
                    # so freq_tsvs has uniform contents.
                    entry.name = os.path.basename(entry.name)
                    data.extract(entry, "freq_tsvs")


# Hack for recursively attempting to download data. 
langs = download(MATCHES)
while langs:
    langs = download(langs)

unzip()




# Attempting to do everything in one step didn't work.
# StreamError, seeking backwards...too much work to fix that.
# data = response.raw
# with tarfile.open(fileobj=data, mode="r|gz") as dataum:
#     for entry in dataum.getnames():
#         # print(entry)
#         if entry.endswith("words.txt"):
#             dataum.extract(entry, "freq_tsvs")