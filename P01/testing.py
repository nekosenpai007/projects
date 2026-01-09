# Test basic internet connectivity first
import urllib.request
try:
    urllib.request.urlopen('http://www.google.com', timeout=5)
    print("Internet connection is working")
except:
    print("No internet connection")