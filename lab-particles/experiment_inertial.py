from view import *
import math

n = 20
particles = []
for i in range(n):
    theta = i*2*math.pi/n
    u = Vec(math.cos(theta),math.sin(theta))
    pos = 10 * u
    vel = -1 * u 
    particles.append(Particle(1,pos,vel,0.2))

def no_force(dt,particles):
    pass

def combined_walls(dt, particles):
    k = 100.0
    #left, top, right, bottom
    a = [Vec(-8,0), Vec(0,8), Vec(8,0),  Vec(0,-8)]
    n = [Vec(10,0),  Vec(0,-10), Vec(-10,0), Vec(0,10)]

    """  a_left,n_left = Vec(-8,0), Vec(2,0)
    a_top,n_top = Vec(0,8), Vec(0,-2)
    a_right,n_right = Vec(8,0), Vec(-2,0)
    a_bottom,n_bottom = Vec(0,-8), Vec(0,2) """

    for i in range(4):
        wall_force(dt, particles, k, n[i], a[i])



simulation_loop(combined_walls, 0.00005, particles)
