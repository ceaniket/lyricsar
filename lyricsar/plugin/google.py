
import string
import sys
import urllib
import json
import httplib
from bs4 import BeautifulSoup
from setting import GOOGLE_API_URL
from lyricsar.errorlist import errorlist
class google:
    response=""
    """ this plugin provide link by traverse results of google.com with extra keyword"""
    def __init__(self,title):
        self.search_url=GOOGLE_API_URL
        self.title=title

    def get_search(self):
        """get_search function make a url from title and url"""
        string.replace(self.title," ","%20")
        url=self.search_url+self.title
        return str(url)

    def get_link(self,searchpage):
        """get_link fetch first link from google results """
        try:
            results = json.loads(searchpage)
            print results
            return results
        except:
            sys.exit(errorlist['0e02'])


#================================ tesing =======================================
if __name__=="__main__":

    gogle=google("meherbaan+lyrics")
    url=gogle.get_search()
    htp=httplib.Http()
    response,searchpage=htp.request(url,'GET')
    lyrcweb=gogle.get_link(searchpage)
    print lyrcweb
