import time
import os

PROPERTY = "/backdrop/screen0/monitorVGA-1/workspace0/last-image"

IMG_1 = "~/Wallpapers/Adwaita/Adwaita-l.png"
IMG_2 = "~/Wallpapers/Adwaita/Adwaita-d.png"

def change_wallpaper(image):
    os.system(f"xfconf-query -c xfce4-desktop -p {PROPERTY} -s {image}")

def get_time():
    t = time.localtime()
    current_time = time.strftime("%H", t)
    return int(current_time)

# Main loop
while (True):
    t = get_time()

    # light wallpaper
    if t >= 6 and t <= 16:
        change_wallpaper(IMG_1)

    elif t > 16 and t <= 23:
        change_wallpaper(IMG_2)

    elif t >= 0 and t < 6:
        change_wallpaper(IMG_2)

    time.sleep(300)