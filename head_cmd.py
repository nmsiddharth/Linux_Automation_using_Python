import subprocess

def head_command(file_path):
    try:
        result = subprocess.run(['wsl','head','-1',file_path],check=True,text=True,capture_output=True)
        print("Success")
        print(result.stdout)
    except subprocess.CalledProcessError:
       print('Failed')

file_path = input("Enter fileName: ")
head_command(file_path)
