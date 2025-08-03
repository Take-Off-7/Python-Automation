import urllib.request

print("starting dowload...")

url = "https://www.python.org/static/img/python-logo.png"

# urllib.request.urlretrieve(url, "python.png")
# print("Image downloaded!")

with urllib.request.urlopen(url) as response:
    if response.status == 200:
        with open("python.png", "wb") as f:
            f.write(response.read())
        print("Download complete!")
    else:
        print("Failed to download:", response.status)
