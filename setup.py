from setuptools import setup, find_packages

setup(
    name='your_project_name',
    version='0.1.0',
    description='A short description of your project',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/bi-kash/your_project_name',
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=[
        # List your project dependencies here, e.g.
        # 'numpy',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        # Add more classifiers as needed
    ],
)