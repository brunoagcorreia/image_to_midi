# provides methods that result in scales to be used in main.py

pitches = {  # pitches based on central C (C4).
    'C': 48,
    'C#': 49,
    'D': 50,
    'D#': 51,
    'E': 52,
    'F': 53,
    'F#': 54,
    'G': 55,
    'G#': 56,
    'A': 57,
    'A#': 58,
    'B': 59
}


def allowed_pitches(scale):  # which pitches are allowed per scale (only support Cmaj atm)
    allowed_pitches_list = []

    if scale == 'Cmaj' or scale == 'cmaj':
        notes_in_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

    if scale == 'Dmaj' or scale == 'dmaj':
        notes_in_scale = ['C#', 'D', 'E', 'F#', 'G', 'A', 'B']

    for note in notes_in_scale:
        allowed_pitches_list.append(pitches[note])

    return allowed_pitches_list


def return_closed_pitch(pitches_to_allow, pitch):
    return min(pitches_to_allow, key=lambda x: abs(x - pitch))




_pitch_ = (152.231234 / 3)

print(return_closed_pitch(allowed_pitches('Cmaj'), _pitch_))
