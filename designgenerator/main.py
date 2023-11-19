import json
import random

homepath = "/home/salzi/"

with open(f"{homepath}.config/designgenerator/config.json", "r") as file:
    configs = json.load(file)


def Replace(input):
    for key in config:
        input = input.replace(f"--{key}--", config[key])
        
    return input


def ReplaceContentAndSaveFile(filepath, destinationpath):
    with open(f"{homepath}{filepath}", "r") as file:
        configcontent = file.read()

    configcontent = Replace(configcontent)

    with open(f"{homepath}{destinationpath}", "w") as file:
        file.write(configcontent)

config = random.choice(configs)

# sway
ReplaceContentAndSaveFile(".config/designgenerator/sway/config", ".config/sway/config")

# waybar
ReplaceContentAndSaveFile(".config/designgenerator/waybar/style.css", ".config/waybar/style.css")
ReplaceContentAndSaveFile(".config/designgenerator/waybar/config", ".config/waybar/config")

# rofi
ReplaceContentAndSaveFile(".config/designgenerator/rofi/config.rasi", ".config/rofi/config.rasi")

# swaylock
ReplaceContentAndSaveFile(".config/designgenerator/swaylock/config", ".config/swaylock/config")

# alacritty
ReplaceContentAndSaveFile(".config/designgenerator/alacritty/alacritty.yml", ".config/alacritty/alacritty.yml")
ReplaceContentAndSaveFile(".config/designgenerator/alacritty/theme.yml", ".config/alacritty/theme.yml")


"""
{
        "comment": "old style",
        "wallpaper": "~/.config/designgenerator/wallpapers/arch.png",
        
        "waybarbottom": "#64727d",
    
        "backgroundcolor": "#2b303b",
        "backgroundcolor2": "#566076",
    
        "textcolor": "#70e5ff",
        "textcolor2": "#ffffff",
    
        "correctcolor": "00ff00",
        "wrongcolor": "ff0000",
    
        "opacity": "0.3"
    },
"""