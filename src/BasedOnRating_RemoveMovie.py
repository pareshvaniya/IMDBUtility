#Author_PareshVaniya
#Dependancies

from bs4 import BeautifulSoup
import requests
import json
import os
import shutil
from movie_renamer import rename

def getJSONMOVIEDATA(html):
            
    moviedata = {}
    moviedata['title'] =  html.find(itemprop='name').text.strip()
    moviedata['rating'] = html.find(itemprop='ratingValue').text
           
    json_movie_data = json.dumps(moviedata, ensure_ascii=False)
    
    
    return json_movie_data
    
def getHTML(url):
    #response = requests.get(url,proxies={"http": "http://username:password@ip:port","https": "https://username:password@ip:port"})
    response = requests.get(url)
    return BeautifulSoup(response.content,'html.parser')    
    
def getURL(file):
    try:
        html = getHTML('https://www.google.co.in/search?q='+file)
        for cite in html.findAll('cite'):
                if 'imdb.com/title/tt' in cite.text:
                    html = getHTML('http://'+cite.text)
                    break
        return getJSONMOVIEDATA(html)    
    except Exception as e:
        return ''

path = "E:/testmovie"

print("We are in this movie folder : "+path)

print "Sr.No" + " | "+ "Original Name" +" | "+ "Converted Name"  + " | " + "IMDB Rating"

i = 0
rm = 0

for file in os.listdir(path):
    try:    
        
        original_name = os.path.splitext(file)[0]
        
        converted_name = rename(original_name)
        
        data = getURL(converted_name + " imdb rating")
        resp = json.loads(data)
        
        n = float(resp['rating'])
        
        i+=1
        
        print repr(i) +".) " + original_name +" | "+ converted_name + " | " , n
        
        
        if n < 6:
            input = raw_input("Do you want to remove this movie ? : y / n ")
            
            if input == "y":
                rm+=1
                if os.path.isfile(path+"/"+file):
                    os.remove(path+"/"+file)    
                    print(original_name +" is successfully removed")
                else:
                    shutil.rmtree(path+"/"+file, ignore_errors=False, onerror=None)
                    print(original_name +" is successfully removed")
            else:
                print ""
    except Exception as e:
        print("")



print(repr(rm) +" movies removed from this folder "+path)        