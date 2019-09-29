'''
Utility functions that can be shared across all code.

===============================================================================
Author:        Mike Stanley
Created:       September 29, 2019
Last Modified: September 29, 2019

===============================================================================

TODO:
1. Might want to consider making read_song a class so that it can have several
   different methds available.
2. research how to programmatically convert between audio formats

'''

# import numpy as np

class convertAudio:
    """
    Class to programmatically convert between two audio file types.

    This function might not be necessary...but does reflect some desired 
    functionality.

    """
    def mp3_to_wav(self, audio_file_path):
        """
        mp3 to wav conversion

        TODO: I'm not sure how this will work. Will I read in as an mp3 and then 
        convert to wav? Will I call another application that converts the mp3 to
        wav and then import the wav file?
        """
        pass

def read_song(song_filepath):
    """
    Read in a song given a filepath.

    Parameters:
        song_filepath (str) : location of song to be read in

    Returns:
        two channel audio numpy array and sampling frequency.
    """
    pass

def read_periodogram(periodogram_filepath):
    """
    Will likely only be used for testing.

    Parameters:
        periodogram_filepath (str) : location of periodogram to read in.

    Returns:
        the periodogram
    """
    pass