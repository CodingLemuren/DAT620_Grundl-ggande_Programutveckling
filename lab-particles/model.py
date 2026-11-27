import math

class Vec:
	def	__init__(self, x, y):
		self.x = x
		self.y = y

	def	__repr__(self):
		return f"({self.x}, {self.y})"

	def	__rmul__(self, factor):
		x = self.x * factor
		y = self.y * factor
		return Vec(x,y)

	def	__add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vec(x,y)

	def	__sub__(self, other):
		x = self.x - other.x
		y = self.y - other.y
		return Vec(x,y)

	def norm(self):
		norm = math.sqrt(self.x**2 + self.y**2)
		return norm

	def get_coords(self):
		return self.x, self.y

def dot(u, v):
	prod = u.x*v.x + u.y*v.y
	return prod



class Particle:
	def __init__(self, mass, position, velocity, radius):
		self.mass = mass
		self.position = position
		self.velocity = velocity
		self.radius = radius



	def inertial_move(self, dt):
		self.position = (dt*self.velocity + self.position)

	def apply_force(self, dt, f):
		self.velocity = dt*((1/self.mass)*f) + self.velocity

	def bounding_box(self):
		top_left = Vec(self.position.x - self.radius, self.position.y + self.radius)
		bottom_right = Vec(self.position.x + self.radius, self.position.y - self.radius)
		return (top_left, bottom_right)

def gravitational_force(dt, particles, G):
	for particle_1 in particles:
		force = Vec(0,0)
		for particle_2 in particles:
			if particle_1 != particle_2:
				x1 = particle_1.position
				x2 = particle_2.position
				r = (x2-x1).norm()
				f = G*(particle_1.mass*particle_2.mass)/(r**2)
				f_2 = (f/r)*(x2-x1)
				force = force + f_2
		particle_1.apply_force(dt, force)

def wall_force(dt, particles, k, n, a):
	for particle in particles:
		d = dot(particle.position-a,n)
		force = -1*k*d*n
		if d < 0:
			particle.apply_force(dt, force)