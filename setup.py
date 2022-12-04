# whenever we are working in a pythin project, the first file we need is setup.py so that whatever code or programs 
# we are writing in our project can be used as a library in another file or project.
# In python project, a folder which contains __init__.py file will be considered as packages
from setuptools import find_packages,setup

REQUIREMENT_FILE_NAME = "requirements.txt"
# we are keeping requirements.txt file in a variable

from typing import List
def get_requirements() -> List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file :
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list] # in notepad \n will be there for a new line. so that can be removed.
        if HYPHEN_E_DOT in requirement_list :# -e . is not a library in requirements.txt, so we are just removing that
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list
# now this get_requirements() function will return all the list of libraries.

#... means pass we use in function
# we want to return function as list items. so have written like that 
# to trigger setup.py file we use -e . at the end of requirements.txt file

setup(
    name = "sensor",
    version = "0.0.1",
    author = "motishree",
    author_email = "motishreepatel89@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),

)