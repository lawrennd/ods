#!/usr/bin/env python
import os
import sys
import toml


def get_version_from_toml(file_path='pyproject.toml'):
    data = toml.load(file_path)
    return data['tool']['poetry']['version']


if __name__ == "__main__":
    print("This project has transitioned to using Poetry for package management.")
    print("setup.py is now just a wrapper for backwards compatibility.")    
    print("Switching to Poetry for package management...")
    
    os.system("pip install poetry")
    
    if "install" in sys.argv:
        print("Emulating setup.py with poetry. Try running poetry install instead.")
        os.system("poetry install")
    elif "build" in sys.argv:
        print("Emulating setup.py with poetry. Try running poetry build instead.")
        os.system("poetry build")
    elif "upload" in sys.argv:
        print("Using twine to publish. Please consider switching to using poetry.")
        os.system("poetry build")
        os.system("twine upload dist/*")
        print("Pushing git tags.")
        version = get_version_from_toml()
        os.system(f"git tag v{version}")
        os.system("git push --tags")
        #os.system("poetry publish")
    else:
        print("Unsupported command. Please use poetry directly or update this setup.py accordingly.")
'''#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://github.com/navdeep-G/setup.py

# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command


# Package meta-data.
NAME = "pods"
DESCRIPTION = "Python software for Open Data Science"
URL = "https://github.com/lawrennd/ods"
EMAIL = "lawrennd@gmail.com"
AUTHOR = "Neil D. Lawrence"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = "0.1.14"

# What packages are required for this module to be executed?
REQUIRED = [
    "pandas",
    "PyYAML",
    "scipy",
    "h5py",
]

# What packages are optional?
EXTRAS = {
    "google trends interface": ["pytrends"],
    "Nigerian NMIS data": ["geopandas"],
    "Kepler telescope light curves": ["astropy"],
    "Olivetti Faces": ["netpbmfile"],
}

PACKAGE_DATA = {"pods": ["defaults.cfg", "data_resources.json", "football_teams.json"]}

DEPENDENCY_LINKS = []

CONSOLE_SCRIPTS = []
ENTRY_POINTS = {
    "console_scripts": CONSOLE_SCRIPTS,
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        self.status("Pushing git tags…")
        os.system("git tag v{0}".format(about["__version__"]))
        os.system("git push --tags")

        sys.exit()


# Where the magic happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    package_data=PACKAGE_DATA,
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],
    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    entry_points=ENTRY_POINTS,
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    dependency_links=DEPENDENCY_LINKS,
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    # $ setup.py publish support.
    cmdclass={"upload": UploadCommand,},
)
'''
