from setuptools import setup, find_packages
from codecs import open
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gxsimcom',
    packages=find_packages(where='./src'), 
    package_dir={'': 'src'},
    version='0.0.7', 
    license='MIT', 
    install_requires=['psutil'], 
    author='tyaromax',
    author_email='tkentyan@hotmail.com',  
    url='https://github.com/tyaro/GXSim2Com', 
    description='Communication to GXSimulator2', 
    keywords ='GXSimulator GXSim gxsimcom', 
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    long_description=long_description,
    long_description_content_type='text/x-rst',

)

### python setup.py sdist
### python setup.py bdist_wheel
### twine upload --repository pypi dist/*