# built my machine learning application as a package
# anybody can use the installation and use it 

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e.'
def get_requirements(file_path:str)->List[str]:
    '''This function will return the list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements

# metadata information about the entire project
setup(
    name = 'mlprojects',
    version='0.0.1',
    author='Sneha Das Karmakar',
    author_email='snehadaskarmakar2@gmail.com',
    packages=find_packages(),
    # install_requires = ['pandas','numpy','seaborn']
    install_requires = get_requirements('requirements.txt')
)
