# Getting started  <!-- TODO: Delete this section when everything is done. -->

1. Update fields in [`pyproject.toml`](pyproject.toml): replace or remove dummy data, choose a build backend, etc.
2. Replace all placeholders (e.g. `<your_source>`, etc.) in all files and directory names.
3. Describe your plugin [below](#hermes-harvest-plugin-for-your_source).
4. License your plugin: we recommend following the [REUSE specifications](https://reuse.software/tutorial/) and use of the [`reuse` tool](https://reuse.readthedocs.io/en/stable/).
5. Delete this section and start implementing.
6. When release-ready, [add your plugin](https://github.com/softwarepub/hermes/issues/new?template=add-plugin-to-marketplace.yml) to the [HERMES Marketplace](https://hermes.software-metadata.pub/en/latest/#plugins).

# Hermes harvest plugin for <your_source>  <!-- TODO: Replace placeholder -->

This plugin enables the harvesting of metadata stored in <your_source>.  <!-- TODO: Replace placeholder -->

## Related

- The Github [repository of the `hermes`](https://github.com/hermes-hmc/hermes) project

## Run Locally

Clone this project, go to the project directory and install this project:

```bash
  git clone link_to_your_repository
  cd your_folder
  
  # Recommended: Create a virtual environment to install into
  pip install .
```

Go to the project folder you want to harvest:

```bash
  cd your_project_to_harvest
```

Make sure that you have a file named `hermes.toml` in your project with the following content:

  <!-- TODO: Replace placeholder "your_source" in following code snippet -->
```toml
  [harvest]
  sources = ["hermes_plugin_your_source"]
```

Run the `harvest` command:

```bash
  hermes harvest
```

The harvested metadata from <your_source> is stored in the local cache at `.hermes/harvest/`.  <!-- TODO: Replace placeholder -->

![HERMES logo](https://software-metadata.pub/hermes-logo.png)
