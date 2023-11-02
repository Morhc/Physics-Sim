from numpy import array

class Particle:

    def __init__(self, m, x, y, z):
        '''At the moment, I am using SI units.
        '''

        #position, velocity, acceleration
        self.features = {'pos': array([x, y, z]),
                         'vel': array([0, 0, 0]),
                         'accel': array([0, 0, 0]),

                         'm': m,
                         'q': 0,
                         }

    def get_keys(self):
        return list(self.features.keys())

    def get(self, key):
        return self.features[key]

    def set(self, key, value):
        self.features[key] = value
