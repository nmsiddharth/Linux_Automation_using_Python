import subprocess

def ip_addr():
    result = subprocess.run(['wsl','ip','addr'],text=True,capture_output=True)
    print(result.stdout)

ip_addr()
