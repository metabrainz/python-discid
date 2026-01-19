# Copyright (C) 2013  Johannes Dewender
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Please submit bug reports to GitHub:
# https://github.com/metabrainz/python-discid/issues
"""utility functions
"""

import math

SECTORS_PER_SECOND = 75

def _encode(string: str|bytes):
    """Encode (unicode) string to byte string
    """
    if isinstance(string, str):
        return string.encode()
    elif isinstance(string, bytes):
        return string
    raise TypeError('Unexpected type, expected string or bytes')
    # UnicodeDecodeError (Python 2) is NOT caught
    # device names should be ASCII

def _decode(byte_string: bytes|str):
    """Decode byte string to (unicode) string
    """
    # this test for bytes works on Python 2 and 3
    if isinstance(byte_string, bytes):
        return byte_string.decode()
    elif isinstance(byte_string, str):
        return byte_string
    raise TypeError('Unexpected type, expected string or bytes')

def _sectors_to_seconds(sectors):
    """Round sectors to seconds like done on MusicBrainz Server

    The result is forced to :obj:int to make formatted output easier.
    """
    # note that `round(2.5) == 2` on Python 3
    # and math.floor doesn't return :obj:int on Python 2
    # additionally always `int / int =^= int` in Python 2
    return int(math.floor((sectors / float(SECTORS_PER_SECOND)) + 0.5))


# vim:set shiftwidth=4 smarttab expandtab:
