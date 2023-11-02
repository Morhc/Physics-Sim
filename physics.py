from numpy import sum, zeros

import tools

#in SI units
G = 6.673e-11
k = 8.988e9

def gravity(p1,p2,r12): return G * p1.get('m') * p2.get('m') / (r12 ** 2)
def electricity(p1,p2,r12): return -k * p1.get('q') * p2.get('q') / (r12 ** 2)

def Forces(origin, *particles):
    '''Calculates the gravitational force.
    Parameters
    ----------
    origin :: a numpy array of what the zero point of the frame is
    particles :: particle.Particle() objects

    Returns
    ----------
    forces :: an Nx3 array of the forces felt by object N in the x,y,z directions
    '''

    num_particles = len(particles)

    force = zeros(( num_particles, num_particles, 3 ))

    pairs = []
    for i, particle in enumerate(particles):
        for j, other in enumerate(particles):
            if i == j: continue
            pair = (i,j)

            if pair in pairs or pair[::-1] in pairs: continue

            r12, r12hat = tools.vector(particle, other, 'pos')

            '''
            TO-DO: force field with respect to an origin?
            rhat = r12hat + ro1hat 
            '''

            F = gravity(particle,other,r12) + electricity(particle,other,r12)

            force[i][j] = F*r12hat
            force[j][i] = -F*r12hat

            pairs.append(pair)

    forces = sum(force, axis=1)

    return forces
