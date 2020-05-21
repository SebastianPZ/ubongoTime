import pygame
from models.componente import Componente
from models.boton import Boton
logo = pygame.image.load('assets/Acciones/ubongo logo1.png')
menu = pygame.image.load('assets/Fondos/fondoUbongo.jpg')
widthMenu = menu.get_rect().width
heightMenu = menu.get_rect().height
sub = logo.subsurface((0, 1000 // 3, 1000, 1000 // 3))
class Menu(Componente):
    def __init__(self, window, width = widthMenu, height = heightMenu):
        Componente.__init__(self, window.get_rect().width / 2 - width / 2, window.get_rect().height / 2 - height / 2, width, height)
        self.window = window
        self.logoRect = logo.get_rect()
        self.botonIniciar = None
        self.botonDificultad = None

    def dibujarMenu(self):
        self.window.blit(menu, (self.x, self.y))
        xLogo = (2*self.x + self.width)/2 - self.logoRect.width/2
        yLogo = (2*self.y + self.height)/ 2 - self.logoRect.height / 2 - 100
        self.window.blit(logo, (xLogo, yLogo))
        self.botonIniciar = Boton((0, 0, 0), (255, 255, 255), (2*self.x + self.width)/2 - 250/2, yLogo + self.logoRect.height/3 + self.height / 2, 250, 70,
                             "Iniciar juego")
        self.botonDificultad = Boton((0, 0, 0), (255, 255, 255), self.botonIniciar.x, self.botonIniciar.y + self.botonIniciar.height + 40,
                                250, 70, "Dificultad")
        self.botonIniciar.draw(self.window)
        self.botonDificultad.draw(self.window)
