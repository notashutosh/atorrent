from setuptools import setup, find_packages

setup(
    name='atorrent',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'atorrent=atorrent.main:main',
        ],
    },
    author='Ashutosh Mohan',
    author_email='ashutoshmohan@outlook.in',
    description='A command line tool for managing torrents',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/atorrent',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
