from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


VERSION = '1.0.2'

setup(
    name='masked_ai',
    version=VERSION,
    description='Masked AI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Cado Security',
    author_email='maskedai@cadosecurity.com',
    url='https://github.com/cado-security/masked-ai',
    download_url='https://github.com/cado-security/masked-ai/archive/refs/heads/main.zip',
    py_modules=['masked_ai'],
    install_requires=['nltk'],
    packages=find_packages()
)
