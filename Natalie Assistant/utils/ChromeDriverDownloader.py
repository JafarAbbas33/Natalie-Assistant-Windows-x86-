import subprocess, os, sys
import webbrowser
from zipfile import ZipFile
##import os
##import sys

class ChromeDriverDownloader:
    chrome = ""
    @staticmethod
    def download(application_path):
        is_chrome_available = False

        def is_chrome_available(path):
            for root, dirs, files in os.walk(path):
                global chrome
                if "chrome.exe" in files:
                    path = path.replace("/", "\\\\")
                    ChromeDriverDownloader.chrome = path + "\\\\chrome.exe"
                    return True
                else:
                    print("Couldn't find Google Chrome.")
                    return False

        if not is_chrome_available("C:/Program Files/Google/Chrome/Application"):
            if not is_chrome_available("C:/Program Files (x86)/Google/Chrome/Application"):
                if(input("Couldn't find chrome. Do you want to download it?[y/n]: ") == "n"):
                   sys.exit()
                else:
                    webbrowser.open("https://www.google.com/chrome/", new=2)
                    sys.exit()
            
        query = "wmic datafile where name='" + ChromeDriverDownloader.chrome + "' get Version /value"

        output = subprocess.check_output(query, shell=True).decode("ASCII")
        output = output.replace("\n", "")
        output = output.replace("\r", "")
        output = output.replace("Version=", "")
        output = output[:output.rfind(".")+1]

        import requests

        try:
            url = requests.get("https://chromedriver.chromium.org/downloads")
        except requests.exceptions.ConnectionError:
            print("Connection Error. Please check your internet connection.")
            sys.exit()
        htmltext = url.text
        for line in htmltext.splitlines():
            line.find(output) + 3
            if output in line:
                index = line.find(output)
                available_driver = line[index:index+13]
                try:
                    int(available_driver[-1])
                except ValueError:
                    available_driver = available_driver[:-1]
                    
                print("Downloading...")

                url = "https://chromedriver.storage.googleapis.com/"+available_driver+"/chromedriver_win32.zip"
                r = requests.get(url, allow_redirects=True)

                with open("chromedriver_win32.zip", 'wb') as f:
                    f.write(r.content)

                 
          
                # specifying the zip file name 
                file_name = "chromedriver_win32.zip"
                  
                # opening the zip file in READ mode
                try:
                    try:
                        with ZipFile(file_name, 'r') as zip:
                            # extracting all the files 
                            print('Extracting...') 
                            zip.extractall(application_path) 
                            print('Done!')
##                            os.environ['PATH'] += ";" + application_path
                            
                    except zipfile.BadZipFile:
                        pass
                except NameError:
                    print("Bad Zip File.")
                    sys.exit()

                os.remove("chromedriver_win32.zip")
                return True


if __name__ == "__main__":
    ChromeDriverDownloader.download(os.getcwd())
