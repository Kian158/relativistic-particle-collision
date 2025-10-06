# Relativistic Particle Collision

This Python code simulates the collision of two particles using relativistic methods, and then visualises the outcome with a 3D plot.
This project taught me a lot, as I have not formally learned relativity in school / university. I wanted to prove my understanding to myself with this simulation, and quickly found gaps in understanding. I finally understand Lorentz boosting and it's purpose.

<img width="410" height="423" alt="download" src="https://github.com/user-attachments/assets/17799c35-95fa-417c-a15b-72325d95fdc9" />

# Algorithm 
- The initial momenta are defined as 3 vectors in NumPy arrays, along with mass
- The total energies are calculated
- The 4 momentum vectors are deduced, being (E, px, py, pz)
- The velocity of the centre of mass is calculated, and then all velocities are Lorentz boosted to this
- The resultant energies and momenta are calculated
- We Lorentz boost back into the initial reference frame
- The results are plotted.

# Tools used
- NumPy
- Matplotlib
  

