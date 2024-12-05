import subprocess

def create_directory(dirName):
   try:
        subprocess.run(['wsl','mkdir',dirName],check=True,capture_output=True,text=True)
        print(f"{dirName} created successfully")
   except subprocess.CalledProcessError:
       print(f"{dirName} failed to create")

dirName = input("Enter Directory Name: ")
create_directory(dirName)