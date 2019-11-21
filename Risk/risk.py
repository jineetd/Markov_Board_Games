#import tkinter as tk
#import Canvas
import random
import matplotlib.pyplot as plt 
import tkinter as tk
import tkinter.messagebox
import numpy as np
#import pygame
#import tkinter as tk

from matrix2 import *
from risk_simulator import *
from time_pass import *
#def getBattles():
#	attacker=7

#	defender=6

#	no_of_battles=0

#	while (attacker!=0 and defender!=0):
#		aturn = random.choice([1,2,3,4,5,6])
#		dturn = random.choice([1,2,3,4,5,6])
#		if aturn>dturn:
#			defender=defender-1
#		else:
#			attacker=attacker-1
#		no_of_battles=no_of_battles+1

#	if(attacker==0):
#		return no_of_battles,0,1
#	else:
#		return no_of_battles,1,0


def plotter():
	if inp.get()=='':
		tkMessageBox.showerror("Error","Please enter No of Iterations!!!!")
		return
	print(inp.get())
	print(type(inp.get()))

	if inpa.get()=='':
		tkMessageBox.showerror("Error","Please enter No of Attackers!!!!")
		return
	if inpd.get()=='':
		tkMessageBox.showerror("Error","Please enter No of Defenders!!!!")
		return

	max_no_of_iterations=inp.get()
	attack=inpa.get()
	defend=inpd.get()

	attack=int(attack)
	defend=int(defend)
	max_no_of_iterations=int(max_no_of_iterations)
	x=[]
	y=[]
	for i in range(1,max_no_of_iterations+1,1):
		ans=0
		for j in range(1,i+1,1):
			num,a,d=getBattles(attack,defend)
			ans=ans+num
		ans=float(ans)/i
		x.append(i)
		y.append(ans)
    # plotting the points 
	num,v,b=theoretical_dynamic(attack,defend)
	plt.plot(x, y , label = 'Simulated no. of battles')
	#plt.legend(['Simulated no. of battles']) 
	plt.axhline(y=num, color='r', linestyle='-',label="Theoretical battles")
	leg = plt.legend();
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
	if inpa.get()=='':
		tkMessageBox.showerror("Error","Please enter No of Attackers!!!!")
		return
	if inpd.get()=='':
		tkMessageBox.showerror("Error","Please enter No of Defenders!!!!")
		return
	max_no_of_iterations=inp1.get()
	max_no_of_iterations=int(max_no_of_iterations)

	attack=inpa.get()
	defend=inpd.get()
	attack=int(attack)
	defend=int(defend)
	x=[]
	y1=[]
	y2=[]
	for i in range(1,max_no_of_iterations+1,1):
		ans=0
		awin=0
		bwin=0
		for j in range(1,i,1):
			res,a,d=getBattles(attack,defend)
			ans=ans+res
			awin=awin+a
			bwin=bwin+d
		x.append(i)
		y1.append(float(awin)/i)
		y2.append(float(bwin)/i)
	
	num,v,b=theoretical_dynamic(attack,defend)
	plt.plot(x, y1 , label = 'Attacker Probability')
	#plt.legend(['Attacker Probability'])
	plt.plot(x, y2 , label = 'Defender Probability') 
	#plt.legend(['Defender Probability'])
	plt.axhline(y=v, color='k', linestyle='--',label="Theoretical attacker win Probability")
	plt.axhline(y=b, color='r', linestyle='--',label="Theoretical defender win Probability")
	leg = plt.legend();
	# naming the x axis 
	plt.xlabel('NO OF ITERATIONS') 
	# naming the y axis 
	plt.ylabel('SIMULATED PROBABILITIES') 

	# giving a title to my graph 
	plt.title('SIMULATED PROBABILITIES V/S NO OF ITERATIONS')
	plt.legend
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

tb4="Enter no. of attackers:"

tb5="Enter no. of defenders:"

wa = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=tb4,fg="green",font=2).place(x=10,y=250)
inpa=tk.StringVar()
ea = tk.Entry(root,textvariable=inpa,width=4).place(x=200,y=250)


wd = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=tb5,fg="green",font=2).place(x=250,y=250)
inpd=tk.StringVar()
ed = tk.Entry(root,textvariable=inpd,width=4).place(x=450,y=250)


#wtext = tk.Label(root, 
 #             justify=tk.LEFT,
  #            padx = 10, 
   #           text=tb1,fg="blue",font=2).place(x=10,y=290)

wtext1 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=tb2,fg="red",font=2).place(x=10,y=330)

inp=tk.StringVar()
e1 = tk.Entry(root,textvariable=inp,width=8).place(x=270,y=330)


plot_getter = tk.Button(root, text="Get Plot", command=plotter).place(x=350,y=330) 


wtextw = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=tb3,fg="orange",font=2).place(x=10,y=400)

inp1=tk.StringVar()
e2 = tk.Entry(root,textvariable=inp1,width=8).place(x=370,y=400)


plot_getter1 = tk.Button(root, text="Plot Probability", command=plotter1).place(x=450,y=400)


root.mainloop()