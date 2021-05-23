from youtubesearchpython import SearchVideos
from pytube import YouTube
from media_controller import *
import subprocess, os
import json

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
    print('Downloading...')
    selected_file.download('Songs')
    return selected_file.default_filename
    
def download_and_play_song(query):
    vid_name = download_video(query)
    play_song(vid_name)

if __name__ == '__main__':
    download_and_play_song('7 ring')
