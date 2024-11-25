import subprocess

def cat_command(file_path):
    try:
        result = subprocess.run(['wsl','cat',file_path],check=True,text=True)
        print("Success")
    except subprocess.CalledProcessError:
       print('Failed')

file_path = input("Enter fileName: ")
cat_command(file_path)
