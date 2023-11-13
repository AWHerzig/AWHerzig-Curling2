import pygame
import numpy
import pandas
import random
import math
from colormath.color_diff import delta_e_cie2000
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color

global leaguePick 

screen = (1000, 700)
button = (500, 100)
hRad = 70
sRad = 10
xlim = (400, 600)
ylim = (10, screen[1]-25)
hogLine = 250
start = (500, 600)
space, underscore = ' ', '_'

WhiteC = (250, 250, 250)
BlackC = (0, 0, 0)
RedC = (148, 10, 13)
BlueC = (12, 15, 153)
GreenC = (5, 51, 4)
PurpleC = (41, 8, 51)
OrangeC = (148, 43, 4)
YellowC = (191, 173, 10)

seriesLoc = [
    None,
    [0],
    None,
    [0, 1, 0],
    None,
    [0, 0, 1, 1, 0],
    None,
    [0, 0, 1, 1, 0, 1, 0]
]

endmatch = {
    '1': 'st',
    '2': 'nd',
    '3': 'rd',
    '4': 'th',
    '5': 'th',
    '6': 'th',
    '7': 'th',
    '8': 'th',
    '9': 'th',
    '0': 'th',
}


def text(string, pos, size, surface, color=BlackC):
    font = pygame.font.Font('freesansbold.ttf', size)
    obj = font.render(str(string), True, color)
    textRect = obj.get_rect()
    textRect.center = pos
    surface.blit(obj, textRect)

def image(path, out, tl, size):
    pic = pygame.transform.scale(pygame.image.load(path), size)
    picrect = pic.get_rect().move(tl)
    out.blit(pic, picrect)

def checkpoint(str, pos=(500, 300), size=40, out=None, color=BlackC, filter=None):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
            if event.type == pygame.QUIT:
                pygame.quit()
        out.fill(WhiteC)
        text('Click to continue', (500, 50), 16, out, BlackC)
        text(str, pos, size, out, color)
        pygame.display.update()

def pythag(a, b):  # A lot of this file is gonna be "just nice to have"
    return math.sqrt(a ** 2 + b ** 2)


def odds(chance):  # inputs are 0 to 1, default of uniform()
    X = numpy.random.uniform()
    if X < chance:
        return True
    else:
        return False


def quad(var, a, b, c):  # "just nice to have"
    return (a * (var ** 2)) + (var * b) + c

class Spot:
    def __init__(self, obj):
        self.x = obj[0]
        self.y = obj[1]


def distanceFormula(a, b):
    return math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)


def clamp(val, low=0, high=1):  # nice2have, really surprised it isn't built-in Python
    if val < low:
        val = low
    elif val > high:
        val = high
    return val

def dfSpotChecker(df, row, col, val):
    try:
        return df.iloc[row, col] == val
    except IndexError:
        return False


def listsub(x, y):
    return [x[0]-y[0], x[1]- y[1]]

def listmult(x, scalar):
    return [scalar * x[0], scalar * x[1]]
    
def rgbTOlab(color):
    rgb = sRGBColor(rgb_r = color[0], rgb_g =color[1], rgb_b = color[2], is_upscaled=True)
    lab = convert_color(rgb, LabColor)
    return lab


def fancycolor(color):
    return sRGBColor(rgb_r = color[0], rgb_g =color[1], rgb_b = color[2], is_upscaled=True)

def colorscore(colors):
    return delta_e_cie2000(rgbTOlab(colors[0]), rgbTOlab(colors[1]))


def colorchecker(homecols, awaycols, req = 0):
    order = [
        [homecols[0], awaycols[0]],
        [homecols[0], awaycols[1]],
        [homecols[1], awaycols[1]],
        [homecols[1], awaycols[0]]
    ]
    for pair in order:
        if colorscore(pair) > req:
            return pair
    return [BlueC, RedC]


def bracket(teams, surf, topL = (0, 25), botR = (1000, 700), page = True, leng = None):  # This shit is dope, teams should be seeded. More than 32 really get squeezed.
    surf.fill(color=WhiteC)
    minX, minY = topL
    maxX, maxY = botR
    n = len(teams)
    R = math.ceil(math.log(n, 2)) + 1
    xpr = (maxX - minX) / R
    bracketRecursive((maxX, .5*(minY+maxY)), 1, R, xpr, minY, maxY, surf, teams, 1)
    topFirst = (botR[0] - topL[0]) / (2*R)
    topSplit = (botR[0] - topL[0]) / (R)
    for i in range(len(leng)):
        text(f'Best of {leng[i]}', (topFirst + i*topSplit, 15), 12, surf)
    pygame.display.update()
    while page:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                page = False
            if event.type == pygame.QUIT:
                pygame.quit()


def bracketRecursive(front, r, maxr, xpr, ceil, floor, surf, teams, seed):  # ceil in minY, floor is maxY
    back = front[0] - xpr, front[1]
    up = back[0], .5*(back[1] + ceil)
    down = back[0], .5*(floor + back[1])
    pygame.draw.line(surf, BlackC, front, back)
    if r == maxr or 2**r + 1 - seed > len(teams):
        text(f'{teams[seed-1]} ({teams[seed-1].pwins})', (.5*(front[0]+back[0]), front[1]-10), 16, surf)
        #text(f'{teams[seed-1]}', (.5*(front[0]+back[0]), front[1]-10), 16, surf)
        return
    if r < maxr:
        pygame.draw.line(surf, BlackC, back, up)
        pygame.draw.line(surf, BlackC, back, down)
        bracketRecursive(up, r + 1, maxr, xpr, ceil, front[1], surf, teams, seed)
        bracketRecursive(down, r + 1, maxr, xpr, front[1], floor, surf, teams, 2**r + 1 - seed)

def resultsDisplayer(out, games, addedText = ''): # Takes up to 12
    if len(games) > 12:
        print(len(games), 'is bigger than 12')
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
            if event.type == pygame.QUIT:
                pygame.quit()
        out.fill(WhiteC)
        text('Click to continue', (500, 50), 16, out, BlackC)
        text(addedText, (250, 50), 24, out, BlackC)
        text(addedText, (750, 50), 24, out, BlackC)
        for sheet in range(len(games)):
            games[sheet].board.output(out, 200 + 300*(sheet%3), 100 + 150*(sheet//3))
        pygame.display.update()

def standingsDisplayer(out, tables, addedText = ''): # Takes up to 4
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
            if event.type == pygame.QUIT:
                pygame.quit()
        out.fill(WhiteC)
        text('Click to continue', (500, 50), 16, out, BlackC)
        text(addedText, (250, 50), 24, out, BlackC)
        text(addedText, (750, 50), 24, out, BlackC)
        for i in range(len(tables)):
            tables[i].output(out, 1000//4 + 500*(i%2), 100 + 300 * (i//2))
        pygame.display.update()


def strViaList(x, ind):
    y = list(x)
    return f"{ind} |{strup(y[0], 15)} |{strup(y[1], 7)} |{strup(y[2], 7)} |{strup(y[3], 7)}"

def strup(x, leng):  # String up... but im calling it strup from now on
    y = str(x)
    return y + max(0, int(1.6*(leng-len(y))))*' '


"""
RegionT = [ # This is here for future
    Team('', '', [(), ()]),
    Team('', '', [(), ()]),
    Team('', '', [(), ()]),
    Team('', '', [(), ()]),
    Team('', '', [(), ()]),
    Team('', '', [(), ()]),
    Team('', '', [(), ()])
]
"""

def seeder_full(matchups):
    x = [None]*100
    recD = seeder_rec(matchups, 0, 1)
    high = max(list(recD.values()))
    for team in list(recD.keys()):
        x[recD[team]] = team
    return x[:high+1]

    #recD.update

def seeder_rec(split, high, turn):
    if isinstance(split, tuple) or isinstance(split, list):
        smallD = {}
        smallD.update(seeder_rec(split[0], high = high, turn = turn + 1))
        smallD.update(seeder_rec(split[1], high = 2**turn - 1 - high, turn = turn + 1))
        return smallD
    else:
        return {split: high}
            

def findMatchups(teams, depth, path):
    #print(teams, depth, path)
    #print(path.append(0))
    if isinstance(teams, tuple) or isinstance(teams, list):
        if depth == 1:
            return {teams: path}
        else:
            smallD = {}
            smallD.update(findMatchups(teams[0], depth = depth-1, path = path + [0]))
            smallD.update(findMatchups(teams[1], depth = depth-1, path = path + [1]))
            return smallD
    else:
        return {}


def path_replacer(big, path, rep):
    if len(path) == 0:
        return rep
    else:
        if path[0] == 0: # Either 0 or 1
            return path_replacer(big[0], path[1:], rep), big[1]
        else:
            return big[0], path_replacer(big[1], path[1:], rep)





    