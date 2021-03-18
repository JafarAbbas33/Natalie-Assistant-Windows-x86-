import subprocess

pid = 0

def play_song(path='song.mp3'):
    global pid
    print('Playing...')

    vlc_path = r'C:\Program Files\VideoLAN\VLC\vlc.exe'

    test = subprocess.Popen([vlc_path, '--play-and-exit', '-I', 'dummy', '--dummy-quiet', 'Songs/'+path])
    pid = test.pid
    test.communicate()
    
    print('Stopped')

def stop_media():
    test = subprocess.Popen(['tskill', str(pid)])
    test.communicate()
    
    print('Stopped')


if __name__ == '__main__':
    import time, threading, os
    os.chdir('..')
    threading.Thread(target=play_song, daemon=True).start()
    time.sleep(5)
    stop_media()
