# {{ cookiecutter.title }}

**Version**: {{ cookiecutter.version }}
{% if cookiecutter.author != "" -%}
**Author**: {{ cookiecutter.author }}
{% endif %}

{{ cookiecutter.description }}

## Prerequisites
- Anaconda >=4.x 

## Create environment
```bash
conda env create -f environment environment.yml
activate {{ cookiecutter.name }}
```

## Project organisation
```

## Project organization

    {{ cookiecutter.name }}
        ├── data
        │   ├── processed      <- The final, canonical data sets for modeling.
        │   └── raw            <- The original, immutable data dump.
        │
        ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
        │                         the creator's initials, and a short `-` delimited description, e.g.
        │                         `1.0-jvelezmagic-initial-data-exploration`.
        │
        ├── .gitignore         <- Files to ignore by `git`.
        │
        ├── environment.yml    <- The requirements file for reproducing the analysis environment.
        │
        └── README.md          <- The top-level README for developers using this project.

---