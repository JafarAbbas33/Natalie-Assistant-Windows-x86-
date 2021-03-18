
import sys, os, time

from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from pynput import keyboard as kb
from pynput.keyboard import Key, Listener
from pynput.keyboard import Controller as kb2

kb = kb2()
driver = None

def initialize_driver():
    global driver
    options = Options()
    options.add_argument("--log-level=3")
    #options.add_argument("--silent")
    options.add_argument("--headless")
    options.add_argument("--disable-logging")
    options.add_argument("disable-gpu")
    options.add_argument("--use-fake-ui-for-media-stream")
    options.add_argument("--user-data-dir=" + os.getcwd() + "\\CacheUserData")

    try:
        driver = webdriver.Chrome(options=options)
    except:
        from ChromeDriverDownloader import ChromeDriverDownloader
        ChromeDriverDownloader.download(os.getcwd())
        driver = webdriver.Chrome(options=options)
        
    driver.implicitly_wait(10)
    #driver.maximize_window()
    driver.get("https://picovoice.ai/demos/lamp/")




def start_detection(root=None):
    global driver
    #while 'Press the microphone button to activate the demo' not in driver.page_source:
    #    pass
    element = driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div[1]/div[1]/div[1]/button')
    
    while 'Say “Hey Edison”' not in driver.page_source:
        time.sleep(0.2)
        driver.execute_script("arguments[0].click();", element)
    
    print('Listening...')
    app_terminator.update_text('Listening')
    time.sleep(0.8)
    if __name__ != "__main__":
        root.state('iconic')
    
    while 'Say a color' not in driver.page_source:
        if not listener.is_alive():
            if __name__ == "__main__":
                driver.quit()
                sys.exit()
            driver.quit()
            app_terminator.terminate()
            return False
        
    print('Hotword detected\n')

    driver.execute_script("arguments[0].click();", element)


def wait_for_esc(key):
    if key == Key.esc:
        return False

listener = Listener(on_release=wait_for_esc)
listener.start()


if __name__ == "__main__":
    initialize_driver()
    while True:
        start_detection()
else:
    import app_terminator






