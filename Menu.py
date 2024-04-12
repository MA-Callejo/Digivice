from math import ceil

import pygame


class Menu:
    fila = 0
    columna = 0
    columnas = 3
    iconos = []
    size = 40
    offset = 2
    colorFondo = (244, 204, 204)
    adapter = pygame.image.load("src/img/iconos/menuAdapter.png")  # 40x 40
    selectedAdapter = pygame.image.load("src/img/iconos/menuAdapterSelected.png")  # 40x 40
    def dibujar(self, screen):
        screen.fill(self.colorFondo)
        for i in range(ceil(len(self.iconos)/self.columnas)):
            for j in range(self.columnas):
                if (self.fila == i) and (self.columna == j):
                    marco = self.adapter
                else:
                    marco = self.selectedAdapter
                screen.blit(marco, (2 + ((self.size + self.offset)*i), 2 + ((self.size + self.offset)*j)))




class subMenu(Menu):
    columnas = 2
    size = 50
    offset = 5
    adapter = pygame.image.load("src/img/iconos/menuAdapter.png")  # 40x 40
    selectedAdapter = pygame.image.load("src/img/iconos/menuAdapterSelected.png")  # 40x 40


class MainMenu(Menu):
    iconos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
