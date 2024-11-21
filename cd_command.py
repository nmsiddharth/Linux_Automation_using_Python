import subprocess

def cd_cmd(file):
    try:
        subprocess.run(['wsl','--exec','cd',file],check=True,text=True)
        print("Directory change successfully")

    except subprocess.CalledProcessError:
        print("Directory change failed")

file = input("Enter file path: ")
cd_cmd(file)
