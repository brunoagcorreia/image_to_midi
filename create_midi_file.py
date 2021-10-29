

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