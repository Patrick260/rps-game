#    Copyright (C) 2022  Patrick260
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.MD').read_text(encoding='utf-8')

setup(
    name='py-rps-game',
    version='1.0',
    description='A simple CLI based Rock-Paper-Scissors written in Python.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Patrick260',
    author_email='Patrick260@protonmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
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
        'Source': 'https://github.com/Patrick260/rps-game',
        'Bug Reports': 'https://github.com/Patrick260/rps-game/issues'
    }
)
