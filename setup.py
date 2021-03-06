from setuptools import setup, find_packages

setup(
    name="schoolsoftapi",
    version="0.4.0.dev1",
    packages=find_packages(),
    install_requires=['requests', 'xlrd'],
    description="SchooSoft API",
    long_description=open('README.rst').read(),
    author="William Wu",
    author_email="william@pylabs.org",
    url="https://github.com/fossnio/schoolsoftapi",
    license="GPL 3",
    entry_points={
        'console_scripts': ['schoolsoftapi=schoolsoftapi.command_line:main'],
        },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3'
    ]
)
