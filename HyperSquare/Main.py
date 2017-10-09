import os
import pico2d as p2
import game_framework
import EasyGame
import MidGame
import HardGame

os.chdir('C:\\Users\\qnpfr\\Documents\\Python\\HyperSquare\\HyperSquare\\Pictures')

p2.open_canvas()

class MainE:
    def Init(self):
        self.BackGroundE=p2.load_image('BackGroundE.png')
        self.GoButtonE=p2.load_image('GoButtonE.png')
        self.WallE=p2.load_image('WallE.png')
        self.LeftButtonE=p2.load_image('LeftButtonE.png')
        self.RightButtonE=p2.load_image('RightButtonE.png')
        self.GameLogoE=p2.load_image('GameLogoE.png')
        self.PressSpaceE=p2.load_image('PressSpaceE.png')

    def draw(self):
        self.BackGroundE.draw(400,300)
        self.WallE.draw(400,10)
        self.WallE.draw(400,590)
        self.GameLogoE.draw(400,500)
        self.GoButtonE.draw(400,300)
        self.LeftButtonE.draw(50,300)
        self.RightButtonE.draw(750,300)
        self.PressSpaceE.draw(400,100)
        
class MainM:
    def Init(self):
        self.BackGroundM=p2.load_image('BackGroundM.png')
        self.GoButtonM=p2.load_image('GoButtonM.png')
        self.WallM=p2.load_image('WallM.png')
        self.LeftButtonM=p2.load_image('LeftButtonM.png')
        self.RightButtonM=p2.load_image('RightButtonM.png')
        self.GameLogoM=p2.load_image('GameLogoM.png')
        self.PressSpaceM=p2.load_image('PressSpaceM.png')

    def draw(self):
        self.BackGroundM.draw(400,300)
        self.WallM.draw(400,10)
        self.WallM.draw(400,590)
        self.GameLogoM.draw(400,500)
        self.GoButtonM.draw(400,300)
        self.LeftButtonM.draw(50,300)
        self.RightButtonM.draw(750,300)
        self.PressSpaceM.draw(400,100)

class MainH:
    def Init(self):
        self.BackGroundH=p2.load_image('BackGroundH.png')
        self.GoButtonH=p2.load_image('GoButtonH.png')
        self.WallH=p2.load_image('WallH.png')
        self.LeftButtonH=p2.load_image('LeftButtonH.png')
        self.RightButtonH=p2.load_image('RightButtonH.png')
        self.GameLogoH=p2.load_image('GameLogoH.png')
        self.PressSpaceH=p2.load_image('PressSpaceH.png')

    def draw(self):
        self.BackGroundH.draw(400,300)
        self.WallH.draw(400,10)
        self.WallH.draw(400,590)
        self.GameLogoH.draw(400,500)
        self.GoButtonH.draw(400,300)
        self.LeftButtonH.draw(50,300)
        self.RightButtonH.draw(750,300)
        self.PressSpaceH.draw(400,100)

def exit():
    scene=-1
        

def handle_events():
    global scene
    events=p2.get_events()
    for event in events:
        if event.type==p2.SDL_KEYDOWN:
            if event.key==p2.SDLK_ESCAPE:
                scene=-1
            if event.key==p2.SDLK_LEFT:
                if scene>0:
                    scene-=1
            if event.key==p2.SDLK_RIGHT:
                if scene<2:
                    scene+=1
            if event.key==p2.SDLK_SPACE:
                if scene==0:
                    game_framework.change_state(EasyGame)
                if scene==1:
                    game_framework.change_state(MidGame)
                if scene==2:
                    game_framework.change_state(HardGame)
                    

scene=0

def main():
    mainE=MainE()
    mainM=MainM()
    mainH=MainH()
    mainE.Init()
    mainM.Init()
    mainH.Init()

    while(scene>=0):       
        while(scene==0):
            p2.clear_canvas()

            mainE.draw()
            p2.update_canvas()
            p2.delay(0.1)
    
            handle_events()

        while(scene==1):
            p2.clear_canvas()

            mainM.draw()
            p2.update_canvas()
            p2.delay(0.1)
    
            handle_events()
            
        while(scene==2):
            p2.clear_canvas()

            mainH.draw()
            p2.update_canvas()
            p2.delay(0.1)
    
            handle_events()

    p2.close_canvas()
