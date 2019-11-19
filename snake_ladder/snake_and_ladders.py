import tkinter as tk
import random
import matplotlib.pyplot as plt 
import tkMessageBox
import numpy as np



def no_of_steps() :
    path=[]
    path.append(0)
    turn = random.choice([1,2,3,4,5,6])
    count = 0
    while turn != 6 :
        turn = random.choice([1,2,3,4,5,6])
        count=count+1
    start = 0
    
    turn = random.choice([1,2,3,4,5,6])
    curr_val = start + turn
    while curr_val != 100:
        count = count + 1
        path.append(curr_val)
        if (curr_val == 2):
            curr_val = 23
            count=count-1
        elif curr_val == 4:
            curr_val = 68
            count=count-1
        elif curr_val == 6:
            curr_val = 45
            count=count-1
        elif curr_val == 20:
            curr_val = 59
            count=count-1
        elif curr_val == 30:
            curr_val = 96
            count=count-1
        elif curr_val == 43:
            curr_val = 17
            count=count-1
        elif curr_val == 50:
            curr_val = 5
            count=count-1
        elif curr_val == 52:
            curr_val = 72
            count=count-1
        elif curr_val == 56:
            curr_val = 8
            count=count-1
        elif curr_val == 57:
            curr_val = 96
            count=count-1
        elif curr_val == 71:
            curr_val = 92
            count=count-1
        elif curr_val == 73:
            curr_val = 15
            count=count-1
        elif curr_val == 84:
            curr_val = 58
            count=count-1
        elif curr_val == 87:
            curr_val = 49
            count=count-1
        elif curr_val == 98:
            curr_val = 40
            count=count-1
        else :
            rec_turn = random.choice([1,2,3,4,5,6])
            curr_val = curr_val + rec_turn
        if(curr_val > 100):
            curr_val = curr_val - rec_turn
    path.append(100)
    return count,path
        	 	

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
        res=0
        for j in range(1,i+1,1):
            z=[]
            num,z=no_of_steps()
            res+=num
        res=float(res)
        res=res/i
        x.append(i)
        y.append(res)
    print(y[len(y)-1])
    # plotting the points  
    plt.plot(x, y) 
    plt.axhline(y=theorotical_no_of_steps(), color='r', linestyle='-')
    # naming the x axis 
    plt.xlabel('NO OF ITERATIONS') 
    # naming the y axis 
    plt.ylabel('SIMULATED STEPS') 
  
    # giving a title to my graph 
    plt.title('SIMULATED STEPS V/S NO OF ITERATIONS')
    # function to show the plot 
    plt.show() 



def theorotical_no_of_steps():
    transition_matrix = [[0]*86 for _ in range(86)]
    Q_matrix =[[0]*85 for _ in range(85)]
    #for state 0 and number 0
    transition_matrix[0][0] = float(5)/6
    transition_matrix[0][1] = float(1)/36
    transition_matrix[0][2] = float(1)/36
    transition_matrix[0][19] = float(1)/36
    transition_matrix[0][58] = float(1)/36
    transition_matrix[0][3] = float(1)/36
    transition_matrix[0][39] = float(1)/36

    #for state 1 and number 1
    transition_matrix[1][19] = float(1)/6
    transition_matrix[1][2] = float(1)/6
    transition_matrix[1][58] = float(1)/6
    transition_matrix[1][3] = float(1)/6
    transition_matrix[1][39] = float(1)/6
    transition_matrix[1][4] = float(1)/6

    #for state 2 and number 3
    transition_matrix[2][58] = float(1)/6
    transition_matrix[2][3] = float(1)/6
    transition_matrix[2][39] = float(1)/6
    transition_matrix[2][4] = float(1)/6
    transition_matrix[2][5] = float(1)/6
    transition_matrix[2][6] = float(1)/6

    #for state 3 and number 5
    transition_matrix[3][39] = float(1)/6
    transition_matrix[3][4] = float(1)/6
    transition_matrix[3][5] = float(1)/6
    transition_matrix[3][6] = float(1)/6
    transition_matrix[3][7] = float(1)/6
    transition_matrix[3][8] = float(1)/6

    #for state 4 and number 7
    transition_matrix[4][5] = float(1)/6
    transition_matrix[4][6] = float(1)/6
    transition_matrix[4][7] = float(1)/6
    transition_matrix[4][8] = float(1)/6
    transition_matrix[4][9] = float(1)/6
    transition_matrix[4][10] = float(1)/6

    #for state 5 and number 8
    transition_matrix[5][6] = float(1)/6
    transition_matrix[5][7] = float(1)/6
    transition_matrix[5][8] = float(1)/6
    transition_matrix[5][9] = float(1)/6
    transition_matrix[5][10] = float(1)/6
    transition_matrix[5][11] = float(1)/6

    #for state 6 and number 9
    transition_matrix[6][7] = float(1)/6
    transition_matrix[6][8] = float(1)/6
    transition_matrix[6][9] = float(1)/6
    transition_matrix[6][10] = float(1)/6
    transition_matrix[6][11] = float(1)/6
    transition_matrix[6][12] = float(1)/6

    #for state 7 and number 10
    transition_matrix[7][8] = float(1)/6
    transition_matrix[7][9] = float(1)/6
    transition_matrix[7][10] = float(1)/6
    transition_matrix[7][11] = float(1)/6
    transition_matrix[7][12] = float(1)/6
    transition_matrix[7][13] = float(1)/6

    #for state 8 and number 11
    transition_matrix[8][9] = float(1)/6
    transition_matrix[8][10] = float(1)/6
    transition_matrix[8][11] = float(1)/6
    transition_matrix[8][12] = float(1)/6
    transition_matrix[8][13] = float(1)/6
    transition_matrix[8][14] = float(1)/6

    #for state 9 and number 12
    transition_matrix[9][10] = float(1)/6
    transition_matrix[9][11] = float(1)/6
    transition_matrix[9][12] = float(1)/6
    transition_matrix[9][13] = float(1)/6
    transition_matrix[9][14] = float(1)/6
    transition_matrix[9][15] = float(1)/6

    #for state 10 and number 13
    transition_matrix[10][11] = float(1)/6
    transition_matrix[10][12] = float(1)/6
    transition_matrix[10][13] = float(1)/6
    transition_matrix[10][14] = float(1)/6
    transition_matrix[10][15] = float(1)/6
    transition_matrix[10][16] = float(1)/6

    #for state 11 and number 14
    transition_matrix[11][12] = float(1)/6
    transition_matrix[11][13] = float(1)/6
    transition_matrix[11][14] = float(1)/6
    transition_matrix[11][15] = float(1)/6
    transition_matrix[11][16] = float(1)/6
    transition_matrix[11][49] = float(1)/6

    #for state 12 and number 15
    transition_matrix[12][13] = float(1)/6
    transition_matrix[12][14] = float(1)/6
    transition_matrix[12][15] = float(1)/6
    transition_matrix[12][16] = float(1)/6
    transition_matrix[12][49] = float(1)/6
    transition_matrix[12][17] = float(1)/6

    #for state 13 and number 16
    transition_matrix[13][14] = float(1)/6
    transition_matrix[13][15] = float(1)/6
    transition_matrix[13][16] = float(1)/6
    transition_matrix[13][49] = float(1)/6
    transition_matrix[13][17] = float(1)/6
    transition_matrix[13][18] = float(1)/6

    #for state 14 and number 17
    transition_matrix[14][15] = float(1)/6
    transition_matrix[14][16] = float(1)/6
    transition_matrix[14][49] = float(1)/6
    transition_matrix[14][17] = float(1)/6
    transition_matrix[14][18] = float(1)/6
    transition_matrix[14][19] = float(1)/6

    #for state 15 and number 18
    transition_matrix[15][16] = float(1)/6
    transition_matrix[15][49] = float(1)/6
    transition_matrix[15][17] = float(1)/6
    transition_matrix[15][18] = float(1)/6
    transition_matrix[15][19] = float(1)/6
    transition_matrix[15][20] = float(1)/6

    #for state 16 and number 19
    transition_matrix[16][49] = float(1)/6
    transition_matrix[16][17] = float(1)/6
    transition_matrix[16][18] = float(1)/6
    transition_matrix[16][19] = float(1)/6
    transition_matrix[15][20] = float(1)/6
    transition_matrix[16][21] = float(1)/6

    #for state 17 and number 21
    transition_matrix[17][18] = float(1)/6
    transition_matrix[17][19] = float(1)/6
    transition_matrix[17][20] = float(1)/6
    transition_matrix[17][21] = float(1)/6
    transition_matrix[17][22] = float(1)/6
    transition_matrix[17][23] = float(1)/6

    #for state 18 and number 22
    transition_matrix[18][19] = float(1)/6
    transition_matrix[18][20] = float(1)/6
    transition_matrix[18][21] = float(1)/6
    transition_matrix[18][22] = float(1)/6
    transition_matrix[18][23] = float(1)/6
    transition_matrix[18][24] = float(1)/6

    #for state 19 and number 23
    transition_matrix[19][20] = float(1)/6
    transition_matrix[19][21] = float(1)/6
    transition_matrix[19][22] = float(1)/6
    transition_matrix[19][23] = float(1)/6
    transition_matrix[19][24] = float(1)/6
    transition_matrix[19][25] = float(1)/6

    #for state 20 and number 24
    transition_matrix[20][21] = float(1)/6
    transition_matrix[20][22] = float(1)/6
    transition_matrix[20][23] = float(1)/6
    transition_matrix[20][24] = float(1)/6
    transition_matrix[20][25] = float(1)/6
    transition_matrix[20][82] = float(1)/6

    #for state 21 and number 25
    transition_matrix[21][22] = float(1)/6
    transition_matrix[21][23] = float(1)/6
    transition_matrix[21][24] = float(1)/6
    transition_matrix[21][25] = float(1)/6
    transition_matrix[21][82] = float(1)/6
    transition_matrix[21][26] = float(1)/6

    #for state 22 and number 26
    transition_matrix[22][23] = float(1)/6
    transition_matrix[22][24] = float(1)/6
    transition_matrix[22][25] = float(1)/6
    transition_matrix[22][82] = float(1)/6
    transition_matrix[22][26] = float(1)/6
    transition_matrix[22][27] = float(1)/6

    #for state 23 and number 27
    transition_matrix[23][24] = float(1)/6
    transition_matrix[23][25] = float(1)/6
    transition_matrix[23][82] = float(1)/6
    transition_matrix[23][26] = float(1)/6
    transition_matrix[23][27] = float(1)/6
    transition_matrix[23][28] = float(1)/6

    #for state 24 and number 28
    transition_matrix[24][25] = float(1)/6
    transition_matrix[24][82] = float(1)/6
    transition_matrix[24][26] = float(1)/6
    transition_matrix[24][27] = float(1)/6
    transition_matrix[24][28] = float(1)/6
    transition_matrix[24][29] = float(1)/6

    #for state 25 and number 29
    transition_matrix[25][82] = float(1)/6
    transition_matrix[25][26] = float(1)/6
    transition_matrix[25][27] = float(1)/6
    transition_matrix[25][28] = float(1)/6
    transition_matrix[25][29] = float(1)/6
    transition_matrix[25][30] = float(1)/6

    #for state 26 and number 31
    transition_matrix[26][27] = float(1)/6
    transition_matrix[26][28] = float(1)/6
    transition_matrix[26][29] = float(1)/6
    transition_matrix[26][30] = float(1)/6
    transition_matrix[26][31] = float(1)/6
    transition_matrix[26][32] = float(1)/6

    #for state 27 and number 32
    transition_matrix[27][28] = float(1)/6
    transition_matrix[27][29] = float(1)/6
    transition_matrix[27][30] = float(1)/6
    transition_matrix[27][31] = float(1)/6
    transition_matrix[27][32] = float(1)/6
    transition_matrix[27][33] = float(1)/6

    #for state 28 and number 33
    transition_matrix[28][29] = float(1)/6
    transition_matrix[28][30] = float(1)/6
    transition_matrix[28][31] = float(1)/6
    transition_matrix[28][32] = float(1)/6
    transition_matrix[28][33] = float(1)/6
    transition_matrix[28][34] = float(1)/6

    #for state 29 and number 34
    transition_matrix[29][30] = float(1)/6
    transition_matrix[29][31] = float(1)/6
    transition_matrix[29][32] = float(1)/6
    transition_matrix[29][33] = float(1)/6
    transition_matrix[29][34] = float(1)/6
    transition_matrix[29][35] = float(1)/6

    #for state 30 and number 35
    transition_matrix[30][31] = float(1)/6
    transition_matrix[30][32] = float(1)/6
    transition_matrix[30][33] = float(1)/6
    transition_matrix[30][34] = float(1)/6
    transition_matrix[30][35] = float(1)/6
    transition_matrix[30][36] = float(1)/6

    #for state 31 and number 36
    transition_matrix[31][32] = float(1)/6
    transition_matrix[31][33] = float(1)/6
    transition_matrix[31][34] = float(1)/6
    transition_matrix[31][35] = float(1)/6
    transition_matrix[31][36] = float(1)/6
    transition_matrix[31][37] = float(1)/6

    #for state 32 and number 37
    transition_matrix[32][33] = float(1)/6
    transition_matrix[32][34] = float(1)/6
    transition_matrix[32][35] = float(1)/6
    transition_matrix[32][36] = float(1)/6
    transition_matrix[32][37] = float(1)/6
    transition_matrix[32][14] = float(1)/6

    #for state 33 and number 38
    transition_matrix[33][34] = float(1)/6
    transition_matrix[33][35] = float(1)/6
    transition_matrix[33][36] = float(1)/6
    transition_matrix[33][37] = float(1)/6
    transition_matrix[33][14] = float(1)/6
    transition_matrix[33][38] = float(1)/6

    #for state 34 and number 39
    transition_matrix[34][35] = float(1)/6
    transition_matrix[34][36] = float(1)/6
    transition_matrix[34][37] = float(1)/6
    transition_matrix[34][14] = float(1)/6
    transition_matrix[34][38] = float(1)/6
    transition_matrix[34][39] = float(1)/6

    #for state 35 and number 40
    transition_matrix[35][36] = float(1)/6
    transition_matrix[35][37] = float(1)/6
    transition_matrix[35][14] = float(1)/6
    transition_matrix[35][38] = float(1)/6
    transition_matrix[35][39] = float(1)/6
    transition_matrix[35][40] = float(1)/6

    #for state 36 and number 41
    transition_matrix[36][37] = float(1)/6
    transition_matrix[36][14] = float(1)/6
    transition_matrix[36][38] = float(1)/6
    transition_matrix[36][39] = float(1)/6
    transition_matrix[36][40] = float(1)/6
    transition_matrix[36][41] = float(1)/6

    #for state 37 and number 42
    transition_matrix[37][14] = float(1)/6
    transition_matrix[37][38] = float(1)/6
    transition_matrix[37][39] = float(1)/6
    transition_matrix[37][40] = float(1)/6
    transition_matrix[37][41] = float(1)/6
    transition_matrix[37][42] = float(1)/6

    #for state 38 and number 44
    transition_matrix[38][39] = float(1)/6
    transition_matrix[38][40] = float(1)/6
    transition_matrix[38][41] = float(1)/6
    transition_matrix[38][42] = float(1)/6
    transition_matrix[38][43] = float(1)/6
    transition_matrix[38][3] = float(1)/6

    #for state 39 and number 45
    transition_matrix[39][40] = float(1)/6
    transition_matrix[39][41] = float(1)/6
    transition_matrix[39][42] = float(1)/6
    transition_matrix[39][43] = float(1)/6
    transition_matrix[39][3] = float(1)/6
    transition_matrix[39][44] = float(1)/6

    #for state 40 and number 46
    transition_matrix[40][41] = float(1)/6
    transition_matrix[40][42] = float(1)/6
    transition_matrix[40][43] = float(1)/6
    transition_matrix[40][3] = float(1)/6
    transition_matrix[40][44] = float(1)/6
    transition_matrix[40][61] = float(1)/6

    #for state 41 and number 47
    transition_matrix[41][42] = float(1)/6
    transition_matrix[41][43] = float(1)/6
    transition_matrix[41][3] = float(1)/6
    transition_matrix[41][44] = float(1)/6
    transition_matrix[41][61] = float(1)/6
    transition_matrix[41][45] = float(1)/6

    #for state 42 and number 48
    transition_matrix[42][43] = float(1)/6
    transition_matrix[42][3] = float(1)/6
    transition_matrix[42][44] = float(1)/6
    transition_matrix[42][61] = float(1)/6
    transition_matrix[42][45] = float(1)/6
    transition_matrix[42][46] = float(1)/6

    #for state 43 and number 49
    transition_matrix[43][3] = float(1)/6
    transition_matrix[43][44] = float(1)/6
    transition_matrix[43][61] = float(1)/6
    transition_matrix[43][45] = float(1)/6
    transition_matrix[43][46] = float(1)/6
    transition_matrix[43][47] = float(1)/6

    #for state 44 and number 51
    transition_matrix[44][61] = float(1)/6
    transition_matrix[44][45] = float(1)/6
    transition_matrix[44][46] = float(1)/6
    transition_matrix[44][47] = float(1)/6
    transition_matrix[44][5] = float(1)/6
    transition_matrix[44][82] = float(1)/6

    #for state 45 and number 53
    transition_matrix[45][46] = float(1)/6
    transition_matrix[45][47] = float(1)/6
    transition_matrix[45][5] = float(1)/6
    transition_matrix[45][82] = float(1)/6
    transition_matrix[45][48] = float(1)/6
    transition_matrix[45][49] = float(1)/6

    #for state 46 and number 54
    transition_matrix[46][47] = float(1)/6
    transition_matrix[46][5] = float(1)/6
    transition_matrix[46][82] = float(1)/6
    transition_matrix[46][48] = float(1)/6
    transition_matrix[46][49] = float(1)/6
    transition_matrix[46][50] = float(1)/6

    #for state 47 and number 55
    transition_matrix[47][5] = float(1)/6
    transition_matrix[47][82] = float(1)/6
    transition_matrix[47][48] = float(1)/6
    transition_matrix[47][49] = float(1)/6
    transition_matrix[47][50] = float(1)/6
    transition_matrix[47][51] = float(1)/6

    #for state 48 and number 58
    transition_matrix[48][49] = float(1)/6
    transition_matrix[48][50] = float(1)/6
    transition_matrix[48][51] = float(1)/6
    transition_matrix[48][52] = float(1)/6
    transition_matrix[48][53] = float(1)/6
    transition_matrix[48][54] = float(1)/6

    #for state 49 and number 59
    transition_matrix[49][50] = float(1)/6
    transition_matrix[49][51] = float(1)/6
    transition_matrix[49][52] = float(1)/6
    transition_matrix[49][53] = float(1)/6
    transition_matrix[49][54] = float(1)/6
    transition_matrix[49][55] = float(1)/6

    #for state 50 and number 60
    transition_matrix[50][51] = float(1)/6
    transition_matrix[50][52] = float(1)/6
    transition_matrix[50][53] = float(1)/6
    transition_matrix[50][54] = float(1)/6
    transition_matrix[50][55] = float(1)/6
    transition_matrix[50][56] = float(1)/6

    #for state 51 and number 61
    transition_matrix[51][52] = float(1)/6
    transition_matrix[51][53] = float(1)/6
    transition_matrix[51][54] = float(1)/6
    transition_matrix[51][55] = float(1)/6
    transition_matrix[51][56] = float(1)/6
    transition_matrix[51][57] = float(1)/6

    #for state 52 and number 62
    transition_matrix[52][53] = float(1)/6
    transition_matrix[52][54] = float(1)/6
    transition_matrix[52][55] = float(1)/6
    transition_matrix[52][56] = float(1)/6
    transition_matrix[52][57] = float(1)/6
    transition_matrix[52][58] = float(1)/6

    #for state 53 and number 63
    transition_matrix[53][54] = float(1)/6
    transition_matrix[53][55] = float(1)/6
    transition_matrix[53][56] = float(1)/6
    transition_matrix[53][57] = float(1)/6
    transition_matrix[53][58] = float(1)/6
    transition_matrix[53][59] = float(1)/6

    #for state 54 and number 64
    transition_matrix[54][55] = float(1)/6
    transition_matrix[54][56] = float(1)/6
    transition_matrix[54][57] = float(1)/6
    transition_matrix[54][58] = float(1)/6
    transition_matrix[54][59] = float(1)/6
    transition_matrix[54][60] = float(1)/6

    #for state 55 and number 65
    transition_matrix[55][56] = float(1)/6
    transition_matrix[55][57] = float(1)/6
    transition_matrix[55][58] = float(1)/6
    transition_matrix[55][59] = float(1)/6
    transition_matrix[55][60] = float(1)/6
    transition_matrix[55][78] = float(1)/6

    #for state 56 and number 66
    transition_matrix[56][57] = float(1)/6
    transition_matrix[56][58] = float(1)/6
    transition_matrix[56][59] = float(1)/6
    transition_matrix[56][60] = float(1)/6
    transition_matrix[56][78] = float(1)/6
    transition_matrix[56][61] = float(1)/6

    #for state 57 and number 67
    transition_matrix[57][58] = float(1)/6
    transition_matrix[57][59] = float(1)/6
    transition_matrix[57][60] = float(1)/6
    transition_matrix[57][78] = float(1)/6
    transition_matrix[57][61] = float(1)/6
    transition_matrix[57][12] = float(1)/6

    #for state 58 and number 68
    transition_matrix[58][59] = float(1)/6
    transition_matrix[58][60] = float(1)/6
    transition_matrix[58][78] = float(1)/6
    transition_matrix[58][61] = float(1)/6
    transition_matrix[58][12] = float(1)/6
    transition_matrix[58][62] = float(1)/6

    #for state 59 and number 69
    transition_matrix[59][60] = float(1)/6
    transition_matrix[59][78] = float(1)/6
    transition_matrix[59][61] = float(1)/6
    transition_matrix[59][12] = float(1)/6
    transition_matrix[59][62] = float(1)/6
    transition_matrix[59][63] = float(1)/6

    #for state 60 and number 70
    transition_matrix[60][78] = float(1)/6
    transition_matrix[60][61] = float(1)/6
    transition_matrix[60][12] = float(1)/6
    transition_matrix[60][62] = float(1)/6
    transition_matrix[60][63] = float(1)/6
    transition_matrix[60][64] = float(1)/6

    #for state 61 and number 72
    transition_matrix[61][12] = float(1)/6
    transition_matrix[61][62] = float(1)/6
    transition_matrix[61][63] = float(1)/6
    transition_matrix[61][64] = float(1)/6
    transition_matrix[61][65] = float(1)/6
    transition_matrix[61][66] = float(1)/6

    #for state 62 and number 74
    transition_matrix[62][63] = float(1)/6
    transition_matrix[62][64] = float(1)/6
    transition_matrix[62][65] = float(1)/6
    transition_matrix[62][66] = float(1)/6
    transition_matrix[62][67] = float(1)/6
    transition_matrix[62][68] = float(1)/6

    #for state 63 and number 75
    transition_matrix[63][64] = float(1)/6
    transition_matrix[63][65] = float(1)/6
    transition_matrix[63][66] = float(1)/6
    transition_matrix[63][67] = float(1)/6
    transition_matrix[63][68] = float(1)/6
    transition_matrix[63][69] = float(1)/6

    #for state 64 and number 76
    transition_matrix[64][65] = float(1)/6
    transition_matrix[64][66] = float(1)/6
    transition_matrix[64][67] = float(1)/6
    transition_matrix[64][68] = float(1)/6
    transition_matrix[64][69] = float(1)/6
    transition_matrix[64][70] = float(1)/6

    #for state 65 and number 77
    transition_matrix[65][66] = float(1)/6
    transition_matrix[65][67] = float(1)/6
    transition_matrix[65][68] = float(1)/6
    transition_matrix[65][69] = float(1)/6
    transition_matrix[65][70] = float(1)/6
    transition_matrix[65][71] = float(1)/6

    #for state 66 and number 78
    transition_matrix[66][67] = float(1)/6
    transition_matrix[66][68] = float(1)/6
    transition_matrix[66][69] = float(1)/6
    transition_matrix[66][70] = float(1)/6
    transition_matrix[66][71] = float(1)/6
    transition_matrix[66][48] = float(1)/6

    #for state 67 and number 79
    transition_matrix[67][68] = float(1)/6
    transition_matrix[67][69] = float(1)/6
    transition_matrix[67][70] = float(1)/6
    transition_matrix[67][71] = float(1)/6
    transition_matrix[67][48] = float(1)/6
    transition_matrix[67][72] = float(1)/6

    #for state 68 and number 80
    transition_matrix[68][69] = float(1)/6
    transition_matrix[68][70] = float(1)/6
    transition_matrix[68][71] = float(1)/6
    transition_matrix[68][48] = float(1)/6
    transition_matrix[68][72] = float(1)/6
    transition_matrix[68][73] = float(1)/6

    #for state 69 and number 81
    transition_matrix[69][70] = float(1)/6
    transition_matrix[69][71] = float(1)/6
    transition_matrix[69][48] = float(1)/6
    transition_matrix[69][72] = float(1)/6
    transition_matrix[69][73] = float(1)/6
    transition_matrix[69][43] = float(1)/6

    #for state 70 and number 82
    transition_matrix[70][71] = float(1)/6
    transition_matrix[70][48] = float(1)/6
    transition_matrix[70][72] = float(1)/6
    transition_matrix[70][73] = float(1)/6
    transition_matrix[70][43] = float(1)/6
    transition_matrix[70][74] = float(1)/6

    #for state 71 and number 83
    transition_matrix[71][48] = float(1)/6
    transition_matrix[71][72] = float(1)/6
    transition_matrix[71][73] = float(1)/6
    transition_matrix[71][43] = float(1)/6
    transition_matrix[71][74] = float(1)/6
    transition_matrix[71][75] = float(1)/6

    #for state 72 and number 85
    transition_matrix[72][73] = float(1)/6
    transition_matrix[72][43] = float(1)/6
    transition_matrix[72][74] = float(1)/6
    transition_matrix[72][75] = float(1)/6
    transition_matrix[72][76] = float(1)/6
    transition_matrix[72][77] = float(1)/6

    #for state 73 and number 86
    transition_matrix[73][43] = float(1)/6
    transition_matrix[73][74] = float(1)/6
    transition_matrix[73][75] = float(1)/6
    transition_matrix[73][76] = float(1)/6
    transition_matrix[73][77] = float(1)/6
    transition_matrix[73][78] = float(1)/6

    #for state 74 and number 88
    transition_matrix[74][75] = float(1)/6
    transition_matrix[74][76] = float(1)/6
    transition_matrix[74][77] = float(1)/6
    transition_matrix[74][78] = float(1)/6
    transition_matrix[74][79] = float(1)/6
    transition_matrix[74][80] = float(1)/6

    #for state 75 and number 89
    transition_matrix[75][76] = float(1)/6
    transition_matrix[75][77] = float(1)/6
    transition_matrix[75][78] = float(1)/6
    transition_matrix[75][79] = float(1)/6
    transition_matrix[75][80] = float(1)/6
    transition_matrix[75][81] = float(1)/6

    #for state 76 and number 90
    transition_matrix[76][77] = float(1)/6
    transition_matrix[76][78] = float(1)/6
    transition_matrix[76][79] = float(1)/6
    transition_matrix[76][80] = float(1)/6
    transition_matrix[76][81] = float(1)/6
    transition_matrix[76][82] = float(1)/6

    #for state 77 and number 91
    transition_matrix[77][78] = float(1)/6
    transition_matrix[77][79] = float(1)/6
    transition_matrix[77][80] = float(1)/6
    transition_matrix[77][81] = float(1)/6
    transition_matrix[77][82] = float(1)/6
    transition_matrix[77][83] = float(1)/6

    #for state 78 and number 92
    transition_matrix[78][79] = float(1)/6
    transition_matrix[78][80] = float(1)/6
    transition_matrix[78][81] = float(1)/6
    transition_matrix[78][82] = float(1)/6
    transition_matrix[78][83] = float(1)/6
    transition_matrix[78][35] = float(1)/6

    #for state 79 and number 93
    transition_matrix[79][80] = float(1)/6
    transition_matrix[79][81] = float(1)/6
    transition_matrix[79][82] = float(1)/6
    transition_matrix[79][83] = float(1)/6
    transition_matrix[79][35] = float(1)/6
    transition_matrix[79][84] = float(1)/6

    #for state 80 and number 94
    transition_matrix[80][81] = float(1)/6
    transition_matrix[80][82] = float(1)/6
    transition_matrix[80][83] = float(1)/6
    transition_matrix[80][35] = float(1)/6
    transition_matrix[80][84] = float(1)/6
    transition_matrix[80][85] = float(1)/6

    #for state 81 and number 95
    transition_matrix[81][82] = float(1)/6
    transition_matrix[81][83] = float(1)/6
    transition_matrix[81][35] = float(1)/6
    transition_matrix[81][84] = float(1)/6
    transition_matrix[81][85] = float(1)/6
    transition_matrix[81][81] = float(1)/6

    #for state 82 and number 96
    transition_matrix[82][83] = float(1)/6
    transition_matrix[82][35] = float(1)/6
    transition_matrix[82][84] = float(1)/6
    transition_matrix[82][85] = float(1)/6
    transition_matrix[82][82] = float(2)/6

    #for state 83 and number 97
    transition_matrix[83][35] = float(1)/6
    transition_matrix[83][84] = float(1)/6
    transition_matrix[83][85] = float(1)/6
    transition_matrix[83][83] = float(3)/6

    #for state 84 and number 99
    transition_matrix[84][85] = float(1)/6
    transition_matrix[84][84] = float(5)/6

    #for state 85 and number 100 
    transition_matrix[85][85] = 1

    transition_matrix = np.array(transition_matrix) #converting into numpy 2d array

    i = 0
    while (i<85):
        j=0
        while(j<85):
            Q_matrix[i][j] = transition_matrix[i][j]
            j = j+1
        i = i+1
    identity_matrix = np.identity(85)

    subtracted_matrix = np.subtract(identity_matrix , Q_matrix)
    inverse_matrix = np.linalg.inv(subtracted_matrix)
    ans = 1
    i=0
    while (i<85):
        ans = ans + inverse_matrix[0][i]
        i=i+1
    return ans



root = tk.Tk()
logo = tk.PhotoImage(file="board.gif")
logo=logo.subsample(2)
w1 = tk.Label(root, image=logo).pack(side="top")
root.title("Snakes and Ladders Simulator")
root.geometry("600x800")
textbox="No of simulations:"

num,path=no_of_steps()
path=np.array(path)
tb1 = """No of steps(theoretical):""" + str(theorotical_no_of_steps())
tb2="Random simulated path:"+"\n"+str(path)
#print("Expected number of steps simulated:"+str(num))
print("Theoretical steps:"+str(theorotical_no_of_steps()))
print(path)
wtext = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=textbox,fg="blue",font=2).place(x=10,y=550)

inp=tk.StringVar()
e1 = tk.Entry(root,textvariable=inp).place(x=180,y=550)


plot_getter = tk.Button(root, text="Get Plot", command=plotter).place(x=400,y=550)  


w1 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=tb1,fg="red",font=2).place(x=10,y=600)

w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=tb2,fg="blue",font=2).place(x=10,y=630)

root.mainloop()





	

