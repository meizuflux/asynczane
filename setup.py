from setuptools import setup

description = 'Asynchronous wrapper for Zane API.'

with open("README.md", 'r') as readme:
    long_description = readme.read()

version = "1.0"

setup(
    name='asynczane',
    version=version,
    author='ppotatoo',
    description=description,
    long_description_content_type='text/markdown',
    long_description=long_description,
    url='https://github.com/ppotatoo/asynczane',
    license='MIT',
    packages=['asynczane'],
    install_requires=['aiohttp'],
    python_requires='>=3.6'
)



