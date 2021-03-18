import threading
from youtube_mp3 import download_and_play_song, play_song

threading.Thread(target=lambda:download_and_play_song('faded')).run()

print('Below')
