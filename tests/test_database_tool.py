'''
Unit tests for databaseTool components.

===============================================================================
Author:        Mike Stanley
Created:       September 28, 2019
Last Modified: September 28, 2019

===============================================================================

Useful Links
- testing with psycopg2: 
    - http://initd.org/psycopg/docs/extensions.html#connection-status-constants

===============================================================================

TODO:
1. Understand how I can import classes from py files in parent directory.
2. Establish test audio filepath.
3. Figure out how want to implement checking if song is in database.
4. Create a song in DB so that I can test the exists functionality.
5. Capture and test stdout.
6. Think about how to test generated song features.
7. Figure out if I want the search_db method in the databaseTool class.

'''

import pytest

from database_tool import databaseTool
import psycopg2

# Database connection constants
DB_USER = 'freezam_0'
DB_USER_PWD = 'statcomp'
DB_NM = 'audio_lib_0'

# Existing song constant
EXISTING_SONG_ID = 1234 #TODO - this should be updated to something real

# Song test constants
SONG_BAD_FILEPATH = '/this/is/not/a/real/path.wav'
SONG_FILEPATH = '/put/a/song/path/here.wav'
SONG_FILEPATH_MP3 = '/put/a/song/path/here.mp3'
SONG_TITLE = 'Candy Shop'
SONG_ARTIST = '50 Cent'
SONG_ALBUM = 'The Massacre'

# File transform constant
OUT_FORMAT = 'wav'

def test_connect_to_db():
    """
    TODO: 
     - test connection with psycopg2
    """

    # instantiate vanilla database object
    db_obj = databaseTool(
        db_user=DB_USER, db_user_pwd=DB_USER_PWD, db_nm=DB_NM, 
        connect_to_db=False
    )

    # test that a connection is made
    assert db_obj.status == psycopg2.extensions.STATUS_READY

def test_song_in_db():

    # instantiate vanilla database object
    db_obj = databaseTool(
        db_user=DB_USER, db_user_pwd=DB_USER_PWD, db_nm=DB_NM
    )

    # test if existing song ID is in database
    assert db_obj.song_in_db(EXISTING_SONG_ID) != {}
    assert db_obj.song_in_db(EXISTING_SONG_ID).song_id == EXISTING_SONG_ID

def test_add_song():
    """
    TODO:
     - establish test audio filepath
    """

    # instantiate vanilla database object
    db_obj = databaseTool(
        db_user=DB_USER, db_user_pwd=DB_USER_PWD, db_nm=DB_NM
    )

    # try to add a song using a bad file path
    with pytest.raises(FileExistsError):
        db_obj.add_song(
            song_filepath=SONG_BAD_FILEPATH,
            song_title=SONG_TITLE,
            artist=SONG_ARTIST,
            album=SONG_ALBUM
        )

    # add a song
    new_song_id = db_obj.add_song(
        song_filepath=SONG_FILEPATH,
        song_title=SONG_TITLE,
        artist=SONG_ARTIST,
        album=SONG_ALBUM
    )

    # check to see if song is in database
    assert db_obj.song_in_db(new_song_id) == True

def test_remove_song():

    # instantiate vanilla database object
    db_obj = databaseTool(
        db_user=DB_USER, db_user_pwd=DB_USER_PWD, db_nm=DB_NM
    )

    # add a song
    new_song_id = db_obj.add_song(
        song_filepath=SONG_FILEPATH,
        song_title=SONG_TITLE,
        artist=SONG_ARTIST,
        album=SONG_ALBUM
    )

    # remove song
    db_obj.remove_song(new_song_id)

    # check that song is no longer in database
    assert db_obj.song_in_db(new_song_id) == False

def test_list_songs():
    """
    TODO: 
    - Figure out how to capture stdout 
    """
    pass 

def test_create_song_features():

    # instantiate vanilla database object
    db_obj = databaseTool(
        db_user=DB_USER, db_user_pwd=DB_USER_PWD, db_nm=DB_NM
    )

    # add a song
    new_song_id = db_obj.add_song(
        song_filepath=SONG_FILEPATH,
        song_title=SONG_TITLE,
        artist=SONG_ARTIST,
        album=SONG_ALBUM
    )

    # create song features
    song_features = db_obj.create_song_features(new_song_id, test_out=True)

    # TODO - create some assert statements about how this should look
    # assert blah blah
    # assert testing stuff
    # assert yep

def test_change_song_format():

    # instantiate vanilla database object
    db_obj = databaseTool(
        db_user=DB_USER, db_user_pwd=DB_USER_PWD, db_nm=DB_NM
    )

    # add a song (mp3)
    new_song_id = db_obj.add_song(
        song_filepath=SONG_FILEPATH_MP3,
        song_title=SONG_TITLE,
        artist=SONG_ARTIST,
        album=SONG_ALBUM
    )

    # transform format of song
    db_obj.change_song_format(new_song_id, out_format=OUT_FORMAT)
    
    # check that the song is now in the OUT_FORMAT
    assert db_obj.song_in_db(new_song_id).song_format == OUT_FORMAT

def test_search_db():
    pass