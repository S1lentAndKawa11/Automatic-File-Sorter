import os
import shutil


def sortFiles(targetFldr):
    target_folder = targetFldr
    extensions = {item.split('.')[-1] for item in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, item))}
    print(extensions)

    for extension in extensions:
        if not os.path.exists(os.path.join(target_folder, extension)):
            os.mkdir(os.path.join(target_folder, extension))

    for item in os.listdir(target_folder):
        if os.path.isfile(os.path.join(target_folder, item)):
            file_extension = item.split('.')[-1]
            shutil.move(os.path.join(target_folder, item), os.path.join(target_folder, file_extension, item))

    print("Files have been sorted successfully!")
    menu()

def menu():

    banner = """
    
    db    8    8 88888 .d88b. 8b   d8    db    88888 888 .d88b
  dPYb   8    8   8   8P  Y8 8YbmdP8   dPYb     8    8  8P   
 dPwwYb  8b..d8   8   8b  d8 8  "  8  dPwwYb    8    8  8b   
dP    Yb `Y88P'   8   `Y88P' 8     8 dP    Yb   8   888 `Y88P
                                                             
.d88b. .d88b. 888b. 88888 8888 888b.                         
YPwww. 8P  Y8 8  .8   8   8www 8  .8                         
    d8 8b  d8 8wwK'   8   8    8wwK'                         
`Y88P' `Y88P' 8  Yb   8   8888 8  Yb                                         
    """

# banner = """

    print(banner)
    print("\n\n")
    print("V1.0 by ADITYA")
    print("\n\n")
    print("Press [1] to sort files")
    print("Press [2] to exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        targetFldr = input("Enter the folder path to sort files: ")
        sortFiles(targetFldr)
    else:
        exit()


menu()

