from tkinter import *
from model import * 



# Task (7/12): Draw on canvas

# Task (8/12): Define a new function 
def to_canvas_coords(canvas, u):
    canvas_u = (canvas.winfo_reqheight()/20)*(u)
    canvas_u.y = (-1)*canvas_u.y + (canvas.winfo_reqheight()/2)
    canvas_u.x = canvas_u.x + (canvas.winfo_reqwidth()/2)
    return canvas_u


root = Tk()
canvas = Canvas(root, bg="white", width=800, height=600)
canvas.pack()

vector1 = Vec(-10,10)
vector2 = Vec(2,4)
part_u = Particle(5,vector1,vector2,2)
topl, botr = part_u.bounding_box()
topl_c = to_canvas_coords(canvas, topl)
botr_c = to_canvas_coords(canvas, botr)
oc = canvas.create_oval(topl_c.x,topl_c.y, botr_c.x,botr_c.y, fill="red" )
input()


#######################################
### NB. Task 9 is done in model.py. ###
#######################################

# Task (10/12): Define a new function move_oval_to(o, u1, u2)

# Task (11/12): Define a new function create_oval(canvas, particle)

# Task (12/12): Define a function simulation_loop(f, timestep, particles)
