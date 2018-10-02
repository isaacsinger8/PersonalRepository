

```python
from scipy.constants import Boltzmann as kB_sc # I've imported the unitless value for kB from SciPy

kB = kB_sc * u.joule / u.kelvin # I've given kB units for you in J/K; you can use the kB variable to give you Boltzmann's constant with units

import math from aide_design.play import *

def stokesEinsteinEquation(T, r, v):
  Temperature = T * u.kelvin
  particle_radius = r * u.meters
  viscosity = v * u.kilograms/u.meters/u.seconds
  D = (kB * T)/(6 * pi)(v)(r)

  stokesEinsteinEquation(100, 1, 20)
