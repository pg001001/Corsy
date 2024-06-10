
from setuptools import setup, find_packages

# Read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='Corsy',
    version='1.0.0',
    author='Somdev Sangwan',
    author_email='somdevsangwan@pm.me',
    description='CORS misconfiguration scanner',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/s0md3v/Corsy',
    packages=find_packages(),
    py_modules=['corsy'],  # This should match the name of your script
    install_requires=[
        'requests',
        'tldextract',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'corsy=corsy:main',
        ],
    },
)
