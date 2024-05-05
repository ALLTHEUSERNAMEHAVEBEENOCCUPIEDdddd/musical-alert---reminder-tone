import winsound
import time


def musik():
    note_frequencies = {
        '1': 262*2,  # Middle C
        '2': 294*2,  # D
        '3': 330*2,  # E
        '4': 349*2,  # F
        'f': 370*2,  # F# (fa#)
        '5': 392*2,  # G
        's': 415*2,  # G# (so#)
        '6': 440*2,  # A
        '7': 494*2,  # B
        'C': 523*2,  # High C
        'D': 587*2,  # High D
        'E': 659*2,  # High E
        'F': 698*2,  # High F
        'G': 784*2,  # High G
        'A': 880*2,  # High A
    }

    # (music) paraphrase
    score = "6--6-C-7-6-6---4---7---6--6--3-6-6-6-s-6-7-----7-7C7-6-7-C-----6--6-C-7-6-6---4---7---6---6--3-6-6-6-s-6-7---s--6-s-f-s-6-----F---E-D-C-7-6---E---A-----"
    notes = []
    duration = 55  # The duration of each note

    for char in score:
        if char in note_frequencies:
            notes.append((note_frequencies[char], duration))
        elif char == '-':
            if notes:
                notes[-1] = (notes[-1][0], notes[-1][1] + duration)  # Extend the duration of the previous note

    # 播放音乐
    for freq, dur in notes:
        winsound.Beep(freq, dur)
        time.sleep(0.015)  # Short intervals make the melody more coherent
