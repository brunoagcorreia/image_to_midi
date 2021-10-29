import os
from PIL import Image
from midiutil.MidiFile import MIDIFile

path = "img"
filename = "test_g.jpg"

# Value creating
def single_file(filename):
    im = Image.open(path + "/" + filename, 'r')
    pix_val = list(im.getdata())
    return pix_val

def multi_file(path):
    for filename in os.listdir(path):
        im = Image.open(path + "/" + filename, 'r')
        pix_val = list(im.getdata())
    return pix_val

def mode(filename):
    im = Image.open(path + "/" + filename, 'r')
    return im.mode

def get_tempo(l):
    average = sum(l) / len(l)
    tempo = round(average)
    return tempo

def print_val(num):
    for val in single_file(filename):
        if (val % num == 0):
            val = int(val / 2)
            print(val)

def calculate_duration(val):
    if (val % 2 == 0):
        duration = 2
    elif (val % 3 == 0):
        duration = 3
    elif (val % 4 == 0):
        duration = 4
    else:
        duration = 1
    return duration


# Midi creation
mf = MIDIFile(1)
track = 0
time = 0
tempo = get_tempo(single_file(filename))

mf.addTrackName(track, time, "Test1")
mf.addTempo(track, time, tempo)

def create_midi_file():
    channel = 0
    volume = 100
    time = 0

    for i in range(200):
        duration = calculate_duration(int(single_file(filename)[i]))
        pitch = (int(single_file(filename)[i] / 3))
        mf.addNote(track, channel, pitch, time, duration, volume)
        time += duration

    with open("output.mid", "wb") as outf:
        mf.writeFile(outf)

    print("Done!")

create_midi_file()