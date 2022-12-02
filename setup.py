# whenever we are working in a pythin project, the first file we need is setup.py so that whatever code or programs 
# we are writing in our project can be used as a library in another file or project.
# In python project, a folder which contains __init__.py file will be considered as packages
from setuptools import find_packages,setup

setup(
    name = "sensor",
    version = "0.0.1",
    author = "motishree",
    author_email = "motishreepatel89@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),

)