import subprocess


def dlt_group(group):
    try:
        subprocess.run(['wsl','sudo','groupdel',group],check=True,text=True)
        print(f"deleted {group}")
    except subprocess.CalledProcessError:
        print(f"Failed to delete {group}.")

group = input("Enter group: ")
dlt_group(group)