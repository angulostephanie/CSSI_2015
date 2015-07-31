import urllib2
import json

url = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=funny+pugs"
string = urllib2.urlopen(url)
bigdictionary =json.loads(string.read())
# data = bigdictionary['data']
print bigdictionary['data']['image_url']



import urlib2
import json
import jinja2
