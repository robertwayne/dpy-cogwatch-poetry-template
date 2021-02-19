# dpy-cogwatch-poetry-template

This is a simple starter template for projects built with `discord.py`. In addition, the template is built around
a few key libraries:

**[poetry](https://python-poetry.org/)** -- package manager, scripts

**[cogwatch](https://github.com/robertwayne/cogwatch)** -- automatic command loading, hot-reloading

**[uvloop](https://github.com/MagicStack/uvloop)** -- ultra fast asyncio event loop

**[black](https://github.com/psf/black)** -- code formatting


## Setup

1) Ensure you have Poetry installed with `poetry --version`. If not, follow the official
[installation](https://python-poetry.org/docs/#installation) instructions.

2) Rename the `.env.template` file to `.env` and add your API token and user ID. You can set the prefix here as well.

## Scripts

The included *scripts.py* file is the recommended way to access CLI scripts with Poetry.

`poetry run bot` -- starts the bot client

`poetry run fmt` -- formats your code with `black` based on the configuration defined in *pyproject.toml*
