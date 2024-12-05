import subprocess

def chage_command(username):
    try:
        subprocess.run(['wsl','sudo','chage','-m','3','-M','10','-d','15','-W','3',username],check=True,text=True)
        print('success')
    except subprocess.CalledProcessError:
        print('failed')

user = input('Enter user Name: ')
chage_command(user)


# To verify in terminal : chage -l username