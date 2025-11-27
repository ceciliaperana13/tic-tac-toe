import pygame
import sys
import subprocess

pygame.init()
pygame.mixer.init()
# fenetre
width, height = 800, 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("tic-tac")
