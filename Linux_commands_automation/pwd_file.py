import subprocess
from tabnanny import check


def get_pwd():
        subprocess.run(['wsl','pwd'],text=True)
        print("success")

get_pwd()

# Current working Directory in Linux :
#  /mnt/d/SIDDU/Technical/Python/Python_Pycharm/Python_Automation

# If we directly type filename ,when creating a file or directory, it stores in above location