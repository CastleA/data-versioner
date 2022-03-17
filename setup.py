from setuptools import setup, find_packages

setup(
    name='dataversioner',
    version='0.1.0',
    packages=find_packages(),
    author='Castle Leonard',
    author_email='caleona@uw.edu',
    url='https://github.com/CastleA/data-versioner',
    description=('A python package for git-like data tracking.'),
    install_requires=['pandas'],
    tests_require=['flake8']
)
