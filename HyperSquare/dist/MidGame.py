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
            self.PlayerE = p2.load_image('Pictures\\PlayerM.png')
        self.x = -50
        self.y = bottomY
        self.currentY = self.y
        self.position = self.bottom
        self.B = bottomY
        self.T = topsideY
        self.rotate = False
        self.angle = 0
        self.divide = 10
        self.anglegrowth = 180 / self.divide

    def draw(self):
        if self.rotate == False:
            self.PlayerE.clip_draw(0, 0, 50, 50, self.x, self.y, 50 * Scale, 50 * Scale)
        elif self.rotate == True:
            self.PlayerE.rotate_draw(-(self.angle * 3.14) / 180, self.x, self.y, 50 * Scale, 50 * Scale)

    def update(self):
        self.Rotate()

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

    def handle_evnet(self, event):
        if (event.type, event.key == p2.SDL_KEYDOWN, p2.SDLK_SPACE):
            if self.rotate == False:
                self.rotate = True
                self.currentY = self.y
                self.B = bottomY
                self.T = topsideY

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
            self.ToStart = p2.load_image('Pictures\\ToStart.png')
        if self.ToMenu == None:
            self.ToMenu = p2.load_image('Pictures\\ToMenu.png')
        if self.highscore == None:
            self.highscore = p2.load_image('Pictures\\highscore.png')
        if self.currentscore == None:
            self.currentscore = p2.load_image('Pictures\\currentscore.png')
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
    time_per_speed = 80

    left,right,up,down=0,1,2,3

    def __init__(self, X, Y, Width, Height):
        self.x = X
        self.y = Y
        self.width=Width
        self.height=Height
        self.colorR = random.randint(204, 255)
        self.colorG = random.randint(80, 150)
        self.colorB = random.randint(80, 150)

    def draw(self):
        p2.draw_rendercolor(self.colorR,self.colorG,self.colorB,255)
        p2.draw_fillrectangle(self.x-self.width,self.y-self.height,self.x,self.y)

    def set_again(self):
        self.x+=880
        self.colorR = random.randint(204, 255)
        self.colorG = random.randint(80, 150)
        self.colorB = random.randint(80, 150)

    def update(self, frame_time):
        self.x-=speed*frame_time*self.time_per_speed
        if self.x<0:
            self.set_again()

    def get_bb(self):
        return self.x-self.width,self.y-self.height,self.x+self.width,self.y+self.height

class Background:
    time_per_speed = 30

    def __init__(self, X, Y, Width, Height):
        self.x = X
        self.y = Y
        self.width=Width
        self.height=Height
        self.colorR = random.randint(170, 230)
        self.colorG = random.randint(70, 130)
        self.colorB = random.randint(70, 130)

    def draw(self):
        p2.draw_rendercolor(self.colorR,self.colorG,self.colorB,255)
        p2.draw_fillrectangle(self.x-self.width,self.y-self.height,self.x,self.y)

    def set_again(self):
        self.x+=880
        self.colorR = random.randint(170, 230)
        self.colorG = random.randint(70, 130)
        self.colorB = random.randint(70, 130)

    def update(self, frame_time):
        self.x-=speed*frame_time*self.time_per_speed
        if self.x<0:
            self.set_again()

    def get_bb(self):
        return self.x-self.width,self.y-self.height,self.x+self.width,self.y+self.height


# obstacle
class Rect:
    global topsideY, bottomY, speed, scene

    time_per_speed = 100
    left,right,up,down=0,1,2,3

    def __init__(self, X, Y, Width, Height):
        self.x = X
        self.y = Y
        self.width = Width
        self.height = Height
        self.movement = random.randint(0, 3)
        self.movespeed=2
        self.timer=0
        self.colorR = random.randint(204, 255)
        self.colorG = random.randint(80, 150)
        self.colorB = random.randint(80, 150)
        self.once = 0

    def draw(self):
        p2.draw_rendercolor(self.colorR,self.colorG,self.colorB, 255)
        p2.draw_fillrectangle(self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height)

    def update(self, frame_time):
        a_left, a_bottom, a_right, a_top = player.get_bb()

        self.timer+=frame_time
        self.move(frame_time)
        self.x -= speed * frame_time * self.time_per_speed
        self.InArea(a_left, a_bottom, a_right, a_top)
        self.falldown(a_left, a_bottom, a_right, a_top)
        if player.rotate==0:
            self.collision(a_left, a_bottom, a_right, a_top)

    def delete(self):
        if self.x + self.width < 0:
            return True

    def call_pattern(self):
        if self.once == 0:
            if self.x < 400:
                self.once = 1
                return True

    def move(self,frame_time):
        if self.movement==self.left:
            self.x-=self.movespeed* frame_time * self.time_per_speed
        elif self.movement==self.right:
            self.x+=self.movespeed* frame_time * self.time_per_speed
        elif self.movement==self.up:
            self.y+=self.movespeed* frame_time * self.time_per_speed
        elif self.movement==self.down:
            self.y-=self.movespeed* frame_time * self.time_per_speed
        if self.timer>=1:
            self.timer=0
            self.movement = random.randint(0, 3)

    def InArea(self, a_left, a_bottom, a_right, a_top):
        if a_right+speed*10 >= self.x - self.width-5:
            if a_left+speed*10 <= self.x + self.width+5:
                if self.y < player.y:
                    if self.y>35 + 150:
                        ChangeBottomAndTop(self.y + self.height + Scale * 25, topsideY)
                if self.y > player.y:
                    if self.y<615-150:
                        ChangeBottomAndTop(bottomY, self.y - self.height - Scale * 25)

    def falldown(self, a_left, a_bottom, a_right, a_top):
        if a_left >= self.x + self.width:
            if a_left <= self.x + self.width + 150:
                if (player.position, player.rotate) == (player.bottom, False):
                    if a_bottom >= self.y + self.height - 5:
                        if a_bottom <= self.y + self.height + 20:
                            player.rotate = True
                            player.currentY = player.y
                            player.B = bottomY
                            player.position = player.top
                elif (player.position, player.rotate) == (player.top, False):
                    if a_top <= self.y - self.height + 5:
                        if a_top >= self.y - self.height - 20:
                            player.rotate = True
                            player.currentY = player.y
                            player.T = topsideY
                            player.position = player.bottom

    def collision(self, a_left, a_bottom, a_right, a_top):
        if a_right >= self.x - self.width:
            if a_right <= self.x - self.width + 15:
                if a_bottom <= self.y + self.height - 1:
                    if a_bottom >= self.y - self.height + 1:
                        if scene == 1:
                            Death()
                if a_top <= self.y + self.height - 1:
                    if a_top >= self.y - self.height + 1:
                        if scene == 1:
                            Death()

def handle_events():
    global scene, topsideY, bottomY
    global start, run, flash, scoreboard, revive,pause

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
    global scene, score, topsideY, bottomY, Scale, speed, current_time

    file_name = 'DataText\\SetMidGame.txt'
    setVariable_file = open(file_name, 'r')
    setVariable = json.load(setVariable_file)
    setVariable_file.close()

    scene = setVariable['variable']['scene']
    score = setVariable['variable']['score']
    speed = setVariable['variable']['speed']
    Scale = setVariable['variable']['Scale']
    gravity()
    current_time = time.time()
    player.x = -200
    player.y = bottomY
    player.position = player.bottom
    player.rotate = 0
    player.angle = 0
    bgm.resume()


def read_patterns():
    global obstacleNum, call_read_pattern

    startX = 1400
    patternName = ['pattern1', 'pattern2', 'pattern3', 'pattern4', 'pattern5', 'pattern6', 'pattern7',
                   'pattern8', 'pattern9', 'pattern10', 'pattern11', 'pattern12', 'pattern13', 'pattern14',
                   'pattern15', 'pattern16', 'pattern17', 'pattern18', 'pattern19', 'pattern20']

    patterns_file = open('DataText\\patternsMid.txt', 'r')
    patterns = json.load(patterns_file)
    patterns_file.close()

    patternsRandom = random.randint(0, 0)

    patternlength=int((int(score)/100)+1)
    call_read_pattern = patternlength

    for i in range(patternlength):
        position = patterns[patternName[patternsRandom]]['data'][2]
        patternShape = patterns[patternName[patternsRandom]]['data'][1]
        patternX = patterns[patternName[patternsRandom]]['data'][3]
        patternY = patterns[patternName[patternsRandom]]['data'][4]
        patternWidth = patterns[patternName[patternsRandom]]['data'][5]
        patternHeight = patterns[patternName[patternsRandom]]['data'][6]
        if position == -1:
            position = random.randint(0, 1)
            patternY = random.randint(0, 100)
        if patternShape == 1:
            if position == 0:
                obstacle.append(Rect(startX + patternX,
                                     75 + 150 + patternY,
                                     patternWidth * Scale,
                                     patternHeight * Scale))
                obstacleNum += 1
            elif position == 1:
                obstacle.append(Rect(startX + patternX,
                                     575 - 150 - patternY,
                                     patternWidth * Scale,
                                     patternHeight * Scale))
                obstacleNum += 1


def enter():
    global scene, score, highscore, Scale, speed, call_read_pattern, obstacleNum, topsideY, bottomY, alive
    global current_time, thornimage, numberimage, file_name, wallR, wallG, wallB, backgroundR, backgroundG, backgroundB
    global player, obstacle, stopIngredient, bgm, musicDie, musicRevive,background,wall1,wall2
    global start, run, flash, scoreboard, revive, pause

    p2.hide_cursor()

    file_name = 'DataText\\SetMidGame.txt'
    setVariable_file = open(file_name, 'r')
    setVariable = json.load(setVariable_file)
    setVariable_file.close()

    start, run, flash, scoreboard, revive,pause = 0, 1, 2, 3, 4,5
    alive = 0
    speed = setVariable['variable']['speed']
    scene = setVariable['variable']['scene']
    score = setVariable['variable']['score']
    highscore = setVariable['variable']['highscore']
    Scale = setVariable['variable']['Scale']
    obstacleNum = setVariable['variable']['obstacleNum']
    call_read_pattern = setVariable['variable']['call_read_pattern']
    numberimage = p2.load_image('Pictures\\numbersM.png')
    bgm = p2.Music('Musics\\PurelyGrey-Chasm[HyperflexOST].mp3')
    bgm.set_volume(64)
    bgm.repeat_play()
    musicDie = p2.Wav('Musics\\MusicDie.wav')
    musicDie.set_volume(64)
    musicRevive = p2.Wav('Musics\\MusicRevive.wav')
    musicRevive.set_volume(64)
    current_time = time.time()

    background = [
        [Background((col + 1) * 80 - 80, (row + 1) * 80 ,80,80) for col in range(11)] for row in
        range(8)]
    wall1 = [
        [Wall((col + 1) * 80 - 80, (row + 1) * 80 - 56, 80, 80) for col in range(11)] for row in
        range(3)]
    wall2 = [
        [Wall((col + 1) * 80 - 80, (row + 1) * 80 + 465, 80,80) for col in range(11)] for row in
        range(3)]
    topsideY, bottomY =  615 - 150 - Scale * 25,35 + 150 + Scale * 25

    stopIngredient = StopIngredient()
    player = Player()
    player._Init_()

    obstacle = []


def update():
    global scene, score, obstacleNum, speed, current_time, call_read_pattern, highscore, score,frame_time
    global start, run, flash, scoreboard, revive,pause

    start, run, revive = 0, 1, 4
    p2.clear_canvas()

    frame_time = time.time() - current_time
    current_time = time.time()
    if (scene == start):
        firstMove()
        update_wall(frame_time)
        update_background(frame_time)
        player.update()
    elif (scene == run):
        update_wall(frame_time)
        update_background(frame_time)
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

        if call_read_pattern == 0:
            read_patterns()


        player.update()
    elif (scene == revive):
        speed = 20

        update_wall(frame_time)
        update_background(frame_time)
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
    global obstacleNum, scene, highscore, score, alive, frame_time, current_time
    global start, run, flash, scoreboard, revive,pause

    draw_background()
    if (scene == start):
        alive = 0
        draw_wall()
        player.draw()
        numberDraw(score, 60, 580, 0.3)
    elif (scene == run):
        draw_wall()
        for i in range(obstacleNum):
            obstacle[i].draw()
        player.draw()
        numberDraw(int(score), 60, 580, 0.3)
    elif (scene == flash):
        highscore_file = open('DataText\\HighScoreMid.txt', 'r')
        highscore = json.load(highscore_file)
        highscore_file.close()

        if highscore < score:
            highscore_file = open('DataText\\HighScoreMid.txt', 'w')
            json.dump(score, highscore_file)
            highscore_file.close()
            highscore = score

        scene = scoreboard
        bgm.pause()
        musicDie.play()

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

def player_rotate():
    player.rotate = True
    player.currentY = player.y
    player.B = bottomY
    player.T = topsideY

def gravity():
    ChangeBottomAndTop(35 + 150 + Scale * 25, 615 - 150 - Scale * 25)
    if player.rotate==0:
        if player.position==player.bottom:
            if player.y>=bottomY+5:
                player_rotate()
            elif player.y<=bottomY-5:
                player_rotate()
        elif player.position==player.top:
            if player.y>=topsideY+5:
                player_rotate()
            elif player.y<=topsideY-5:
                player_rotate()


def ChangeBottomAndTop(B, T):
    global topsideY, bottomY
    bottomY = B
    topsideY = T


def Death():
    global scene
    scene = 2

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
    for i in range(3):
        for j in range(11):
            wall1[i][j].draw()
    for i in range(3):
        for j in range(11):
            wall2[i][j].draw()

def update_wall(frame_time):
    for i in range(3):
        for j in range(11):
            wall1[i][j].update(frame_time)
    for i in range(3):
        for j in range(11):
            wall2[i][j].update(frame_time)

def draw_background():
    for i in range(8):
        for j in range(11):
            background[i][j].draw()

def update_background(frame_time):
    for i in range(8):
        for j in range(11):
            background[i][j].update(frame_time)


def firstMove():
    global scene

    if player.x < 200:
        player.x += 5
    elif player.x >= 200:
        scene = 1
        read_patterns()

def exit():
    global player, background, obstacle, stopIngredient, bgm, musicDie, musicRevive
    del (player, background, obstacle, stopIngredient, bgm, musicDie, musicRevive)


def pause():
    pass


def resume():
    pass
