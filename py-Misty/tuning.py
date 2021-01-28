import scales
import numpy

Chromatic_C = {0:'C',1:'C#',2:'D',3:'D#',4:'E',5:'F',6:'F#',7:'G',8:'G#',9:'A',10:'A#',11:'B'}

# Creates a General Pitch Continuum
class Continuum:
    def __init__(self, lowest, highest):
        self.lowest = lowest
        self.highest = highest
    # Helper function for appending all pitches in a tuned continuum up to 8ve equivalency
    def contained(self, pitch): return (pitch >= self.lowest) and (pitch <= self.highest)

class Tuning(Continuum):
    def __init__(self, lowest, highest, root):
        self.lowest = lowest
        self.highest = highest
        self.root = root
        self.pitches = []
        self.continuum = []
        self.octaves = []
        # Recall if the system was tuned. Only allow for one instance of tuning
        self.tuned = False
    def tuneTET(self, N):
        pitches = []
        # Append the root scale pitches in an n-TET system
        for i in range(0,N):
            pitches.append(self.root*(2**(i/N)))
        # Keep track of tuning status
        if(not self.tuned):
            # Add root scale pitches
            self.pitches = pitches
            # Tune the continuum upto that root scales octave equivalent pitches
            self.octaves = self.tuneContinuum()
            self.continuum.sort()
            self.tuned = True
    # Once the root scale pitches are generated, tune the Continuum up to 8ve equivalency
    def tuneContinuum(self):
        # Hold values for octave tuple for each pitch
        octaves = []
        for pitch in self.pitches:
            self.continuum.append(pitch)
            # Initialize placeholder octave counters
            curr_lowest, curr_highest = 0,0
            # Find lower notes
            curr = pitch
            while self.contained(curr/2):
                self.continuum.append(curr)
                # Make current note octave lower and update register
                curr = curr/2
                curr_lowest += 1
            # Find higher notes
            curr = pitch
            while self.contained(curr*2):
                self.continuum.append(curr)
                # Make current note octave lower and update register
                curr = curr*2
                curr_highest += 1
            # Append that pitches octave extrema tuple
            octaves.append((curr_lowest,curr_highest))
        return octaves

# Returns a square tuning matrixx
def tuningMatrix(pitches):
    # Get number of pitches
    N = length(pitches)
    matrix = []
    for i in range(0,N):
        row = []
        for j in range(0,N):
            row.append(pitches[j]/pitches[i])
        matrix.append(row)
    return matrix



#=======================#
#    TESTING SECTION    #
#=======================#
