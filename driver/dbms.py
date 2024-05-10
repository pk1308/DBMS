from git import Repo

import os
from pathlib import Path
import yaml
import sys
from loguru import logger


logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")

def get_git_status_files(repo_path):
  """
  This function takes the path to a Git repository and returns a list of files 
  with their paths based on the git status.

  Args:
      repo_path (str): Path to the Git repository.

  Returns:
      list: List of strings representing file paths.
  """
  
  # Open the Git repository
  repo = Repo(repo_path)

  # Initialize an empty list to store file paths
  files = []

  # Get modified and staged files
  for item in repo.index.diff(None):
    files.append(item.a_path)

  # Get untracked files
  files.extend(repo.untracked_files)

  # Return the list of files
  return files



def read_yaml_as_dict(path_to_yaml: Path):
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return content
    except Exception as e:
        raise e


def write_yaml(file_path: Path, data: dict = None):
    """ write yaml file from dict

    Args:
        file_path (Path):  file path with file name 
        data (dict, optional): Data to save as yaml

    Raises:
        App_Exception: _description_
    """

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as yaml_file:
            if data is not None:
                yaml.dump(data, yaml_file)
    except Exception as e:
        raise e


def update_mydocs(folder_path="./docs"):
    """_summary_

    Args:
        folder_path (str, optional): _description_. Defaults to "./docs".
    """
    yaml_file = read_yaml_as_dict(Path("mkdocs.yml"))
    markdown_files = []
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".md"):
                full_path = os.path.join(root, filename)
                directory_name = "/".join(full_path.split("/")[2:])
                markdown_files.append(directory_name)

    nav_value = {"Home": []}
    for file in markdown_files:
        split_value = file.split("/")
        if len(split_value) == 1:
            nav_value["Home"].append(file)
        else:
            key = split_value[0]
            if key not in nav_value.keys():
                nav_value[key] = [file]
            else:
                nav_value[key].append(file)
                
    yaml_file['nav'] = [{key:value}for key , value in nav_value.items()]

    file_path = Path(os.path.join(os.getcwd(), "mkdocs.yml"))
    write_yaml(file_path, yaml_file)
    

def create_md(files):
  """
  This function attempts to create Markdown files with information about 
  provided PDF files.

  Args:
      files (list): List of file paths.

  Returns:
      bool: True if successful, False otherwise.
  """
  success = True
  for file_to in files:
    if file_to.endswith(".pdf"):
      new_filename = os.path.splitext(file_to)[0] + ".md"
      try:
        with open(new_filename, "w+") as f:
          f.write(f"# {os.path.basename(file_to)} (PDF file)\n")
          path_= os.path.basename("docs/week2/Lecture 2.4 - Introduction to SQL2_annotated.pdf")
          data = f"![Alt text](<./{path_}>)"+'{ type=application/pdf style="min-height:100vh;width:100%" }'
          f.write(data)
        
      except Exception as e:
        print(f"Error creating {new_filename}: {e}")
        success = False
    else:
      print(f"{file_to} is not a PDF file.")
  return success


if __name__ == "__main__":
    
    repo_path = "."  # Replace with your actual Git repository path

    files = get_git_status_files(repo_path)
    
    status = create_md(files=files)
    if status:
        files = get_git_status_files(repo_path)
        update_mydocs(files)
    
    else:
        raise "error"
    
