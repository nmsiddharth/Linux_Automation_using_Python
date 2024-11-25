import subprocess


def passwd_user(username):
    try:
        subprocess.run(['wsl','sudo','passwd',username],check=True,text=True)
        print(f"Password added to {username}")
    except subprocess.CalledProcessError:
        print(f"Password adding failed to {username}")

username = input('Enter username: ')
passwd_user(username)

