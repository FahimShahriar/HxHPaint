'''
graphicsT.py
Mr. McKenzie
This is a template that you can use for your simple graphics programs.
'''
from pygame import *
screen = display.set_mode((800,600))
screen.fill((255,255,255))
Backround = image.load("Pictures/Hunter X Hunter Wallpaper.png")
screen.blit(Backround,(0,0))

hold=False
click=False
rectget=False
drag=False


running=True
while running:                   
    for e in event.get():
        if e.type == QUIT:     
            running = False     
        if e.type == MOUSEBUTTONDOWN:
            screenOld=screen.copy()
            oomx,oomy=mouse.get_pos()

    # -------- Your code goes between these two line -------------------------    
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed() 

    """if mb[0]==1 and not rectget:
        click=True
        screen.blit(screenOld,(0,0))
        draw.rect(screen,(0,0,0), (oomx,oomy,mx-oomx,my-oomy),1)
        SelectRect=Rect(oomx,oomy,mx-oomx,my-oomy)
        Select=screen.subsurface(oomx,oomy,mx-oomx,my-oomy)

    if mb[0]==0 and click and not rectget:
        rectget=True
        Select=Select.copy()
        draw.rect(screen,(255,255,255),SelectRect)
        copy=screen.copy()
        
    if mb[0]==1 and SelectRect.collidepoint(mx,my) and rectget and not drag:
        drag=True
        draw.rect(screen,(255,255,255), SelectRect)
        screen.blit(copy,(0,0))
        screen.blit(Select,(mx,my))

    if mb[0]==1 and drag and rectget:
        screen.blit(copy,(0,0))
        screen.blit(Select,(mx,my))"""

    if mb[0]==1 and not rectget:
        click=True
        screen.blit(screenOld,(0,0))
        draw.rect(screen,(0,0,0), (oomx,oomy,mx-oomx,my-oomy),1)
        SelectRect=Rect(oomx,oomy,mx-oomx,my-oomy)
        Select=screen.subsurface(oomx,oomy,mx-oomx,my-oomy)
    

    if mb[0]==0 and click:
        

        

      
    omx,omy=mx,my

    # ------------------------------------------------------------------------ 
    display.flip()  # all drawing happens to memory, this copies it to the screen


quit()
