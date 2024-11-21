import subprocess


def delete_directory(dirName):
    try:
        subprocess.run(['wsl','rmdir',dirName],check=True,text=True)
        print(f"{dirName} removed successfully")
    except subprocess.CalledProcessError:
        print(f"{dirName} failed to remove")

dirName = input('Enter Directory name: ')
delete_directory(dirName)