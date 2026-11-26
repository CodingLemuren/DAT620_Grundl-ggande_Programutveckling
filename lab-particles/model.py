import math

# Task (2/12): Define a class Vec

class Vec:
	def	__init__(self, x, y):
		self.x = x
		self.y = y

	def	__repr__(self):
		pass

		#return a string which is a suitable representation of the vector. For instance "(1.34,45.7)" if the self has coordinates x=1.34 and y=45.7.
	def	__rmul__(self, factor):
		pass

		#return a new vector scaled by the given factor
	def	__add__(self, other):
		pass

		#return a new vector which is the addition of self and other.
	def	__sub__(self, other):
		pass

		#return a new vector which is the subtraction of self and other.

	def norm(self):
		norm = math.sqrt(self.x**2 + self.y**2)
		return norm

	def get_coords(self):
		return self.x, self.y

# Task (3/12): Additionally define a function dot(u, v)
def dot(u, v):
	prod = u.x*v.x + u.y*v.y
	return prod


# Task (4/12): Create a class Particle

class Particle:
	def __init__(self, mass, position, velocity, radius):
		self.mass = mass
		self.position = position
		self.velocity = velocity
		self.radius = radius

# Task (5/12): In the Particle class, implement a method inertial_move(self, dt).

	def inertial_move(self, dt):
		#This method modifies the position attribute of a particle according to the above formula, over a small interval of time dt.
		pass

# Task (6/12): In the Particle class, implement a method apply_force(self, dt, f)
	def apply_force(self, dt, f):
		print(f)
		self.velocity = dt*((1/self.mass)*f) + self.velocity
		print(self.velocity)

##########################################
### NB. Tasks 7–8 are done in view.py. ###
##########################################


# Task (9/12): In the Particle class, add a method bounding_box(self)






###########################################
### When you're done with all 12 tasks: ###
### forces/other features in this file! ###
###########################################


vector_1 = Vec(1,2)
vector_2 = Vec(2,4)
part = Particle(5,vector_1,vector_1,2)

part.apply_force(2,vector_2)