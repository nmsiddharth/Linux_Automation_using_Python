import subprocess

def change_permisssions(permissions,file_name):
    try:
        subprocess.run(['wsl','sudo','chmod',permissions,file_name],check=True,text=True)
        print(f"Permissions changed for {file_name}.")
    except subprocess.CalledProcessError as e:
        print(f"Error changing file permissions: {e}")

filename = input("Enter filename: ")
permissions = input("Enter new permission: ")
change_permisssions(permissions,filename)

