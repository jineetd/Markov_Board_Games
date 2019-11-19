#import tkinter as tk
#import Canvas
import random
import matplotlib.pyplot as plt 
import tkMessageBox
import numpy as np
import pygame
import tkinter as tk

from matrix2 import *
def getBattles():
	attacker=7

	defender=6

	no_of_battles=0

	while (attacker!=0 and defender!=0):
		aturn = random.choice([1,2,3,4,5,6])
		dturn = random.choice([1,2,3,4,5,6])
		if aturn>dturn:
			defender=defender-1
		else:
			attacker=attacker-1
		no_of_battles=no_of_battles+1

	if(attacker==0):
		return no_of_battles,0,1
	else:
		return no_of_battles,1,0


def plotter():
	if inp.get()=='':
		tkMessageBox.showerror("Error","Please enter No of Iterations!!!!")
   		return
	print(inp.get())
	print(type(inp.get()))
	max_no_of_iterations=inp.get()


	max_no_of_iterations=int(max_no_of_iterations)
   	x=[]
   	y=[]
   	for i in range(1,max_no_of_iterations+1,1):
   		ans=0
   		for j in range(1,i+1,1):
   			num,a,d=getBattles()
   			ans=ans+num
   		ans=float(ans)/i
   		x.append(i)
   		y.append(ans)
    # plotting the points  
	plt.plot(x, y) 
	plt.axhline(y=10.168180083907123, color='r', linestyle='-',label="Theoretical battles")
	# naming the x axis 
	plt.xlabel('NO OF ITERATIONS') 
	# naming the y axis 
	plt.ylabel('SIMULATED BATTLES') 

	# giving a title to my graph 
	plt.title('SIMULATED BATTLES V/S NO OF ITERATIONS')
	# function to show the plot 
	plt.show()


#print(getBattles())

def plotter1():
	if inp1.get()=='':
		tkMessageBox.showerror("Error","Please enter No of Iterations!!!!")
		return
	print(inp1.get())
	print(type(inp1.get()))
	max_no_of_iterations=inp1.get()
	max_no_of_iterations=int(max_no_of_iterations)
	x=[]
	y1=[]
	y2=[]
	for i in range(1,max_no_of_iterations+1,1):
		ans=0
		awin=0
		bwin=0
		for j in range(1,i,1):
			res,a,d=getBattles()
			ans=ans+res
			awin=awin+a
			bwin=bwin+d
		x.append(i)
		y1.append(float(awin)/i)
		y2.append(float(bwin)/i)
	
	plt.plot(x, y1)
	plt.plot(x, y2) 
	plt.axhline(y=0.3797688225251342, color='r', linestyle='--',label="Attacker winning")
	plt.axhline(y=0.6202311774748666, color='k', linestyle='--',label="Attacker winning")
	# naming the x axis 
	plt.xlabel('NO OF ITERATIONS') 
	# naming the y axis 
	plt.ylabel('SIMULATED PROBABILITIES') 

	# giving a title to my graph 
	plt.title('SIMULATED PROBABILITIES V/S NO OF ITERATIONS')
	# function to show the plot 
	plt.show()


root = tk.Tk()
logo = tk.PhotoImage(file="risk_image.gif")
logo=logo.subsample(3)
w1 = tk.Label(root, image=logo).pack(side="top")
root.title("Risk Simulator")
root.geometry("600x500")
textbox="No of simulations:"

ans,prob_attackers,prob_defender=theoretical_values()

tb1 = """Expected number of battles(theoretical):""" + str(ans)
#print("Expected number of steps simulated:"+str(num))

tb2="Enter number of simulations:"


tb3="Enter number of iterations for Probability:"

wtext = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=tb1,fg="blue",font=2).place(x=10,y=260)

wtext1 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=tb2,fg="red",font=2).place(x=10,y=300)

inp=tk.StringVar()
e1 = tk.Entry(root,textvariable=inp).place(x=270,y=300)


plot_getter = tk.Button(root, text="Get Plot", command=plotter).place(x=450,y=300)  


wtextw = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=tb3,fg="orange",font=2).place(x=10,y=400)

inp1=tk.StringVar()
e2 = tk.Entry(root,textvariable=inp1).place(x=370,y=400)


plot_getter1 = tk.Button(root, text="Plot Probability", command=plotter1).place(x=250,y=450)


root.mainloop()