import subprocess

def change_owner(owner,file_name):
    try:
        subprocess.run(['wsl','sudo','chown',owner,file_name],check=True,text=True)
        print(f"Ownership changed for {file_name} to {owner}.")
    except subprocess.CalledProcessError as e:
        print(f"Error changing file ownership: {e}")

filename = input("Enter filename: ")
owner = input("Enter new owner: ")
change_owner(owner,filename)

