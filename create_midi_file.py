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

def map_intensity_to_pitch(allowed, intensity):
    index = int((intensity / 255) * (len(allowed) - 1))
    return allowed[index]

def create_midi_file(channel, volume, time, track, bpm, duration, scale, length):
    mf = MIDIFile(1)
    pitches_list = []

    mf.addTrackName(track, time, "Image Midi")
    mf.addTempo(track, time, bpm)

    # Assuming single_file(filename_hr) returns a list of RGB tuples - color photo
    pixel_data = single_file(filename_hr)
    
    #sets regular intervals for pixels from image according to lenght
    interval = len(pixel_data)/length
    
    # array containing all selected pixels from image
    pixel_param = []

    for i in range(length):
        # populate array of selected pixels from image
        pixel_param.append(pixel_data[i * int(interval)])

    allowed = allowed_pitches(scale)

    for i in range(length):
        if i < len(pixel_param):
            r, g, b = pixel_param[i]
            intensity = (r + g + b) / 3  # range: 0–255

            pitch = map_intensity_to_pitch(allowed, intensity)

            mf.addNote(track, channel, pitch, time, duration, volume)
            time += duration
            pitches_list.append(pitch)

    with open("output/" + filename_hr + ".mid", "wb") as outf:
        mf.writeFile(outf)

    print(pitches_list)
    print("Done!")