import subprocess

def tail_command(file_path):
    try:
        result = subprocess.run(['wsl','tail','-1',file_path],check=True,text=True,capture_output=True)
        print("Success")
        print(result.stdout)
    except subprocess.CalledProcessError:
       print('Failed')

file_path = input("Enter fileName: ")  # /home/siddu/p1
tail_command(file_path)
