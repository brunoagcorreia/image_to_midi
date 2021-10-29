

from midiutil.MidiFile import MIDIFile





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


#create_midi_file()
print(sum(single_file(filename=filename)) / len(single_file(filename)))