import sys
import os
import re

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

def name_validator(name):
  return re.match(r"[a-z0-9_]+$", name) is not None

if __name__ == "__main__":
  project_name = "{{ cookiecutter.name }}"
  
  if not name_validator(project_name):
    print(f"{ERROR_COLOR}ERROR: {project_name} is not a valid name for this template.{RESET_ALL}")
    sys.exit(1)

  print(f"{MESSAGE_COLOR} Creating data science project at { os.getcwd() }{RESET_ALL}")
