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
    print('Read Only is off')
    
    with open(DIRECTORY, 'r') as file:
        content = file.read()


    print(""" 
$$\   $$\ $$\     $$\ $$$$$$$\   $$$$$$\          $$$$$$$\  
$$ |  $$ |\$$\   $$  |$$  __$$\ $$  __$$\         $$  __$$\ 
$$ |  $$ | \$$\ $$  / $$ |  $$ |$$ /  $$ |        $$ |  $$ |
$$$$$$$$ |  \$$$$  /  $$$$$$$  |$$ |  $$ |$$$$$$\ $$$$$$$  |
$$  __$$ |   \$$  /   $$  __$$< $$ |  $$ |\______|$$  ____/ 
$$ |  $$ |    $$ |    $$ |  $$ |$$ |  $$ |        $$ |      
$$ |  $$ |    $$ |    $$ |  $$ | $$$$$$  |        $$ |      
\__|  \__|    \__|    \__|  \__| \______/         \__|      
                                                            
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
    print('Read-Only is on')

except FileNotFoundError:
    print(f"Error: File '{DIRECTORY}' does not exist.")
except IOError:
    print("Error: A problem occurred while reading or writing the file.")
except ValueError:
    print("Error: Please enter valid integer values for the resolutions.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

