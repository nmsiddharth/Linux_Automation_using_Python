import subprocess


def add_group_to_user(userName,group):
    try:
        subprocess.run(['wsl','sudo','usermod','-aG',group,userName],check=True,text=True)
        print(f"{userName} added to {group}")
    except subprocess.CalledProcessError:
        print(f"Failed to add {userName} to {group}.")


userName = input("Enter username: ")
group = input("Enter group: ")
add_group_to_user(userName,group)