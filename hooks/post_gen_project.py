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
  subprocess.call(['git', 'commit', '-m', 'Initial commit for {title} project'])

  print(f"{SUCCESS_COLOR} Git repository has been created successfully {RESET_ALL}")
                                           

if __name__ == "__main__":
  title = "{{ cookiecutter.title }}"
  create_repo(title)