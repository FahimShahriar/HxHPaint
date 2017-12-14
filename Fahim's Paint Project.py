    # Paint Project
#Shahriar,Fahim
#init==============================================
from pygame import *
from random import randint
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

root = Tk()
root.withdraw()

screen = display.set_mode((1200, 743))
tool = "pencil"
color = (0, 0, 0)
size = 11
filled = False
cback = False
polypointx = []
polypointy = []

undo = []
redo = []
undoDraw = False

#resizing images===================================
def backSize(image):
    return transform.smoothscale(image, (750, 550))


def stickResize(image, size):
    sizex, sizey = image.get_rect().size
    if sizex > sizey:
        ratio = sizey / sizex
        return transform.smoothscale(image, (size * 4, int(size * 4 * ratio)))
    elif sizey > sizex:
        ratio = sizex / sizey
        return transform.smoothscale(image, (int(size * 4 * ratio), size * 4))
    else:
        return transform.smoothscale(image, (size * 4, size * 4))


def backIcon(image):
    return transform.smoothscale(image, (70, 70))


def stickSize(image):
    sizex, sizey = image.get_rect().size
    sizex = sizex // 4
    sizey = sizey // 4
    return transform.smoothscale(image, (sizex, sizey))


def stickIcon(image):
    sizex, sizey = image.get_rect().size
    if sizex > sizey:
        ratio = sizey / sizex
        return transform.smoothscale(image, (60, int(60 * ratio)))
    elif sizey > sizex:
        ratio = sizex / sizey
        return transform.smoothscale(image, (int(60 * ratio), 60))
    else:
        return transform.smoothscale(image, (60, 60))


def stickHold(mx, my, image):
    sizex, sizey = image.get_rect().size
    return mx - (sizex // 2), my - (sizey // 2)


#selecting options=================================
def clearselect():
    draw.rect(screen, (0, 0, 0), brushButt, 3)
    draw.rect(screen, (0, 0, 0), pencilButt, 3)
    draw.rect(screen, (0, 0, 0), eraserButt, 3)
    draw.rect(screen, (0, 0, 0), theRectButt, 3)
    draw.rect(screen, (0, 0, 0), lineButt, 3)
    draw.rect(screen, (0, 0, 0), spraypaintButt, 3)
    draw.rect(screen, (0, 0, 0), theEllipseButt, 3)
    draw.rect(screen, (0, 0, 0), polygonButt, 3)
    draw.rect(screen, (0, 0, 0), fillButt, 3)
    draw.rect(screen, (0, 0, 0), nenButt, 3)
    draw.rect(screen, (0, 0, 0), pickerButt, 3)
    draw.rect(screen, (0, 0, 0), lightningButt, 3)

    draw.rect(screen, (0, 0, 0), gangButt, 3)
    draw.rect(screen, (0, 0, 0), gonButt, 3)
    draw.rect(screen, (0, 0, 0), killuaButt, 3)
    draw.rect(screen, (0, 0, 0), hunterButt, 3)
    draw.rect(screen, (0, 0, 0), leorioButt, 3)
    draw.rect(screen, (0, 0, 0), kurapikaButt, 3)
    draw.rect(screen, (0, 0, 0), hisokaButt, 3)


def clearselectBack():
    draw.rect(screen, (0, 0, 0), backroundButt, 3)
    draw.rect(screen, (0, 0, 0), beginningButt, 3)
    draw.rect(screen, (0, 0, 0), beyondButt, 3)
    draw.rect(screen, (0, 0, 0), endButt, 3)
    draw.rect(screen, (0, 0, 0), greedislandButt, 3)
    draw.rect(screen, (0, 0, 0), moonButt, 3)
    draw.rect(screen, (0, 0, 0), nglButt, 3)
    draw.rect(screen, (0, 0, 0), worldtreeButt, 3)

#LoadImages========================================
Backround = image.load("Pictures/Hunter X Hunter Wallpaper.png")
pallet = image.load("Pictures/pallet.png")
pallet = transform.flip(pallet, False, True)
pallet = transform.smoothscale(pallet, (200, 200))
logo = image.load("Pictures/Logo.png")
logo = stickSize(logo)

pencilIcon = image.load("Pictures/Icons/pencil.png")
brushIcon = image.load("Pictures/Icons/brush.png")
eraserIcon = image.load("Pictures/Icons/eraser.png")
lineIcon = image.load("Pictures/Icons/line.png")
spraypaintIcon = image.load("Pictures/Icons/spray.png")
rectIcon = image.load("Pictures/Icons/rectangle.png")
ellipseIcon = image.load("Pictures/Icons/ellipse.png")
polygonIcon = image.load("Pictures/Icons/polygon.png")
fillIcon = image.load("Pictures/Icons/bucketfill.png")
nenIcon = transform.smoothscale(image.load("Pictures/Icons/nen.png"), (40, 40))
pickerIcon = image.load("Pictures/Icons/picker.png")
undoIcon = stickIcon(image.load("Pictures/Icons/undo.png"))
redoIcon = stickIcon(image.load("Pictures/Icons/redo.png"))
saveIcon = stickIcon(image.load("Pictures/Icons/save.png"))
loadIcon = stickIcon(image.load("Pictures/Icons/load.png"))

gangSticker = image.load("Pictures/Stickers/Gang.png")
gonSticker = image.load("Pictures/Stickers/Gon.png")
killuaSticker = image.load("Pictures/Stickers/Killua.png")
hunterSticker = image.load("Pictures/Stickers/Hunter.png")
leorioSticker = image.load("Pictures/Stickers/Leorio.png")
kurapikaSticker = image.load("Pictures/Stickers/Kurapika.png")
hisokaSticker = image.load("Pictures/Stickers/Hisoka.png")
stickerIcons = []
stickers = [gangSticker, gonSticker, killuaSticker, hunterSticker, leorioSticker, kurapikaSticker, hisokaSticker]
for sticker in stickers:
    stickerIcons.append(stickIcon(sticker))
for i in range(len(stickers)):
    stickers[i] = stickSize(stickers[i])

beginningBack = backSize(image.load("Pictures/Backrounds/Beggening1.png"))
beyondBack = backSize(image.load("Pictures/Backrounds/Beyond1.png"))
endBack = backSize(image.load("Pictures/Backrounds/End1.png"))
greedislandBack = backSize(image.load("Pictures/Backrounds/Greed Island1.png"))
moonBack = backSize(image.load("Pictures/Backrounds/Moon1.png"))
nglBack = backSize(image.load("Pictures/Backrounds/NGL1.png"))
worldtreeBack = backSize(image.load("Pictures/Backrounds/World Tree1.png"))
backIcons = []
backrounds = [beginningBack, beyondBack, endBack, greedislandBack, moonBack, nglBack, worldtreeBack]
for back in backrounds:
    backIcons.append(backIcon(back))

#Backround=========================================

display.set_caption("Hunter X Hunter Paint")
screen.blit(Backround, (0, 0))

canvasRect = Rect(80, 80, 750, 550)
draw.rect(screen, (255, 255, 255), canvasRect)
draw.rect(screen, (0, 0, 0), canvasRect, 3)

#Alpha Surface=====================================
cover = Surface((1200, 675)).convert()
cover.set_alpha(55, RLEACCEL)
cover.set_colorkey((255, 254, 255))

#Tools=============================================
def pencil(omx, omy, mx, my):
    draw.line(screen, (color), (omx, omy), (mx, my))


def brush(omx, omy, mx, my):
    x = mx - omx
    y = my - omy
    d = int((x ** 2 + y ** 2) ** 0.5)
    if d == 0:
        d = 1
    for i in range(int(d)):
        dx = int(omx + i / d * x)
        dy = int(omy + i / d * y)
        draw.circle(screen, (color), (dx, dy), size)



def eraser(omx, omy, mx, my):
    x = mx - omx
    y = my - omy
    d = int(((x) ** 2 + (y) ** 2) ** 0.5)
    if d == 0:
        d = 1
    for i in range(int(d)):
        dx = int(omx + i / d * x)
        dy = int(omy + i / d * y)
        draw.circle(screen, (255, 255, 255), (dx, dy), size)


def line(oomx, oomy, mx, my, screenOld):
    screen.blit(screenOld, (0, 0))
    screen.set_clip(canvasRect)
    draw.line(screen, (color), (oomx, oomy), (mx, my), size)
    screen.set_clip(None)


def spraypaint(mx, my):
    for i in range(10):
        rx = mx + randint(-1 * size, size)
        ry = my + randint(-1 * size, size)
        dist = int(((mx - rx) ** 2 + (my - ry) ** 2) ** 0.5)
        if dist < size:
            draw.line(screen, (color), (rx, ry), (rx, ry))


def theRect(omx, omy, mx, my, screenOld):
    screen.blit(screenOld, (0, 0))
    screen.set_clip(canvasRect)
    if not filled:
        draw.rect(screen, (color), (omx, omy, mx - omx, my - omy), size)

        draw.rect(screen, (color), (omx - size // 2, omy - size // 2, size, size))
        draw.rect(screen, (color), (mx - size // 2 - 1, my - size // 2 - 1, size, size))
        draw.rect(screen, (color), (mx - size // 2 - 1, omy - size // 2, size, size))
        draw.rect(screen, (color), (omx - size // 2, my - size // 2 - 1, size, size))
    else:
        draw.rect(screen, (color), (omx, omy, mx - omx, my - omy))
    screen.set_clip(None)


def theEllipse(oomx, oomy, mx, my, screenOld):
    screen.blit(screenOld, (0, 0))
    screen.set_clip(canvasRect)
    ellipseRect = Rect(oomx, oomy, mx - oomx, my - oomy)
    ellipseRect.normalize()
    if ellipseRect.height < size * 2 or ellipseRect.width < size * 2 or filled:
        draw.ellipse(screen, (color), ellipseRect, 0)
    else:
        draw.ellipse(screen, (color), ellipseRect, size)
    screen.set_clip(None)


def polygon(mx, my, mb):
    global polypointx, polypointy
    if mb[0] == 1 and canvasRect.collidepoint(mx, my):
        polypointx.append(mx)
        polypointy.append(my)
    elif mb[2] == 1 and len(polypointx) > 1:
        draw.line(screen, (color), (polypointx[0], polypointy[0]), (polypointx[-1], polypointy[-1]), size)
        polypointx = []
        polypointy = []

    if len(polypointx) > 1:
        for i in range(len(polypointx) - 1):
            draw.line(screen, (color), (polypointx[i], polypointy[i]), (polypointx[i + 1], polypointy[i + 1]), size)


def fill(mx, my):
    fill = []
    oldColor = screen.get_at((mx, my))
    fill.append((mx, my))
    if color != oldColor:
        while len(fill) > 0:
            for i in range(len(fill)):
                cx, cy = fill.pop()
                screen.set_at((cx, cy), color)
                if screen.get_at((cx + 1, cy)) == oldColor:
                    fill.append((cx + 1, cy))
                if screen.get_at((cx - 1, cy)) == oldColor:
                    fill.append((cx - 1, cy))
                if screen.get_at((cx, cy + 1)) == oldColor:
                    fill.append((cx, cy + 1))
                if screen.get_at((cx, cy - 1)) == oldColor:
                    fill.append((cx, cy - 1))


def nen(mx, my, omx, omy, screenOld):
    x = mx - omx
    y = my - omy
    d = int(((x) ** 2 + (y) ** 2) ** 0.5)
    if d == 0:
        d = 1
    for i in range(int(d)):
        dx = int(omx + i / d * x)
        dy = int(omy + i / d * y)
        draw.circle(cover, color, (dx, dy), size)
    screen.blit(screenOld, (0, 0))
    screen.blit(cover, (0, 0))


def picker(mx, my):
    return screen.get_at((mx, my))


def lightning(screen, col, x, y, steps):
    if steps > 0:
        x2 = x + randint(-20, 20)
        y2 = y + randint(-20, 20)
        for i in range(randint(0, 3)):
            draw.line(screen, col, (x, y), (x2, y2))
            lightning(screen, col, x2, y2, steps - 1)


def sticker(mx, my, sticker, screenOld):
    screen.blit(screenOld, (0, 0))
    screen.set_clip(canvasRect)
    sticker = stickResize(sticker, size)
    mx, my = stickHold(mx, my, sticker)
    screen.blit(sticker, (mx, my))
    screen.set_clip(None)


def backround(back):
    screen.blit(back, (80, 80))

#TheLayout|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
screen.blit(logo, (0, 0))

#The Tools=========================================
#pencil
pencilButt = Rect(10, 80, 50, 50)
draw.rect(screen, (255, 255, 255), pencilButt)
screen.blit(pencilIcon, (15, 85, 50, 50))

#brush
brushButt = Rect(10, 140, 50, 50)
draw.rect(screen, (255, 255, 255), brushButt)
screen.blit(brushIcon, (15, 145, 50, 50))

#eraser
eraserButt = Rect(10, 200, 50, 50)
draw.rect(screen, (255, 255, 255), eraserButt)
screen.blit(eraserIcon, (15, 205, 50, 50))

#line
lineButt = Rect(10, 260, 50, 50)
draw.rect(screen, (255, 255, 255), lineButt)
screen.blit(lineIcon, (15, 265, 50, 50))

#spraypaint
spraypaintButt = Rect(10, 320, 50, 50)
draw.rect(screen, (255, 255, 255), spraypaintButt)
screen.blit(spraypaintIcon, (15, 325, 50, 50))

#theRect
theRectButt = Rect(10, 380, 50, 50)
draw.rect(screen, (255, 255, 255), theRectButt)
screen.blit(rectIcon, (15, 385, 50, 50))

#theEllipse
theEllipseButt = Rect(10, 440, 50, 50)
draw.rect(screen, (255, 255, 255), theEllipseButt)
screen.blit(ellipseIcon, (15, 445, 50, 50))

#polygon
polygonButt = Rect(10, 500, 50, 50)
draw.rect(screen, (255, 255, 255), polygonButt)
screen.blit(polygonIcon, (15, 505, 50, 50))

#fill
fillButt = Rect(10, 560, 50, 50)
draw.rect(screen, (255, 255, 255), fillButt)
screen.blit(fillIcon, (15, 565, 50, 50))

#nen
nenButt = Rect(10, 620, 50, 50)
draw.rect(screen, (255, 255, 255), nenButt)
screen.blit(nenIcon, (15, 625, 50, 50))

#filled
filledButt = Rect(10, 680, 50, 40)
draw.rect(screen, (255, 255, 255), filledButt)
draw.rect(screen, (0, 0, 0), filledButt, 3)
draw.rect(screen, (0, 0, 0), (15, 685, 40, 30), 1)

#color picker
pickerButt = Rect(950, 550, 50, 50)
draw.rect(screen, (255, 255, 255), pickerButt)
screen.blit(pickerIcon, (955, 555))

#lightning
lightningButt = Rect(850, 450, 80, 100)
draw.rect(screen, (255, 255, 255), lightningButt)
draw.rect(screen, (0, 0, 0), lightningButt, 3)
screen.set_clip(lightningButt)
for i in range(100):
    col = (randint(0, 255), randint(0, 255), randint(0, 255))
    lightning(screen, col, 890, 500, 4)
screen.set_clip(None)

#The Stickers======================================
#Gang
gangButt = Rect(80, 650, 70, 70)
draw.rect(screen, (255, 255, 255), gangButt)
screen.blit(stickerIcons[0], (85, 655, 70, 70))

#Gon
gonButt = Rect(160, 650, 70, 70)
draw.rect(screen, (255, 255, 255), gonButt)
screen.blit(stickerIcons[1], (185, 655, 70, 70))

#Killua
killuaButt = Rect(240, 650, 70, 70)
draw.rect(screen, (255, 255, 255), killuaButt)
screen.blit(stickerIcons[2], (257, 655, 70, 70))

#Hunter
hunterButt = Rect(320, 650, 70, 70)
draw.rect(screen, (255, 255, 255), hunterButt)
screen.blit(stickerIcons[3], (326, 665, 70, 70))

#Leorio
leorioButt = Rect(400, 650, 70, 70)
draw.rect(screen, (255, 255, 255), leorioButt)
screen.blit(stickerIcons[4], (405, 655, 70, 70))

#Kurapika
kurapikaButt = Rect(480, 650, 70, 70)
draw.rect(screen, (255, 255, 255), kurapikaButt)
screen.blit(stickerIcons[5], (485, 655, 70, 70))

#Hisoka
hisokaButt = Rect(560, 650, 70, 70)
draw.rect(screen, (255, 255, 255), hisokaButt)
screen.blit(stickerIcons[6], (565, 655, 70, 70))

#Backrounds========================================
backroundButt = Rect(160, 5, 70, 70)
draw.rect(screen, color, backroundButt)

#beginning
beginningButt = Rect(240, 5, 70, 70)
draw.rect(screen, (255, 255, 255), beginningButt)
screen.blit(backIcons[0], beginningButt)

#beyond
beyondButt = Rect(320, 5, 70, 70)
draw.rect(screen, (255, 255, 255), beyondButt)
screen.blit(backIcons[1], beyondButt)

#end
endButt = Rect(400, 5, 70, 70)
draw.rect(screen, (255, 255, 255), endButt)
screen.blit(backIcons[2], endButt)

#greedisland
greedislandButt = Rect(480, 5, 70, 70)
draw.rect(screen, (255, 255, 255), greedislandButt)
screen.blit(backIcons[3], greedislandButt)

#moon
moonButt = Rect(560, 5, 70, 70)
draw.rect(screen, (255, 255, 255), moonButt)
screen.blit(backIcons[4], moonButt)

#ngl
nglButt = Rect(640, 5, 70, 70)
draw.rect(screen, (255, 255, 255), nglButt)
screen.blit(backIcons[5], nglButt)

#worldtree
worldtreeButt = Rect(720, 5, 70, 70)
draw.rect(screen, (255, 255, 255), worldtreeButt)
screen.blit(backIcons[6], worldtreeButt)

#Discription=======================================
fontRect = Rect(640, 640, 300, 95)
draw.rect(screen, (255, 255, 255), fontRect)
draw.rect(screen, (0, 0, 0), fontRect, 3)
draw.rect(screen, (0, 255, 0), fontRect, 1)

font.init()
titleFont = font.Font("Fonts/Title.ttf", 30)
titleFont.set_underline(True)
titleFont.set_bold(True)
hunterFont = font.Font("Fonts/Hunter.ttf", 20)

Title = titleFont.render("Pencil Tool", True, (0, 0, 0))
screen.blit(Title, (645, 645))
Hunter = hunterFont.render("Draws thin freehanded lines", True, (0, 0, 0))
screen.blit(Hunter, (645, 680))
Hunter2 = hunterFont.render("that changes color.", True, (0, 0, 0))
screen.blit(Hunter2, (645, 705))


def stickd(name):
    draw.rect(screen, (255, 255, 255), fontRect)
    draw.rect(screen, (0, 0, 0), fontRect, 3)
    draw.rect(screen, (0, 255, 0), fontRect, 1)
    Title = titleFont.render("%s Sticker" % (name), True, (0, 0, 0))
    screen.blit(Title, (645, 645))
    Hunter = hunterFont.render("Drag to draw %s " % (name), True, (0, 0, 0))
    screen.blit(Hunter, (645, 680))
    Hunter2 = hunterFont.render("sticker on specified place.", True, (0, 0, 0))
    screen.blit(Hunter2, (645, 705))

#Extra=============================================
#save
saveRect = Rect(1110, 10, 70, 70)
draw.rect(screen, (255, 255, 255), saveRect)
draw.rect(screen, (0, 0, 0), saveRect, 3)
screen.blit(saveIcon, (1115, 15))

#load
loadRect = Rect(1030, 10, 70, 70)
draw.rect(screen, (255, 255, 255), loadRect)
draw.rect(screen, (0, 0, 0), loadRect, 3)
screen.blit(loadIcon, (1035, 15))

#redo
redoRect = Rect(950, 10, 70, 70)
draw.rect(screen, (255, 255, 255), redoRect)
draw.rect(screen, (0, 0, 0), redoRect, 3)
screen.blit(redoIcon, (955, 15))

#undo
undoRect = Rect(870, 10, 70, 70)
draw.rect(screen, (255, 255, 255), undoRect)
draw.rect(screen, (0, 0, 0), undoRect, 3)
screen.blit(undoIcon, (875, 15))

#Music=============================================
init()
mixer.music.load("Audio/hunter background.wav")
mixer.music.set_volume(0.5)
mixer.music.play(-1)

Playing = True
playIcon = stickIcon(image.load("Pictures/Icons/play.png"))
pauseIcon = stickIcon(image.load("Pictures/Icons/pause.png"))
musicButt = Rect(850, 560, 80, 70)
draw.rect(screen, (255, 255, 255), musicButt)
draw.rect(screen, (0, 0, 255), musicButt, 3)
screen.blit(pauseIcon, (860, 565))

#color pallet======================================
palletRect = Rect(1000, 550, 200, 200)
screen.blit(pallet, (1000, 550))
draw.rect(screen, (0, 0, 0), palletRect, 3)

shadeRect = Rect(1050, 450, 250, 100)
draw.rect(screen, (255, 255, 255), shadeRect)
for i in range(95):
    draw.line(screen, (255 - 255 / 100 * i, 255 - 255 / 100 * i, 255 - 255 / 100 * i), (1050, 455 + i), (1200, 455 + i))

draw.rect(screen, (0, 0, 0), shadeRect, 3)

#size==============================================
sizeRect = Rect(950, 450, 100, 100)

dback = False
clearselect()
clearselectBack()
draw.rect(screen, (255, 0, 0), pencilButt, 3)
#TheLoop|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
omx, omy = 0, 0
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

        #copy old screen and scroll size~~~~~~~~~~~~~~~~~~~
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 4:
                size = min(size + 2, 101)
            elif e.button == 5:
                size = max(size - 2, 1)
            else:
                oomx, oomy = mouse.get_pos()
                screenOld = screen.copy()
                cover.fill((255, 254, 255))

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()

        #Undo Redo~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if ((e.type == MOUSEBUTTONUP and e.button != 4 and e.button != 5) and canvasRect.collidepoint(oomx,
                                                                                                      oomy) and tool != "picker") or cback:
            cback = False
            undo.append(screen.subsurface(80, 0, 750, 630).copy())

        if e.type == MOUSEBUTTONUP and undoRect.collidepoint(mx, my) and len(undo) > 1:
            screen.blit(undo[-2], (80, 0))
            last = undo.pop()
            redo.append(last)
            undoDraw = True

        if e.type == MOUSEBUTTONUP and redoRect.collidepoint(mx, my) and len(redo) > 0:
            screen.blit(redo[-1], (80, 0))
            del redo[-1]
            undo.append(screen.subsurface(80, 0, 750, 630).copy())

        if (((e.type == MOUSEBUTTONUP and e.button != 4 and e.button != 5) and canvasRect.collidepoint(oomx,
                                                                                                       oomy) and tool != "picker") or cback) and undoDraw:
            undoDraw == False
            redo = []

        #Save Load~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if e.type == MOUSEBUTTONUP and saveRect.collidepoint(mx, my):
            fileName = asksaveasfilename(parent=root, title="Save Image As:")
            if fileName != "":
                image.save(screen.subsurface(canvasRect), "%s.png" % (fileName))

        elif e.type == MOUSEBUTTONUP and loadRect.collidepoint(mx, my):
            fileName = askopenfilename(parent=root, title="Open Image:")
            if fileName != "":
                load_img = image.load(fileName)
                screen.set_clip(canvasRect)
                screen.blit(load_img, (80, 80))
                screen.set_clip(None)
                cback = True
                redolist = []

            #color pallet~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if (palletRect.collidepoint(mx, my) or shadeRect.collidepoint(mx, my)) and mb[0] == 1:
            color = screen.get_at((mx, my))
        draw.rect(screen, color, (950, 600, 50, 150))
        draw.rect(screen, (0, 0, 0), (950, 600, 50, 150), 3)

        #size~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        draw.rect(screen, (255, 255, 255), sizeRect)
        draw.rect(screen, (0, 0, 0), sizeRect, 3)
        screen.set_clip(sizeRect)
        draw.circle(screen, (0, 0, 0), (1000, 500), size)
        screen.set_clip(None)

        #filled~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if filledButt.collidepoint(mx, my) and e.type == MOUSEBUTTONDOWN:
            filled = not filled
            if filled:
                draw.rect(screen, (255, 255, 255), filledButt)
                draw.rect(screen, (0, 0, 255), filledButt, 3)
                draw.rect(screen, (0, 0, 0), (15, 685, 40, 30))
            else:
                draw.rect(screen, (255, 255, 255), filledButt)
                draw.rect(screen, (0, 0, 0), filledButt, 3)
                draw.rect(screen, (0, 0, 0), (15, 685, 40, 30), 1)

            #Music~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if musicButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
            Playing = not Playing

            if Playing:
                draw.rect(screen, (255, 255, 255), musicButt)
                draw.rect(screen, (0, 0, 255), musicButt, 3)
                screen.blit(pauseIcon, (860, 565))
                mixer.music.unpause()
            else:
                draw.rect(screen, (255, 255, 255), musicButt)
                draw.rect(screen, (0, 0, 0), musicButt, 3)
                screen.blit(playIcon, (860, 565))
                mixer.music.pause()


            #selecting tools~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    if pencilButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        tool = "pencil"
        clearselect()
        draw.rect(screen, (255, 0, 0), pencilButt, 3)

        draw.rect(screen, (255, 255, 255), fontRect)
        draw.rect(screen, (0, 0, 0), fontRect, 3)
        draw.rect(screen, (0, 255, 0), fontRect, 1)
        Title = titleFont.render("Pencil Tool", True, (0, 0, 0))
        screen.blit(Title, (645, 645))
        Hunter = hunterFont.render("Draws thin freehanded lines", True, (0, 0, 0))
        screen.blit(Hunter, (645, 680))
        Hunter2 = hunterFont.render("that changes color.", True, (0, 0, 0))
        screen.blit(Hunter2, (645, 705))

    elif brushButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        tool = "brush"
        clearselect()
        draw.rect(screen, (255, 0, 0), brushButt, 3)

        draw.rect(screen, (255, 255, 255), fontRect)
        draw.rect(screen, (0, 0, 0), fontRect, 3)
        draw.rect(screen, (0, 255, 0), fontRect, 1)
        Title = titleFont.render("Paintbrush Tool", True, (0, 0, 0))
        screen.blit(Title, (645, 645))
        Hunter = hunterFont.render("Draws like a paintbrush", True, (0, 0, 0))
        screen.blit(Hunter, (645, 680))
        Hunter2 = hunterFont.render("that changes color and size.", True, (0, 0, 0))
        screen.blit(Hunter2, (645, 705))

    elif eraserButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        tool = "eraser"
        clearselect()
        draw.rect(screen, (255, 0, 0), eraserButt, 3)

        draw.rect(screen, (255, 255, 255), fontRect)
        draw.rect(screen, (0, 0, 0), fontRect, 3)
        draw.rect(screen, (0, 255, 0), fontRect, 1)
        Title = titleFont.render("Eraser Tool", True, (0, 0, 0))
        screen.blit(Title, (645, 645))
        Hunter = hunterFont.render("Erases mistakes with white", True, (0, 0, 0))
        screen.blit(Hunter, (645, 680))
        Hunter2 = hunterFont.render("and changes size.", True, (0, 0, 0))
        screen.blit(Hunter2, (645, 705))

    elif lineButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        tool = "line"
        clearselect()
        draw.rect(screen, (255, 0, 0), lineButt, 3)

        draw.rect(screen, (255, 255, 255), fontRect)
        draw.rect(screen, (0, 0, 0), fontRect, 3)
        draw.rect(screen, (0, 255, 0), fontRect, 1)
        Title = titleFont.render("Line Tool", True, (0, 0, 0))
        screen.blit(Title, (645, 645))
        Hunter = hunterFont.render("Drag to draw lines that can", True, (0, 0, 0))
        screen.blit(Hunter, (645, 680))
        Hunter2 = hunterFont.render("changes thickness and color.", True, (0, 0, 0))
        screen.blit(Hunter2, (645, 705))

    elif spraypaintButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        tool = "spraypaint"
        clearselect()
        draw.rect(screen, (255, 0, 0), spraypaintButt, 3)

        draw.rect(screen, (255, 255, 255), fontRect)
        draw.rect(screen, (0, 0, 0), fontRect, 3)
        draw.rect(screen, (0, 255, 0), fontRect, 1)
        Title = titleFont.render("Spraypaint Tool", True, (0, 0, 0))
        screen.blit(Title, (645, 645))
        Hunter = hunterFont.render("Fills in random pixels within", True, (0, 0, 0))
        screen.blit(Hunter, (645, 680))
        Hunter2 = hunterFont.render("range and changes color.", True, (0, 0, 0))
        screen.blit(Hunter2, (645, 705))

    elif theRectButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        tool = "theRect"
        clearselect()
        draw.rect(screen, (255, 0, 0), theRectButt, 3)

        draw.rect(screen, (255, 255, 255), fontRect)
        draw.rect(screen, (0, 0, 0), fontRect, 3)
        draw.rect(screen, (0, 255, 0), fontRect, 1)
        Title = titleFont.render("Rectangle Tool", True, (0, 0, 0))
        screen.blit(Title, (645, 645))
        Hunter = hunterFont.render("Drag to draw rectangles that", True, (0, 0, 0))
        screen.blit(Hunter, (645, 680))
        Hunter2 = hunterFont.render("changes thickness and color.", True, (0, 0, 0))
        screen.blit(Hunter2, (645, 705))

    elif theEllipseButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        tool = "theEllipse"
        clearselect()
        draw.rect(screen, (255, 0, 0), theEllipseButt, 3)

        draw.rect(screen, (255, 255, 255), fontRect)
        draw.rect(screen, (0, 0, 0), fontRect, 3)
        draw.rect(screen, (0, 255, 0), fontRect, 1)
        Title = titleFont.render("Elipse Tool", True, (0, 0, 0))
        screen.blit(Title, (645, 645))
        Hunter = hunterFont.render("Drag to draw an ellipse that", True, (0, 0, 0))
        screen.blit(Hunter, (645, 680))
        Hunter2 = hunterFont.render("changes thickness and color.", True, (0, 0, 0))
        screen.blit(Hunter2, (645, 705))

    elif polygonButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        tool = "polygon"
        clearselect()
        draw.rect(screen, (255, 0, 0), polygonButt, 3)

        draw.rect(screen, (255, 255, 255), fontRect)
        draw.rect(screen, (0, 0, 0), fontRect, 3)
        draw.rect(screen, (0, 255, 0), fontRect, 1)
        Title = titleFont.render("Polygon Tool", True, (0, 0, 0))
        screen.blit(Title, (645, 645))
        Hunter = hunterFont.render("Left clich to set corners and", True, (0, 0, 0))
        screen.blit(Hunter, (645, 680))
        Hunter2 = hunterFont.render("right click to close polygon.", True, (0, 0, 0))
        screen.blit(Hunter2, (645, 705))

    elif fillButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        tool = "fill"
        clearselect()
        draw.rect(screen, (255, 0, 0), fillButt, 3)

        draw.rect(screen, (255, 255, 255), fontRect)
        draw.rect(screen, (0, 0, 0), fontRect, 3)
        draw.rect(screen, (0, 255, 0), fontRect, 1)
        Title = titleFont.render("Fill Tool", True, (0, 0, 0))
        screen.blit(Title, (645, 645))
        Hunter = hunterFont.render("Fills the area with the same", True, (0, 0, 0))
        screen.blit(Hunter, (645, 680))
        Hunter2 = hunterFont.render("color with another color.", True, (0, 0, 0))
        screen.blit(Hunter2, (645, 705))

    elif nenButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        tool = "nen"
        clearselect()
        draw.rect(screen, (255, 0, 0), nenButt, 3)

        draw.rect(screen, (255, 255, 255), fontRect)
        draw.rect(screen, (0, 0, 0), fontRect, 3)
        draw.rect(screen, (0, 255, 0), fontRect, 1)
        Title = titleFont.render("Nen Tool", True, (0, 0, 0))
        screen.blit(Title, (645, 645))
        Hunter = hunterFont.render("Draws like a paintbrush that", True, (0, 0, 0))
        screen.blit(Hunter, (645, 680))
        Hunter2 = hunterFont.render("has transparency.", True, (0, 0, 0))
        screen.blit(Hunter2, (645, 705))

    elif pickerButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        tool = "picker"
        clearselect()
        draw.rect(screen, (255, 0, 0), pickerButt, 3)

        draw.rect(screen, (255, 255, 255), fontRect)
        draw.rect(screen, (0, 0, 0), fontRect, 3)
        draw.rect(screen, (0, 255, 0), fontRect, 1)
        Title = titleFont.render("Color Picker Tool", True, (0, 0, 0))
        screen.blit(Title, (645, 645))
        Hunter = hunterFont.render("Finds the color of the pixel", True, (0, 0, 0))
        screen.blit(Hunter, (645, 680))
        Hunter2 = hunterFont.render("that you pick in the canvas.", True, (0, 0, 0))
        screen.blit(Hunter2, (645, 705))

    elif lightningButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        tool = "lightning"
        clearselect()
        draw.rect(screen, (255, 0, 0), lightningButt, 3)

        draw.rect(screen, (255, 255, 255), fontRect)
        draw.rect(screen, (0, 0, 0), fontRect, 3)
        draw.rect(screen, (0, 255, 0), fontRect, 1)
        Title = titleFont.render("Lightning Tool", True, (0, 0, 0))
        screen.blit(Title, (645, 645))
        Hunter = hunterFont.render("Randomly draws lighning of", True, (0, 0, 0))
        screen.blit(Hunter, (645, 680))
        Hunter2 = hunterFont.render("reandom colors.", True, (0, 0, 0))
        screen.blit(Hunter2, (645, 705))

    #selecting stickers~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    elif gangButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        tool = "gang"
        clearselect()
        draw.rect(screen, (255, 0, 0), gangButt, 3)
        stickd("Group")

    elif gonButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        tool = "gon"
        clearselect()
        draw.rect(screen, (255, 0, 0), gonButt, 3)
        stickd("Gon")

    elif killuaButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        tool = "killua"
        clearselect()
        draw.rect(screen, (255, 0, 0), killuaButt, 3)
        stickd("Killua")

    elif hunterButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        tool = "hunter"
        clearselect()
        draw.rect(screen, (255, 0, 0), hunterButt, 3)
        stickd("Hunter")

    elif leorioButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        tool = "leorio"
        clearselect()
        draw.rect(screen, (255, 0, 0), leorioButt, 3)
        stickd("Leorio")

    elif kurapikaButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        tool = "kurapika"
        clearselect()
        draw.rect(screen, (255, 0, 0), kurapikaButt, 3)
        stickd("Kurapika")

    elif hisokaButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        tool = "hisoka"
        clearselect()
        draw.rect(screen, (255, 0, 0), hisokaButt, 3)
        stickd("Hisoka")

    #selecting backrounds~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    draw.rect(screen, color, backroundButt)

    if backroundButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        clearselectBack()
        draw.rect(screen, (255, 0, 0), backroundButt, 3)
        draw.rect(screen, color, canvasRect, 0)
        dback = True
        cback = True

    elif beginningButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        clearselectBack()
        draw.rect(screen, (255, 0, 0), beginningButt, 3)
        backround(beginningBack)
        dback = False
        cback = True

    elif beyondButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        clearselectBack()
        draw.rect(screen, (255, 0, 0), beyondButt, 3)
        backround(beyondBack)
        dback = False
        cback = True

    elif endButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        clearselectBack()
        draw.rect(screen, (255, 0, 0), endButt, 3)
        backround(endBack)
        dback = False
        cback = True

    elif greedislandButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        clearselectBack()
        draw.rect(screen, (255, 0, 0), greedislandButt, 3)
        backround(greedislandBack)
        dback = False
        cback = True

    elif moonButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        clearselectBack()
        draw.rect(screen, (255, 0, 0), moonButt, 3)
        backround(moonBack)
        dback = False
        cback = True

    elif nglButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        clearselectBack()
        draw.rect(screen, (255, 0, 0), nglButt, 3)
        backround(nglBack)
        dback = False
        cback = True

    elif worldtreeButt.collidepoint(mx, my) and e.type == MOUSEBUTTONUP:
        clearselectBack()
        draw.rect(screen, (255, 0, 0), worldtreeButt, 3)
        backround(worldtreeBack)
        dback = False
        cback = True

    if dback:
        draw.rect(screen, (255, 0, 0), backroundButt, 3)
    else:
        draw.rect(screen, (0, 0, 0), backroundButt, 3)

    #using tools~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if tool == "pencil" and mb[0] == 1 and canvasRect.collidepoint(mx, my):
        screen.set_clip(canvasRect)
        pencil(omx, omy, mx, my)
        screen.set_clip(None)

    elif tool == "brush" and mb[0] == 1 and canvasRect.collidepoint(mx, my):
        screen.set_clip(canvasRect)
        brush(omx, omy, mx, my)
        screen.set_clip(None)

    elif tool == "eraser" and mb[0] == 1 and canvasRect.collidepoint(mx, my):
        screen.set_clip(canvasRect)
        eraser(omx, omy, mx, my)
        screen.set_clip(None)

    elif tool == "line" and mb[0] == 1 and canvasRect.collidepoint(mx, my):
        line(oomx, oomy, mx, my, screenOld)

    elif tool == "spraypaint" and mb[0] == 1 and canvasRect.collidepoint(mx, my):
        screen.set_clip(canvasRect)
        spraypaint(mx, my)
        screen.set_clip(None)

    elif tool == "theRect" and mb[0] == 1 and canvasRect.collidepoint(mx, my):
        theRect(oomx, oomy, mx, my, screenOld)
        clearselect()
        draw.rect(screen, (255, 0, 0), theRectButt, 3)

    elif tool == "theEllipse" and mb[0] == 1 and canvasRect.collidepoint(mx, my):
        theEllipse(oomx, oomy, mx, my, screenOld)
        clearselect()
        draw.rect(screen, (255, 0, 0), theEllipseButt, 3)

    elif tool == "polygon" and (mb[0] == 1 or mb[2] == 1) and canvasRect.collidepoint(mx, my):
        screen.set_clip(canvasRect)
        polygon(mx, my, mb)
        screen.set_clip(None)

    elif tool == "fill" and mb[0] == 1 and canvasRect.collidepoint(mx, my):
        screen.set_clip(canvasRect)
        fill(mx, my)
        screen.set_clip(None)

    elif tool == "nen" and mb[0] == 1 and canvasRect.collidepoint(mx, my):
        screen.set_clip(canvasRect)
        nen(mx, my, omx, omy, screenOld)
        screen.set_clip(None)

    elif tool == "picker" and mb[0] == 1 and canvasRect.collidepoint(mx, my):
        screen.set_clip(canvasRect)
        color = picker(mx, my)
        screen.set_clip(None)

    elif tool == "lightning" and mb[0] == 1 and canvasRect.collidepoint(mx, my):
        screen.set_clip(canvasRect)
        col = (randint(0, 255), randint(0, 255), randint(0, 255))
        lightning(screen, col, mx, my, 4)
        screen.set_clip(None)

    #using stickers~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif tool == "gang" and mb[0] == 1 and canvasRect.collidepoint(mx, my):
        sticker(mx, my, stickers[0], screenOld)
        clearselect()
        draw.rect(screen, (255, 0, 0), gangButt, 3)

    elif tool == "gon" and mb[0] == 1 and canvasRect.collidepoint(mx, my):
        sticker(mx, my, stickers[1], screenOld)
        clearselect()
        draw.rect(screen, (255, 0, 0), gonButt, 3)

    elif tool == "killua" and mb[0] == 1 and canvasRect.collidepoint(mx, my):
        sticker(mx, my, stickers[2], screenOld)
        clearselect()
        draw.rect(screen, (255, 0, 0), killuaButt, 3)

    elif tool == "hunter" and mb[0] == 1 and canvasRect.collidepoint(mx, my):
        sticker(mx, my, stickers[3], screenOld)
        clearselect()
        draw.rect(screen, (255, 0, 0), hunterButt, 3)

    elif tool == "leorio" and mb[0] == 1 and canvasRect.collidepoint(mx, my):
        sticker(mx, my, stickers[4], screenOld)
        clearselect()
        draw.rect(screen, (255, 0, 0), leorioButt, 3)

    elif tool == "kurapika" and mb[0] == 1 and canvasRect.collidepoint(mx, my):
        sticker(mx, my, stickers[5], screenOld)
        clearselect()
        draw.rect(screen, (255, 0, 0), kurapikaButt, 3)

    elif tool == "hisoka" and mb[0] == 1 and canvasRect.collidepoint(mx, my):
        sticker(mx, my, stickers[6], screenOld)
        clearselect()
        draw.rect(screen, (255, 0, 0), hisokaButt, 3)

    omx, omy = mx, my

    draw.rect(screen, (0, 0, 0), canvasRect, 3)
    draw.rect(screen, (255, 0, 0), canvasRect, 1)
    display.flip()
quit()