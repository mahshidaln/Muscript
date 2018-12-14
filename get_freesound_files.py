import os
import mimetypes
import urllib.request
from bs4 import BeautifulSoup

def get_files(tag, pages, directory):
    for p in range(1, pages):
        print(p)
        url = 'https://freesound.org/browse/tags/' + tag + '/?page=' + str(p)
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        samples = soup.find_all('a', {'class':'mp3_file'})
        names = soup.find_all('a', {'class':'title'})
        print(len(samples))
        print(len(names))
        links = []
        for s in samples:
            links.append('https://freesound.org' + s['href'])
            print('downloading from ' + links[-1])
            name = to_name_files(names[samples.index(s)]['title'])
            print(name)
            r = urllib.request.urlretrieve(links[samples.index(s)], directory + name)
           
            

def to_name_files(title):
    name = title if(mimetypes.guess_type(title) != (None, None)) else (title +'.wav')
    return name


directory = 'C:/Users/Mahshid/Desktop/ASP/'
tag = 'guitar'
pages = 3
directory = directory + tag + '/'
os.mkdir(directory)
get_files(tag, pages, directory)


