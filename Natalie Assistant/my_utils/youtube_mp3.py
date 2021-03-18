from youtubesearchpython import SearchVideos
from pytube import YouTube
from media_controller import *
#from pygame import mixer
import subprocess, os
import json

#mixer.init()
##os.remove('song.mp3')

def get_video_url(query="faded"):
    search = SearchVideos(query, offset = 1, mode = "json", max_results = 3)
    result = json.loads(search.result())
    
    vid_id = result['search_result'][0]['id']
    return 'http://youtube.com/watch?v=' + vid_id

def convert_video_to_audio(vid_name):
    print('Converting...')
    test = subprocess.Popen(['ffmpeg',  '-i', vid_name, 'song.mp3'], stdout=subprocess.PIPE)
    output = test.communicate()[0]
    os.remove(vid_name)

def download_video(query):
    vid_url = get_video_url(query)
    yt = YouTube(vid_url)
    selected_file = yt.streams.filter(adaptive=True, only_audio=True)[0]
##    print('Highest video:', yt.streams.filter(progressive=True))
    print('Downloading...')
    selected_file.download('Songs')
    return selected_file.default_filename
    
##    yt.streams.get_highest_resolution().download()
##    YouTube(vid_url).streams[0].download()


def download_and_play_song(query):
    vid_name = download_video(query)
##    convert_video_to_audio(vid_name)
    play_song(vid_name)

if __name__ == '__main__':
    download_and_play_song('7 ring')

##    yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
##    yt.streams
##    .filter(progressive=True, file_extension='mp4')
##    .order_by('resolution')[-1]
##    .download()

