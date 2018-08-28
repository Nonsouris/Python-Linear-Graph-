import pygame
import cmath
import random

pygame.font.init()
pygame.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
font = pygame.font.SysFont('Comic Sans MS', 20)
predict = myfont.render('Prediction Accuracy(y)', False, (255, 255, 255))
legend1 = font.render('Legend', False, (255, 255, 255))
legend2 = font.render('White - Actual trend line', False, (255, 255, 255))
legend3 = font.render('Green - Predicted band', False, (255, 255, 255))
time = myfont.render('Time(x)', False, (255, 255, 255))
#year0 = myfont.render('2019', False, (255, 255, 255))
year1 = myfont.render('2018', False, (255, 255, 255))
year2 = myfont.render('2017', False, (255, 255, 255))
year3 = myfont.render('2016', False, (255, 255, 255))
year4 = myfont.render('2015', False, (255, 255, 255))
screen = pygame.display.set_mode((1150, 800))
screen.blit(legend1,(900,300))
screen.blit(legend2,(900,350))
screen.blit(legend3,(900,400))
screen.blit(predict,(20,100))
screen.blit(time,(800,700))
#screen.blit(year0,(700,700))
screen.blit(year1,(600,700))
screen.blit(year2,(400,700))
screen.blit(year3,(200,700))
done = False
is_blue = True
x = 30
y = 700
a = 30
b = 700
z = 30
w = 700
color = (255, 255, 255)
p = 0
yellow = (255, 255, 255)
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
			is_blue = not is_blue
		
		pressed = pygame.key.get_pressed()
		if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
			p = 0
			while p < 60:
				if y > 180 :
					x += 3 
					y -= 2
					if z < 550:
						z += 3
						w -= 2
					else:
						z += 3
						w -= 1
					if b < 701:
						a += 3
						b -= 2
						if a > 550:
							yellow =(81,165,16)
							b +=5
				p += 1
				pygame.draw.rect(screen, color, pygame.Rect(z, w, 5, 5))
				pygame.draw.rect(screen, yellow, pygame.Rect(x, y, 5, 5))
				pygame.draw.rect(screen, yellow, pygame.Rect(a, b, 5, 5))
		pygame.draw.rect(screen, color, pygame.Rect(30, 700, 4, -550))
		pygame.draw.rect(screen, color, pygame.Rect(30, 700, 850, 4))
		pygame.display.flip()