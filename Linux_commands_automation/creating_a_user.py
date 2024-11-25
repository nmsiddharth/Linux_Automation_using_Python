import subprocess

def create_user(username):
    try:
        result = subprocess.run(
            ['wsl', 'sudo', 'useradd', username],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"User {username} created successfully.")
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

username = input("Enter Username to create: ")
create_user(username)
