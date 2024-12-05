import subprocess

def change_grpowner(owner,file_name):
    try:
        subprocess.run(['wsl','sudo','chgrp',owner,file_name],check=True,text=True)
        print(f"Group ownership changed for {file_name} to {owner}.")
    except subprocess.CalledProcessError as e:
        print(f"Error changing file group ownership: {e}")

filename = input("Enter filename: ")
owner = input("Enter new owner: ")
change_grpowner(owner,filename)

