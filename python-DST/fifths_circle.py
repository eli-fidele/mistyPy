C_notes = {0:'C',1:'C#',2:'D',3:'D#',4:'E',5:'F',6:'F#',7:'G',8:'G#',9:'A',10:'A#',11:'B'}
class Scale():
    def __init__(self, notes):
        self.notes = notes
        self.MAJ = [0,2,4,5,7,9,11,0]
        self.MIN = [0,2,3,5,7,8,10,0]
        #Major and Minor Chord Triads
        self.MAJ_Triad = self.make_chord([0,4,7])
        self.MIN_Triad = self.make_chord([0,3,7])
    def print_scale(self, ls_idx):
        for idx in ls_idx:
            print(self.notes[idx])
    def make_chord(self,ls_idx):
        chord = {}
        for idx in ls_idx:
            chord[idx] = (self.notes[idx])
        return chord
    def print_chord(self, chord):
        for key in chord:
            print(chord[key])
def transpose_notes(notes, k):
    i = 0
    t_notes = {}
    while i < 12:
        t_notes[i] = notes[(i+k)%12]
        i += 1
    return t_notes

C = Scale(C_notes)
#C.print_scale(C.MAJ)

#D_notes = transpose_notes(C_notes, 2)
#D = Scale(D_notes)

def fifths_circle():
    circle = {}
    i = 0
    while i < 12:
        curr = (7*i)%12
        circle[i] = C.notes[curr]
        MAJ = []
        MAJ.append(C.notes[(curr + 0)%12])
        MAJ.append(C.notes[(curr + 4)%12])
        MAJ.append(C.notes[(curr + 7)%12])
        print(MAJ)
        MAJ = []
        i += 1
    return circle

notes_fifths = fifths_circle()
#print(notes_fifths)
