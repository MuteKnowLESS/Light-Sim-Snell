from tkinter import *
from tkinter import ttk
import numpy as np
import turtle

# configs and setsup main window
widthx = 400
heighty = 300
ws = Tk()
ws.title('Light Sim')
ws.geometry('400x300')
ws.resizable(False, False)
ws.config(bg='white')
x = 100
y = -100

# sets up canvas within main window to display graphics
c = Canvas(bg="black", height=heighty, width=widthx,)
c.grid(row=3, column=0, stick='sw')
screen = turtle.TurtleScreen(c)

c.create_rectangle(-100,-1,100,100, fill = '#A2BAF5', outline='#A2BAF5')
c.create_line(y, 0, x,0, fill='blue', width=2)
c.create_line(0,y,0,x,fill='grey', width=2, dash=(10,5))


# makes a list of materials and assings them a value
mat = ['air','diamond', 'ice','glass', 'water']
reflective_index = {
  'air': 1.00,
  'water': 1.33,
  'ice': 1.30,
  'glass': 1.49,
  'lime glass': 1.46,
  'diamond': 2.42}

  
# Function to draw graph
def draw_graph():
  global theta_1_fl, _n2_dis
  theta_1_fl = float(theta_1_in.get())
  n2_dis = n2_in.get()
  
  #translates polar coordinate pair to cartigian coordinate pair
  angle_in_radians_re = (theta_1_fl+90) * np.pi/180
  angle_in_radians_de = (90-theta_2) * np.pi/180
  line_length = 100
  center_x = 0
  center_y = 0
  end_x_re = center_x + line_length * np.cos(angle_in_radians_re)
  end_y_re = center_y + line_length * np.sin(angle_in_radians_re)
  end_x_de = center_x + line_length * np.cos(angle_in_radians_de)
  end_y_de = center_y + line_length * np.sin(angle_in_radians_de)
  c.delete('ref')
  
  # draws lines
  c.create_line(0,0,-end_x_re,-end_y_re, fill='red',width=2, tags='ref')
  c.create_line(0,0,end_x_re,-end_y_re, fill='green',width=2, tags='ref')
  c.create_line(0,0,-end_x_re,end_y_re, dash=(10,5), fill=('green'), width=2, tags='ref')
  c.create_line(0,0,end_x_de,end_y_de, fill='red',width=2, tags='ref')
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
n1 = float(reflective_index['air'])

# setting n2_in for Integers
n2_in = StringVar()
n2_in.set(mat[4])

# creating drop down widget
dropdown = OptionMenu(ws,n2_in,*mat,command=calc_theta_2)

# creates slider widget
theta_1_in = Scale(ws, from_=0.00, to=90.00, length = widthx/2, orient = 'horizontal')
theta_1_in.bind("<ButtonRelease-1>", calc_theta_2)
# positioning widget
theta_1_in.grid(row = 0, column = 0, padx = 0, sticky = 'nw')
dropdown.grid(row = 0, column = 0, padx = 250, sticky = 'nw')
_n2_dis=Label(ws, text = n2_in.get(), bg = '#A2BAF5')
_n2_dis.place(x=115,y=195)
theta_1_dis = Label(ws, text = 'angle of incidence: 0\N{DEGREE SIGN}', bg = 'white', font=('Arial', 10))
theta_1_dis.place(x=5,y=45)
theta_2_dis = Label(ws, text = 'angle of refraction: 0\N{DEGREE SIGN}', bg = 'white', font=('Arial', 10))
theta_2_dis.place(x=5,y=65)

# infinite loop 
ws.mainloop()