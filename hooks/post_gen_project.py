import os
import subprocess

MESSAGE_COLOR = "\x1b[34m"
SUCCESS_COLOR = "\x1b[32m"
RESET_ALL = "\x1b[0m"

def create_repo(title):
  print(f"{MESSAGE_COLOR}Almost done!")
  print(f"Initializing a git repository...{RESET_ALL}")

  subprocess.call(['git', 'init'])
  subprocess.call(['git', 'add', '*'])
  subprocess.call(['git', 'commit', '-m', f'Initial commit for {title} project'])

  print(f"{SUCCESS_COLOR} Git repository has been created successfully {RESET_ALL}")

def create_conda_env():
  if os.path.isfile("environment.yml"):
    print("Creating conda environment from environment.yml")
    subprocess.call(["conda", "env","create", "--file=environment.yml"])

    print(f"{SUCCESS_COLOR} Conda env been created successfully {RESET_ALL}")
  else:
    print(f"{MESSAGE_COLOR}environment.yml not found. Please ensure the file exists in the project directory.{RESET_ALL}")
  pass                                       

def main():
  title = "{{ cookiecutter.title }}"
  create_repo(title)

  print("Do you want to create a Conda env using environment.yml file? (y/n)")
  choice = input("Enter y or n: ").strip().lower()

  if(choice == "y"):
    create_conda_env()
  elif(choice == "n"):
    pass
  else:
    print(f"{MESSAGE_COLOR}Invalid choice, please run the script again and choose y or n{RESET_ALL}")


if __name__ == "__main__":
  main()