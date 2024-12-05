import subprocess

def create_file(fileName):
    try:
        subprocess.run(['wsl','touch',fileName],
                       check=True,
                       capture_output=True,
                       text=True)

        print(f"{fileName} created successfully")
    except subprocess.CalledProcessError:
        print(f"{fileName} failed to create")

fileName = input("Enter Filename: ")
create_file(fileName)
