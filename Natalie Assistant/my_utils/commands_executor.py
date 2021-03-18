import subprocess

def set_brightness(value):
    test = subprocess.Popen(["xrandr",  "--output",  "LVDS-1", "--brightness",  str(value)], stdout=subprocess.PIPE)
    output = test.communicate()[0]
    print(output)

def comparative_brightness_adjustment(value):
    """powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,<Brightness Level>)"""

    'This will get: powercfg /q'
    'Search: aded5e82-b909-4619-9949-f5d71dac0bcb'
    test = subprocess.Popen(["/usr/lib/gnome-settings-daemon/gsd-backlight-helper",  "--get-brightness"], stdout=subprocess.PIPE)
    output = int(test.communicate()[0].decode())
    print(output + value)
    set_brightness(output + value)

def shutdown():
    test = subprocess.Popen(["shutdown",  "/s",  "/t", '5'], stdout=subprocess.PIPE)
    output = int(test.communicate()[0].decode())
