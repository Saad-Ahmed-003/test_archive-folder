import requests

header2 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                  "110.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

respond1 = requests.get(url=f"https://api.genderize.io/?name=saad")
respond2 = requests.get(url=f"https://api.agify.io/?name=saad")
respond3 = requests.get(url="")

print(respond1.text, "\n", respond2.text)

get_name = respond2.json()
blog = respond3.json()
print(get_name["age"])
for i in blog:
    print(i)
