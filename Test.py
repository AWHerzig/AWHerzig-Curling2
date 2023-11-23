from Objects import *
"""
class ID:
    def __init__(self, grid, shot):
        self.grid = grid
        self.shot = shot
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.grid == other.grid and self.shot == other.shot
        else:
            return False

    def __str__(self):
        return f'{len(self.grid)} {self.shot}'
"""
def griddr(sheet, hammer):
    hammergrid = dict()
    leadgrid = dict()
    for rock in sheet.stones:
        if distanceFormula(rock, Spot(button)) <= hRad + sRad:
            key = round(2*(rock.x-button[0]), -2)//2, round(2*(rock.y-button[1]), -2)//2
            if rock.team == hammer:
                if key in hammergrid.keys():
                    hammergrid[key] += 1
                else:
                    hammergrid[key] = 1
            else:
                if key in leadgrid.keys():
                    leadgrid[key] += 1
                else:
                    leadgrid[key] = 1
    return hammergrid, leadgrid



def takeouttarget(sheet, team):
    df = pandas.DataFrame({
            'stones': [i for i in sheet.stones],
            'color': [i.team for i in sheet.stones],
            'dist': [distanceFormula(i, Spot(button)) for i in sheet.stones]
        }).sort_values(['dist'], ascending=True, ignore_index=True)
    df = df[df.color != team]
    if len(df) == 0:
        return 0
    tar = df.iloc[0, 0]
    ratio = (tar.y-start[1])/(tar.x-start[0]) if tar.x != start[0] else 0    # y/x
    yv = -7
    xv = ratio / yv
    return xv, yv, 0

comShots = [
        (0, -5, 0), # Button
        (-.3, -5.3, 0), # Backleft
        (-.33, -4.7, 0), # Frontleft
        (.3, -5.3, 0), # Backright
        (.33, -4.7, 0), # Frontright
        (-.8, -5.3, .03), # Middleback
        (1, -4.8, -.04), # Middle-in
        (0, -4, 0) # Center Guardd
    ]

def randoshot(sheet, team):
    localshots = comShots.copy()
    if takeouttarget(sheet, team):
        localshots.append(takeouttarget(sheet, team))
    return random.choice(localshots)

bigtable = [None] * 17
for i in range(len(bigtable)):
    bigtable[i] = pandas.DataFrame(columns=['hammer', 'lead', 'shot', 'curscore', 'hammerscore'], dtype=int)

Team1 = Team('HAMMER TEAM', 'HAM')
Team2 = Team('LEAD TEAM', 'LED')

hammerKey = {}
hammerCur = 0
leadKey = {}
leadCur = 0 
shotKey = {}
shotCur = 0 

class hashabledict(dict):
  def __key(self):
    return tuple((k,self[k]) for k in sorted(self))
  def __hash__(self):
    return hash(self.__key())
  def __eq__(self, other):
    return self.__key() == other.__key()

def hscoring(sheet, hammer):
    scoreBase = sheet.scoring()
    return scoreBase[1] if scoreBase[0] == hammer else -scoreBase[1]


def testend(lead, hammer, sheet, rocks):
    holder = []
    sheet.clear(0, hammer)
    for i in range(rocks):
        cur = randoshot(sheet, lead)
        holder.append([(rocks-i)*2, griddr(sheet, hammer), cur, hscoring(sheet, hammer)])
        testshot(sheet, lead, cur)
        cur = randoshot(sheet, hammer)
        holder.append([((rocks-i)*2)-1, griddr(sheet, hammer), cur, hscoring(sheet, hammer)])
        testshot(sheet, hammer, cur)
    score = hscoring(sheet, hammer)
    for i in holder:
        i.append(score)
    return tuple(holder)

def testshot(sheet, team, shot):
    newStone = Stone(team)
    sheet.addStone(newStone)
    newStone.xv, newStone.yv, newStone.curve = shot
    """
    newStone.xv = numpy.random.normal(newStone.xv, abs(.2 - .02*team.Xacc))
    newStone.yv = numpy.random.normal(newStone.yv, abs(.2 - .02*team.Yacc))
    newStone.curve = numpy.random.normal(newStone.curve, abs(.02 - .002*team.Cacc))
    """
    inmotion_blind(sheet)

def inmotion_blind(sheet):
    time = 0
    while sheet.aStoneMoves():
        if time > 10000:
            print('woop')
        time += 1
        for stone in sheet.movers:
            res = stone.move(time % 10 == 0 and time > 0)
            if not res:
                sheet.clearStone(stone)
        pairs = [(i, j) for i in sheet.stones for j in sheet.stones]
        for a, b in pairs:
            if a != b and distanceFormula(a, b) < 2*sRad:
                if sheet.whitelist(a, b, time): # only want this called if they in range
                    s1 = collision(a, b)
                    s2 = collision(b, a)
                    a.xv, a.yv = s1
                    b.xv, b.yv = s2
                    a.curve, b.curve = 0, 0
        
def collision(stone1, stone2):  # call it for both before setting v's
    v1 = [stone1.xv, stone1.yv]
    v2 = [stone2.xv, stone2.yv]
    xvec = [stone1.x - stone2.x, stone1.y - stone2.y]
    vvec = listsub(v1, v2)
    dotted = numpy.dot(vvec, xvec)
    magx = pythag(xvec[0], xvec[1]) ** 2
    diff = listmult(xvec, dotted/magx)
    final = listsub(v1, diff)
    return final

print('starting')
for numstones in range(1):
    numstones = 4 # Always 4
    print(numstones, 'stones')
    testsheet = Sheet(Team1, Team2, 10, numstones)
    for i in range(1000):
        print(i)
        cur = testend(Team2, Team1, testsheet, numstones)
        for shotsleft, grid, shot, curscore, hammerscore in cur:
            # hammer
            hashhammer = hashabledict(grid[0])
            hashlead = hashabledict(grid[1])
            #hashshot = shot[0] * shot[1] + shot[2]
            hashshot = shot
            if hashhammer in hammerKey.keys():
                hammerOut = hammerKey[hashhammer]
            else:
                hammerOut = hammerCur
                hammerKey[hashhammer] = hammerCur
                hammerCur += 1
            # lead
            if hashlead in leadKey.keys():
                leadOut = leadKey[hashlead]
            else:
                leadOut = leadCur
                leadKey[hashlead] = leadCur
                leadCur += 1
            # shot
            if shot[1] == -7:
                shotOut = 99
            elif hashshot in shotKey.keys():
                shotOut = shotKey[hashshot]
            else:
                shotOut = shotCur
                shotKey[hashshot] = shotCur
                shotCur += 1
            if shotOut == -1:
                print(shot)
            if hammerOut == 0 and leadOut == 0 and shot == 'takeout':
                print('whjatj fd')
            bigtable[shotsleft].loc[len(bigtable[shotsleft])] = [hammerOut, leadOut, shotOut, curscore, hammerscore]

for num in range(len(bigtable)):
    print('ouputting', num)
    bigtable[num].to_csv(f'./Testing/ShotsLeft_{num}.csv')
    #bigtable[num].groupby(by=['hammer', 'lead', 'shot', 'curscore']).mean().to_csv(f'./Testing/ShotsLeft_{num}.csv')

pandas.DataFrame({
    'Hammer_PKEY': list(hammerKey.keys()),
    'Hammer_Grid': list(hammerKey.values())
}).to_csv(f'./Testing/hammer.csv')
pandas.DataFrame({
    'Lead_PKEY': list(leadKey.keys()),
    'Lead_Grid': list(leadKey.values())
}).to_csv(f'./Testing/lead.csv')
pandas.DataFrame({
    'Shot_PKEY': list(shotKey.keys()),
    'Shot_Grid': list(shotKey.values())
}).to_csv(f'./Testing/shot.csv')