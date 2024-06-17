import os
import re

DIRECTORY = "C:/Users/ilros/AppData/Local/FortniteGame/Saved/Config/WindowsClient/GameUserSettings.ini"

def remove_read_only(file_path):
    permissions = os.stat(file_path).st_mode
    os.chmod(file_path, permissions | 0o200)

def set_read_only(file_path):
    permissions = os.stat(file_path).st_mode
    os.chmod(file_path, permissions & ~0o200)

try:
    remove_read_only(DIRECTORY)
    
    with open(DIRECTORY, 'r') as file:
        content = file.read()


    print(""" 
    $$$$$$$\                               $$$$$$\  $$\                                                                 $$$$$$$$\        
    $$  __$$\                             $$  __$$\ $$ |                                                                $$  _____|       
    $$ |  $$ | $$$$$$\   $$$$$$$\         $$ /  \__|$$$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\          $$ |   $$$$$$$\  
    $$$$$$$  |$$  __$$\ $$  _____|$$$$$$\ $$ |      $$  __$$\  \____$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$$$$$\ $$$$$\ $$  __$$\ 
    $$  __$$< $$$$$$$$ |\$$$$$$\  \______|$$ |      $$ |  $$ | $$$$$$$ |$$ |  $$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|\______|$$  __|$$ |  $$ |
    $$ |  $$ |$$   ____| \____$$\         $$ |  $$\ $$ |  $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |              $$ |   $$ |  $$ |
    $$ |  $$ |\$$$$$$$\ $$$$$$$  |        \$$$$$$  |$$ |  $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |\$$$$$$$\ $$ |              $$ |   $$ |  $$ |
    \__|  \__| \_______|\_______/          \______/ \__|  \__| \_______|\__|  \__| \____$$ | \_______|\__|              \__|   \__|  \__|
                                                                                $$\   $$ |                                             
                                                                                \$$$$$$  |                                             
                                                                                \______/                                                  
                                                                
    ⌜―――――――――――――――――――――――――――――――――――――――――――――――――――――⌝
    ┇      [Github]  https://github.com/HyRo-P             ┇
    ┇      [Telegram] @Hyro_99                             ┇
    ⌞―――――――――――――――――――――――――――――――――――――――――――――――――――――⌟
          
          
          """)

    Resolution = input('Enter the X value (Exm: 1920x1080): ').split('x')
    ResX = Resolution[0]
    ResY = Resolution[1]

    new_contentX = re.sub(r"ResolutionSizeX=\d+", f"ResolutionSizeX={ResX}", content)
    new_contentY = re.sub(r"ResolutionSizeY=\d+", f"ResolutionSizeY={ResY}", content)
    
    
    with open(DIRECTORY, "w") as file:
        file.write(new_contentX)
        file.write(new_contentY)
        

    set_read_only(DIRECTORY)
    
    

except FileNotFoundError:
    print(f"Error: File '{DIRECTORY}' does not exist.")
except IOError:
    print("Error: A problem occurred while reading or writing the file.")
except ValueError:
    print("Error: Please enter valid integer values for the resolutions.")
except Exception:
    print("Error, remember to put the 'x' between the two numbers, without spaces")

