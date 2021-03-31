# Installation

The project requirements can be installed using Python's builtin package manager `pip`.

## Table of Contents

* [Requirements](#requirements)
* [Python Installation](#python-installation)
* [Virtual Environment](#virtual-environment)


## Requirements

The following requirements are needed to successfully install the `Shorty` project.

### Software

* [Python 3.7.x](https://www.python.org/)

## Python Installation

Make sure that Python version `== 3.7.x` is installed in your system. You can locate the Python
installation with
```bash
$ which python
```
and check the Python version with
```bash
$ python --version
```
In case multiple Python installations are available, the `python` keyword might be assigned to a
different Python version than the one required. Make sure you are using the correct Python executable,
by searching for a specific version, e.g.
```bash
$ which python3
```
or
```bash
$ which python3.7
```
In case Python is not installed, follow the OS specific instructions for installing `Python3.7`. For
example in CentOS 7
```bash
$ yum -y update
$ yum -y install python3
```
will install Python3.7. Python releases are available [here](https://www.python.org/downloads/source/).


## Virtual Environment

With Python installed, change directory to a desired location and create a Python virtual environment,
with
```bash
$ cd /path2/MoS_Index_venv
$ python -m venv MoS_Index
```
Again, make sure you are using the correct Python executable, i.e. the correct `python` entry point.

Activate the virtual environment using
```bash
$ source /path2/MoS_Index_venv/bin/activate
$ pip install -r requirements.txt
```
