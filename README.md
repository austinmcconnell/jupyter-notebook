# Jupyter Notebooks

This repo contains all needed to get jupyter lab running locally with some common data science and plotting packages pre-installed.

## Development Setup

Build and start the container with

```shell
dc up -d
```

Access the notebooks at [http://localhost:8888](http://localhost:8888)

Exec into the service with

```shell
dc exec jupyter /bin/bash
```

## Slides

To set the Slide Type for each cell, first click on the Common Tools gear icon in the top-right

![Common Tools](img/common-tools-icon.png)

Then, set the cell type using to the Slide Type dropdown box

![Slide Type](img/slide-type-box.png)

To preview the slides directly from jupyter lab, click the Slides button

![Slides Button](img/rise-icon.png)

Finally, to export the notebook into a slides presentation, either export directly from jupyter lab

![Export Slides](img/export-as-html-slides.png)

or use the CLI commands below.

### CLI Commands

Run the following command to generate slides including code blocks:

```shell
jupyter nbconvert --to slides presentation.ipynb
```

If you want to serve the presentation immediately after conversion, run

```shell
jupyter nbconvert --to slides presentation.ipynb --post serve
```

IF you want to exclude code blocks from the slides (only see the output of cells), run

```shell
jupyter nbconvert --to slides --no-input presentation.ipynb
```

### Presentation Mode

During a presentation, know the following keyboard shortcuts:

- `Esc` or 'O": Slide overview
- `S`: Speaker notes view
- `?`: See all keyboard shortcuts
