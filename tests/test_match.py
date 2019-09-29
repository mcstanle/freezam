'''
Unit tests for match components.

===============================================================================

Author:        Mike Stanley
Created:       September 28, 2019
Last Modified: September 29, 2019

===============================================================================
TODO:
1. find snippet info to use

'''

import pytest

from database_tool import databaseTool
from match import matcher
from process_audio import processAudio
from utils import read_song

# constants
WINDOW_TYPE='blackman'
WINDOW_SIZE=1234
WINDOW_SHIFT=10
SIGNATURE_TYPE='unsmoothed'
DB_USER = 'freezam_0'
DB_USER_PWD = 'statcomp'
DB_NM = 'audio_lib_0'

SNIPPET_FILEPATH = '/this/is/a/filepath/to/snippet'
CORRECT_SNIPPET_INFO = {'song_name':'alsdkfjsd', 'other_info':'goes here'}

def test_match():

    # instantiate match object
    match_snippet = matcher(
        window_type=WINDOW_TYPE,
        window_size=WINDOW_SIZE,
        window_shift=WINDOW_SHIFT,
        signature_type=SIGNATURE_TYPE,
        db_user=DB_USER,
        db_user_pwd=DB_USER_PWD,
        db_nm=DB_NM,
    )

    # find match to snippet
    snippet_match = match_snippet.match(SNIPPET_FILEPATH)
    assert snippet_match == CORRECT_SNIPPET_INFO