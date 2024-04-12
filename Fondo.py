import pygame


class Habitacion:
    higiene = 10
    estado = 1


class Jardin(Habitacion):
    nombre = "Jardin"
    fondoLimpio = pygame.image.load("src/img/fondos/jardin.png")
    def dibujar(self, screen):
        screen.blit(self.fondoLimpio, (0, 0))


class Salon(Habitacion):
    nombre = "Salon"
    fondoLimpio = pygame.image.load("src/img/fondos/salon.png")
    def dibujar(self, screen):
        screen.blit(self.fondoLimpio, (0, 0))


class Cocina(Habitacion):
    nombre = "Cocina"
    fondoLimpio = pygame.image.load("src/img/fondos/cocina.png")
    def dibujar(self, screen):
        screen.blit(self.fondoLimpio, (0, 0))


class Dormitorio(Habitacion):
    nombre = "Dormitorio"
    fondoLimpio = pygame.image.load("src/img/fondos/dormitorio.png")
    def dibujar(self, screen):
        screen.blit(self.fondoLimpio, (0, 0))


class Bano(Habitacion):
    nombre = "Bano"
    fondoLimpio = pygame.image.load("src/img/fondos/banno.png")
    def dibujar(self, screen):
        screen.blit(self.fondoLimpio, (0, 0))


class Fondo:
    piso = 0
    habitacion = 1
    # 0-0: Jardin
    # 0-1: Salon
    # 0-2: Cocina
    # 1-0: Dormitorio
    # 1-1: Baño
    habitaciones = [[Jardin(), Salon(), Cocina()], [Dormitorio(), Bano()]]

    def dibujar(self, screen):
        self.habitaciones[self.piso][self.habitacion].dibujar(screen)

    def setDireccion(self, direccion):  # Right: 0, Up: 1, Left: 2, Down: 3
        if direccion == 0:
            if self.habitacion < len(self.habitaciones[self.piso])-1:
                self.habitacion = self.habitacion + 1
        if direccion == 1:
            if self.piso < len(self.habitaciones)-1:
                self.piso = self.piso + 1
                self.habitacion = 0
        if direccion == 2:
            if self.habitacion > 0:
                self.habitacion = self.habitacion - 1
        if direccion == 3:
            if self.piso > 0:
                self.piso = self.piso - 1
                self.habitacion = 1