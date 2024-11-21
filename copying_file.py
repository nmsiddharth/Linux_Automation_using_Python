import subprocess

def copy_file(source_file,destination_file):
    try:
        subprocess.run(['wsl','cp',source_file,destination_file],check=True,text=True)
        print("Copied successfully")
    except subprocess.CalledProcessError:
        print("Copied failed")

source_file = input("Enter source file path: ")
destination_file = input("Enter Destination file path: ")

copy_file(source_file,destination_file)