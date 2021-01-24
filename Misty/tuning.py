import scales

Chromatic_C = {0:'C',1:'C#',2:'D',3:'D#',4:'E',5:'F',6:'F#',7:'G',8:'G#',9:'A',10:'A#',11:'B'}

# Creates a General Pitch Continuum
class Continuum:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def contained(self, pitch): return (pitch >= self.lower) and (pitch <= self.upper)

class Tuning(Continuum):
    def __init__(self, lower, upper, root):
        self.lower = lower
        self.upper = upper

#=======================#
#    TESTING SECTION    #
#=======================#
