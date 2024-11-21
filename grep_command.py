import subprocess

def grep_cmd(dir,file):
    try:
        result = subprocess.run(['wsl','ls','-ltr',dir,'|','grep','-i',file],check=True,text=True,capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(e.stderr)

dir = input('Enter directory: ')
file = input('Enter file name: ')
grep_cmd(dir,file)