import os
import requests
import tarfile

from matches import MATCHES

def download():
    os.mkdir("tars")
    for language in MATCHES:
        url = MATCHES[language]["data_url"]
        # stream=True seems to basically be saying, don't bother downloading and unpacking it. 
        data = requests.get(url, stream=True)

        target_path = url.split("/")[-1]
        print("Downloading:", target_path)

        # I think I need the 'wb' - write binary. This seems to mean that it won't mess with the tar in any way.
        with open(f"tars/{target_path}", 'wb') as f:
            f.write(data.raw.read())


def unzip():
    os.mkdir("freq_tsvs")
    for tarball in os.listdir("tars"):
        print(tarball)
        with tarfile.open(name=f"tars/{tarball}", mode="r") as data:
            for entry in data.getnames():
                # print(entry)
                if entry.endswith("words.txt"):
                    data.extract(entry, "freq_tsvs")

# download()
unzip()