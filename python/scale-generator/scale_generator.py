SHARP_NOTES = ['G', 'D', 'A', 'E', 'B', 'F#', 'e', 'b', 'f#', 'c#', 'g#', 'd#']
FLAT_NOTES = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd', 'g', 'c', 'f', 'bb', 'eb']
SHARP_SCALE = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
FLAT_SCALE = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

class Scale:

    def __init__(self, tonic):
        
        self.scale = None
        self.tonic = tonic

        self._set_scale()
        
        
    def _set_scale(self):
        if self.tonic in SHARP_NOTES or self.tonic == 'C' or self.tonic == 'a':
            self.scale = SHARP_SCALE
        elif self.tonic in FLAT_NOTES:
            self.scale = FLAT_SCALE
        else:
            raise ValueError(f'Tonic is not valid {self.tonic}')

    def chromatic(self):

        tonic_scaled = self.tonic[0].upper() + self.tonic[1] if len(self.tonic) > 1 else self.tonic[0].upper()
        
        tonic_index = self.scale.index(tonic_scaled)

        return self.scale[tonic_index:] + self.scale[:tonic_index]
        

    def interval(self, intervals):
        
        chromatic_scale = self.chromatic()

        helper_steps = self._helper_map(intervals)

        diatonic_scale = [chromatic_scale[step] for step in helper_steps]

        return diatonic_scale

    def _helper_map(self, intervals):

        helper_steps = [0]

        for step in intervals:

            if step == 'm':
                helper_steps.append(helper_steps[-1] + 1)
            elif step == 'M':
                helper_steps.append(helper_steps[-1] + 2)
            elif step == "A":
                helper_steps.append(helper_steps[-1] + 3)
            else:
                raise ValueError(f'Interval step is not valid: {step}. Must be "m", "M" or "A".')
            
        if helper_steps[-1] >= 12: helper_steps[-1] = 0

        return helper_steps
