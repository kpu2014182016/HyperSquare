import pico2d_addtion as p2
import random
import time
import json
import title
import game_framework


class Player:
    global topsideY, bottomY

    bottom, top = 1, -1
    PlayerE = None

    def _Init_(self):
        if self.PlayerE == None:
            self.PlayerE = p2.load_image('Pictures\\PlayerH.png')
        self.x = -50
        self.y = bottomY
        self.currentY = self.y
        self.position = self.bottom
        self.B = bottomY
        self.T = topsideY
        self.rotate = False
        self.angle = 0
        self.divide=8
        self.anglegrowth = 180 / self.divide
    def draw(self):
        if self.rotate == False:
            self.PlayerE.clip_draw(0, 0, 50, 50, self.x, self.y, 50 * Scale, 50 * Scale)
        elif self.rotate == True:
            self.PlayerE.rotate_draw(-(self.angle * 3.14) / 180, self.x, self.y, 50 * Scale, 50 * Scale)

    def update(self):
        self.Rotate()
        self.FallDie()

    def Rotate(self):
        if self.rotate == True:
            if self.position == self.bottom:
                self.y += (self.T - self.currentY) / self.divide
                self.angle += self.anglegrowth
                if self.angle >= 180:
                    self.position = player.top
                    self.angle = 0
                    self.rotate = False
            elif self.position == self.top:
                self.y -= (self.currentY - self.B) / self.divide
                self.angle += self.anglegrowth
                if self.angle >= 180:
                    self.position = player.bottom
                    self.angle = 0
                    self.rotate = False

    def handle_evnet(self,event):
        if (event.type,event.key==p2.SDL_KEYDOWN,p2.SDLK_SPACE):
            if self.rotate==False:
                self.rotate=True
                self.currentY=self.y
                self.B = bottomY
                self.T = topsideY

    def FallDie(self):
        if self.y < 0:
            Death()
        if self.y > 600:
            Death()

    def get_bb(self):
        return self.x - Scale * 25, self.y - Scale * 25, self.x + Scale * 25, self.y + Scale * 25


class StopIngredient:
    ToStart = None
    ToMenu = None
    highscore = None
    currentscore = None
    pauseimage = None

    def __init__(self):
        if self.ToStart == None:
            self.ToStart = p2.load_image('Pictures\\ToStartH.png')
        if self.ToMenu == None:
            self.ToMenu = p2.load_image('Pictures\\ToMenuH.png')
        if self.highscore == None:
            self.highscore = p2.load_image('Pictures\\highscoreH.png')
        if self.currentscore == None:
            self.currentscore = p2.load_image('Pictures\\currentscoreH.png')
        if self.pauseimage == None:
            self.pauseimage = p2.load_image('Pictures\\pauseH.png')

    def draw(self):
        self.ToStart.draw(180, 120)
        self.ToMenu.draw(650, 120)
        self.highscore.draw(80, 550)
        self.currentscore.draw(40, 500)

    def stopdraw(self):
        self.pauseimage.draw(400,300)


class Wall:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y

    def get_bb(self):
        return self.x - 600, self.y - 150, self.x + 600, self.y + 150


#obstacle
class Rect:
    global topsideY, bottomY, speed, scene

    time_per_speed = 100
    bottom,top=0,1

    def __init__(self, Posi,X, Y, Width, Height,Center=300,Move=0):
        self.x = X
        self.width = Width
        self.height = Height
        self.once = 0
        self.movement=Move
        self.Position = Posi
        if self.Position == self.bottom:
            self.positionY = Center-Y
            self.y = -300
        elif self.Position == self.top:
            self.positionY = Center+Y
            self.y = 900

    def draw(self):
        p2.draw_rendercolor(wallR, wallG, wallB, 255)
        p2.draw_fillrectangle(self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height)

    def update(self, frame_time):
        a_left, a_bottom, a_right, a_top = player.get_bb()

        self.x -= speed * frame_time * self.time_per_speed
        self.InArea(a_left, a_bottom, a_right, a_top)
        self.falldown(a_left, a_bottom, a_right, a_top)
        self.collision(a_left, a_bottom, a_right, a_top)
        if self.movement==0:
            self.move(frame_time)
        else:
            self.anothermove(frame_time)

    def move(self,frame_time):
        if self.Position == self.bottom:
            if self.positionY>self.y:
                self.y+=15*frame_time*self.time_per_speed
            if self.positionY<=self.y:
                self.y = self.positionY
        elif self.Position == self.top:
            if self.positionY<self.y:
                self.y-=15*frame_time*self.time_per_speed
            if self.positionY>=self.y:
                self.y = self.positionY

    def anothermove(self,frame_time):
        if self.x<800:
            if self.x > 100:
                if self.Position == self.bottom:
                    if self.positionY>self.y:
                        self.y+=15*frame_time*self.time_per_speed
                    if self.positionY<=self.y:
                        self.y = self.positionY
                elif self.Position == self.top:
                    if self.positionY<self.y:
                        self.y-=15*frame_time*self.time_per_speed
                    if self.positionY>=self.y:
                        self.y = self.positionY
            elif self.x<=100:
                if self.Position == self.bottom:
                    if self.y>-300:
                        self.y-=15*frame_time*self.time_per_speed
                elif self.Position == self.top:
                    if self.y<900:
                        self.y+=15*frame_time*self.time_per_speed

    def delete(self):
        if self.x + self.width < 0:
            return True

    def call_pattern(self):
        if self.once == 0:
            if self.x < 400:
                self.once = 1
                return True

    def InArea(self, a_left, a_bottom, a_right, a_top):
        if a_right + speed * 8 >= self.x - self.width:
            if a_left + speed * 8< self.x + self.width:
                if self.y < player.y:
                    ChangeBottomAndTop(self.y + self.height + Scale * 25, topsideY)
                if self.y > player.y:
                    ChangeBottomAndTop(bottomY, self.y - self.height - Scale * 25)

    def falldown(self, a_left, a_bottom, a_right, a_top):
        if a_left >= self.x + self.width:
            if a_left <= self.x + self.width + speed +30:
                if (player.position, player.rotate) == (player.bottom, False):
                    if a_bottom >= self.y + self.height:
                        if a_bottom <= self.y + self.height + 5:
                            if player.y>bottomY:
                                player.rotate = True
                                player.currentY = player.y
                                player.B = bottomY
                                player.position = player.top
                elif (player.position, player.rotate) == (player.top, False):
                    if a_top <= self.y - self.height:
                        if a_top >= self.y - self.height - 5:
                            if player.y<topsideY:
                                player.rotate = True
                                player.currentY = player.y
                                player.T = topsideY
                                player.position = player.bottom

    def collision(self,a_left, a_bottom, a_right, a_top):
        if a_right >= self.x - self.width + 5:
            if a_right <= self.x - self.width + 15:
                if a_bottom <= self.y + self.height - 1:
                    if a_bottom >= self.y - self.height + 1:
                        if scene == 1:
                            Death()
                if a_top <= self.y + self.height - 1:
                    if a_top >= self.y - self.height + 1:
                        if scene == 1:
                            Death()

#obstacle
class Thorn:
    global speed, Scale, thornimage

    time_per_speed = 100
    bottom, top = 0, 1

    def __init__(self, X, Y, Dir):
        self.x = X
        self.y = Y
        self.once = 0
        self.Position=Dir
        if self.Position==self.bottom:
            self.positionY = 300-Y
            self.y=-300
        elif self.Position==self.top:
            self.positionY = 300+Y
            self.y = 900

    def draw(self):
        if self.Position == 0:
            thornimage.clip_draw(0, 0, 20, 20, self.x, self.y + 10 * Scale, 20 * Scale, 20 * Scale)
        else:
            thornimage.rotate_draw(3.14, self.x, self.y + 2 - 10 * Scale, 20 * Scale, 20 * Scale)

    def update(self, frame_time):
        self.x -= speed * frame_time * self.time_per_speed
        self.collision()
        if self.Position == self.bottom:
            if self.positionY>self.y:
                self.y+=15*frame_time*self.time_per_speed
            if self.positionY<=self.y:
                self.y = self.positionY
        elif self.Position == self.top:
            if self.positionY<self.y:
                self.y-=15*frame_time*self.time_per_speed
            if self.positionY>=self.y:
                self.y = self.positionY

    def delete(self):
        if self.x + 10 < 0:
            return True

    def call_pattern(self):
        if self.once == 0:
            if self.x < 400:
                self.once = 1
                return True

    def collision(self):
        if (player.x - self.x) * (player.x - self.x) + (player.y - self.y) * (player.y - self.y) <= 200 + (
            Scale * 25) * (Scale * 25) + (Scale * 25) * (Scale * 25):
            if scene == 1:
                Death()

def handle_events():
    global scene,topsideY,bottomY
    global start, run, flash, scoreboard, revive, pause

    events = p2.get_events()
    for event in events:
        if event.type == p2.SDL_KEYDOWN:
            if event.key == p2.SDLK_ESCAPE:
                if scene == run:
                    scene = pause
                    bgm.pause()
                elif scene == scoreboard:
                    game_framework.change_state(title)
                elif scene == pause:
                    game_framework.change_state(title)
            elif event.key == p2.SDLK_SPACE:
                if (scene <= run):
                    player.handle_evnet(event)
                elif (scene == scoreboard):
                    scene = revive
                elif scene == pause:
                    scene = run
                    bgm.resume()


def set_variable():
    global scene, score, topsideY, bottomY, Scale, speed, current_time,obstacleNum,call_read_pattern,lastposition

    file_name = 'DataText\\SetHardGame.txt'
    setVariable_file = open(file_name, 'r')
    setVariable = json.load(setVariable_file)
    setVariable_file.close()

    scene = setVariable['variable']['scene']
    score = setVariable['variable']['score']
    speed = setVariable['variable']['speed']
    Scale = setVariable['variable']['Scale']
    lastposition=0
    ChangeBottomAndTop(100 + 150 + Scale * 25, 75 + 150 + Scale * 25)
    current_time = time.time()
    player.x = -200
    player.y = bottomY
    player.position = player.bottom
    player.rotate = 0
    player.angle = 0
    bgm.resume()
    obstacle.append(Rect(0, 0, 200, 600, 150));
    obstacleNum+=1
    call_read_pattern += 1

def read_patterns():
    global obstacleNum, call_read_pattern,lastposition

    startX = 750
    patternName = ['pattern1', 'pattern2', 'pattern3', 'pattern4', 'pattern5', 'pattern6', 'pattern7',
                   'pattern8', 'pattern9', 'pattern10', 'pattern11', 'pattern12', 'pattern13', 'pattern14',
                   'pattern15', 'pattern16', 'pattern17', 'pattern18', 'pattern19', 'pattern20']

    patterns_file = open('DataText\\patternsHard.txt', 'r')
    patterns = json.load(patterns_file)
    patterns_file.close()

    patternsRandom = random.randint(0, 9)
    while(lastposition==patterns[patternName[patternsRandom]]['data'][2]):
        patternsRandom = random.randint(0, 9)

    patternlength = patterns[patternName[patternsRandom]]['data'][0]
    call_read_pattern = patternlength

    center = 300
    for i in range(patternlength):
        position = patterns[patternName[patternsRandom]]['data'][2 + i * 6]
        patternShape = patterns[patternName[patternsRandom]]['data'][1 + i * 6]
        patternX = patterns[patternName[patternsRandom]]['data'][3 + i * 6]
        patternY = patterns[patternName[patternsRandom]]['data'][4 + i * 6]
        patternWidth = patterns[patternName[patternsRandom]]['data'][5 + i * 6]
        patternHeight = patterns[patternName[patternsRandom]]['data'][6 + i * 6]
        if position == -1:
            position = random.randint(0, 1)
        if patternY == -1:
            patternY = random.randint(150, 250)
        if patternShape == 1:
            if position == 0:
                obstacle.append(Rect(position,startX + patternX,
                                     patternY,
                                     patternWidth * Scale,
                                     patternHeight * Scale,
                                     center))
                obstacleNum += 1
            elif position == 1:
                obstacle.append(Rect(position, startX + patternX,
                                     patternY,
                                     patternWidth * Scale,
                                     patternHeight * Scale,
                                     center))
                obstacleNum += 1
        elif patternShape == 2:
            if position == 0:
                obstacle.append(Rect(position,startX + patternX,
                                     patternY,
                                     patternWidth * Scale,
                                     patternHeight * Scale,
                                     center,
                                     1))
                obstacleNum += 1
            elif position == 1:
                obstacle.append(Rect(position, startX + patternX,
                                     patternY,
                                     patternWidth * Scale,
                                     patternHeight * Scale,
                                     center,
                                     1))
                obstacleNum += 1
        elif patternShape == 3:
            if position == 0:
                obstacle.append(Thorn(startX + patternX,
                                     patternY,
                                     position))
                obstacleNum += 1
            elif position == 1:
                obstacle.append(Thorn(startX + patternX,
                                      patternY,
                                      position))
                obstacleNum += 1

        if i==patternlength-1:
            lastposition=position

def enter():
    global scene, score, highscore, Scale, speed, call_read_pattern, obstacleNum, topsideY, bottomY,alive,lastposition
    global current_time, thornimage, numberimage, file_name, wallR, wallG, wallB, backgroundR, backgroundG, backgroundB
    global player, wall1, wall2, obstacle, stopIngredient, bgm, musicDie, musicRevive
    global start, run, flash, scoreboard, revive, pause

    p2.hide_cursor()

    file_name = 'DataText\\SetHardGame.txt'
    setVariable_file = open(file_name, 'r')
    setVariable = json.load(setVariable_file)
    setVariable_file.close()

    start, run, flash, scoreboard, revive, pause = 0, 1, 2, 3, 4, 5
    alive = 0
    lastposition=0
    speed = setVariable['variable']['speed']
    scene = setVariable['variable']['scene']
    score = setVariable['variable']['score']
    highscore = setVariable['variable']['highscore']
    Scale = setVariable['variable']['Scale']
    obstacleNum = setVariable['variable']['obstacleNum']
    call_read_pattern = setVariable['variable']['call_read_pattern']
    wallR = setVariable['wall']['color']['R']
    wallG = setVariable['wall']['color']['G']
    wallB = setVariable['wall']['color']['B']
    backgroundR = setVariable['background']['color']['R']
    backgroundG = setVariable['background']['color']['G']
    backgroundB = setVariable['background']['color']['B']
    numberimage = p2.load_image('Pictures\\numbersH.png')
    thornimage = p2.load_image('Pictures\\ThornH.png')
    current_time = time.time()
    bgm = p2.Music('Musics\\PurelyGrey-Void[HyperflexOST].mp3')
    bgm.set_volume(64)
    bgm.repeat_play()
    musicDie = p2.Wav('Musics\\MusicDie.wav')
    musicDie.set_volume(64)
    musicRevive = p2.Wav('Musics\\MusicRevive.wav')
    musicRevive.set_volume(64)

    wall1 = Wall(setVariable['wall']['1']['x'], setVariable['wall']['1']['y'])
    wall2 = Wall(setVariable['wall']['2']['x'], setVariable['wall']['2']['y'])
    topsideY, bottomY = wall2.y - 150 - Scale * 25, 100 + 150 + Scale * 25

    stopIngredient = StopIngredient()

    player = Player()
    player._Init_()

    obstacle = []
    obstacle.append(Rect(0,0,200,600,150));
    obstacleNum+=1
    call_read_pattern+=1

def update():
    global scene, score, obstacleNum, speed, current_time, call_read_pattern, highscore, score
    global start, run, flash, scoreboard, revive, pause

    p2.clear_canvas()

    frame_time = time.time() - current_time
    current_time = time.time()
    if (scene == start):
        firstMove()
        gravity()
        for i in range(1):
            obstacle[i].update(frame_time)
            obstacle[i].x+=speed * frame_time * obstacle[i].time_per_speed
        player.update()
    elif (scene == run):
        score += frame_time * 20
        gravity()

        i = obstacleNum - 1
        while (0 <= i):
            obstacle[i].update(frame_time)
            if obstacle[i].call_pattern():
                call_read_pattern -= 1
            if obstacle[i].delete():
                del obstacle[i]
                obstacleNum -= 1
                i -= 1
            i -= 1

        if call_read_pattern <= 0:
            read_patterns()

        player.update()
    elif (scene == revive):
        speed = 20
        i = 0
        while (obstacleNum > i):
            obstacle[i].update(frame_time)
            if obstacle[i].delete():
                del obstacle[i]
                obstacleNum -= 1
                i -= 1
            i += 1

        if len(obstacle) == 0:
            set_variable()


def draw():
    global pobstacleNum, scene, highscore, score, alive, frame_time, current_time
    global start, run, flash, scoreboard, revive, pause

    if (scene == start):
        alive = 0
        draw_wall()
        for i in range(obstacleNum):
            obstacle[i].draw()
        player.draw()
        numberDraw(score, 60, 580, 0.3)
    elif (scene == run):
        draw_wall()
        numberDraw(int(score), 60, 580, 0.3)

        for i in range(obstacleNum):
            obstacle[i].draw()

        player.draw()
    elif (scene == flash):
        highscore_file = open('DataText\\HighScoreHard.txt', 'r')
        highscore = json.load(highscore_file)
        highscore_file.close()

        if highscore < score:
            highscore_file = open('DataText\\HighScoreHard.txt', 'w')
            json.dump(score, highscore_file)
            highscore_file.close()
            highscore = score

        scene = 3
        bgm.pause()
        musicDie.play()

        p2.draw_rendercolor(backgroundR, backgroundG, backgroundB, 255)
        p2.draw_fillrectangle(0, 0, 800, 600)
        p2.update_canvas()
        p2.delay(0.3)
    elif (scene == scoreboard):
        draw_wall()
        for i in range(obstacleNum):
            obstacle[i].draw()

        stopIngredient.draw()
        numberDraw(int(highscore), 110, 550, 0.3)
        numberDraw(int(score), 70, 500, 0.3)
    elif (scene == revive):
        draw_wall()

        if alive == 0:
            musicRevive.play()
            alive = 1

        for i in range(obstacleNum):
            obstacle[i].draw()

    elif (scene == pause):
        draw_wall()
        numberDraw(int(score), 60, 580, 0.3)
        for i in range(obstacleNum):
            obstacle[i].draw()
        player.draw()
        stopIngredient.stopdraw()

    p2.update_canvas()
    p2.delay(0.01)

def Death():
    global scene
    scene = 2


def ChangeBottomAndTop(B, T):
    global topsideY, bottomY
    bottomY = B
    topsideY = T

def gravity():
    ChangeBottomAndTop(wall1.y + 150 + Scale * 25, wall2.y - 150 - Scale * 25)

def numberDraw(num, x, y, scale):
    global numberimage

    dx = 40 * scale
    dy = 64 * scale
    while (True):
        digit = num % 10
        sx = digit * 40
        numberimage.clip_draw(sx, 0, 40, 64, x, y, dx, dy)
        num = int(num / 10)
        if num == 0:
            break
        x -= dx

def draw_wall():
    global wall1, wall2, wallR, wallG, wallB, backgroundR, backgroundG, backgroundB

    p2.draw_rendercolor(backgroundR, backgroundG, backgroundB, 255)
    p2.draw_fillrectangle(0, 0, 800, 600)
    p2.draw_rendercolor(wallR, wallG, wallB, 255)
    p2.draw_fillrectangle(wall1.x - 600, wall1.y - 150, wall1.x + 600, wall1.y + 150)
    p2.draw_fillrectangle(wall2.x - 600, wall2.y - 150, wall2.x + 600, wall2.y + 150)


def firstMove():
    global scene

    if player.x < 200:
        player.x += 5
    elif player.x >= 200:
        scene = 1
        read_patterns()

def exit():
    global player, wall1, wall2, obstacle, stopIngredient, bgm, musicDie,musicRevive
    del (player, wall1, wall2, obstacle, stopIngredient, bgm,musicDie,musicRevive)

def pause():
    pass

def resume():
    pass
