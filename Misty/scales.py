
#===============================#
#    UNIVERSAL DECLARATIONS     #
#===============================#

# Chromatic base C scale, meaning C = 0
Chromatic = {0:'C',1:'C#',2:'D',3:'D#',4:'E',5:'F',6:'F#',7:'G',8:'G#',9:'A',10:'A#',11:'B'}

#======================#
#    SCALE CLASSES     #
#======================#

# Basic scales inputs a dictionary/mapping (notes) as its main input
class Scale():
    def __init__(self, notes):
        self.notes = notes
    # Makes a chord out of the scale degrees of the scale's notes
    def make_subscale(self,ls_idx):
        chord = {}
        for idx in ls_idx:
            chord[idx] = (self.notes[idx])
        return Scale(chord)
    # Prints the notes of the scale
    def print_notes(self, ls_idx = None):
        # If no subscale is chosen, print the entire scale
        if(ls_idx == None):
            for idx in self.notes.keys():
                print(self.notes[idx])
        # If a subscale is chosen, print the specified subscale
        else:
            for idx in ls_idx:
                print(self.notes[idx])

# Given a root, returns a full circle of fifths
class Fifths(Scale):
    # Initialize a complete circle of fifths given a root (base C)
    def __init__(self, root):
        self.notes = self.fifths_circle(root)

    # Wind up a circle of fifths given a root
    def fifths_circle(self, root):
        # Transpose a Chromatic scale to a given root
        CHROM = transpose_notes(Chromatic, root)
        # Create a circle of fifths given a same-root Chromatic scale
        circle = {}
        i = 0
        while i < 12:
            curr = (7*i)%12
            circle[i] = CHROM[curr]
            i += 1
        return circle

# Also allows extraction of the Diatonic Scales as Scale objects
class Diatonic(Scale):
    def __init__(self, root):
        # Initializes a Chromatic Scale by transposing the C-scale to the wanted root
        self.notes = transpose_notes(Chromatic, root)

    def make_MAJ(self):
        MAJ = [0,2,4,5,7,9,11,0]
        return self.make_subscale(MAJ)

    def make_MIN(self):
        MIN = [0,2,3,5,7,8,10,0]
        return self.make_subscale(MIN)

    def make_triad(self):
        # Returns first, third, and fifth element of a Diatonic Scale
        return self.make_subscale([0,2,4])

#=======================#
#    HELPER METHODS     #
#=======================#

# Transposes notes given a key, assuming Chromatic scale starts at C = 0
def transpose_notes(notes, k):
    transposed = {}
    i = 0
    while i < 12:
        # Transposes a 12-note scale using modular arithmetic of list indexing
        transposed[i] = notes[(i+k)%12]
        i += 1
    return transposed
