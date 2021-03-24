import pygame
import sys
import random
import time
import re

from pygame.locals import *
movie=open("movies.txt","r")
movie_list=[]
for x in movie:
    movie_list.append(x.rstrip("\n").upper())

def random_movie(movie_list):
    guess_word=movie_list[random.randint(0,len(movie_list)-1)]
    return guess_word

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

GREY = (200,200,200)

LEFT_CLICK = (1,0,0)
RIGHT_CLICK = (0,0,1)

pygame.init()

pygame.display.set_caption("Hangman")

#32 bit display
Display = pygame.display.set_mode((800,500),0,32)


Font = pygame.font.Font("freesansbold.ttf",30)
Font2 = pygame.font.Font("freesansbold.ttf",20)

Display.fill(WHITE)
def duplicates(lst,item):
    return [i for i,x in enumerate(lst) if x==item]

def Hangman(condition):
    if (condition == 0):
        pygame.draw.line(Display, GREY, (10,400),(300,400),8)#baseline
        pygame.draw.line(Display, GREY, (50,50),(50,400),8)#stick1
        pygame.draw.line(Display, GREY, (50,60),(250,60),8)#stick2
        pygame.draw.line(Display, GREY, (150,60),(150,100),8)#rope
        pygame.draw.circle(Display, GREY, (150,150),50,8)#head
        pygame.draw.line(Display, GREY, (150,200),(150,300),8)#body
        pygame.draw.line(Display, GREY, (150,210),(100,250),8)#lefthand
        pygame.draw.line(Display, GREY, (150,210),(200,250),8)#righthand
        pygame.draw.line(Display, GREY, (150,300),(100,350),8)#leftleg
        pygame.draw.line(Display, GREY, (150,300),(200,350),8)#rightleg

    elif (condition == 1):
        pygame.draw.line(Display, BLACK, (10,400),(300,400),8)#baseline

    elif (condition == 2):
        pygame.draw.line(Display, BLACK, (50,50),(50,400),8)#stick1

    elif (condition == 3):
        pygame.draw.line(Display, BLACK, (50,60),(250,60),8)#stick2

    elif (condition == 4):
        pygame.draw.line(Display, BLACK, (150,60),(150,100),8)#rope

    elif (condition == 5):
        pygame.draw.circle(Display, BLACK, (150,150),50,8)#head

    elif (condition == 6):
        pygame.draw.line(Display, BLACK, (150,200),(150,300),8)#body

    elif (condition == 7):
        pygame.draw.line(Display, BLACK, (150,210),(100,250),8)#lefthand

    elif (condition == 8):
        pygame.draw.line(Display, BLACK, (150,210),(200,250),8)#righthand

    elif (condition == 9):
        pygame.draw.line(Display, BLACK, (150,300),(100,350),8)#leftleg

    elif (condition == 10):
        pygame.draw.line(Display, BLACK, (150,300),(200,350),8)#rightleg

    #game over
    elif (condition == 11):
        pygame.draw.line(Display, BLUE, (10,400),(300,400),8)#baseline
        pygame.draw.line(Display, BLUE, (50,50),(50,400),8)#stick1
        pygame.draw.line(Display, BLUE, (50,60),(250,60),8)#stick2
        pygame.draw.line(Display, BLUE, (150,60),(150,100),8)#rope
        pygame.draw.circle(Display, BLUE, (150,150),50,8)#head
        pygame.draw.line(Display, BLUE, (150,200),(150,300),8)#body
        pygame.draw.line(Display, BLUE, (150,210),(100,250),8)#lefthand
        pygame.draw.line(Display, BLUE, (150,210),(200,250),8)#righthand
        pygame.draw.line(Display, BLUE, (150,300),(100,350),8)#leftleg
        pygame.draw.line(Display, BLUE, (150,300),(200,350),8)#rightleg

def Alphabet():
    al=[["A","B","C","D"],["E","F","G","H"],["I","J","K","L"],["M","N","O","P"],["Q","R","S","T"],["U","V","W","X"],["Y","Z"," "," "]]
    h=w=0
    for i in range(7):
        for j in range(4):
            Draw_circle(al[i][j],w,h)
            w+=5
        h+=5
        w=0
alpha_cen_list=[]
def Draw_circle(Alpha,x,y):
    if Alpha==" ":
        pass
    else:
        pygame.draw.circle(Display,BLUE,(300+10*x,180+10*y),20)
        Display.blit(Font.render(Alpha,True,BLACK),(290+10*x,168+10*y))
def check(tup):
    if(280<tup[0]<320 and 160<tup[1]<200):
        update_word("A")
        return (300, 180)
    elif(330<tup[0]<370 and 160<tup[1]<200):
        update_word("B")
        return (350, 180)
    elif(380<tup[0]<420 and 160<tup[1]<200):
        update_word("C")
        return (400, 180)
    elif(430<tup[0]<470 and 160<tup[1]<200):
        update_word("D")
        return (450, 180)
    elif(280<tup[0]<320 and 210<tup[1]<250):
        update_word("E")
        return (300, 230)
    elif(330<tup[0]<370 and 210<tup[1]<250):
        update_word("F")
        return (350, 230)
    elif(380<tup[0]<420 and 210<tup[1]<250):
        update_word("G")
        return (400, 230)
    elif(430<tup[0]<470 and 210<tup[1]<250):
        update_word("H")
        return (450, 230)
    elif(280<tup[0]<320 and 260<tup[1]<300):
        update_word("I")
        return (300, 280)
    elif(330<tup[0]<370 and 260<tup[1]<300):
        update_word("J")
        return (350, 280)
    elif(380<tup[0]<420 and 260<tup[1]<300):
        update_word("K")
        return (400, 280)
    elif(430<tup[0]<470 and 260<tup[1]<300):
        update_word("L")
        return (450, 280)
    elif(280<tup[0]<320 and 310<tup[1]<350):
        update_word("M")
        return (300, 330)
    elif(330<tup[0]<370 and 310<tup[1]<350):
        update_word("N")
        return (350, 330)
    elif(380<tup[0]<420 and 310<tup[1]<350):
        update_word("O")
        return (400, 330)
    elif(430<tup[0]<470 and 310<tup[1]<350):
        update_word("P")
        return (450, 330)
    elif(280<tup[0]<320 and 360<tup[1]<400):
        update_word("Q")
        return (300, 380)
    elif(330<tup[0]<370 and 360<tup[1]<400):
        update_word("R")
        return (350, 380)
    elif(380<tup[0]<420 and 360<tup[1]<400):
        update_word("S")
        return (400, 380)
    elif(430<tup[0]<470 and 360<tup[1]<400):
        update_word("T")
        return (450, 380)
    elif(280<tup[0]<320 and 410<tup[1]<450):
        update_word("U")
        return (300, 430)
    elif(330<tup[0]<370 and 410<tup[1]<450):
        update_word("V")
        return (350, 430)
    elif(380<tup[0]<420 and 410<tup[1]<450):
        update_word("W")
        return (400, 430)
    elif(430<tup[0]<470 and 410<tup[1]<450):
        update_word("X")
        return (450, 430)
    elif(280<tup[0]<320 and 410<tup[1]<500):
        update_word("Y")
        return (300, 480)
    elif(330<tup[0]<370 and 410<tup[1]<500):
        update_word("Z")
        return (350, 480)
    else:
        print("error")

def del_let(h,w):
    pygame.draw.circle(Display,WHITE,(h,w),20)
    pygame.display.update()

def hinted(guess_word):
    hints=len(guess_word)//3
    hints_list=[]
    for i in range(hints):
        hints_list.append(random.randint(0,len(guess_word)))

    #guess_string=["_" for i in range(len(guess_word))]
    for i in range(len(guess_word)):
        if i in hints_list:
            dups=duplicates(list(guess_word),guess_word[i])
            for k in dups:
                guess_string[k]=guess_word[k]
    
    Display.blit(Font2.render(" ".join(guess_string),True,BLACK),(320,100))
    pygame.display.update()

def update_word(letter):
    global guesses
    if letter in guess_word:
        idx=duplicates(guess_word,letter)
        for k in idx:
            guess_string[k]=letter
        rect=pygame.draw.rect(Display,WHITE,pygame.Rect(320,100,400,40))
        Display.blit(Font2.render(" ".join(guess_string),True,BLACK),(300,100))
        pygame.display.flip()
    else:
        guesses+=1
        Hangman(guesses)
Hangman(0)
Alphabet()

guesses=0
guess_word=random_movie(movie_list)
print(guess_word)
guess_string=["_"  if guess_word[i] != " " else " " for i in range(len(guess_word))]
hinted(guess_word)

def main():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                cen_pos=check(pygame.mouse.get_pos())
                if cen_pos is not None:
                    del_let(cen_pos[0],cen_pos[1])
            if(guesses==10):
                run=False
                Hangman(11)
                time.sleep(2)
                rect=pygame.draw.rect(Display,WHITE,pygame.Rect(200,100,400,200))
                Display.blit(Font2.render("YOU LOST",True,RED),(300,100))
                pygame.display.update()
                time.sleep(5)
                pygame.quit()
                sys.exit()
            print("".join(guess_string))   
            if("".join(guess_string)==guess_word):
                rect=pygame.draw.rect(Display,WHITE,pygame.Rect(200,100,400,200))
                Display.blit(Font2.render("YOU WON",True,RED),(300,100))
                pygame.display.update()
                time.sleep(5)
                pygame.quit()
                sys.exit()
        pygame.display.update()
    

    
main()
