from numpy import array

import particle
import physics

origin = array([0,0,0])

trucks = particle.Particle(5e10, 10,0,0)
more_trucks = particle.Particle(5e10, 0,0,0)
photon = particle.Particle(0, 0,0,10)

forces = physics.Forces(origin, trucks, more_trucks, photon)
print('The force components felt between trucks, more trucks, and a photon.')
print(forces)


electrons = []
for i in range(4):
    e = particle.Particle(9.11e-31, 0,0,i)
    e.set('q', -1)
    electrons.append(e)

forces = physics.Forces(origin, electron, electron2)
print('The force components felt between electrons.')
print(forces)
