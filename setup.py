from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads the requirements file and returns a list of dependencies.
    """
    requirements = []
    with open(file_path, "r") as file_obj:  # Corrected file reading
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Strip newlines

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  # Remove '-e .' if present

    return requirements

setup(
    name="MLProject",
    version="0.0.1",
    author="Niroshan",
    author_email="shanniro174@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
