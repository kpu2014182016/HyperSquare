import pico2d_addtion as p2
import math
import random
import EasyGame
import HardGame
import MidGame
import game_framework


class MainE:
    CLOCKWISE,COUNTERCLOCKWISE=1,-1
    
    def __Init__(self):
        self.GoButtonE=p2.load_image('Pictures\\GoButtonE.png')
        self.ButtonE=p2.load_image('Pictures\\ButtonE.png')
        self.GameLogoE=p2.load_image('Pictures\\GameLogoE.png')
        self.PressSpace=p2.load_image('Pictures\\PressSpace.png')
        self.rad=0
        self.angle=0
        self.dir=1
        self.maxangle=7
        self.anglegrowth=0.5
        self.WallR=18
        self.WallG=105
        self.WallB=120
        self.WallDir=1
        self.BackGroundR=72
        self.BackGroundG=202
        self.BackGroundB=225
        self.BackGroundDir=1

    def draw(self):
        p2.draw_rendercolor(self.BackGroundR,self.BackGroundG,self.BackGroundB,255)
        p2.draw_fillrectangle(0,0,800,600)
        p2.draw_rendercolor(self.WallR,self.WallG,self.WallB,255)
        p2.draw_fillrectangle(0,0,800,200)
        p2.draw_fillrectangle(0,400,800,600)
        self.GameLogoE.draw(400,500)
        self.ButtonE.rotate_draw(180*3.14/180,750,300,46,51)
        self.PressSpace.draw(400,100)
        self.GoButtonE.rotate_draw(self.rad,400,300,208,106)

    def update(self):
        if self.angle>self.maxangle:
            self.dir=self.COUNTERCLOCKWISE
        elif self.angle<-self.maxangle:
            self.dir=self.CLOCKWISE
        if self.dir==self.CLOCKWISE:
            self.rad=(self.angle*3.14)/180
            self.angle+=self.anglegrowth
        elif self.dir==self.COUNTERCLOCKWISE:
            self.rad=(self.angle*3.14)/180
            self.angle-=self.anglegrowth
        if (self.BackGroundDir==1):
            self.BackGroundR-=1
            self.BackGroundG-=1
            self.BackGroundB-=1
            if(self.BackGroundR<=0):
                self.BackGroundDir=-1
        elif (self.BackGroundDir==-1):
            self.BackGroundR+=1
            self.BackGroundG+=1
            self.BackGroundB+=1
            if(self.BackGroundR>=100):
                self.BackGroundDir=1
        if (self.WallDir==1):
            self.WallR-=1
            self.WallG-=1
            self.WallB-=1
            if(self.WallR<=0):
                self.WallDir=-1
        elif (self.WallDir==-1):
            self.WallR+=1
            self.WallG+=1
            self.WallB+=1
            if(self.WallR>=150):
                self.WallDir=1
            
        
class MainM:
    CLOCKWISE,COUNTERCLOCKWISE=1,-1

    def __Init__(self):
        self.GoButtonM=p2.load_image('Pictures\\GoButtonM.png')
        self.ButtonM=p2.load_image('Pictures\\ButtonM.png')
        self.GameLogoM=p2.load_image('Pictures\\GameLogoM.png')
        self.PressSpace=p2.load_image('Pictures\\PressSpace.png')
        self.rad=0
        self.angle=0
        self.dir=1
        self.maxangle=7
        self.anglegrowth=0.5
        self.WallR=204
        self.WallG=61
        self.WallB=61
        self.WallDir=1
        self.BackGroundR=255
        self.BackGroundG=151
        self.BackGroundB=151
        self.BackGroundDir=1

    def draw(self):
        self.GameLogoM.draw(400,500)
        self.ButtonM.draw(50,300)
        self.ButtonM.rotate_draw(180*3.14/180,750,300,46,51)
        self.PressSpace.draw(400,100)
        self.GoButtonM.rotate_draw(self.rad,400,300,208,106)

    def update(self):
        if self.angle>self.maxangle:
            self.dir=self.COUNTERCLOCKWISE
        elif self.angle<-self.maxangle:
            self.dir=self.CLOCKWISE
        if self.dir==self.CLOCKWISE:
            self.rad=(self.angle*3.14)/180
            self.angle+=self.anglegrowth
        elif self.dir==self.COUNTERCLOCKWISE:
            self.rad=(self.angle*3.14)/180
            self.angle-=self.anglegrowth
        if(self.BackGroundDir==1):
            self.BackGroundR-=1
            self.BackGroundG-=1
            self.BackGroundB-=1
            if(self.BackGroundG<=0):
                self.BackGroundDir=-1
        elif(self.BackGroundDir==-1):
            self.BackGroundR+=1
            self.BackGroundG+=1
            self.BackGroundB+=1
            if(self.BackGroundG>=100):
                self.BackGroundDir=1
        if(self.WallDir==1):
            self.WallR-=1
            self.WallG-=1
            self.WallB-=1
            if(self.WallB<=0):
                self.WallDir=-1
        elif(self.WallDir==-1):
            self.WallR+=1
            self.WallG+=1
            self.WallB+=1
            if(self.WallB>=100):
                self.WallDir=1

class MainH:
    CLOCKWISE,COUNTERCLOCKWISE=1,-1

    def __Init__(self):
        self.GoButtonH=p2.load_image('Pictures\\GoButtonH.png')
        self.ButtonH=p2.load_image('Pictures\\ButtonH.png')
        self.GameLogoH=p2.load_image('Pictures\\GameLogoH.png')
        self.PressSpace=p2.load_image('Pictures\\PressSpace.png')
        self.rad=0
        self.angle=0
        self.dir=1
        self.maxangle=7
        self.anglegrowth=0.5
        self.WallR=0
        self.WallG=0
        self.WallB=0
        self.WallDir=-1
        self.BackGroundR=255
        self.BackGroundG=255
        self.BackGroundB=255
        self.BackGroundDir=1
        self.Wallx1=-200
        self.Wally1=-200
        self.Wallx2=1000
        self.Wally2=200
        self.Wallx3=-200
        self.Wally3=400
        self.Wallx4=1000
        self.Wally4=600
        
    def draw(self):
        p2.draw_rendercolor(self.BackGroundR,self.BackGroundG,self.BackGroundB,255)
        p2.draw_fillrectangle(0,0,800,600)
        p2.draw_rendercolor(self.WallR,self.WallG,self.WallB,255)
        p2.draw_fillrectangle(self.Wallx1,self.Wally1,self.Wallx2,self.Wally2)
        p2.draw_fillrectangle(self.Wallx3,self.Wally3,self.Wallx4,self.Wally4)
        self.GameLogoH.draw(400,500)
        self.ButtonH.draw(50,300)
        self.PressSpace.draw(400,100)
        self.GoButtonH.rotate_draw(self.rad,400,300,208,106)

    def update(self):
        if self.angle>self.maxangle:
            self.dir=self.COUNTERCLOCKWISE
        elif self.angle<-self.maxangle:
            self.dir=self.CLOCKWISE
        if self.dir==self.CLOCKWISE:
            self.rad=(self.angle*3.14)/180
            self.angle+=self.anglegrowth
        elif self.dir==self.COUNTERCLOCKWISE:
            self.rad=(self.angle*3.14)/180
            self.angle-=self.anglegrowth
        if(self.BackGroundDir==1):
            self.BackGroundR-=2
            self.BackGroundG-=2
            self.BackGroundB-=2
            if(self.BackGroundR<=5):
                self.BackGroundDir=-1
        elif(self.BackGroundDir==-1):
            self.BackGroundR+=2
            self.BackGroundG+=2
            self.BackGroundB+=2
            if(self.BackGroundR>=250):
                self.BackGroundDir=1
        if(self.WallDir==1):
            self.WallR-=1
            self.WallG-=1
            self.WallB-=1
            if(self.WallR<=0):
                self.WallDir=-1
        elif(self.WallDir==-1):
            self.WallR+=1
            self.WallG+=1
            self.WallB+=1
            if(self.WallR>=150):
                self.WallDir=1

class CheckPattern:
    def __init__(self,X,Y,Width,Height,R,G,B):
        self.x=X
        self.y=Y
        self.width=Width
        self.height=Height
        self.colorRm=R
        self.colorRM=R+20
        self.colorGm=G
        self.colorGM=G+20
        self.colorBm=B
        self.colorBM=B+20
        self.colorDir=1
        self.colorR=random.randint(204,255)
        self.colorG=random.randint(100,155)
        self.colorB=random.randint(100,155)

    def draw(self):
        p2.draw_rendercolor(self.colorR,self.colorG,self.colorB,255)
        p2.draw_fillrectangle(self.x-self.width,self.y-self.height,self.x,self.y)

    def update(self):
        self.colorR=random.randint(self.colorRm,self.colorRM)
        self.colorG=random.randint(self.colorGm,self.colorGM)
        self.colorB=random.randint(self.colorBm,self.colorBM)
        if self.colorDir==1:
            if self.colorRM>=150:
                self.colorRm-=1
                self.colorRM-=1
                self.colorGm-=1
                self.colorGM-=1
                self.colorBm-=1
                self.colorBM-=1
            else:
                self.colorDir=-1
        elif self.colorDir==-1:
            if self.colorRM<=250:
                self.colorRm+=1
                self.colorRM+=1
                self.colorGm+=1
                self.colorGM+=1
                self.colorBm+=1
                self.colorBM+=1
            else:
                self.colorDir=1

def handle_events():
    global scene
    events=p2.get_events()
    for event in events:
        if event.type==p2.SDL_KEYDOWN:
            if event.key==p2.SDLK_ESCAPE:
                game_framework.quit()
            if event.key==p2.SDLK_LEFT:
                if scene>0:
                    scene-=1
                    ChangeSound.play()
            if event.key==p2.SDLK_RIGHT:
                if scene<2:
                    scene+=1
                    ChangeSound.play()
            if event.key==p2.SDLK_SPACE:
                if scene==0:
                    scene=-1
                    game_framework.push_state(EasyGame)
                if scene==1:
                    scene=-1
                    game_framework.push_state(MidGame)
                if scene==2:
                    scene=-1
                    game_framework.push_state(HardGame)

def Rotate(x,y,CenterX,CenterY,Angle):
    global X,Y
    X=x-CenterX
    Y=y-CenterY
    x=X*math.cos(math.pi*Angle/180)-Y*math.sin(math.pi*Angle/180)
    y=X*math.sin(math.pi*Angle/180)+Y*math.cos(math.pi*Angle/180)
    x=x+CenterX
    y=y+CenterY
    return x,y

def exit():
    scene=-1

def pause():
    pause=0

def resume():
    resume=0

def update():
    if(scene==0):
        mainE.update()
    elif(scene==1):
        mainM.update()
        for i in range(10):
            for j in range(10):
                checkpatternArray3[i][j].update()
        for i in range(10):
            for j in range(10):
                checkpatternArray[i][j].update()
        for i in range(10):
            for j in range(10):
                checkpatternArray2[i][j].update()
    elif(scene==2):
        mainH.update()

        mainH.Wallx1,mainH.Wally1=Rotate(mainH.Wallx1,mainH.Wally1,400,300,5)
        mainH.Wallx2,mainH.Wally2=Rotate(mainH.Wallx2,mainH.Wally2,400,300,1)
        mainH.Wallx3,mainH.Wally3=Rotate(mainH.Wallx3,mainH.Wally3,400,300,-3)
        mainH.Wallx4,mainH.Wally4=Rotate(mainH.Wallx4,mainH.Wally4,400,300,-4)

def enter():
    global mainE,mainM,mainH,checkpatternArray,scene,checkpatternArray2,checkpatternArray3,ChangeSound
    

    scene=0
    
    mainE=MainE()
    mainM=MainM()
    mainH=MainH()
    mainE.__Init__()
    mainM.__Init__()
    mainH.__Init__()
    ChangeSound = p2.Music('Musics\\ChangeSound.mp3')
    ChangeSound.set_volume(64)
    ChangeSound.play()

    checkpatternArray = [[CheckPattern((col+1)*80,(row+1)*80-600,80,80,200,100,100) for col in range(10)] for row in range(10)]
    checkpatternArray2 = [[CheckPattern((col+1)*80,(row+1)*80+400,80,80,200,100,100) for col in range(10)] for row in range(10)]
    checkpatternArray3 = [[CheckPattern((col+1)*80,(row+1)*80-200,80,80,150,50,50) for col in range(10)] for row in range(10)]


    p2.hide_cursor()

def draw():
    global mainE,mainM,mainH,checkpatternArray,scene,checkpatternArray2,checkpatternArray3

    p2.clear_canvas()

    if(scene==0):
        mainE.draw()
    elif(scene==1):
        for i in range(10):
            for j in range(10):
                checkpatternArray3[i][j].draw()
        for i in range(10):
            for j in range(10):
                checkpatternArray[i][j].draw()
        for i in range(10):
            for j in range(10):
                checkpatternArray2[i][j].draw()

        mainM.draw()    
    elif(scene==2):
        mainH.draw()

    p2.update_canvas()
    p2.delay(0.05)

    
