'''
Unit tests for utils functions.

===============================================================================
Author:        Mike Stanley
Created:       September 29, 2019
Last Modified: September 29, 2019

===============================================================================

TODO:
1. figure out how the periodograms are going to be stored

'''

import pytest

from utils import read_song, read_periodogram

# read_song constants
BAD_SONG_FILEPATH = '/this/is/a/bad/filepath'
SONG_FILEPATH = '/path/to/example/song'

# read_periodogram constants
PERIODOGRAM_FILEPATH = '/this/is/filepath/to/periodogram'

def test_convertAudio():
    """
    I'm not sure if I am even going to build out this function.
    """
    pass

def test_read_song():

    # test with the bad filepath
    with pytest.raises(FileExistsError):
        read_song(BAD_SONG_FILEPATH)

    # read in song with function
    data, fs = read_song(SONG_FILEPATH)
    assert data.shape[0] > 0
    assert data.shape[1] == 2
    assert fs > 0

def test_read_periodogram():

    # read it in
    periodogram = read_periodogram(PERIODOGRAM_FILEPATH)
    assert isinstance(periodogram, list)