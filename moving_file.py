import subprocess

def copy_file(src_file,dest_file):
    try:
        subprocess.run(['wsl','mv',src_file,dest_file],check=True,text=True)
        print("Moved successfully")
    except subprocess.CalledProcessError:
        print("Moved failed")

src_file = input("Enter source file path: ")
dest_file = input("Enter Destination file path: ")

copy_file(src_file,dest_file)