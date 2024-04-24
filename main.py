import pygame as pygame, sys
from pygame.locals import *

from Fondo import Fondo
from Menu import MainMenu, MenuController

pygame.init()
size = (128, 128)
screen = pygame.display.set_mode(size)

fondo = Fondo()
menu = MenuController()
isMenu = False
colorFondo = (244, 204, 204)
clock = pygame.time.Clock()


def leerEventos():
    global fondo, isMenu, menu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isMenu = not isMenu
            if event.key == pygame.K_UP:
                if menu.isActive():
                    menu.setDireccion(1)
                else:
                    fondo.setDireccion(1)  # Right: 0, Up: 1, Left: 2, Down: 3
            if event.key == pygame.K_DOWN:
                if menu.isActive():
                    menu.setDireccion(3)
                else:
                    fondo.setDireccion(3)  # Right: 0, Up: 1, Left: 2, Down: 3
            if event.key == pygame.K_LEFT:
                if menu.isActive():
                    menu.setDireccion(2)
                else:
                    fondo.setDireccion(2)  # Right: 0, Up: 1, Left: 2, Down: 3
            if event.key == pygame.K_RIGHT:
                if menu.isActive():
                    menu.setDireccion(0)
                else:
                    fondo.setDireccion(0)  # Right: 0, Up: 1, Left: 2, Down: 3
            if event.key == pygame.K_a:
                menu.enter()
            if event.key == pygame.K_b:
                menu.esc()


def dibujarPantalla():
    screen.fill(colorFondo)
    if menu.isActive():
        menu.dibujar(screen)
    else:
        fondo.dibujar(screen)
    pygame.display.flip()


while True:
    leerEventos()
    dibujarPantalla()
    clock.tick(1000/60)
