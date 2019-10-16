import requests
from matches import MATCHES

for language in MATCHES:
    url = MATCHES[language]["data_url"]
    # stream=True seems to basically be saying, don't bother downloading and unpacking it. 
    data = requests.get(url, stream=True)

    target_path = url.split("/")[-1]
    print("Downloading:", target_path)

    # I think I need the 'wb' - write binary. This seems to mean that it won't mess with the tar in any way.
    with open(f"./tars/{target_path}", 'wb') as f:
        f.write(data.raw.read())