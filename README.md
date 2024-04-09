# Tamplate for data science projects
Project structure for doing and sharing data science work or personal projects.

## Requirements 
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html), it can be installed with pip or conda depending how you manage your python packages.

```bash
pip install cookiecutter
```
or
```bash
conda install -c conda-forge cookiecutter
```

## Create a new project
```bash
cookiecutter https://github.com/pahoalapizco/data-science-template
```

## Set up project's module
To move beyond notebook prototyping, all reusable code should go into the {{ module_name }}/ folder package. To use that package inside your project, install the project's module in editable mode, so you can edit files in the final folder and use the modules inside your notebooks :

```bash
pip install --editable .
```

To use the module inside your notebooks, add `%autoreload` at the top of your notebook :

```python
%load_ext autoreload
%autoreload 2
```

Example of module usage :

```python
from {{ module_name }}.utils.paths import data_dir
data_dir()
```