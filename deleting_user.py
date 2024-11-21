import subprocess

def delete_user(username):
    try:
        subprocess.run(['wsl','sudo','userdel',username],check=True,capture_output=True,text=True)
        print(f"{username} deleted successfully")
    except subprocess.CalledProcessError:
        print(f"{username} failed to delete.")
  #  except subprocess.TimeoutExpired:
   #     print("Process timed out")
username = input("Enter Username to delete")
delete_user(username)