from commands_executor import *
import muzmo
from youtube_mp3 import download_and_play_song, play_song
import logging
import app_terminator, media_controller
import threading, subprocess

logging.basicConfig(filename='command_exec.log', filemode='w', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

def log(data):
    logging.debug('\n\n\n' + data.encode('unicode-escape').decode('utf-8'))


def is_com_present(my_spoken_text, req = [], single = []):
    if all(x in my_spoken_text for x in req) or len(req) == 0:
        if any(x in my_spoken_text for x in single) or len(single) == 0:
            return True
    return False


def command_present(my_spoken_text):
    my_spoken_text = my_spoken_text.lower()
##    if is_com_present(my_spoken_text, ['brightness', 'by']):
##        value = int(my_spoken_text[my_spoken_text.rfind(' ')+1:])
##        if 'decrease' in my_spoken_text:
##            value *= -1
##        threading.Thread(
##                target=lambda:comparative_brightness_adjustment(value)).start()
##        return True
##
##    if is_com_present(my_spoken_text, ['brightness', 'set', 'to']):
##        value = int(my_spoken_text[my_spoken_text.rfind(' ')+1:])
##        threading.Thread(target=lambda:set_brightness(value)).start()
##        return True

    if 'shutdown' in my_spoken_text:
        shutdown()
        app_terminator.terminate(ter=False)
        return True

##    if 'play best' in my_spoken_text:
##        media_name = my_spoken_text.replace('play best ', '')
##        threading.Thread(
##            target=lambda:muzmo.download_and_play_song(media_name)).run()
##        return True

    if is_com_present(my_spoken_text, [], ['play a random song', 'play', 'play a song', 'play song', 'play some music', 'play music']):
        threading.Thread(
            target=lambda:muzmo.download_and_play_random()).start()
        return True

    if my_spoken_text.startswith('play'):
        media_name = my_spoken_text.replace('play ', '')
        threading.Thread(
            target=lambda:download_and_play_song(media_name)).start()
        return True

##    if 'pause' in my_spoken_text:
##        pause_media()
##        return True
##
##    if 'resume' in my_spoken_text:
##        resume_media()
##        return True

    if 'stop' in my_spoken_text:
        media_controller.stop_media()
        return True
    
    if is_com_present(my_spoken_text, [], ['goodbye', 'quit', 'exit', 'good bye']):
        app_terminator.terminate()
        return True
    
    return False
