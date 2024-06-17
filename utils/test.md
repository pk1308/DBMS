```python
import json
import os
import sys
from pathlib import Path
from typing import Any
import yaml
from ensure import ensure_annotations
from loguru import logger
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")


@ensure_annotations
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



@ensure_annotations
def write_yaml(file_path: Path, data: dict = None):
    """ write yaml file from dic

    Args:
        file_path (Path):  file path with file name 
        data (dict, optional): Data to same as yaml

    Raises:
        App_Exception: _description_
    """

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as yaml_file:
            if data is not None:
                yaml.dump(data, yaml_file , default_flow_style=False, sort_keys=False)
    except Exception as e:
        raise  e
    
import subprocess
import os

def convert_ipynb_to_markdown(folder_path):
  """Converts all Jupyter notebooks in a folder to markdown files.

  Args:
    folder_path: The path to the directory containing the notebooks.
  """
  for root, dirs, files in os.walk(folder_path):
    for filename in files:
      if filename.endswith(".ipynb"):
        full_path = os.path.join(root, filename)
        # Check for nbconvert existence before running command
        try:
          subprocess.run(["jupyter", "nbconvert", "--to", "markdown", full_path], check=True)
          print(f"Converted {filename} to markdown successfully.")
        except subprocess.CalledProcessError:
          print(f"Error converting {filename}. nbconvert might not be installed.")

```

```python
import os
from pathlib import Path

def create_navigation_from_markdown(folder_path="./docs", mkdocs_config_file="mkdocs.yml"):
  """
  Generates a navigation menu for MkDocs based on the structure of Markdown files.

  Args:
      folder_path (str, optional): Path to the directory containing Markdown files. Defaults to "./docs".
      mkdocs_config_file (str, optional): Path to the MkDocs configuration file. Defaults to "mkdocs.yml".

  Returns:
      dict: The generated navigation structure dictionary in MkDocs format.

  Raises:
      FileNotFoundError: If the MkDocs configuration file is not found.
  """
  markdown_files = []
  for root, dirs, files in os.walk(folder_path):
      for filename in files:
          if filename.endswith(".md"):
              full_path = os.path.join(root, filename)
              directory_name = Path("/".join(full_path.split("/")[2:]))
              markdown_files.append(directory_name)

  nav_value = {"Home": []}
  for file in markdown_files:
      split_value = str(file).split("/")
      if len(split_value) == 1:
          nav_value["Home"].append(str(file))
      else:
          key = split_value[0]
          if key not in nav_value.keys():
              nav_value[key] = [str(file)]
          else:
              nav_value[key].append(str(file))

  return {"nav": [{"name": key, "children": value} for key, value in nav_value.items()]}

def update_mkdocs_config(navigation_data, mkdocs_config_file="mkdocs.yml"):
  """
  Updates the navigation section in an MkDocs configuration file.

  Args:
      navigation_data (dict): The navigation structure dictionary in MkDocs format.
      mkdocs_config_file (str, optional): Path to the MkDocs configuration file. Defaults to "mkdocs.yml".

  Raises:
      FileNotFoundError: If the MkDocs configuration file is not found.
  """
  file_path = Path(os.path.join(os.getcwd(), mkdocs_config_file))
  # Assuming you have a function to read and write YAML files (e.g., from previous code)
  try:
      yaml_data = read_yaml_as_dict(file_path)
      yaml_data.update(navigation_data)
      write_yaml(file_path, yaml_data)
  except FileNotFoundError:
      raise FileNotFoundError(f"MkDocs configuration file not found: {file_path}")

if __name__ == "__main__":
    convert_ipynb_to_markdown(folder_path = "./docs")
    navigation_data = create_navigation_from_markdown()
    update_mkdocs_config(navigation_data)
    print("Navigation menu for MkDocs created and potentially updated in mkdocs.yml")
    subprocess.run("")

```

```python
os.chdir("..")
```

```python
yaml_file = read_yaml_as_dict(Path("mkdocs.yml" ))
```

```
[32m2024-05-13 21:22:03.717[0m | [1mINFO    [0m | [36m__main__[0m:[36mread_yaml_as_dict[0m:[36m29[0m - [1myaml file: mkdocs.yml loaded successfully[0m


[32m2024-05-13T21:22:03.717706+0400[0m [1myaml file: mkdocs.yml loaded successfully[0m
```

```python
yaml_file['nav']
```

```
[{'name': 'Home', 'children': ['cheatsheet.md', 'index.md']},
 {'name': 'week3',
  'children': ['week3/Lecture 3.1 - SQL Examples_annotated.md',
   'week3/Lecture 3.2 - Intermediate SQL1_annotated.md']},
 {'name': 'week1',
  'children': ['week1/textbook.md',
   'week1/check_list.md',
   'week1/summary.md']},
 {'name': 'week2',
  'children': ['week2/Lecture 2.2 - Introduction to Relational Model2_annotated.md',
   'week2/Lecture 2.5 - Introduction to SQL3_annotated.md',
   'week2/Lecture 2.4 - Introduction to SQL2_annotated.md',
   'week2/Lecture 2.3 - Introduction to SQL1_annotated.md',
   'week2/tutorial_2.1.md',
   'week2/check_list.md',
   'week2/Lecture 2.1 - Introduction to Relational Model1_annotated.md']}]
```

```python
[{key: value} for key , value in nav_value.items()]
```

```python

```

```python
folder_path = "./docs"
markdown_files = []
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith(".md"):
            full_path = os.path.join(root, filename)
            directory_name = Path("/".join(full_path.split("/")[2:]))
            markdown_files.append(directory_name)

nav_value = {"Home" : []}
for file in markdown_files:
    split_value = str(file).split("/")
    if len(split_value)==1:
        nav_value["Home"].append(str(file))
    else:
        key = split_value[0]
        if key not in nav_value.keys():
            nav_value[key] = [str(file)]
        else:
            nav_value[key].append(str(file))
to_update = [{key: value} for key , value in nav_value.items()]
yaml_file['nav'] = to_update
file_path = Path(os.path.join(os.getcwd(), "mkdocs.yml"))
write_yaml(file_path, yaml_file)
```

```python
to_update
```

```python
yaml_file['nav'] = to_update
```

```python
file_path = Path(os.path.join(os.getcwd(), "mkdocs.yml"))
```

```python
write_yaml(file_path, yaml_file)
```

```python
import subprocess
import os

def convert_ipynb_to_markdown(folder_path):
  """Converts all Jupyter notebooks in a folder to markdown files.

  Args:
    folder_path: The path to the directory containing the notebooks.
  """
  for root, dirs, files in os.walk(folder_path):
    for filename in files:
      if filename.endswith(".ipynb"):
        full_path = os.path.join(root, filename)
        # Check for nbconvert existence before running command
        try:
          subprocess.run(["jupyter", "nbconvert", "--to", "markdown", full_path], check=True)
          print(f"Converted {filename} to markdown successfully.")
        except subprocess.CalledProcessError:
          print(f"Error converting {filename}. nbconvert might not be installed.")

# Specify the folder path for conversion
folder_path = "./docs"
convert_ipynb_to_markdown(folder_path)

```

```python
os.chdir("..")
```

```python
import os 

os.path.splitext("docs/week2/Lecture 2.4 - Introduction to SQL2_annotated.pdf")[0]
```

```python
path_= os.path.basename("docs/week2/Lecture 2.4 - Introduction to SQL2_annotated.pdf")
data = f"![Alt text](<./{path_}>)"+'{ type=application/pdf style="min-height:100vh;width:100%" }'
```

```python
data = f"![Alt text](<./{path_}>)"+'{ type=application/pdf style="min-height:100vh;width:100%" }'
```

```python
data
```

```python
from collections import OrderedDict
```

```python
@ensure_annotations
def write_yaml(file_path: Path, data: dict):
    """Writes data to a YAML file, preserving key order.

    Args:
        file_path (Path): Path object representing the path to the YAML file.
        data (dict): The data to be serialized as YAML.

    Raises:
        ValueError: If the data is not a dictionary.
        IOError: If there's an error writing to the file.
    """

    if not isinstance(data, dict):
        raise ValueError("Data must be a dictionary")

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as yaml_file:
            import ruamel.yaml  # Import the ruamel.yaml module

            yaml = ruamel.yaml.YAML(typ='safe')  # Use safe loader for security
            yaml.dump(data, yaml_file)
    except OSError as e:
        raise IOError(f"Error writing YAML file: {file_path}") from e

```

```python

```
