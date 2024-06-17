import os
import re

Directory = "C:/Users/ilros/AppData/Local/FortniteGame/Saved/Config/WindowsClient/GameUserSettings.ini"

def remove_read_only(file_path):
    permissions = os.stat(file_path).st_mode
    os.chmod(file_path, permissions | 0o200)

def set_read_only(file_path):
    permissions = os.stat(file_path).st_mode
    os.chmod(file_path, permissions & ~0o200)

try:
    remove_read_only(Directory)
    print('Read Only is off')
    
    with open(Directory, 'r') as file:
        content = file.read()

    NewResX = int(input('Enter the X value (1920): '))
    NewResY = int(input('Enter the Y value (1080): '))


    new_contentX = re.sub(r"ResolutionSizeX=\d+", f"ResolutionSizeX={NewResX}", content)
    new_contentY = re.sub(r"ResolutionSizeY=\d+", f"ResolutionSizeY={NewResY}", content)
    
    
    with open(Directory, "w") as file:
        file.write(new_contentX)
        file.write(new_contentY)
        

    set_read_only(Directory)
    print('Read-Only is on')

except FileNotFoundError:
    print(f"Error: File '{Directory}' does not exist.")
except IOError:
    print("Error: A problem occurred while reading or writing the file.")
except ValueError:
    print("Error: Please enter valid integer values for the resolutions.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
