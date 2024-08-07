from setuptools import setup, find_packages

setup(
    name='pyparseit',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'pyparseit=pyparseit.cli:main',
        ],
    },
    author='uladkaminski',
    author_email='i@uladkaminski.com',
    description='A library to parse Markdown and extract code snippets',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    url='https://github.com/uladkaminski/pyparseit',
)
