from setuptools import setup, find_packages
from typing import List

def get_requirements(filename)-> List[str]:
    
    '''
    This function reads the requirements.txt file and returns a list of requirements
    '''
    HYPHEN_E_DOT = '-e .'
    requirements = []
    with open(filename) as f:
        requirements = f.readlines()
        requirements = [x.replace('\n','') for x in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Zeeshan',
    author_email='zeeshanparvez00843@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)