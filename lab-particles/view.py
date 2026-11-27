from tkinter import *
from model import * 
import time



# Task (7/12): Draw on canvas

# Task (8/12): Define a new function 
def to_canvas_coords(canvas, u):
    canvas_u = (canvas.winfo_reqheight()/20)*(u)
    canvas_u.y = (-1)*canvas_u.y + (canvas.winfo_reqheight()/2)
    canvas_u.x = canvas_u.x + (canvas.winfo_reqwidth()/2)
    return canvas_u

def move_oval_to(canvas, o, u1,u2):
    u1_canvas = to_canvas_coords(canvas, u1)
    u2_canvas = to_canvas_coords(canvas, u2)
    canvas.coords(o, u1_canvas.x, u1_canvas.y, u2_canvas.x, u2_canvas.y)

def create_oval(canvas, particle):
    o = canvas.create_oval(0,0,0,0, fill="blue")
    move_oval_to(canvas, o, particle.bounding_box()[0], particle.bounding_box()[1])
    return o

def simulation_loop(f, timestep, particles):
    ovals = []
    for particle in particles:
        ovals.append(create_oval(canvas, particle))

    previous_time = time.time()
    while True:
        f(timestep, particles)
        for i, particle in enumerate(particles):
            particle.inertial_move(timestep)
            move_oval_to(canvas, ovals[i], particle.bounding_box()[0],  particle.bounding_box()[1])

        current_time = time.time()
        if current_time - previous_time >= (1/30):
            canvas.update()
            previous_time = current_time



root = Tk()
canvas = Canvas(root, bg="white", width=800, height=600)
canvas.pack()


""" for n in range(5):
  particle = Particle(0, Vec(n,n), Vec(0,0), 0.2)
  create_oval(canvas, particle)
  canvas.update()
  time.sleep(1)

input() """
""" vector1 = Vec(-10,10)
vector2 = Vec(2,4)
part_u = Particle(5,vector1,vector2,2)
topl, botr = part_u.bounding_box()
topl_c = to_canvas_coords(canvas, topl)
botr_c = to_canvas_coords(canvas, botr)
oc = canvas.create_oval(topl_c.x,topl_c.y, botr_c.x,botr_c.y, fill="red" )
input()
u1_test = Vec(1,2)
#u2_test = Vec(2,4)
move_oval_to(oc, u1_test, canvas)
input() """

#######################################
### NB. Task 9 is done in model.py. ###
#######################################

# Task (10/12): Define a new function 
    

# Task (11/12): Define a new function 

# Task (12/12): Define a function simulation_loop(f, timestep, particles)
