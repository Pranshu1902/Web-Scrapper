import requests, bs4

res = requests.get("https://nostarch.com")
res.raise_for_status()

data = bs4.BeautifulSoup(res.text, 'html.parser')

print(data)
