from urllib.parse import urlparse
from tld import get_tld
import re
import pickle
import numpy as np
def finish(a):
    a=a.replace("~","/")
    def lengthOfURL(url):
        return len(str(url))

    def lengthOfHostname(url):
        return len(urlparse(url).netloc)

    def lengthOfPath(url):
        return len(urlparse(url).path)

    def tld(url):
        x=get_tld(url,fail_silently=True)
        try:
            return len(x)
        except:
            return -1

    def Tally_dot(url):
        return url.count('.')

    def Tally_us(url):
        return url.count('-')

    def Tally_atr(url):
        return url.count('@')

    def Tally_per(url):
        return url.count('%')

    def Tally_http(url):
        return url.count('http')

    def Tally_https(url):
        return url.count('https')

    def Tally_www(url):
        return url.count('www')

    def Tally_eq(url):
        return url.count('=')

    def Tally_sl(url):
        return url.count('/')

    def Tally_qu(url):
        return url.count('?')

    def Tally_pl(url):
        return url.count('+')

    def Tally_dsl(url):
        return url.count('//')

    def directories(url):
        urldir = urlparse(url).path
        return urldir.count('/')

    def digit(url):
        digits = 0
        for i in url:
            if i.isnumeric():
                digits = digits + 1
        return digits

    def letter(url):
        letters = 0
        for i in url:
            if i.isalpha():
                letters = letters + 1
        return letters

    def ip_address(url):
        match = re.search(
            '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
            '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|' 
            '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)' # IPv4 in hexadecimal
            '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url) 
        if match:
            return 1
        else:
            return 0

    def parameter(url):
        l=[lengthOfURL(url),lengthOfHostname(url),lengthOfPath(url),tld(url),
        Tally_dot(url),Tally_us(url),Tally_atr(url),Tally_per(url),Tally_http(url),
        Tally_https(url),Tally_www(url),Tally_eq(url),Tally_sl(url),Tally_qu(url),
        Tally_pl(url),Tally_dsl(url),directories(url),digit(url),letter(url),ip_address(url)]
        return l
    
    x = parameter(a)
    loaded_model = pickle.load(open('final_model.sav', 'rb'))
    result = loaded_model.predict(np.array([x]))
    result1 = str(result[0])
    return result1