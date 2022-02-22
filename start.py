from urllib.parse import urlparse
from tld import get_tld
import re
import pickle
from flask import Flask, redirect, url_for, request,render_template
from model import finish
app = Flask(__name__)

@app.route('/success/<url>')
def success(url):
   urlfin = finish(url)
   if urlfin=="0":
      urlfin1 = "Benign"
      urlcol = "green"
   else:
      urlfin1 = "Malicious"
      urlcol = "red"
   urlx1 = url.replace("^","/")
   return render_template('resultpage.html', urlr = urlx1,urlres=urlfin1, urlcol1 = urlcol)
@app.route('/urllookup',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      url1 = request.form['nm']
      url1 = url1.replace("/","^")
      return redirect(url_for('success',url = url1))
   else:
      url1 = request.args.get('nm')
      url1 = url1.replace("/","^")
      return redirect(url_for('success',url = url1))

if __name__ == '__main__':
   app.run(debug = True)