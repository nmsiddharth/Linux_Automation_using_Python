import subprocess

def ls_cmd():
    try:
        result = subprocess.run(['wsl','ls','-l'],check=True,text=True)
        print('listed successfully')
        #print(result.stdout)  # used to print output( ls -l )
    except subprocess.CalledProcessError as e:
        print('listing failed')
        print(e.stderr)


ls_cmd()