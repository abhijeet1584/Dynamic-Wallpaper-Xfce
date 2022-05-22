# mv Dynamic_wallpaper.desktop ~/.config/autostart
import os
import getpass

def get_username():
    return str(getpass.getuser())

def move_files():
    os.system("mkdir ~/Wallpapers")
    os.system("cd ~/Wallpapers && mkdir Adwaita")

def create_autostart_file(usr):
    fc = [
        "[Desktop Entry]\n",
        "Encoding=UTF-8\n",
        "Version=0.9.4\n"
        "Type=Application\n",
        "Name=wallpaper\n",
        "Comment=Dynamic Wallpaper Script\n",
        f"Exec=python3 /home/{usr}/Wallpapers/Adwaita/wallpaper.py\n",
        "OnlyShowIn=XFCE;\n",
        "RunHook=0\n",
        "StartupNotify=false\n",
        "Terminal=false\n",
        "Hidden=false"
    ]
    f = open("Dynamic_wallpaper.desktop", "w")
    f.writelines(fc)
    f.close()

def set_autostart():
    os.system("mv Dynamic_wallpaper.desktop ~/.config/autostart")

create_autostart_file(get_username())
set_autostart()