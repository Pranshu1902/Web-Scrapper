import requests, json

class WebScrapper:
    def __init__(self, baseUrl, fileName):
        self.baseUrl = baseUrl
        self.fileName = fileName
    
    def extractData(self, endPoint=""):
        url = self.baseUrl + endPoint
        res = requests.get(url)
        data = res.content

        # decoding the data
        data = data.decode("utf-8")

        # saving data
        f = open(self.fileName, "w")
        f.write(data)
        f.close()
    
    def readData(self):
        f = open(self.fileName, "r")
        content = f.read()
        content = json.loads(content)
        return content
    
    def getUserCount(self):
        data = self.readData()
        return len(data)
    
    def getUserDetails(self, id):
        data = self.readData()
        return data[id]


moneyManager = WebScrapper("http://money-manager-pranshu1902.herokuapp.com/user/", "moneyUsers.json")

moneyManager.extractData()
print(moneyManager.getUserCount())
