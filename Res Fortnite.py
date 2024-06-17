import os

Directory = "C:/Users/ilros/AppData/Local/FortniteGame/Saved/Config/WindowsClient/GameUserSettings.ini"
try:
    def remove_read_only(Directory):
        permissions = os.stat(Directory).st_mode
        os.chmod(Directory, permissions | 0o200)

    def set_read_only(Directory):
        permissions = os.stat(Directory).st_mode
        os.chmod(Directory, permissions & ~0o200)

    remove_read_only(Directory)
    print('Read Only is off')
    
    with open(Directory, 'r') as file:
        content = file.read()

    OldResX = int(input('Enter the X value you want to change: '))
    OldResY = int(input('Enter the Y value you want to change: '))
    NewResX = int(input('Enter the new X value: '))
    NewResY = int(input('Enter the new Y value: '))

    new_contentX = content.replace(f"ResolutionSizeX={OldResX}", f"ResolutionSizeX={NewResX}")
    new_contentY = content.replace(f"ResolutionSizeY={OldResY}", f"ResolutionSizeY={NewResY}")
    
    
    with open(Directory, "w") as file:
        file.write(new_contentX)
        file.write(new_contentY)

    set_read_only(Directory)
    print('Read-Only is on')

except FileNotFoundError:
    print(f"Error: File '{Directory}' does not exist.")
except IOError:
    print("Error: A problem occurred while reading or writing the file.")
