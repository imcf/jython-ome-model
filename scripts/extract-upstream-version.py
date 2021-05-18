#!/usr/bin/env python3

"""Extract the package version from the upstream `pom.xml`.

The script is parsing the `pom.xml` file located in the `upstream` directory, extracts
the <version> tag and writes it into a file (that is supposed to shadow the same file
from the upstream project in the resulting package).

The functions herein are largely taken from the `setup.py` of the upstream project with
minor adaptations to make the paths match this package.
"""

from os.path import abspath, dirname, join
import xml.etree.ElementTree as ElementTree


def get_version():
    tree = ElementTree.parse('upstream/pom.xml')
    ns = {'maven': 'http://maven.apache.org/POM/4.0.0'}
    version = tree.find('maven:version', ns).text
    print(version)
    return version.replace('-SNAPSHOT', '.dev0')


def write_version(version):
    target = abspath(join(dirname(__file__), '..', 'local', 'ome_model', '__init__.py'))
    # print(target)
    with open(target, 'w') as f:
        f.write('__version__ = "%s"\n' % version)


version = get_version()
write_version(version)
