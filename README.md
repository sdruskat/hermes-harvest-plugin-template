# Getting started

- Replace all placeholders (e.g. your_source, your_plugin) in all files and directory names.
- Fill in all fields of the pyproject.toml (replace or remove the dummy data)
- Describe your plugin in this file (down below)
- Add licenses if desired
- Now you are good to go, delete this section and start implementing.

# Hermes harvest plugin for your_source
This plugin enables the harvesting of metadata stored in your_source.

## Authors

- [@your_github_username](https://www.github.com/your_github_username)

## Related

[The Github repository](https://github.com/hermes-hmc/hermes) of the hermes project

[The Github repository](https://github.com/hermes-hmc/hermes-git) of the hermes harvest plugin for git

[The Github repository](https://github.com/hermes-hmc/hermes-plugin-python) of the hermes harvest plugin for python projects

## Run Locally

Install hermes e.g. using pip

```bash
  pip install hermes
```

<ins>**or**</ins> clone the Hermes project, go to the project directory and make a python package out of it

```bash
  git clone https://github.com/hermes-hmc/hermes.git
  cd hermes
  pip install .
```

Clone this project, go to the project directory and make a python package out of it

```bash
  git clone link_to_your_repository
  cd your_folder
  pip install .
```

Go to the project folder you want to harvest

```bash
  cd your_project_to_harvest
```

Controll that you have a file named "hermes.toml" in your project with the following content.
```
  [harvest]
  sources = ["cff", "your_plugin"]

  [deposit.invenio_rdm]
  site_url = "https://sandbox.zenodo.org"
  access_right = "open"
```

Run harvest command

```bash
  hermes harvest
```

![Logo](https://docs.software-metadata.pub/en/latest/_static/hermes-visual-blue.svg)

