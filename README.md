# Purpose
This code is meant to be a stripped down version of the capabilities that power the Shazam app. 

# Broad Components
There are three primary parts to this code:
1. Database Tool

···Move and do things with data

2. Audio Processing

···Manipulate and create features from audio files.

3. Matching

···Match audio snippet to correct song in database (this is the key functionality)

## Database Tool
Importantly, this portion of the code is not a database in and of itself, but rather it should 
hook into an actual database either on the local machine where the code is being run, or to a
database on a server somewhere. This module should have the following functionality:
1. List all current songs in DB.
2. Add songs to DB - note that each audio file that is added should include other song 
information as well.
3. Remove songs from DB.
4. Generate song features - this functionality will be a wrapper around an audio processing
object (see below).
5. Change song audio formats. 
6. Search capability.

## Audio Processing
Features of songs will be generated by this portion of the code. More specifically:
1. Apply a window function to an audio file.
2. Compute local periodograms from windowed signal.
3. Smooth periodograms.

## Matching
The flagship functionality of this app, this module will accept a song snippet, call the
audio processing module to generate features, and then call the database object to search
against current library.