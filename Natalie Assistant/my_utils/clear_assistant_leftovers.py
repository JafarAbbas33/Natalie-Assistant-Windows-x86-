import subprocess

def clear_assistant_leftovers():
    test = subprocess.Popen(['tskill', 'chrome'])
    test.communicate()
    test = subprocess.Popen(['tskill', 'chromedriver'])
    test.communicate()
    test = subprocess.Popen(['tskill', 'vlc'])
    test.communicate()
    
    print('Stopped')

if __name__ == '__main__':
    clear_assistant_leftovers()
    input('Press Enter')
