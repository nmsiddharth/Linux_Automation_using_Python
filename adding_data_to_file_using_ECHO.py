import subprocess

def echo_cmd(data,file_path):
    try:
        subprocess.run(['wsl','echo',data,'>>',file_path],check=True,text=True)
        print("Data added successfully.")
    except:
        print("Data adding failed.")

data = input("Enter data: ")
file_path = input("Enter fileName: ")

echo_cmd(data,file_path)
