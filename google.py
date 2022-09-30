import requests, sys, json, webbrowser, bs4

address = "https://google.com/search?q="

if len(sys.argv)>1:
    address += '+'.join(sys.argv[1:])

res = requests.get("https://google.com/search?q=coding")

soup = bs4.BeautifulSoup(res.text, 'html.parser')

linkElems = soup.select('.package-snippet')

numOpen = min(5, len(linkElems))

for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
