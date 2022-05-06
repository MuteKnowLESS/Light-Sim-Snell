from tkinter import *
from tkinter import ttk
import numpy as np
import turtle

# configs and setsup main window
widthx = 800
heighty = 700
ws = Tk()
ws.title('Light Sim')
ws.geometry('800x700')
ws.resizable(False, False)
ws.config(bg='white')
x = 250
y = -250
style = ttk.Style(ws)

# sets up canvas within main window to display graphics
c = Canvas(bg="black", height=heighty, width=widthx,)
c.place(x=0, y=115)
screen = turtle.TurtleScreen(c)

c.create_rectangle(-250,-1,250,250, fill = '#A2BAF5', outline='#A2BAF5')
c.create_line(y, 0, x,0, fill='blue', width=2)
c.create_line(0,y,0,x,fill='grey', width=2, dash=(10,5))


# makes a list of materials and assings them a value
mat = ['water','diamond', 'ice','glass', 'water']
reflective_index = {
  'water': 1.33,
  'ice': 1.30,
  'glass': 1.49,
  'lime glass': 1.46,
  'diamond': 2.42
  }

# Function to draw graph

def draw_graph():
  global theta_1_fl, _n2_dis
  theta_1_fl = float(theta_1_in.get())
  n2_dis = n2_in.get()
 
  #translates polar coordinate pair to cartigian coordinate pair
  angle_in_radians_re = (theta_1_fl+90) * np.pi/180
  angle_in_radians_de = (90-theta_2) * np.pi/180
  line_length = 250
  center_x = 0
  center_y = 0
  end_x_re = center_x + line_length * np.cos(angle_in_radians_re)
  end_y_re = center_y + line_length * np.sin(angle_in_radians_re)
  end_x_de = center_x + line_length * np.cos(angle_in_radians_de)
  end_y_de = center_y + line_length * np.sin(angle_in_radians_de)
  c.delete('ref')
 
  # draws lines
  c.create_line(0,0,-end_x_re,-end_y_re, fill='#ff6161',width=3, tags='ref')
  c.create_line(0,0,end_x_de,end_y_de, fill='red',width=3, tags='ref')
  c.create_line(0,0,end_x_re,-end_y_re, fill='green',width=3, tags='ref')
  c.create_line(0,0,-end_x_re,end_y_re, dash=(10,5), fill=('green'), width=3, tags='ref')
  _n2_dis.configure(text=n2_dis)
  theta_1_dis.configure(text='angle of incidence: ' + str(int(theta_1_fl)) + '\N{DEGREE SIGN}')
  theta_2_dis.configure(text='angle of refraction: ' + str(int(theta_2)) + '\N{DEGREE SIGN}')
 
# calulates the theta_2 value then triggers the draw event
def calc_theta_2(event):
  global theta_1, theta_2, theta_1_in, n2
  n2 = (reflective_index[n2_in.get()])
  theta_1 = float(np.radians(theta_1_in.get()))
  theta_2 = np.degrees(np.arcsin(n1 / n2 * np.sin(theta_1)))
  draw_graph()
n2 = 1.33
n1 = 1

# setting n2_in for Integers
n2_in = StringVar()
n2_in.set(mat[4])
val = IntVar(ws)

# creating drop down widget
dropdown = ttk.OptionMenu(ws,n2_in,*mat,command=calc_theta_2)
dropdown.config(width=10)
# creates slider widget
theta_1_in = ttk.Scale(ws, from_=0.00, to=90.00, variable=val, length = widthx/2, orient = 'horizontal')
theta_1_in.set(45)
theta_1_in.bind("<B1-Motion>", calc_theta_2)
theta_1_in.bind("<Button-1>", calc_theta_2)
# positioning widget
theta_1_in.grid(row = 0, column = 0, padx = 0, pady = 0,sticky = 'w')
dropdown.grid(row = 0,column=2, sticky='ne')
_n2_dis=Label(ws, text = n2_in.get(), bg = '#A2BAF5', font=('Arial', 15))
_n2_dis.place(x=175,y=475)
theta_1_dis = Label(ws, text = 'angle of incidence: 0\N{DEGREE SIGN}', bg = 'white', font=('Arial', 15))
theta_1_dis.place(x=5,y=45)
theta_2_dis = Label(ws, text = 'angle of refraction: 0\N{DEGREE SIGN}', bg = 'white', font=('Arial', 15))
theta_2_dis.place(x=5,y=75)

calc_theta_2(Event)

# infinite loop
ws.mainloop()
