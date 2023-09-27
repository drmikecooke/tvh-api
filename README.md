# tvh-api

Collecting some simple python interactions with the tvheadend api.

## Installation (local)

> python3 -m pip install --upgrade build

You may get PATH warnings. These will be fixed shortly . . .

> python3 -m pip install --user pipx

PATH warnings again . . .

> python3 -m pipx ensurepath

This should fix the PATH, but you need to open a NEW terminal for it to register . . .

Open terminal in cloned folder, or cd to it, and then . . .

> python3 -m pip install --upgrade build
> pipx install .

Not sure all these steps are necessary - e.g. you may be able to install the apps directly from the build directory?

I work on a system where my tvh servers hostnames are prefixed with rpi and suffixed with .local. I just pass the middle bit.
