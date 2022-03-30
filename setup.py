from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.MD').read_text(encoding='utf-8')

setup(
    name='Rock-Paper-Scissors',
    version='1.0',
    description='A simple CLI based Rock-Paper-Scissors written in Python.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Patrick260/Rock-Paper-Scissors',
    author='Patrick260',
    author_email='Patrick260@protonmail.com',
    classifiers=[
        'Development Status :: 5 - Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Games/Entertainment'
    ],
    keywords='game, games',
    packages=['rock_paper_scissors'],
    python_requires='>=3.6, <4',
    package_data={'': ['LICENSE']},
    entry_points={
        'console_scripts': [
            'rock-paper-scissors=rock_paper_scissors:main'
        ]
    },
    project_urls={
        'Source': 'https://github.com/Patrick260/Rock-Paper-Scissors',
        'Bug Reports': 'https://github.com/Patrick260/Rock-Paper-Scissors/issues'
    }
)
