##############################################################
###   AUTHOR      : Dmitry                                 ###
###   DATE        : 2021-11-24                             ###
###   DESCRIPTION : Pygame demo program                    ###
##############################################################

import pygame

run = True

width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, (49, 236, 233))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height() * 2)))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT\
        or event.type == pygame.MOUSEBUTTONUP\
        or event.type == pygame.KEYUP:
            run = False
