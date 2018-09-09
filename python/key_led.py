import RPi.GPIO as GPIO
import time
import pygame,sys
from pygame.locals import *

pygame.init()

canvas= pygame.display.set_mode((50,50))
pygame.display.set_caption('keyboard Input')
black=(0,0,0)
canvas.fill(black)
pygame.display.update()

i=3
l1=4
l2=17
l3=27
GPIO.setmode(GPIO.BCM)
GPIO.setup(l1, GPIO.OUT)
GPIO.setup(l2, GPIO.OUT)
GPIO.setup(l3, GPIO.OUT)

print("Started")

while 1:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_q:
                #print("w pressed")
                GPIO.output(l1, True)
                

            if event.key == pygame.K_w:
                #print("q pressed")
                GPIO.output(l2, True)

            if event.key == pygame.K_e:
                #print("stop")
                GPIO.output(l3, True)


            if event.key == pygame.K_SPACE:
                #print("q pressed")
                GPIO.output(l1, True)
                GPIO.output(l2, True)
                GPIO.output(l3, True)
                

            if event.key == pygame.K_ESCAPE:
                print("stop")
                GPIO.cleanup()
                pygame.quit()
                sys.exit()


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                #print("stop")
                GPIO.output(l1, False)

        
            if event.key == pygame.K_w:
                #print("stop")
                GPIO.output(l2, False)

        
            if event.key == pygame.K_e:
                #print("stop")
                GPIO.output(l3, False)


        
        
            if event.key == pygame.K_SPACE:
                #print("stop")
                GPIO.output(l1, False)
                GPIO.output(l2, False)
                GPIO.output(l3, False)



                
                





















