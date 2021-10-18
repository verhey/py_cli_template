# py_cli_template

## What?

This is a template package to quickly spin up a python CLI library. There are many like it, but this one is mine.

## Why?

### Background

I found myself writing the same boilerplate `setup.cfg`, `setup.py`, `src/`, `tests/` structure over and over.

I also found that if I start a side project, I spend all my time configuring it, and never actually _do_ the side project.

This is an attempt to alleviate some of that bikeshedding, and give myself a clean place to start future projects, while still retaining some of the _good_ things about that bikeshedding, like having a sensible project structure and tests already configured.

Just clone this repo, plug in the right dependencies, change some names, delete most of this readme, and start actually writing the code you meant to write.

### Why not just use [cookiecutter](https://github.com/cookiecutter/cookiecutter)?

To put it simply, _I don't need it_. Cookiecutter is great, and fully featured, but I don't need a lot of the functionality it provides.
If someday I do, I will cut this over to be a cookiecutter project instead.

## Prerequisites

* Python 3.8.0 or higher
* Git

## Structure

```
+-- .github/workflows
|   +-- ci.yml       # github action for pytest/flake8/black
+-- src              # package containing the main app code
|   +-- __init__.py
|   +-- cli.py       # cli entrypoint
+-- tests            # pytest tests
|   +-- test_cli.py  # single test to get started
+-- .editorconfig    # for standardizing editing across OSs
+-- .gitignore
+-- LICENSE
+-- readme.md
+-- sample.env       # sample .env for secrets
+-- setup.cfg        # app config, dependency definition
+-- setup.py         # basic setup.py - use setup.cfg instead
```

## Usage

### Installation

> This is how you install the package present in the template locally. You probably want to keep this section around after you use the template, as it won't change.

* For installing dev dependencies run `pip install -e .[dev]`
  * Note if you're using `zsh` you may need to quote any brackets:
    * `pip install -e ".[dev]"`
  * See `setup.cfg` for what these dependencies are
* Copy the `sample.env` to just `.env` for envvar loading
  `cp sample.env .env`
* There is an initial CLI entrypoint set up in `setup.cfg` to `src.cli.main()`
  * After installation, you can see this by running the `app` command
    * To change the name - see the "Forking and using" section below
* To run tests, you can run `pytest` for the whole test suite or `pytest tests/your_dir` for a specific subset of tests
* Auto-formatting is handled with `black` which can be run with `black .`
* Linting is handled with `flake8` with can be run with `flake8 .`
  * Custom flake8 config is in `setup.cfg`
* Upon opening a PR or committing to `main` the GitHub Action present in `.github/workflows/ci.yml` will test your project against a matrix of OS' and Python versions, and run `flake8`, `black`, and `pytest`.

### Using

> This is how you use the "template" piece of this repo. You can delete this section of the readme later once you've completed the steps below.

1. Clone this repo, and then initialize a new repo on top of it.
You probably don't want the git history of _this_ project, just the files within it.
```bash
git clone SSH_OR_HTTPS_URL your_project_name
cd your_project_name
rm -rf .git
git init
```

2. Modify the `[metadata]` block of `setup.cfg` with your project's metadata.
```diff
diff --git a/setup.cfg b/setup.cfg
[metadata]
+ name = your_project_name
version = 0.0.1
+ description = What the project does
long_description = file: readme.md
+ author = You, unless you're me
+ author_email = you@email.com
```

3. Modify the `[options]` and [options.entry_points] blocks of `setup.cfg` with your project's dependencies.

4. The default name what you'll use the run the CLI is `app` but you probably want to name it something else.

```diff
diff --git a/setup.cfg b/setup.cfg
[options.entry_points]
console_scripts =
-    app = src.cli:main
+    your_project_name = src.cli:main
```

5. Once you've reconfigured your project, you can install it locally in editable mode with `pip install -e .[dev]` or see the "Installation" section above

6. Delete a bunch of this readme referencing the "template" - you don't have a template anymore, just a blank project, and make an initial commit.

7. Write your project. Easiest part.

## Contributing

PRs and issues welcome, with the caveat that this is my own _personal_ setup. I might not change anything.

### Todos:
* Flesh out the CLI entrypoint further with help, sample arguments, etc.
* Add a `Dockerfile`
