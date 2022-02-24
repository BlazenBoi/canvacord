from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_desc = open("README.md", "r")
long_description = long_desc.read()
with open('src/canvacord/__init__.py', 'r') as f:
    version = [line.split('=')[1].strip(" '\"") for line in f.read().splitlines() if line.startswith('__version__')][0]


setup(
    name='canvacord',
    version=version,
    description='A Python Version of Canvacord',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/BlazenBoi/canvacord.py/issues',
    author='Blazen',
    author_email='contact@fireballbot.com',
    keywords='canvacord, rankcard, image manipulation, meme, discord, discordpy, discord-py',
    packages=find_packages(include=['canvacord']),
    python_requires='>=3.6',
    install_requires=[
    "setuptools>=42",
    "wheel",
    "pillow",
    "disnake",
    "asyncio",
    "aiohttp",
    "typing",
    "datetime"
    ],
    project_urls={
        'Discord Server': 'https://discord.com/invite/mPU3HybBs9',
        'Bug Tracker': 'https://github.com/BlazenBoi/canvacord.py/issues',
        'Source': 'https://github.com/BlazenBoi/canvacord',
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
      ]
)
#© 2021 GitHub, Inc.