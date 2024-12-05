import subprocess


def delete_file(file):
    try:
        subprocess.run(['wsl','rm',file],check=True,text=True)
        print(f"{file} removed successfully")
    except subprocess.CalledProcessError:
        print(f"{file} failed to remove")

file = input('Enter File name: ')
delete_file(file)