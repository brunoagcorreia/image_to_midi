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


def create_midi_file(channel, volume, time, track, bpm, duration, scale):
    mf = MIDIFile(1)
    pitches_list = []

    mf.addTrackName(track, time, "Test1")
    mf.addTempo(track, time, bpm)

    for i in range(1580):
        pitch = return_closest_pitch(allowed_pitches(scale), int(single_file(filename_hr)[i]) / 3)
        mf.addNote(track, channel, pitch, time, duration, volume)
        time += duration
        pitches_list.append(pitch)

    with open("output.mid", "wb") as outf:
        mf.writeFile(outf)

    print("Done!")
    print(pitches_list)
