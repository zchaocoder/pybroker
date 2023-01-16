# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath("../src/"))
sys.path.insert(0, os.path.abspath("../docs/notebooks/"))

nitpick_ignore = [("py:class", "type")]

from importlib import metadata

# PACKAGE_VERSION = metadata.version('pubpypack-pybroker-<firstname>-<lastname>')
# version = release = PACKAGE_VERSION

project = "PyBroker"
copyright = "2023, Edward West"
author = "Edward West"
release = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "nbsphinx",
    "IPython.sphinxext.ipython_console_highlighting",
    "sphinx.ext.autodoc",
    "sphinx.ext.autodoc.typehints",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
master_doc = "index"

add_module_names = False
autosummary_generate = True
keep_warnings = False

python_version = ".".join(map(str, sys.version_info[0:2]))
intersphinx_mapping = {
    'python': ("https://docs.python.org/" + python_version, None),
    'numpy': ("https://numpy.org/doc/stable/", None),
    'pandas': ("https://pandas.pydata.org/docs/", None),
    'diskcache': ("https://grantjenks.com/docs/diskcache/", None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "PyBroker"
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
