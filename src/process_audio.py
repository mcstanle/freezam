'''
Classes and functions to provide the audio processing functionality.
Broadly, the code in this file should do the following:
1. Apply a window function to an audio file.
2. Compute local periodograms from windowed signal.
3. Smooth Periodograms.
4. Compute window signature.

===============================================================================

Author:        Mike Stanley
Created:       September 28, 2019
Last Modified: September 28, 2019

===============================================================================

TODO:
1. How do we deal with the left and right signal?
2. Understand the output of the create_windows function.
3. finish the periodogram function
4. start the signatures function

'''

class process_audio:
    """
    Class to configure audio processing pipeline. This pipeline should include 
    functions that:
    - produce a windowed time series
    - compute periodogram of windowed time series
    - compute signatures of windowed time series

    Note, this class doesn't have any read capabilities because that taks is 
    handled by the database class.
    """
    def __init__(self, window_type, window_size, window_shift):
        self.window_type=window_type
        self.window_size=window_size
        self.window_shift=window_shift


    def create_windows(self, data, fs):
        """
        Created a windowed time series from data. 

        Parameters:
            data (numpy array) : 2 column numpy array with L and R signals
            fs (int) : frequency sample

        Returns:
            ????
        """
        pass

    def create_periodogram(self, single_window):
        """
        Given a single window of a time series, computes the periodogram.

        Parameters:
            single_window (numpy array) : 
        """
        pass