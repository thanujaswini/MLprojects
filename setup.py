from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements file and returns a list of dependencies.

    :param file_path: Path to the requirements file.
    :return: List of dependencies as strings.
    """
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT) 

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Thanu',
    author_email='thanujaswinidadipallly16@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
