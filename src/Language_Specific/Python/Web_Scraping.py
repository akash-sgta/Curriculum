from sys import flags
from bs4 import BeautifulSoup
import requests
import json

HEADER = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0',
          'Accept-Language' : "en-US,en;q=0.5"}

class Amazon(object):

    def __init__(self, search_param=None):
        self.url = "https://www.amazon.in/"
        if search_param == None:
            pass
        else:
            self.query = "+".join(search_param.strip().split())

        self.session = requests.Session()
    
    def run(self):
        
        result = self.session.get(self.url+f"/s/ref=nb_sb_noss?url=search-alias=aps&field-keywords={self.query}", headers=HEADER)
        if result.status_code != 200:
            print("[x] Site fetch")
        else:
            print("[.] Site fetch")

            source = result.content
            soup = BeautifulSoup(source, 'lxml')
        
            items = soup.find_all("div", {'class':"a-section a-spacing-medium"})

            fp = open("junk/amazon_scrape.csv", "w")
            fp.close()

            fp = open("junk/amazon_scrape.csv", "a")
            fp.write("name;price;rating;\n")

            for item in items:
                try:
                    name = item.find("span", {"class":"a-size-medium a-color-base a-text-normal"}).get_text().strip()
                    price = item.find("span", {"class":"a-price-whole"}).get_text().strip()
                    rating = item.find("span", {"class":"a-icon-alt"}).get_text().strip()
                except AttributeError:
                    pass
                else:
                    fp.write(f"{name};{price};{rating};\n")

            fp.close()

    def close_session(self):
        self.session.close()
        return True

def amazon():
    text = "mobile phone under 30000"
    print(f"[.] Amazon : {text}")
    obj = Amazon(search_param=text)
    obj.run()

    count = 0
    while True:
        with open("junk/amazon_scrape.csv", "r") as fp:
            if len(fp.read()) < 20:
                print("[x] Blank Read. Redoing. . . .")
                count += 1
            else:
                break
        if count > 5:
            print("[x] Bad Read. Try again later.")
            break
        obj.run()
    obj.close_session()
    print("[.] Done.")

class Google(object):

    def __init__(self, search_param=None):
        self.url = "https://www.google.com"
        if search_param == None:
            pass
        else:
            self.query = "+".join(search_param.strip().split())

        self.session = requests.Session()
    
    def run(self):
        
        result = self.session.get(self.url+f"/search?q={self.query}", headers=HEADER)
        
        if result.status_code != 200:
            print("[x] Site fetch")
        else:
            print("[.] Site fetch")

            source = result.content
            soup = BeautifulSoup(source, 'lxml')
        
            items = soup.find_all("div", {'class':"g"})

            fp = open("junk/google_scrape.csv", "w")
            fp.close()

            fp = open("junk/google_scrape.csv", "a")
            fp.write("heading;link;\n")

            for item in items:
                try:
                    heading = item.find("h3", {"class":"LC20lb DKV0Md"}).span.get_text().strip()
                    link = item.find("div", {"class":"yuRUbf"}).a.attrs['href'].strip()
                except Exception:
                    pass
                else:
                    fp.write(f"{heading};{link};\n")

            fp.close()

    def close_session(self):
        self.session.close()
        return True
    
def google():
    text = "what is the meaning of life"
    print(f"[.] Google : {text}")
    obj = Google(search_param=text)
    obj.run()

    count = 0
    while True:
        with open("junk/google_scrape.csv", "r") as fp:
            if len(fp.read()) < 15:
                print("[x] Blank Read. Redoing. . . .")
                count += 1
            else:
                break
        if count > 5:
            print("[x] Bad Read. Try again later.")
            break
        obj.run()
    obj.close_session()
    print("[.] Done.")

class Reddit(object):

    def __init__(self, search_param=None):
        self.url = "https://www.reddit.com"
        if search_param == None:
            pass
        else:
            self.query = search_param.strip()

        self.session = requests.Session()
    
    def run(self):
        
        result = self.session.get(self.url+f"/search/?q={self.query}", headers=HEADER)
        
        if result.status_code != 200:
            print("[x] Site fetch")
        else:
            print("[.] Site fetch")

            source = result.content
            soup = BeautifulSoup(source, 'lxml')
        
            items = soup.find_all("div", {'class':"_2XDITKxlj4y3M99thqyCsO"})

            fp = open("junk/reddit_scrape.csv", "w")
            fp.close()

            fp = open("junk/reddit_scrape.csv", "a")
            fp.write("heading;tag;link;\n")

            for item in items:
                try:
                    heading = item.find("h3", {"class":"_eYtD2XCVieq6emjKBH3m"}).find("span").text
                    link = self.url + item.find("a", {"class":"SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE"}).attrs['href']
                except Exception:
                    pass
                else:
                    fp.write(f"{heading};;{link};\n")
            fp.close()

    def close_session(self):
        self.session.close()
        return True

def reddit():
    text = "U mah lau"
    print(f"[.] Reddit : {text}")
    obj = Reddit(search_param=text)
    obj.run()

    count = 0
    while True:
        with open("junk/reddit_scrape.csv", "r") as fp:
            if len(fp.read()) < 25:
                print("[x] Blank Read. Redoing. . . .")
                count += 1
            else:
                break
            
        if count > 5:
            print("[x] Bad Read. Try again later.")
            break
        else:
            obj.run()
    obj.close_session()
    print("[.] Done.")

class Twitter(object):

    def __init__(self, search_param=None):
        self.url = "https://twitter.com"
        if search_param == None:
            pass
        else:
            self.query = search_param.strip()

        self.session = requests.Session()

        self.cred = {"user" : "gwc24629@cuoly.com",
                     "pass" : "abcd!1234"}

    def run(self):

        result = self.session.get(self.url+f"/search?q={self.query}&src=typed_query", headers=HEADER)
        
        if result.status_code != 200:
            print("[x] Site fetch")
        else:
            print("[.] Site fetch")

            source = result.content
            soup = BeautifulSoup(source, 'lxml')
            
            with open("test/test.html", "w") as f:
                f.write(soup.text)
        
            items = soup.find_all("article", {"role":"aritcle"})

            fp = open("junk/twitter_scrape.csv", "w")
            fp.close()

            fp = open("junk/twitter_scrape.csv", "a")
            fp.write("heading;detail;link;\n")

            for item in items:
                try:
                    pass
                    #heading = item.find("div")
                except Exception:
                    pass
                else:
                    #fp.write(f"{heading};;;\n")
                    fp.write(f"{item.content};;;\n")
            fp.close()

    def close_session(self):
        self.session.close()
        return True

def twitter():
    text = "India is great"
    print(f"[.] Twitter : {text}")
    obj = Twitter(search_param=text)
    obj.run()

    count = 0
    while True:
        with open("junk/twitter_scrape.csv", "r") as fp:
            if len(fp.read()) < 25:
                print("[x] Blank Read. Redoing. . . .")
                count += 1
            else:
                break
            
        if count > 5:
            print("[x] Bad Read. Try again later.")
            break
        else:
            obj.run()
    obj.close_session()
    print("[.] Done.")

if __name__ == "__main__":
    amazon()
    google()
    reddit()
    # twitter() # not finished
