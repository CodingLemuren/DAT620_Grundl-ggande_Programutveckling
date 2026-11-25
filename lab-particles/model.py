import math

# Task (2/12): Define a class Vec

class Vec:
	def	__init__(self, x, y):
		#initialize the vector self at the given coordinates.
		pass

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
		#return the Euclidean norm of self.
		#Euclidean norm for a vector is defined as .
		pass

	def get_coords(self):
		pass

# Task (3/12): Additionally define a function dot(u, v)
def dot(u, v):
	#which computes the dot product of u and v
	pass

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
		#This method modifies the velocity attribute of a particle according to the above formulas, assuming a constant force f, over a small interval of time dt
		pass

##########################################
### NB. Tasks 7–8 are done in view.py. ###
##########################################


# Task (9/12): In the Particle class, add a method bounding_box(self)






###########################################
### When you're done with all 12 tasks: ###
### forces/other features in this file! ###
###########################################
