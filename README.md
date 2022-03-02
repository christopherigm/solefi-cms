# BACK

## Linux instructions

Linux does not need instructions ;)


## Windows instructions

### Install Python 

Get it form [here](https://www.python.org/downloads/)

### Download and install PIP

Get it form [here](https://bootstrap.pypa.io/get-pip.py)

Open a GitBash terminal as administrator and do:

```sh
python get-pip.py
```

Install virtualenvwrapper, virtualenv and supertools

```sh
python -m pip install virtualenv virtualenvwrapper supertools
```

### Create virtualenv

```sh
virtualenv.exe my_venv
```

This command will create a folder `venv` with the virtualenv inside of it.

To activate the virtualenv just do

```sh
source ./my_venv/Scripts/activate
```

To deactivate:

```sh
deactivate
```