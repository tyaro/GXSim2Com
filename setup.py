from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description_ = f.read()

setup(
    name='gxsimcom',
    packages=find_packages(where='./src'), 
    package_dir={'': 'src'},
    version='0.0.4', 
    license='MIT', 
    install_requires=['psutil'], 
    author='tyaromax',
    author_email='tkentyan@hotmail.com',  
    url='https://github.com/tyaro/GXSim2Com', 
    description='Communication to GXSimulator2', 
    long_description=long_description_, 
    long_description_content_type='text/markdown', 
    keywords ='GXSimulator GXSim gxsimcom', 
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ], 
)