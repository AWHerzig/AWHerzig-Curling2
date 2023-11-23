from Button import *

class Team:
    def __init__(self, name, ABR, colors = [BlueC, RedC], controlled = False):
        self.name = name
        self.ABR = ABR
        self.Xacc = random.randrange(-10, 11)
        self.Yacc = random.randrange(-10, 11) 
        self.Cacc = random.randrange(-10, 11) 
        self.controlled = controlled
        self.prefs = colors  # Will be list
        self.division = ''
        # Game specifc
        self.score = 0
        self.color = colors[0]  
        # Season info
        self.wins = 0
        self.loss = 0
        self.PointsFor = 0
        self.PointsAgainst = 0
        self.pwins = 0
        self.games = []

    def spot(self):
        return list(self.division.df.Team).index(self) + 1

    def top3rd(self):
        return len(self.division.df)/3 >= self.spot()

    def seeder(self):
        return self.wins + .01*(self.PointsFor - self.PointsAgainst)

    def __str__(self):
        return self.name

BlankTeam = Team('Blank End', 'BLANK')

class Stone:
    def __init__(self, team):
        self.x = start[0]
        self.y = start[1]
        self.xv = 0
        self.yv = 0
        self.curve = 0
        self.team = team
        self.color = self.team.color
        self.rad = sRad

    def move(self, curveBool):
        self.x += self.xv
        self.y += self.yv
        self.xv += (self.curve if curveBool else 0)
        self.xv = clamp(self.xv, self.yv, abs(self.yv))
        self.yv *= .99
        self.xv *= .99
        if abs(self.yv) < .03:
            self.yv = 0
            self.xv = 0
            if self.y > hogLine:
                return False
        if self.x < xlim[0] or self.x > xlim[1] or self.y < ylim[0]:
            return False
        else:
            return True

    def output(self, out):
        pygame.draw.circle(out, self.color, (self.x, self.y), self.rad)

    def __str__(self):
        return self.team.ABR


class Sheet:
    def __init__(self, home, away, ends, rocks):
        self.stones = []
        self.movers = []
        self.pairs = {}
        self.home = home
        self.away = away
        self.board = Scoreboard(home, away, ends)
        self.endnum = 1
        self.rocks = rocks
        self.rockslefthome = rocks
        self.rocksleftaway = rocks
        self.hammer = home

    def clear(self, end, hammer):
        self.stones = []
        self.movers = []
        self.pairs = {}
        self.endnum = end
        self.rockslefthome = self.rocks
        self.rocksleftaway = self.rocks
        self.hammer = hammer

    def aStoneMoves(self):
        self.movers = []
        for i in self.stones:
            if i.xv != 0 or i.yv != 0:
                self.movers.append(i)
        return self.movers

    def addStone(self, stone):
        self.stones.append(stone)
        if stone.team == self.home:
            self.rockslefthome -= 1
        else:
            self.rocksleftaway -= 1
        self.pairs = {}

    def clearStone(self, stone):
        self.stones.remove(stone)

    def view(self, out): 
        out.fill(WhiteC)
        for i in range(hRad//10, 0, -2):
            pygame.draw.circle(out, BlackC, button, (10*i), width = 2)
        pygame.draw.line(out, BlackC, (xlim[0], ylim[0]), (xlim[1], ylim[0]))
        pygame.draw.line(out, BlackC, (xlim[0], ylim[0]), (xlim[0], ylim[1]))
        pygame.draw.line(out, BlackC, (xlim[1], ylim[1]), (xlim[1], ylim[0]))
        pygame.draw.line(out, BlackC, (xlim[1], ylim[1]), (xlim[0], ylim[1]))
        pygame.draw.line(out, BlackC, (xlim[0], hogLine), (xlim[1], hogLine))
        if modePick == '2-player':
            image(f'./{l1}/{self.home.name.replace(space, underscore)}.png', out, tl=(400, 400), size=(200, 200 * (3/4)))
        else:
            image(f'./{leaguePick}/{self.home.name.replace(space, underscore)}.png', out, tl=(400, 400), size=(200, 200 * (3/4)))
        for stone in self.stones:
            stone.output(out)
        self.board.output(out)
        temp = self.scoring()
        text(f'Current Scoring: {temp[0].ABR}  {temp[1]}', (150, 375), 20, out)
        text(f'End Number: {self.endnum}', (150, 425), 20, out)
        #self.home.division.output(out, 800, 100)
        #self.away.division.output(out, 800, 400)
        # Stones left
        width = 150
        text(f'{self.away.ABR}', (100, 450), 20, out)
        for i in range(self.rocksleftaway):
            pygame.draw.circle(out, self.away.color, (width + 25*i, 450), sRad)
        text(f'{self.home.ABR}', (100, 475), 20, out)
        for i in range(self.rockslefthome):
            pygame.draw.circle(out, self.home.color, (width + 25*i, 475), sRad)
        text('(H)', (50, 450 if self.hammer == self.away else 475), 20, out)

    def scoring(self):
        df = pandas.DataFrame({
            'stones': [i for i in self.stones],
            'color': [i.team for i in self.stones],
            'dist': [distanceFormula(i, Spot(button)) for i in self.stones]
        }).sort_values(['dist'], ascending=True, ignore_index=True)
        df = df[df.dist <= hRad + .5*sRad]
        if len(df) == 0:
            return BlankTeam, 0
        else:
            scoreTeam = df.iloc[0, 1]
            score = 1
            while dfSpotChecker(df, score, 1, scoreTeam):  # probably stupid
                score += 1
            return scoreTeam, score

    def whitelist(self, stone1, stone2, time):
        x = (stone1, stone2)
        y = (stone2, stone1)
        if x in list(self.pairs.keys()):
            if time - self.pairs[x] > 20:
                self.pairs[x] = time
                self.pairs[y] = time
                return True
            else:
                self.pairs[x] = time
                self.pairs[y] = time
                return False
        if y in list(self.pairs.keys()):
            if time - self.pairs[y] > 20:
                self.pairs[x] = time
                self.pairs[y] = time
                return True
            else:
                self.pairs[x] = time
                self.pairs[y] = time
                return False
        self.pairs[x] = time
        self.pairs[y] = time
        return True


class Scoreboard:
    def __init__(self, home, away, ends):
        self.top = [['ABR'] + [i+1 for i in range(ends)] + ['E'], 'F']
        self.home = [[home.ABR] + ([0]*(ends+1)), 0]
        self.away = [[away.ABR] + ([0]*(ends+1)), 0]

    def input(self, endnum, hscore, ascore):
        if endnum == 'E':
            endnum = -1
        self.home[0][endnum] = hscore
        self.away[0][endnum] = ascore
        self.home[1] = sum(self.home[0][1:])
        self.away[1] = sum(self.away[0][1:])

    def singleline(self, row):
        return '||'.join(map(str,['|'.join(map(str,row[0])), row[1]]))  # There's no way this works
         
    def output(self, out, startx=150, starty=200):
        size = len(self.singleline(self.top))
        text(self.singleline(self.top), (startx, starty), 24, out)
        text('-'*int(1.2*size), (startx, starty+25), 24, out)
        text(self.singleline(self.away), (startx, starty+50), 24, out)
        text('-'*int(1.2*size), (startx, starty+75), 24, out)
        text(self.singleline(self.home), (startx, starty+100), 24, out)

    def output_small(self, out, startx=150, starty=200):
        text(f'{self.home[0][0]} {self.home[1]}-{self.away[1]} {self.away[0][0]}', (startx, starty), 16, out)

class Standings:
    def __init__(self, teams, name, dset = True):
        self.name = name
        self.df = pandas.DataFrame({
            'Team' : teams,
            'Wins': [0]*len(teams),
            'Losses': [0]*len(teams),
            'PointsDiff': [0]*len(teams)
        })  
        if dset:
            for i in teams:
                i.division = self

    def standingsUpdate(self):
        self.df.Wins = [team.wins for team in self.df.Team] 
        self.df.Losses = [team.loss for team in self.df.Team]
        self.df.PointsDiff = [team.PointsFor - team.PointsAgainst for team in self.df.Team]
        self.df['pct']= numpy.where(self.df.Wins + self.df.Losses > 0,self.df.Wins / (self.df.Wins + self.df.Losses), .5)
        self.df = self.df.sort_values(['pct', 'PointsDiff'], ascending=False, ignore_index=True).drop('pct', axis=1)

    def standingsUpdateDIV(self): # FOR NFL CONFERENCE STANDINGS and Soccer ALL TEAMS
        self.df.Wins = [team.wins for team in self.df.Team] 
        self.df.Losses = [team.loss for team in self.df.Team]
        self.df.PointsDiff = [team.PointsFor - team.PointsAgainst for team in self.df.Team]
        self.df['pct']= numpy.where(self.df.Wins + self.df.Losses > 0,self.df.Wins / (self.df.Wins + self.df.Losses), .5)
        self.df['div']= [team.spot()==1 for team in self.df.Team]
        self.df['final'] = self.df['pct'] + self.df['div']
        self.df = self.df.sort_values(['final', 'PointsDiff'], ascending=False, ignore_index=True).\
            drop('pct', axis=1).drop('div', axis=1).drop('final', axis=1)

    def __str__(self):
        return self.df.to_string()

    def output(self, out, startx, starty):
        curx = startx
        cury = starty
        text(strViaList([self.name, 'W', 'L', '+/-'], ' '), (curx, cury), 16, out)
        for i in range(min(len(self.df), 16)):
            cury += 30
            text(strViaList(self.df.iloc[i], i+1), (curx, cury), 16, out)
        cury = starty
        curx = 1000 - startx
        for i in range(16, len(self.df)):
            cury += 30
            text(strViaList(self.df.iloc[i], i+1), (curx, cury), 16, out)

    def teams(self):
        return list(self.df.Team)




