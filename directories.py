import os

def create_dir(dir_name):
    os.mkdir(dir_name)
    print(f"Directory '{dir_name}' created.")

def change_dir(dir_name):
    os.chdir(dir_name)
    print(f"Current directory changed to: {os.getcwd()}")

def list_dir():
    print(os.listdir())

def remove_dir(dir_name):
    os.rmdir(dir_name)
    print(f"Directory '{dir_name}' removed.")

def get_cwd():
    print(os.getcwd())

# Example usage
create_dir("my_dir")
change_dir("my_dir")
list_dir()
get_cwd()
