
""" Smoke Plume
Hot smoke is emitted from a circular region at the bottom.
The simulation computes the resulting air flow in a closed box.
"""

from phi.flow import *  # minimal dependencies
# from phi.torch.flow import *
# from phi.tf.flow import *
# from phi.jax.flow import *

def mandel(re, im):
    return abs(iterate(lambda z: z**2 + re + im*ij, 30, 0))

plot(CenteredGrid(mandel, re=1000, im=1000, bounds=Box(re=(-1.5, .5),im=(-1, 1))))