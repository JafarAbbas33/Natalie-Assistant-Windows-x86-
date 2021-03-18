
import subprocess

if True:
    test = subprocess.Popen(["/usr/lib/gnome-settings-daemon/gsd-backlight-helper",  "--get-brightness"], stdout=subprocess.PIPE)
    output = test.communicate()[0].decode()
    print(output)
