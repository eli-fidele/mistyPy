
#===============================#
#    UNIVERSAL DECLARATIONS     #
#===============================#

# Chromatic base C scale, meaning C = 0
Chromatic = {0:'C',1:'C#',2:'D',3:'D#',4:'E',5:'F',6:'F#',7:'G',8:'G#',9:'A',10:'A#',11:'B'}

#===========================#
#     ANALYZER FUNCTION     #
#===========================#

# Chords is a harmonic reduction of a score; at every rythmic stop-point/bar, collapse that reigon into a chord.
# Follow the convention that chords are an unordered vector of semitones away from C4.
def analyze(chords, tonic):
	numerals = []
	for chord in chords:
		chord = retonicize(chord, tonic) # Retonicize chords by transposing C4 to the given tonic
		numeral = evaluate_numeral(chord, tonic)
		numerals.append(numeral)
	return numerals

def evaluate_numeral(chord, tonic):
	# Parse a static binary search tree automatically generated using inverions.py
	return numeral

def retonicize(chord, tonic):
	new_chord = chord
	for i in range(0,len(chord)):
		new_chord[i] = chord[i] + tonic
	return new_chord



#=======================#
#    HELPER METHODS     #
#=======================#

