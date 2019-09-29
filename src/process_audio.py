"""
Classes and functions to provide the audio processing functionality.
Broadly, the code in this file should do the following:
1. Apply a window function to an audio file.
2. Compute local periodograms from windowed signal.
3. Smooth Periodograms.
4. Compute window signature --> this is handled by signatureGenerator

===============================================================================

Author:        Mike Stanley
Created:       September 28, 2019
Last Modified: September 29, 2019

===============================================================================

TODO:
1. How do we deal with the left and right signal?
2. Understand the output of the create_windows function.
3. finish the periodogram function
4. start the signatures function
5. add additional signature methods to signatureGenerator

"""

class signatureGenerator:
    """
    Compute signature for periodogram. Several signature schemes will be
    handled in this function corresponding to some of the options in the 
    original pdf.

    1. unsmoothed
    2. smoothed
    ...
    """
    def __init__(self, signature_type):
        self.signature_type=signature_type

    def unsmooth_signature(self, inp_periodogram):
        """
        For signature_type='unsmoothed', finds the unsmoothed periodogram.

        Parameters:
            inp_periodogram (numpy array) : periodgram to be processed

        Returns:
            unsmooted periodogram
        """
        pass

    def smooth_signature(self, inp_periodogram):
        """
        For signature_type='smoothed', finds the smoothed periodogram.

        Parameters:
            inp_periodogram (numpy array) : periodgram to be processed

        Returns:
            smooted periodogram
        """
        pass

        #TODO: add more signature methods

    def generate_signature(self, periodogram):
        """
        Wrapper around all the above signature generating functions.

        Parameters:
            audio_ts (numpy array): periodogram for which we'll generate signature

        Returns:
            generated signature (output varies)
        """
        ### series of elif statements
        pass


class processAudio:
    """
    Class to configure audio processing pipeline. This pipeline should include 
    functions that:
    - produce a windowed time series
    - compute periodogram of windowed time series
    - compute signatures of windowed time series

    Note, this class doesn't have any read capabilities because that taks is 
    handled by the database class.
    """
    def __init__(self, 
        window_type, window_size, window_shift, 
        signature_type
    ):
        self.window_type=window_type
        self.window_size=window_size
        self.window_shift=window_shift
        self.signature_generator=signatureGenerator(signature_type)


    def create_windows(self, data, fs):
        """
        Created a windowed time series from data. 

        Parameters:
            data (numpy array) : 2 column numpy array with L and R signals
            fs (int) : frequency sample

        Returns:
            windowed time series (list of numpy arrays)
        """
        pass

    def create_periodogram(self, single_window):
        """
        Given a single window of a time series, computes the periodogram.

        Parameters:
            single_window (numpy array) : 
        """
        pass

    def create_signature(self, audio_ts):
        """
        Produces a signature given an audio_ts.

        Parameters:
            audio_ts (numpy array) : time series for which we create a signature

        Returns:
            low dimensional signature (output varies depending upon signature type)
        """
        pass