import os
os.system("cls")

import pygame

# init
pygame.init()

# membuat display surface object
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang))

# variable runing game
isRun = True

# object game
# posisi
x = 250
y = 250

# ukuran
panjang = 20
lebar = 20

# kecepatan gerak
speed = 5

while isRun:
    pygame.time.delay(10)
    # user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
            
    # ambil semua keyboard press
    keys = pygame.key.get_pressed()
    
    # ke kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    # ke kanan
    if keys[pygame.K_RIGHT] and x < window_lebar-lebar:
        x += speed
    # ke bawah
    if keys[pygame.K_DOWN] and y < window_panjang-panjang:
        y += speed
    # ke atas
    if keys[pygame.K_UP] and y > 0 :
        y -= speed

    # update asset
    window.fill((255,255,255))
    pygame.draw.rect(window,(255,150,0),(x,y,lebar,panjang))
    
    # render display
    pygame.display.update()

pygame.quit()

