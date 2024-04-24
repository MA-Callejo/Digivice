from math import ceil

import pygame

class Menu:
    fila = 0
    columna = 0
    columnas = 3
    iconos = []
    submenus = []
    size = 40
    offset = 2
    colorFondo = (244, 204, 204)
    adapter = pygame.image.load("src/img/iconos/menuAdapter.png")  # 40x 40
    selectedAdapter = pygame.image.load("src/img/iconos/menuAdapterSelected.png")  # 40x 40

    def getSubmenu(self):
        return self.submenus[(self.fila * self.columnas) + self.columna]

    def dibujar(self, screen):
        screen.fill(self.colorFondo)
        for i in range(ceil(len(self.iconos)/self.columnas)):
            for j in range(self.columnas):
                if (self.columna == i) and (self.fila == j):
                    marco = self.selectedAdapter
                else:
                    marco = self.adapter
                screen.blit(marco, (2 + ((self.size + self.offset)*i), 2 + ((self.size + self.offset)*j)))
                screen.blit(self.iconos[(i*self.columnas)+j], (7 + (42 * i), 7 + (42 * j)))

    def setDireccion(self, direccion):  # Right: 0, Up: 1, Left: 2, Down: 3
        if direccion == 0:
            if self.columna < self.columnas - 1:
                self.columna = self.columna + 1
            else:
                self.columna = 0
        if direccion == 1:
            if self.fila == 0:
                self.fila = ceil(len(self.iconos)/self.columnas) - 1
            else:
                self.fila = self.fila - 1
        if direccion == 2:
            if self.columna == 0:
                self.columna = self.columnas - 1
            else:
                self.columna = self.columna - 1
        if direccion == 3:
            if self.fila < ceil(len(self.iconos)/self.columnas) - 1:
                self.fila = self.fila + 1
            else:
                self.fila = 0


class subMenu(Menu):
    columnas = 2
    size = 50
    offset = 5
    adapter = pygame.image.load("src/img/iconos/menuAdapter.png")  # 40x 40
    selectedAdapter = pygame.image.load("src/img/iconos/menuAdapterSelected.png")  # 40x 40


class MainMenu(Menu):
    iconos = [
        pygame.image.load("src/img/iconos/grafico-de-torta.png"),
        pygame.image.load("src/img/iconos/restaurante.png"),
        pygame.image.load("src/img/iconos/banera.png"),
        pygame.image.load("src/img/iconos/cama.png"),
        pygame.image.load("src/img/iconos/control-de-juego.png"),
        pygame.image.load("src/img/iconos/drogas.png"),
        pygame.image.load("src/img/iconos/carrito-de-compras.png"),
        pygame.image.load("src/img/iconos/limpieza-de-datos.png"),
        # pygame.image.load("src/img/iconos/mapa.png"),
        pygame.image.load("src/img/iconos/ajustes.png"),
    ]
    submenus = []

class MenuController():
    currentMenu = None
    menus = []
    def isActive(self):
        return len(self.menus) > 0
    def enter(self):
        if len(self.menus) == 0:
            self.menus.append(MainMenu())
        else:
            self.menus.append(self.menus[-1].getSubmenu())
    def esc(self):
        if len(self.menus) > 0:
            self.menus.pop()
    def dibujar(self, screen):
        self.menus[-1].dibujar(screen)
    def setDireccion(self, direccion):
        self.menus[-1].setDireccion(direccion)