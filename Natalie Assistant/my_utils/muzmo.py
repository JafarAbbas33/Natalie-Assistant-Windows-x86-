import requests
import subprocess, sys
import random
from media_controller import *
from bs4 import BeautifulSoup
#from pygame import mixer
import logging


#mixer.init()
logging.basicConfig(filename='muzmo.log', filemode='w', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
domain_url = 'https://en.muzmo.org'
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


def log(data):
    logging.debug('\n\n\n' + data.encode('unicode-escape').decode('utf-8'))

def get_song_page_url(query='boss bitch'):

    params = (
        ('q', query),
        ('_pjax', '#mcont'),
    )

    response = requests.get('https://en.muzmo.org/search', params=params)

    while 'Your search request is being processed' in response.text:
        response = requests.get('https://en.muzmo.org/search', params=params)

    soup = BeautifulSoup(response.text, 'lxml')
    log(soup.get_text())
    song = soup.find('div', attrs = {'class':'item-song ajax-item'})
    log(song.get_text())

    song_id = song.find('td', id=True)['id']
    song_rel_url = song.find('a', href=True)['href']
    song_page_url = domain_url + song_rel_url

    song_page_url = domain_url + '/info?id=' + song_id + '&u=1'

    return song_page_url

def get_download_link(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')
    t = soup.find_all('div', attrs = {'class' : 'mzmdrk'})

    for element in t:
        try:
            if 'Download original' in element.get_text():
                return domain_url + element.find('a')['href']
        except:
            pass
    print("Couldn't find download link")

def download_song(link):
    r = requests.get(link, allow_redirects=True)
    print('Downloading...')
    with open('Songs/song.mp3', 'wb') as f:
        f.write(r.content)

def play_song_old(path='song.mp3'):
    print('Playing...')
    #mixer.music.load(path)
    #t = mixer.music.play()
    #while mixer.music.get_busy():
    #    pass
    print('Stopped')

def download_and_play_song(query):
    print('Getting download link...')
    url = get_song_page_url(query)
    song_link = get_download_link(url)
    download_song(song_link)
    play_song()

def top_rated_song_url():
    url = 'https://en.muzmo.org/rated_songs'
    response = requests.get(url)
    log(response.text)
    soup = BeautifulSoup(response.text, 'lxml')
    t = soup.find_all('div', attrs = {'class' : 'mzmlght'}) #'mzmdrk'

    for element in t:
        try:
            if 'Kb/s' in element.get_text():
                #print(element.get_text().strip().replace(' ', ''))
                return domain_url + element.find('a')['href']
                #print(10*'-')
        except:
            pass
    print("Couldn't find download link")

def random_song_url():
    page = 1

    params = (
        ('sort', '0'),
        ('start', str(page*15)),
    )

    response = requests.get('https://en.muzmo.org/top', params=params)

    soup = BeautifulSoup(response.text, 'lxml')
    

    songs_page_urls = []
    t = soup.find_all('div', attrs = {'class' : 'mzmlght'})
    for element in t:
        if 'Kb/s' in element.get_text():
            #song_name = element.get_text().strip().splitlines()[0].strip()
            song_page_url = domain_url + element.find('a')['href']
            songs_page_urls.append(song_page_url)
            #print(song_page_url)
    t = soup.find_all('div', attrs = {'class' : 'mzmdrk'})
    for element in t:
        if 'Kb/s' in element.get_text():
            #song_name = element.get_text().strip().splitlines()[0].strip()
            song_page_url = domain_url + element.find('a')['href']
            songs_page_urls.append(song_page_url)
            #print(song_page_url)

    #print(len(songs_page_urls))
    return songs_page_urls[random.randrange(len(songs_page_urls))]

def download_and_play_top_rated():
    print('Getting download link...')
    url = top_rated_song_url()
    song_link = get_download_link(url)
    download_song(song_link)
    play_song()

def download_and_play_random():
    print('Getting download link...')
    url = random_song_url()
    song_link = get_download_link(url)
    download_song(song_link)
    play_song()

if __name__ == '__main__':
    download_and_play_random()
    #download_and_play_top_rated()
    #download_and_play_song('boss bitch')
