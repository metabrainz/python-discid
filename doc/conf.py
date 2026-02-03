import ctypes
import os
import sys

sys.path.insert(0, os.path.abspath("."))  # for extensions
sys.path.insert(0, os.path.abspath(".."))  # for the code

# -- Mock libdiscid loading ----------------------------------------------------


class Mock:
    def __call__(self, *args):
        return Mock()

    def __getattr__(cls, name):
        return Mock()

    def discid_get_version_string(self):
        return ""


ctypes.cdll.LoadLibrary = Mock()  # type: ignore

# to gather version information
import discid  # noqa: E402

# -- General configuration -----------------------------------------------------

needs_sphinx = "1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",
]
source_suffix = ".rst"
master_doc = "index"
exclude_patterns = ["_build", ".venv"]

# General information about the project.
project = "python-discid"
copyright = "2013, Johannes Dewender"
# The short X.Y version / base version
version = ".".join(discid.__version__.split("-")[0].split(".")[0:2])
# The full version, including alpha/beta/rc tags.
release = discid.__version__
# see below for "current" = base version with "-dev" appended if necessary

download_base = "https://github.com/metabrainz/python-discid/archive"
if release.endswith("dev"):
    current = "%s-dev" % version
    download_url = "%s/master.%%s" % download_base
else:
    current = version
    download_url = "%s/v%s.%%s" % (download_base, release)

extlinks = {
    "source_download": (download_url, "%s"),
    "issue": ("https://github.com/metabrainz/python-discid/issues/%s", "#%s"),
    "musicbrainz": ("https://musicbrainz.org/doc/%s", "%s"),
}

# there seems to be no way to prefer latest python documentation
intersphinx_mapping = {
    "python": ("http://python.readthedocs.org/en/latest/", None),
    "musicbrainzngs": (
        "https://python-musicbrainzngs.readthedocs.org/en/latest/",
        None,
    ),
}

rst_prolog = """
.. currentmodule:: discid
"""

rst_epilog = (
    """
.. |current| replace:: %s
"""
    % current
)

# -- Options for HTML output ---------------------------------------------------

html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "collapse_navigation": True,
    "navigation_depth": 2,
    "version_selector": True,
}

html_title = "%s %s documentation" % (project, current)
html_domain_indices = False

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    (
        "index",
        "python-discid.tex",
        "python-discid Documentation",
        "Johannes Dewender",
        "manual",
    ),
]

latex_domain_indices = False

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ("index", "python-discid", "python-discid Documentation", ["Johannes Dewender"], 1)
]

# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "python-discid",
        "python-discid Documentation",
        "Johannes Dewender",
        "python-discid",
        "One line description of project.",
        "Miscellaneous",
    ),
]

texinfo_domain_indices = False
