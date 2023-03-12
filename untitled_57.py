import requests

respond1 = requests.get(url=f"https://api.genderize.io/?name=saad")
respond2 = requests.get(url=f"https://api.agify.io/?name=saad")

print(respond1.text, "\n", respond2.text)

get_name = respond2.json()

print(get_name["age"])
