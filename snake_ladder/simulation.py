# import pygame
import pygame
from button_module import *
from position_map import *
import random

#initializing the colors
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
black=(0,0,0)
purple=(153,50,204)
orange=(255,140,0)
seagreen=(32,178,170)
# initialize game engine
pygame.init()

window_width=900
window_height=800

animation_increment=10
clock_tick_rate=20

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("Snake And Ladder Simulator")

dead=False

clock = pygame.time.Clock()
#chessboard image
background_image = pygame.image.load("board.gif").convert()
background_image = pygame.transform.scale(background_image, (700, 700))

#win image 
win_image= pygame.image.load("win.jpg").convert()
win_image= pygame.transform.scale(win_image, (700, 700))

#mario image
mario= pygame.image.load("mario2.png").convert()
mario= pygame.transform.scale(mario, (60, 60))



#assigning co-ordinates to the squares
dict={}
dict[-1]=(800,800)
dict[0]=(800,800)
index=100
num1=19
num2=1
while(index>=91):
	x=25+(100-index)*70
	y=25
	num=index
	while(num>0):
		dict[num]=(x,y)
		y=y+63.636363
		num=num-num1
		dict[num]=(x,y)
		y=y+63.636363
		num=num-num2
	num1-=2
	num2+=2
	index=index-1


#defining the button for dice roll
mybutton=button((33,33,200),750,100,110,50,"ROLL")

#defining the test format for roll
font = pygame.font.Font('freesansbold.ttf', 50)

position=-1
turn=0
#x,y=dict[1]
#pygame.draw.rect(screen,(0,100,100),pygame.Rect(x,y,20,20))
while(dead==False):
    for event in pygame.event.get():
    	pos=pygame.mouse.get_pos()

    	if event.type==pygame.MOUSEBUTTONDOWN:
    		if mybutton.isOver(pos):
    			print("Button clicked")
    			val=random.randint(1,6)
    			if(position<0 and val!=6):
					font1 = pygame.font.Font('freesansbold.ttf', 18)
					text = font1.render("KEEP ROLLING TILL 6!!!", True, green, blue)
					screen.blit(text, [700, 200])
					print("Val is:"+str(val))
					turn=turn+1
					continue
                if(position<0 and val==6):
                	print("insdie")
                	position=0
                	font1 = pygame.font.Font('freesansbold.ttf', 50)
                	text = font1.render("START!!!", True, blue, green)
                	screen.blit(text, [700, 0])
                	font2 = pygame.font.Font('freesansbold.ttf', 18)
                	text = font2.render("KEEP ROLLING TILL 6!!!", True, black, black)
                	screen.blit(text, [700, 200])
                	continue
 
                
                print(position)
                if((position+val) in pos_map):
                	position=pos_map[position+val]
                elif(position+val<=100):
                	position=position+val
                else:
                	position=position
                turn=turn+1
                #print(position)
                text = font.render(str(val), True, green, blue)
                screen.blit(text, [785, 200])



    	if event.type==pygame.MOUSEMOTION:
    		if mybutton.isOver(pos):
    			mybutton.color=(0,255,0)
    		else:
    			mybutton.color=(0,0,255)
        if event.type == pygame.QUIT:
            dead = True

    mybutton.draw(screen)
    if(position==100):
    	screen.blit(win_image, [0, 0])
    else:
    	screen.blit(background_image, [0, 0])

    #(x,y,width,length)
    x,y=dict[position]
    #pygame.draw.rect(screen,blue,pygame.Rect(x,y,20,20))
    rect = mario.get_rect()
    rect.center = (x+8, y+15)
    screen.blit(mario, rect)
    #displaying the turns
    font2 = pygame.font.Font('freesansbold.ttf', 58)
    text2 = font2.render("TURNS", True, purple, orange)
    screen.blit(text2, [700, 500])

    font22 = pygame.font.Font('freesansbold.ttf', 17)
    text22 = font22.render("Roll Button rolls the die", True, seagreen, black)
    screen.blit(text22, [700, 70])

    font3 = pygame.font.Font('freesansbold.ttf', 58)
    text3 = font2.render(str(turn), True, purple, orange)
    screen.blit(text3, [780, 600])


    pygame.display.flip()
    clock.tick(clock_tick_rate)