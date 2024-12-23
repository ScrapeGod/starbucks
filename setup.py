from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='starbucks',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,
    author='Bikash',
    description='A Python-based application that scrapes data from Starbucks.',
    url='https://github.com/ScrapeGod/starbucks',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)