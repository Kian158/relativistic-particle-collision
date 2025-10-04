import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

## we choose natural units of c = 1 for this simulation

p1 = np.array([5, -5 , 6])
p2 = np.array([3, 5, 8]) ## define two momentum vectors as 

## define rest masses of particles
m1 = 0.938 ## mass of proton in GeV / c^2
m2 = 0.000511 ## mass of electron in GeV / c^2

## define function to calculate total relativistic energy E = sqrt( px^2 +py^2 + pz^2 + m^2 )
def totalEnergy(p, m):
    return np.sqrt((np.dot(p,p) + m**2))

E1 = totalEnergy(p1, m1)
E2 = totalEnergy(p2, m2)

## define function to find 4 momentum vector, being (E, px, py, pz)
def fourMomentum(p, m):
    return np.array([totalEnergy(p, m), p[0], p[1], p[2]])

## find velocity of centre of mass of system
vCOM = (p1 + p2) / (totalEnergy(p1, m1) + totalEnergy(p2, m2)) ## we take as beta vector as c = 1 in our units

B = np.sqrt( np.dot(vCOM, vCOM) ) ## magnitude of vCOM vector
gamma = 1 / (np.sqrt(1 - B**2)) ## calculate gamma / lorentz factor

def lorentz_boost(p, E, vCOM):
    if B == 0:
        return p, E ## no boost needed
    else:

        Eprime = gamma * (E - np.dot(vCOM, p)) ## calculate new energy
        pprime = p + vCOM* ( ((gamma - 1) * np.dot(vCOM, p ) / (B**2) ) - gamma*E)

        return pprime, Eprime

p1_prime, E1_prime = lorentz_boost(p1, E1, vCOM)
p2_prime, E2_prime = lorentz_boost(p2, E2, vCOM) ## lorentz boost data


ptot = p1_prime + p2_prime
s = (E1_prime + E2_prime)**2 - np.dot(ptot, ptot) ## calculate the mandelstam variable (total invariant mass squared)

p_star = np.sqrt ( (( s - (m1 + m2)**2 ) * ( s - (m1 - m2)**2 ) ) / (4 * s) ) ## the magnitude of both resultant momentum vectors

## we pick a random vector for the first outgoing particle
N = np.array([ np.random.rand(), np.random.rand(), np.random.rand()])

n = N / np.sqrt(np.dot(N, N)) ## make it a unit vector

p1_out = p_star * n
p2_out = p_star * n * -1 ## calculate output momenta from p* and our random vector

E1_out = totalEnergy(p1_out, m1)
E2_out = totalEnergy(p2_out, m2) ## calculate new resultant energies

p1_final, E1_final = lorentz_boost(p1_out, E1_out, -vCOM)
p2_final, E2_final = lorentz_boost(p2_out, E2_out, -vCOM) ## lorentz boost back to original reference frame

def plot_vectors(vectors, colors, labels, title='Particle Momenta'):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for v, c, label in zip(vectors, colors, labels):
        ax.quiver(0, 0, 0, v[0], v[1], v[2], color=c, label=label, arrow_length_ratio=0.1)

    ax.set_xlim([-max_mom, max_mom])
    ax.set_ylim([-max_mom, max_mom])
    ax.set_zlim([-max_mom, max_mom])

    ax.set_xlabel('Px')
    ax.set_ylabel('Py')
    ax.set_zlabel('Pz')
    ax.set_title(title)
    ax.legend()
    plt.show()


vectors = [p1, p2, p1_final, p2_final]
colors = ['cyan', 'blue', 'yellow', 'red']
labels = ['Before particle 1', 'Before particle 2', 'After particle 1', 'After particle 2']

max_mom = max(np.linalg.norm(v) for v in vectors) * 1.2

plot_vectors(vectors, colors, labels)


