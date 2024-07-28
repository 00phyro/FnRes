import os
import re
from pystyle import Colorate, Colors, Center, Write


def get_game_user_settings_path():
    appdata_path = os.getenv('LOCALAPPDATA')
    return os.path.join(appdata_path, "FortniteGame", "Saved", "Config", "WindowsClient", "GameUserSettings.ini")

def remove_read_only(file_path):
    permissions = os.stat(file_path).st_mode
    os.chmod(file_path, permissions | 0o200)

def set_read_only(file_path):
    permissions = os.stat(file_path).st_mode
    os.chmod(file_path, permissions & ~0o200)

DIRECTORY = get_game_user_settings_path()

try:
    remove_read_only(DIRECTORY)
    
    with open(DIRECTORY, 'r') as file:
        content = file.read()

    print(Colorate.Horizontal(Colors.blue_to_green, Center.XCenter(""" 

           ███████╗███╗░░██╗██████╗░███████╗░██████╗
           ██╔════╝████╗░██║██╔══██╗██╔════╝██╔════╝
           █████╗░░██╔██╗██║██████╔╝█████╗░░╚█████╗░
           ██╔══╝░░██║╚████║██╔══██╗██╔══╝░░░╚═══██╗
           ██║░░░░░██║░╚███║██║░░██║███████╗██████╔╝
           ╚═╝░░░░░╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝╚═════╝░
    ⌜―――――――――――――――――――――――――――――――――――――――――――――――――――――⌝
    ┇      [Github]  https://github.com/HyRo-P             ┇
    ┇      [Telegram] @Hyro_99                             ┇
    ⌞―――――――――――――――――――――――――――――――――――――――――――――――――――――⌟
    """, 2)))

    Resolution = input(Colorate.Horizontal(Colors.blue_to_green, Center.XCenter('Enter the X value (Exm: 1920x1080): ', 8))).split('x')
    ResX = Resolution[0]
    ResY = Resolution[1]

    new_content = re.sub(r"ResolutionSizeX=\d+", f"ResolutionSizeX={ResX}", content)
    new_content = re.sub(r"ResolutionSizeY=\d+", f"ResolutionSizeY={ResY}", new_content)
    
    with open(DIRECTORY, "w") as file:
        file.write(new_content)
        
    set_read_only(DIRECTORY)

except FileNotFoundError:
    print(f"Error: File '{DIRECTORY}' does not exist.")
except IOError:
    print("Error: A problem occurred while reading or writing the file.")
except ValueError:
    print("Error: Please enter valid integer values for the resolutions.")
except Exception:
    print("Error: Remember to put the 'x' between the two numbers, without spaces")

