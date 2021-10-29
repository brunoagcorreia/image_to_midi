# provides methods that result in scales to be used in main.py

pitches = {  # pitches based on central C (C4).
    'C': 48,
    'C#': 49,
    'Db': 49,
    'D': 50,
    'D#': 51,
    'Eb': 51,
    'E': 52,
    'F': 53,
    'F#': 54,
    'Gb': 54,
    'G': 55,
    'G#': 56,
    'Ab': 56,
    'A': 57,
    'A#': 58,
    'Bb': 58,
    'B': 59
}


def allowed_pitches(scale):  # which pitches are allowed per scale (only support Cmaj atm)
    allowed_pitches_list = []

    if scale == 'Cmaj' or scale == 'cmaj' or scale == 'Amin' or scale is 'amin':
        notes_in_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

    if scale == 'Dmaj' or scale == 'dmaj' or scale == 'Bmin' or scale is 'bmin':
        notes_in_scale = ['C#', 'D', 'E', 'F#', 'G', 'A', 'B']

    if scale == 'Emaj' or scale == 'emaj' or scale == 'C#min' or scale is 'c#min':
        notes_in_scale = ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']

    if scale == 'Fmaj' or scale == 'fmaj' or scale == 'Dmin' or scale is 'dmin':
        notes_in_scale = ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'Bb']

    if scale == 'Gmaj' or scale == 'gmaj' or scale == 'Emin' or scale is 'emin':
        notes_in_scale = ['C', 'D', 'E', 'F#', 'G', 'A', 'B']

    if scale == 'Amaj' or scale == 'amaj' or scale == 'F#min' or scale is 'f#min':
        notes_in_scale = ['C#', 'D', 'E', 'F#', 'G#', 'A', 'B']

    if scale == 'Bmaj' or scale == 'bmaj'or scale == 'G#min' or scale is 'g#min':
        notes_in_scale = ['C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B']

    if scale == 'C#maj' or scale == 'c#maj' or scale == 'A#min' or scale is 'a#min':
        notes_in_scale = ['C', 'Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb']

    if scale == 'D#maj' or scale == 'd#maj' or scale == 'Cmin' or scale is 'Cmin':
        notes_in_scale = ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb']

    if scale == 'F#maj' or scale == 'f#maj' or scale == 'D#min' or scale is 'd#min':
        notes_in_scale = ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'B']

    if scale == 'G#maj' or scale == 'g#maj' or scale == 'Fmin' or scale is 'fmin':
        notes_in_scale = ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'Bb']

    if scale == 'A#maj' or scale == 'a#maj' or scale == 'Gmin' or scale is 'gmin':
        notes_in_scale = ['C', 'D', 'Eb', 'F', 'G', 'A', 'Bb']

    for note in notes_in_scale:
        allowed_pitches_list.append(pitches[note])

    return allowed_pitches_list


def return_closed_pitch(pitches_to_allow, pitch):
    return min(pitches_to_allow, key=lambda x: abs(x - pitch))



print(allowed_pitches('Cmaj'))
