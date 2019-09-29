'''
Classes and functions that implement the flagship capability of this app; 
matching user-input audio snippets to audio files in a database. 

TODO: write more high level documentation about the functionality within this 
code.

===============================================================================
Author:        Mike Stanley
Created:       September 28, 2019
Last Modified: September 29, 2019

===============================================================================

TODO:
1. 

'''

from database_tool import databaseTool
from process_audio import processAudio
from utils import *

class matcher:
    """
    Match audio snippet to some song in database.
    """
    def __init__(self, 
        window_type, window_size, window_shift, 
        signature_type,
        db_user, db_user_pwd, db_nm, 
        db_host='localhost', db_port=5432
    ):
        # store the values that define the class
        self.window_type=window_type
        self.window_size=window_size
        self.window_shift=window_shift
        self.signature_type=signature_type
        self.db_user=db_user
        self.db_user_pwd=db_user_pwd
        self.db_nm=db_nm
        self.db_host=db_host
        self.db_port=db_port

        # audio processing component
        self.audio_proc=processAudio(
            window_type=window_type,
            window_size=window_size,
            window_shift=window_shift,
            signature_type=signature_type
        )
        
        # database communication component
        self.database_con=databaseTool(
            db_user=db_user, db_user_pwd=db_user_pwd, db_nm=db_nm,
            db_host=db_host, db_port=db_port
        )

    def match(self, snippet_filepath):
        """
        Reads audio file, computes local periodograms, compute signatures, 
        and finds matching song.

        Parameters:
            snippet_filepath (str) : location of snippet.

        Returns:
            Relevant information about matched songs.

        TODO:
        1. consider finding a threshold value for the matching
        """
        # read in snippet -- call read_song from utils

        # compute local periodograms -- call self.audio_proc.create_periodogram

        # compute signatures -- call self.audio_proc.create_signature

        # find closest matches in database -- call self.database_con.search_db
        pass