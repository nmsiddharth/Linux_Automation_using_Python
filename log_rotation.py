import subprocess

def rotate_log():
    try:
        subprocess.run(['wsl','sudo','logrotate','/etc/logrotate.conf'],check=True,text=True)
        print("Log rotation triggered successfully.")
    except subprocess.CalledProcessError:
        print("Failed to trigger log rotation.")

rotate_log()