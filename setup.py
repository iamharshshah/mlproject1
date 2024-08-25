from setuptools import find_packages,setup
from typing import List
HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str) ->List[str]:
    ## This function will return the list of requirements##

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT) ##-e . text automatically gets added in the requirements.txt so by doing this we are ignoring this text and installing our required packages only

    return requirements
    

setup(

name = "mlproject1",
version = "0.0.1",
author = "Harsh",
author_email= "harsh.bitz@gmail.com",
packages= find_packages(),
install_requires = get_requirements("requirements.txt")

)