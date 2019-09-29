'''
Unit tests for process_audio components.

===============================================================================
Author:        Mike Stanley
Created:       September 28, 2019
Last Modified: September 29, 2019

===============================================================================

TODO:
1. create some local periodograms in which we can test signatureGenerator.
2. need to figure out how to save periodograms to be read in.
3. add signature types to list as we continue to build signature functionality.
4. determine how window data will be stored.
5. think about how the window data is going into create_periodogram method

'''

import pytest

from process_audio import signatureGenerator, processAudio
from utils import read_periodogram, read_song

# Constants
PERIODOGRAM_FILEPATH = '/this/is/a/file/path/to/periodogram'
SIGNATURE_TYPES_LIST = ['unsmoothed', 'smoothed']
WINDOW_DATA_FILEPATH = '/filepath/to/window/data'
SAMPLE_SIGNATURE_FILEPATH = '/filepath/to/signature'
SAMPLE_SONG_FILEPATH = '/this/is/a/filepath/to/a/song'

WINDOW_TYPE='blackman'
WINDOW_SIZE=1234
WINDOW_SHIFT=10


### signatureGenerator 
def test_signatureGenerator():
    
    # read in periodogram
    test_periodogram = read_periodogram(PERIODOGRAM_FILEPATH)

    # create signature generator object
    sig_gen = signatureGenerator(signature_type)

    # test unsmooth signature method
    assert sig_gen.unsmooth_signature(test_periodogram)

    # test smooth signature method
    assert sig_gen.smooth_signature(test_periodogram)

    # TODO -- add more tests here accordingly

    # test generate_signature method
    for signature_type in SIGNATURE_TYPES_LIST:
        
        # instantiate an object
        sig_gen = signatureGenerator(signature_type)

        # generate signature with above object
        signature = sig_gen.generate_signature(test_periodogram)

        assert # signature has some properties

def test_processAudio():

    # instantiate the object
    proc_audio = processAudio(
        window_type=WINDOW_TYPE,
        window_size=WINDOW_SIZE,
        window_shift=WINDOW_SHIFT,
        signature_type=SIGNATURE_TYPES_LIST[0]
    )

    # read in some audio data
    data, fs = read_song(SAMPLE_SONG_FILEPATH)

    # creating windows
    sample_window_data = function_to_read_window_data(WINDOW_DATA_FILEPATH)
    created_window_data = proc_audio.create_windows(data, df)
    assert created_window_data == sample_window_data #TODO -- I'm sure this will have to be changed

    # creating periodogram
    sample_periodogram = read_periodogram(PERIODOGRAM_FILEPATH)
    created_periodogram = proc_audio.create_periodogram(sample_window_data)
    assert sample_periodogram == created_periodogram

    # creating signature
    sample_signature = read_signature(SAMPLE_SIGNATURE_FILEPATH) #TODO -- write this function
    created_signature = proc_audio.create_signature(data)
    assert sample_signature == created_signature