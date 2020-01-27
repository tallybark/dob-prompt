# This file exists within 'dob-prompt':
#
#   https://github.com/hotoffthehamster/dob-prompt

"""
Packaging instruction for setup tools.

Refs:

  https://setuptools.readthedocs.io/

  https://packaging.python.org/en/latest/distributing.html

  https://github.com/pypa/sampleproject
"""

from setuptools import find_packages, setup

# *** Package requirements.

requirements = [
    # https://github.com/pytest-dev/apipkg
    'apipkg',
# FIXME/2020-01-05 17:57: Require dob, or the other way around?
    # The dob CLI core.
    'dob',
# FIXME/2020-01-05 17:31: Scrub the `future` library, but now it is!
    # Compatibility layer between Python 2 and Python 3.
    #  https://python-future.org/
    'future',
    # Vocabulary word pluralizer.
    #  https://github.com/ixmatus/inflector
    'Inflector',
    # Elapsed timedelta formatter, e.g., "1.25 days".
    'human-friendly_pedantic-timedelta >= 0.0.6',  #  Imports as pedantic_timedelta.
    # Amazeballs prompt library.
    # FIXME/2019-02-21: Submit PR. Until then, whose fork?
    'prompt-toolkit-dob >= 2.0.9',  # Imports as prompt_toolkit.
# FIXME/2020-01-05 17:50: Remove 'six', 'future', etc.
    # Virtuous Six Python 2 and 3 compatibility library.
    #  https://six.readthedocs.io/
    'six',
]

# *** Minimal setup() function -- Prefer using config where possible.

# (lb): All settings are in setup.cfg, except identifying packages.
# (We could find-packages from within setup.cfg, but it's convoluted.)

setup(
    install_requires=requirements,
    packages=find_packages(exclude=['tests*']),
    # Tell setuptools to determine the version
    # from the latest SCM (git) version tag.
    #
    # Note that if the latest commit is not tagged with a version,
    # or if your working tree or index is dirty, then the version
    # from git will be appended with the commit hash that has the
    # version tag, as well as some sort of 'distance' identifier.
    # E.g., if a project has a '3.0.0a21' version tag but it's not
    # on HEAD, or if the tree or index is dirty, the version might
    # be:
    #   $ python setup.py --version
    #   3.0.0a22.dev3+g6f93d8c.d20190221
    # But if you clean up your working directory and move the tag
    # to the latest commit, you'll get the plain version, e.g.,
    #   $ python setup.py --version
    #   3.0.0a31
    # Ref:
    #   https://github.com/pypa/setuptools_scm
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
)

