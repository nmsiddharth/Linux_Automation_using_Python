import subprocess


def add_group(group):
    try:
        subprocess.run(['wsl','sudo','groupadd',group],check=True,text=True)
        print(f"created {group}")
    except subprocess.CalledProcessError:
        print(f"Failed to add {group}.")

group = input("Enter group: ")
add_group(group)
