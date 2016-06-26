#Written by Dylan Zeng
#some codes inspired by Sherri

import tones

tones.setup()

note = input("enter note: ")
while note != 'q':
    note = float(note)
    if note >= 0.0 and note <= 0.5 or note >= 1.0 and note <= 1.5 or note == 2.0 : 
        pitch = int(note)*6 + ((note - int(note))*10)
        length = input("enter the length of the note: ")
        pause = input("enter the length of the pause: ")
        tones.addNote ( int(pitch), int (length))
        tones.addPause ( int(pause))
        note = input("enter note: ")
    else:
        print("wrong note, try a new one plz")
        note = input("enter note: ")

tones.closefile()


