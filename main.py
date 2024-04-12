import pygame as pygame, sys
from pygame.locals import *

from Fondo import Fondo

pygame.init()
size = (128, 128)
screen = pygame.display.set_mode(size)

fondo = Fondo()
colorFondo = (244, 204, 204)
MENU_ITEMS = 8
clock = pygame.time.Clock()
menuAdapter = pygame.image.load("src/img/iconos/menuAdapter.png")  # 43x43
menuAdapterSelected = pygame.image.load("src/img/iconos/menuAdapterSelected.png")  # 43x43
menu = False
menu_selected = 0
submenu = False
submenuIndex = 0
submenu_selected = 0
MAX_PISO = 1
MAX_HABITACIONES = [2, 1]
habitaciones = [[pygame.image.load("src/img/fondos/jardin.png"), pygame.image.load("src/img/fondos/salon.png"), pygame.image.load("src/img/fondos/cocina.png")],
                [pygame.image.load("src/img/fondos/dormitorio.png"), pygame.image.load("src/img/fondos/banno.png")]]


def leerEventos():
    global menu, menu_selected, submenu_selected, submenu, fondo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu = not menu
            if event.key == pygame.K_UP:
                if menu:
                    if menu_selected - 3 >= 0:
                        menu_selected = menu_selected - 3
                else:
                    fondo.setDireccion(1)  # Right: 0, Up: 1, Left: 2, Down: 3
            if event.key == pygame.K_DOWN:
                if menu:
                    if menu_selected + 3 <= MENU_ITEMS:
                        menu_selected = menu_selected + 3
                else:
                    fondo.setDireccion(3)  # Right: 0, Up: 1, Left: 2, Down: 3
            if event.key == pygame.K_LEFT:
                if menu:
                    if menu_selected - 1 >= 0:
                        menu_selected = menu_selected - 1
                else:
                    fondo.setDireccion(2)  # Right: 0, Up: 1, Left: 2, Down: 3
            if event.key == pygame.K_RIGHT:
                if menu:
                    if menu_selected + 1 <= MENU_ITEMS:
                        menu_selected = menu_selected + 1
                else:
                    fondo.setDireccion(0)  # Right: 0, Up: 1, Left: 2, Down: 3
            if event.key == pygame.K_a:
                if menu:
                    if menu_selected == 0:
                        mostrarEstats()
                    if menu_selected == 1:
                        menuComida()
                    if menu_selected == 2:
                        ducha()
                    if menu_selected == 3:
                        menuLimpieza()
                    if menu_selected == 4:
                        menuCompra()
                    if menu_selected == 5:
                        menuAjustes()
                    if menu_selected == 6:
                        menuJuegos()
                    if menu_selected == 7:
                        dormir()
                    if menu_selected == 8:
                        mapa()
                    if menu_selected == 9:
                        menuMedicina()
                else:
                    if submenu:
                        pass
                    else:
                        menu = True
            if event.key == pygame.K_b:
                if menu:
                    menu = False
                    menu_selected = 0
                if submenu:
                    submenu_selected = 0
                    submenu = False
                    menu = True

submenu_items = []
def mostrarEstats():
    pass

def menuComida():
    submenuIndex = 1
    submenu_items = ["Arroz"]
    submenu = True

def ducha():
    pass

def menuLimpieza():
    submenuIndex = 2
    submenu_items = ["Jardin", "Salon", "Cocina", "Cuarto", "Baño"]

def menuCompra():
    pass

def menuAjustes():
    pass

def menuJuegos():
    pass

def dormir():
    pass

def mapa():
    pass

def menuMedicina():
    pass


def dibujarPantalla():
    screen.fill(colorFondo)
    if menu:
        for i in range(MENU_ITEMS + 1):
            if i == menu_selected:
                marco = menuAdapterSelected
            else:
                marco = menuAdapter
            screen.blit(marco, (2 + (i % 3) * 42, 2 + (i // 3) * 42))
    elif submenu:
        for i in range(len(submenu_items) + 1):
            if i == submenu_selected:
                marco = menuAdapterSelected
            else:
                marco = menuAdapter
            screen.blit(marco, (2 + (i % 3) * 42, 2 + (i // 3) * 42))
    else:
        fondo.dibujar(screen)
    pygame.display.flip()


while True:
    leerEventos()
    dibujarPantalla()
    clock.tick(1000/60)
