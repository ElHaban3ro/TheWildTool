from setuptools import setup


from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name = 'TheWildTool',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = ['TheWildTool'],
    version = '1.2.2',
    license = 'MIT',
    description = 'Generation of video datasets (under research) 🤖',
    author = 'ElHaban3ro',
    author_email = 'habanferd@gmail.com',
    url = 'https://github.com/ElHaban3ro/ConvTool',
    keywords = ['Data Analysis', 'IA', 'datasets', 'Data Engenering', 'DeepLearing'],
    classifiers = ['Programming Language :: Python :: 3.10'],
    install_requires=['moviepy==1.0.3', 'ipython', 'scipy', 'matplotlib']
)