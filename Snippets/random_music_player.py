import quantumrandom
import glob
import os
import natsort
import uuid
import math
import time
import subprocess
import copy

# From https://stackoverflow.com/questions/3844430/how-to-get-the-duration-of-a-video-in-python
def get_length(filename):

    """
    Function to get length of a media file

    Parameters
    ----------
    filename : string
        Filename of the file

    Returns
    -------
    duration : float
        Duration in seconds of the file
    
    """

    result = subprocess.run(["ffprobe",
                             "-v",
                             "error",
                             "-show_entries",
                             "format=duration",
                             "-of",
                             "default=noprint_wrappers=1:nokey=1",
                             filename],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)

    duration = float(result.stdout)

    return duration

# Uses the true random number generator from Australia National University
# Requires Internet to work
# Otherwise default to using uuid4
def generate_seed(track_total):
    
    """
    Function to get length of a media file

    Parameters
    ----------
    track_total : int
        Total number of tracks

    Returns
    -------
    seed : int
        Randomly generated file index
    
    """

    seed = 0
    try:
        seed = quantumrandom.randint(0, track_total - 0.5)
        seed = int(math.floor(seed))

    except:
        print("No Internet")
        print("Using the uuid4 instead")
        seed = (uuid.uuid4().int)
        seed = seed%(track_total + 1)

    return seed

# Some way to identify which tracks do you want to play
glob_key = "*.mp3"
file_list = natsort.natsorted(glob.glob(glob_key))
track_total = (len(file_list))
repeat_last = False
minimize = True
vlc_path = "/usr/bin/vlc"
cvlc_path = "/usr/bin/cvlc"

last_seed = 0
seed = 0

while True:

    seed = generate_seed(track_total)

    # Failsafe
    if seed >= track_total or seed < 0:
        seed = generate_seed(track_total)

    if repeat_last == False:
        while seed == last_seed:
            seed = generate_seed

    filename = file_list[seed]
    duration = get_length(filename)

    FNULL = open(os.devnull, 'w')
    # if you want to have it minimized
    if minimize == False:
        p = subprocess.Popen([vlc_path,filename],
                              stdout=FNULL,
                              stderr=subprocess.STDOUT)
    else:
        p = subprocess.Popen([cvlc_path, filename],
                              stdout=FNULL,
                              stderr=subprocess.STDOUT)

    time.sleep(duration)
    p.terminate()
    last_seed = copy.deepcopy(seed)