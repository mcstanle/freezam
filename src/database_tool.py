"""
Classes and functions to provide database connection functionality. This 
module should interface with a PostgreSQL database in the following ways:
1. List all current songs in DB.
2. Add songs to DB.
3. Remove songs from DB.
4. Create song features in DB for songs already existing in DB.
5. Change audio formats of songs in DB.
6. Initiate databse searching.

===============================================================================

Author:        Mike Stanley
Created:       September 28, 2019
Last Modified: September 28, 2019

===============================================================================

Useful Links/Tutorials:
- working with postgresql in python
    - https://stackabuse.com/working-with-postgresql-in-python/

===============================================================================

TODO:
1. Figure out how python and postgre interact with audiofiles
2. Think about output format for list_songs
3. Understand the types of features that will be made from the raw audio
4. Figure out how the database will be searched with features for search()
5. Relax the exisiting database assumption.
6. Decide if songs should only be searchable by unqiue song ID.

"""

import psycopg2

from utils import *

class databaseTool:
    """ 
    Establishes functionality with Postgres Database 

    Assumptions:
        There already exists a postgresql database on the local system.
    
    Parameters:
        connect_to_db (bool) : Flag to connect to db in init.
    """

    def __init__(self, 
        db_user, db_user_pwd, db_nm, 
        db_host='localhost', db_port=5432, connect_to_db=True
    ):

        # set DB connect parameters
        self.db_user=db_user
        self.db_user_pwd=db_user_pwd
        self.db_nm=db_nm
        self.db_host=db_host
        self.db_port=db_port

        # connect to postgres DB
        if connect_to_db:
            self.con = connect_to_db(
                database=self.db_nm,
                user=self.db_user,
                password=self.db_user_pwd,
                host=self.db_host,
                port=self.db_port
            )
        else:
            self.con = None

    def connect_to_db(self, database_nm, db_user, db_user_pwd, db_host, db_port):
        """
        Establishes connection to postgres DB. Wrapper around psycopg2.connect().

        Note, this is a separate function in case the user wants to more methodical 
        about connecting to their database.

        Parameters:
            database_nm (str): name of database.
            db_user (str): name of user accessing the database.
            db_user_pwd (str): user password.
            db_host (str): database host (default is localhost).
            db_port (int): database port (default is 5432).

        Returns:
            psycopg2 Connect Object
        """
        return psycopg2.connect(
            database=database_nm,
            user=db_user,
            password=db_user_pwd,
            host=db_host,
            port=db_port
        )

    def song_in_db(self, song_id):
        """
        Checks if a song currently exists in database by unique song id.

        Parameters:
            song_id (int) : unique id of song we want to search

        Returns:
            dict : dictionary with song information (song id, song_format, etc)

        TODO: 
         - should existence of songs only be searchable by id?
        """
        pass

    def add_song(self, song_filepath, song_title, artist, album):
        """
        Adds raw audio file to database library.

        Parameters:
            song_filepath (str) : path to song to be uploaded to the database.
            song_title (str) : upload song title.
            artist (str) : upload song artist.
            album (str) : upload song album name.

        Returns:
            int : the unique ID of the song just added.
        """
        pass

    def remove_song(self, song_id):
        """
        Removes a song from database library.

        Parameters:
            song_id (int) : unique id of song we wish to delete.

        Returns:
            None : specified audio file and metadata are deleted from database.
        """
        pass

    def list_songs(self):
        """
        Output to stdout the current song list in database.

        Parameters:
            None

        Returns:
            None

        """
        pass

    def create_song_features(self, song_id, test_out=False):
        """
        Creates features from raw audio file.

        TODO: understand what these features can be.

        Parameters:
            song_id (int) : unique id of song for which we create features.
            test_out (bool) : lets function return the generated features for
                unit testing purposes.

        Returns:
            None : specified audio file and metadata are deleted from database.
        """
        pass

    def change_song_format(self, song_id, out_format):
        """
        Changes audio format of song_id to desired out_format.

        Parameters:
            song_id (int) : unique id of song for which we change format.
            out_format (str) : desired new format of song.

        Returns:
            None : new version of audio file in desired format will be written to DB.
        """
        pass

    def search_db(self, song_feat_vec):
        """
        Search for song by features.

        TODO: 
         - think more about if this function should go here.
         - what is the best data structure for the song feature vector?

        Parameters:
            song_feat_vec (tup) : vector of features for a song snippet.

        Returns:
            Name of closest song match in DB.
        """
        pass