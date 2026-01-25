import os
import sys
import importlib.metadata


CONF_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(CONF_DIR, ".."))
PACKAGE_DIR = os.path.join(REPO_ROOT, "autoeda")
sys.path.insert(0, PACKAGE_DIR)

# AutoAPI config (only once!)
autoapi_type = "python"
autoapi_dirs = [PACKAGE_DIR]
autoapi_add_toctree = False
autoapi_keep_files = False
autoapi_generate_api_docs = True
autoapi_options = ["members", "undoc-members", "show-inheritance"]

# Project info
project = "AutoEDA"
copyright = "Copyright © 2026 Eli Gonzalez, Gurleen Kaur, Gloria Yi, Mantram Sharma"

# Version
try:
    version = importlib.metadata.version("autoeda")
except importlib.metadata.PackageNotFoundError:
    version = "0.0.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "autoapi.extension",
]

autosummary_generate = True
source_suffix = [".rst", ".md"]
master_doc = "index"
language = "en"
html_theme = "pydata_sphinx_theme"

myst_enable_extensions = [
    "html_image",
    "colon_fence",
    "deflist",
    "attrs_inline",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", "https://docs.python.org/3/objects.inv"),
}
