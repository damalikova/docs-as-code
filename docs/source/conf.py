# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'WebSky docs-as-code demo'
copyright = '2023, WebSky.Tech'
author = 'WebSky.Tech Writer'

release = '0.1'
version = '0.1.0'
language = 'ru'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxawesome_theme.docsearch',
    'sphinxawesome_theme.highlighting',
    'sphinxawesome_theme.deprecated',
    'sphinx_design',
    'hoverxref.extension'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']
templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinxawesome_theme'
html_logo = 'https://static.tildacdn.com/tild3136-3634-4662-b064-353530653036/Product.svg'
html_static_path = ['_static']
# html_css_files = ["custom.css"]
