import pygame
import virtkeyboard
mykeys = virtkeyboard.VirtualKeyboard()
pygame.display.init()
size=800,450
screen=pygame.display.set_mode(size)
userinput = mykeys.run(screen)
print userinput
pygame.display.quit()