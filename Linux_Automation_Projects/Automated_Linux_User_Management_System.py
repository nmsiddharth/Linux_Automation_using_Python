import os
import subprocess
import logging
from datetime import datetime


# clear the log file before the program starts
def clear_log_file():
    log_file = "user_log_file.log"
    logging.shutdown()   # We need to close the log file before removing or else it will show error
    if os.path.exists(log_file):
        os.remove(log_file)  # deletes existing log_file


# Setting up logging
logging.basicConfig(filename = 'user_log_file.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')



# Helper function to log actions
def log_action(action,username,status,additional_info=""):
    """Log each action taken on user accounts with detailed info."""
    message = f"{action} || USER '{username}' || Status: {status} || {additional_info}"
    logging.info(message)  # Writes to log_file
    print(message) # print to console for immediate feedback

# Helper function to check if a user exist
def user_exists(username):
    try:
        output = subprocess.check_output(['wsl','id','-u',username],stderr=subprocess.DEVNULL)  # DEVNULL is to suppress error message(like, user not found), focusing on exit status(0)).
        return True
    except subprocess.CalledProcessError:
        return False



# Backup user data before any modification or deletion
def backup_user_data(username):
    try:
        # Ensure compatibility with WSL paths
        home_dir = f"/home/{username}"
        # Use subprocess to check for the directory's existence on Linux
        if subprocess.run(['wsl', 'test', '-d', home_dir], check=False).returncode == 0:
            backup_dir = f"/home/{username}_backup_{datetime.now().strftime('%d-%m-%y')}"
            # Perform the backup using Linux commands via WSL
            subprocess.run(['wsl', 'sudo', 'cp', '-r', home_dir, backup_dir], check=True)
            log_action("Backup", username, "Success", f"Backup saved to {backup_dir}")
        else:
            log_action("Backup", username, "Failed", f"Home directory {home_dir} not found.")
    except subprocess.CalledProcessError as e:
        log_action("Backup", username, "Failed", f"Subprocess error: {e}")
    except Exception as e:
        log_action("Backup", username, "Failed", f"Unexpected error: {str(e)}")



# Create a new user (no password handling)
def create_user(username):
    """
    Create a new user with the specified username.
    If the user-specific directory (/home/username) exists, assign the user to it.
    Otherwise, create the directory and assign the user to it.
    """
    if not username.isalnum() or len(username) < 3:
        log_action("Create", username, "Failed", "Invalid username format")
        print("Error: Username must be alphanumeric and at least 3 characters long.")
        return

    home_dir = f"/home/{username}"  # User-specific directory under /home

    if user_exists(username):
        log_action("Create", username, "Failed", "User already exists.")
        print(f"Error: User '{username}' already exists.")
        return

    try:
        if os.path.exists(home_dir):
            # User directory exists; assign it to the user
            subprocess.run(['wsl', 'sudo', 'useradd', '-d', home_dir, username], check=True)
            log_action("Create", username, "Success", f"User assigned to existing directory {home_dir}")
            print(f"User '{username}' assigned to existing directory '{home_dir}'.")
        else:
            # User directory does not exist; create it and assign the user
            subprocess.run(['wsl', 'sudo', 'useradd', '-m', '-d', home_dir, username], check=True)
            log_action("Create", username, "Success", f"User created with new home directory {home_dir}")
            print(f"User '{username}' created with new home directory '{home_dir}'.")
    except subprocess.CalledProcessError as e:
        log_action("Create", username, "Failed", str(e))
        print(f"Failed to create user '{username}': {e}")



# Deleting an existing user with backup confirmation
def delete_user(username):
    if not user_exists(username):  # Check if the user exists
        log_action("Delete", username, "Failed", "User does not exist.")
        print("Error: User does not exist.")
        return

    home_dir = f"/home/{username}"  # User's home directory

    # Check if the home directory exists using subprocess
    directory_exists = subprocess.run(['wsl', 'test', '-d', home_dir], check=False).returncode == 0

    if not directory_exists:  # If home directory doesn't exist, do not allow deletion
        log_action("Delete", username, "Failed", f"Home directory {home_dir} not found. Deletion aborted.")
        print(f"Error: Home directory for user '{username}' not found. Deletion aborted.")
        return

    # Ask the user if they want to back up the data before deletion
    backup_choice = input(f"Do you want to backup data for user '{username}' before deletion? (y or n): ").lower()

    if backup_choice == 'y':
        try:
            # Perform backup without checking the directory again
            backup_user_data(username)
            print(f"Backup for user '{username}' completed successfully.")
        except Exception as e:
            log_action("Delete", username, "Failed", f"Backup failed: {e}")
            print(f"Backup failed for user '{username}'. Deletion aborted.")
            return  # Abort deletion if backup fails
    elif backup_choice != 'n':  # Handle invalid input for backup choice
        print("Invalid input. Please enter 'y' or 'n'.")
        return

    try:
        # Proceed to delete the user after confirming backup
        subprocess.run(['wsl', 'sudo', 'userdel', '-r', username], check=True)
        log_action("Delete", username, "Success", "User deleted successfully.")
        print(f"User '{username}' deleted successfully.")
    except subprocess.CalledProcessError as e:
        log_action("Delete", username, "Failed", str(e))
        print(f"Failed to delete user: {e}")



# Update user info (without password)
def update_user(username,new_username):
    if not user_exists(username):
        log_action("Update", username, "Failed", "User does not exist.")
        print("Error: User does not exist.")
        return

    home_dir = f'/home/{username}'

    try:
        backup_user_data(username) # backup user before updating
        if new_username:
            subprocess.run(['wsl','sudo','usermod','-l',new_username,'-d',home_dir,'-m',username],check=True)
            subprocess.run(['wsl', 'sudo', 'usermod', '-d', f'/home/{new_username}', '-m', new_username], check=True)
            log_action("Update", username, "Success", f"Username changed to {new_username}")
            username = new_username  # Update variable for further changes
            log_action("Update", username, "Success", "User updated.")
    except subprocess.CalledProcessError as e:
            log_action("Update", username, "Failed", str(e))
            print(f"Failed to update user: {e}")



# List all users on the system
def list_users():
    try:
        output = subprocess.check_output(['wsl','cut','-d:','-f1','/etc/passwd']).decode()
        users = output.splitlines()
        print("System Users : ")
        for user in users:
            print(f"-> {user}")
        log_action("List Users","N/A","Success")
    except subprocess.CalledProcessError as e:
        log_action("List Users","N/A","Failed",str(e))
        print(f"Failed to list users: {e}")



# List all groups on the system
def list_groups():
    try:
        output = subprocess.check_output(['wsl','cut','-d:','-f1','/etc/group']).decode()
        groups = output.splitlines()
        print("System groups : ")
        for grp in groups:
            print(f"-> {grp}")
        log_action("List groups","N/A","Success")
    except subprocess.CalledProcessError as e:
        log_action("List groups","N/A","Failed",str(e))
        print(f"Failed to list groups: {e}")



# Creating groups
def add_group(group):
    try:
        subprocess.run(['wsl','sudo','groupadd',group],check=True,text=True)
        log_action("Creating_group",'N/A',"Success",f"{group} group created successfully")
        print(f"created {group}")
    except subprocess.CalledProcessError:
        print(f"Failed to add {group}.")
        log_action("Creating_group",'N/A',"Failed",f"{group} group creation failed")



# Add user to a group
def add_user_to_group(username,groupname):
    if not user_exists(username):
        log_action("Add to group",username,"Failed","User does not exist")
        print(f"Error: User '{username}' does not exist.")
        return

    try:
        subprocess.run(['wsl','sudo','usermod','-aG',groupname,username],check=True)
        log_action("Add to group", username, "Success", f"User added to {groupname}")
    except subprocess.CalledProcessError as e:
        log_action("Add to group",username,"Failed",str(e))
        print(f"Failed to add user to group: {e}")


# Remove user from group
def remove_user_from_group(username,groupname):
    if not user_exists(username):
        log_action("Remove from group",username,"Failed","User does not exist")
        print(f"Error: User '{username}' does not exist.")
        return

    try:
        subprocess.run(['wsl', 'sudo', 'gpasswd', '-d',username,groupname], check=True)
        log_action("Remove from group", username, "Success", f"User removed from {groupname}")
    except subprocess.CalledProcessError as e:
        log_action("Remove from group", username, "Failed", str(e))
        print(f"Failed to remove user from group: {e}")



# Main menu for user management
def main():
    #clear_log_file()   # Clear log file at the start of each run

    while True:
        print("\nUser Management Menu: ")
        print("1. Create User")
        print("2. Delete User")
        print("3. Update User")
        print("4. List Users")
        print("5. Add User to Group")
        print("6. Remove User from Group")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username to create: ")
            create_user(username)

        elif choice == '2':
            username = input("Enter username to delete: ")
            delete_user(username)

        elif choice == '3':
            username = input("Enter username to update: ")
            new_username = input("Enter new username: ")
            update_user(username,new_username)

        elif choice == '4':
            list_users()

        elif choice == '5':
            # Loop for checking if the user wants to create a new group
            while True:
                new_group_choice = input("Do you want to create a new group? (y or n): ").lower()
                if new_group_choice == 'y':
                    groupname = input('Enter groupname to be created: ')
                    add_group(groupname)
                    break
                elif new_group_choice == 'n':
                    list_groups()
                    groupname = input("Enter groupname: ")
                    username = input("Enter username to add to group: ")
                    add_user_to_group(username, groupname)
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
                    continue  # This will keep asking until a valid input is given

            add_user_to_group(username, groupname)

        elif choice == '6':
            username = input("Enter username to remove from group: ")
            groupname = input("Enter groupname: ")
            remove_user_from_group(username,groupname)

        elif choice == '7':
            print("Exiting User Management System")
            print("Thank You!!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    clear_log_file()
    main()


