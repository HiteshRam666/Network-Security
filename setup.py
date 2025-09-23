from gettext import install
from setuptools import find_packages, setup
from typing import List 

def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """
    requirement_list: List[str] = [] 
    try:
        with open('requirements.txt', 'r') as f:
            # Reading line from the file 
            lines = f.readlines()
            # Process each line 
            for line in lines:
                requirement = line.strip()
                ## Ignoring empty lines and -e.
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print(f"Requirements.txt not found")

    return requirement_list

setup(
    name = "Network Security", 
    version="0.0.1", 
    author="Hitesh Ram",
    author_email= "hiteshram321@gmail.com", 
    packages=find_packages(), 
    install_requires = get_requirements()
)