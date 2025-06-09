from file_parse import *

from midiutil.MidiFile import MIDIFile
from scales import *


def calculate_duration(val):
    if val % 2 == 0:
        duration = 2
    elif val % 3 == 0:
        duration = 3
    elif val % 4 == 0:
        duration = 4
    else:
        duration = 1
    return duration


def create_midi_file(channel, volume, time, track, bpm, duration, scale, length):
    mf = MIDIFile(1)
    pitches_list = []

    mf.addTrackName(track, time, "Image Midi")
    mf.addTempo(track, time, bpm)

    # Assuming single_file(filename_hr) returns a list of RGB tuples - color photo
    pixel_data = single_file(filename_hr)

    for i in range(length):
        if i < len(pixel_data):  # safer than i <= length
            r, g, b = pixel_data[i]
            intensity = (r + g + b) / 3  # convert RGB to single value

            pitch = return_closest_pitch(allowed_pitches(scale), intensity / 3)  # adjust to your scale
            mf.addNote(track, channel, pitch, time, duration, volume)
            time += duration
            pitches_list.append(pitch)

    with open("output/" + filename_hr + ".mid", "wb") as outf:
        mf.writeFile(outf)

    print("Done!")
    print(pitches_list)
