import subprocess
from tabnanny import check


def systemctl_cmd(service):
    try:
        subprocess.run(['wsl','sudo','systemctl','status',service],check=True,text=True)
        print("Success")
    except subprocess.CalledProcessError:
        print('Failed')

name = input("Enter Service name: ")
systemctl_cmd(name)
