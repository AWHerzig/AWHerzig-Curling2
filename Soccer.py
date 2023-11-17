from Game import *
#from Objects import *
#from DirWide import *
# Teams
EnglandS = [
    Team('West Ham', 'WHU', [(122, 38, 58), (27, 177, 231)]),
    Team('Arsenal', 'ARS', [(239, 1, 7), (156, 130, 74)]),
    Team('Spurs', 'TOT', [(160, 160, 160), (19, 34, 87)]),
    Team('Chelsea', 'CHE', [(3, 70, 148), (209, 211, 212)]),
    Team('Brighton', 'BRI', [(0, 87, 184), (255, 205, 0)])
]
EnglandN = [
    Team('Liverpool', 'LIV', [(200, 16, 46), (0, 178, 169)]),
    Team('Man City', 'MNC', [(108, 171, 221), (255, 198, 89)]),
    Team('Man United', 'MNU', [(218, 41, 28), (251, 225, 34)]),
    Team('Newcastle', 'NEW', [(45, 41, 38), (160, 160, 160)]),
    Team('Aston Villa', 'AST', [(149,191,229), (103,14,54)])
]
Spain = [
    Team('Real Madrid', 'RMA', [(160, 160, 160), (0, 82, 159)]),
    Team('FC Barcelona', 'FCB', [(165,0,68), (0, 77, 152)]),
    Team('Atletico', 'AMA', [(39,46,97), (203,53,36)]),
    Team('Villarreal', 'VIL', [(255, 230, 103), (0, 81, 135)]),
    Team('Sevilla', 'SEV', [(244, 51, 51), (160, 160, 160)])
]
Germany = [
    Team('Bayern', 'BAY', [(220,5,45), (0,102,178)]),
    Team('Dortmund', 'DOR', [(253, 225, 0), (0, 0, 0)]),
    Team('Leipzig', 'LEI', [(221, 1, 63), (12, 32, 67)]),
    Team('Leverkusen', 'LEV', [(227, 34, 33), (0, 0, 0)]),
    Team('Hamburg', 'HAM', [(10, 64, 134), (160, 160, 160)])
]
Italy = [
    Team('Juventus', 'JUV', [(0,0,0), (160, 160, 160)]),
    Team('AC Milan', 'ACM', [(251,9,11), (0,0,0)]),
    Team('Inter Milan', 'INT', [(1, 14, 128), (0, 0, 0)]),
    Team('Napoli', 'NAP', [(18, 160, 215), (160, 160, 160)]),
    Team('AS Roma', 'ROM', [(134, 38, 51), (240, 188, 66)])
]
Francugal = [
    Team('Paris SG', 'PSG', [(1, 66, 106), (218, 41, 28)]),
    Team('AS Monaco', 'MON', [(229, 27, 34), (203, 159, 24)]),
    Team('Benfica', 'BEN', [(232, 48, 48), (0, 0, 0)]),
    Team('FC Porto', 'POR', [(0, 66, 140), (214, 0, 25)]),
    Team('Sporting CP', 'SPO', [(0, 128, 87), (243, 194, 66)])
]

Teams = [EnglandS, EnglandN, Spain, Germany, Italy, Francugal]
Tables = [
    Standings(EnglandS, 'England-South'),
    Standings(EnglandN, 'England-North'),
    Standings(Germany, 'Germany'),
    Standings(Spain, 'Spain'),
    Standings(Italy, 'Italy'),
    Standings(Francugal, 'France/Portugal')
]
AllTeams = Standings(EnglandN + EnglandS + Spain + Germany + Italy + Francugal, 'ALL TEAMS', dset=False)
# Schedule 
schedule = [[]]*20 # 8 Div games in 10 slates plus 10 non div games, 2 of non-divs will be against same team its a bitch to fix that ig
for div in Teams: # Front Side
    w = div.copy()
    random.shuffle(w)
    if len(w) % 2 == 1:
        w.append(None)
    n = len(w)
    d = list(range(n))
    mid = n // 2
    for i in range(n - 1):
        l1 = d[:mid]
        l2 = d[mid:]
        l2.reverse()
        round = []
        for j in range(mid):
            t1 = w[l1[j]]
            t2 = w[l2[j]]
            if j == 0 and i % 2 == 1:
                round.append((t2, t1))
            else:
                round.append((t1, t2))
        schedule[i] = schedule[i] + round
        # rotate list by n/2, leaving last element at the end
        d = d[mid:-1] + d[:mid] + d[-1:]
for div in Teams: # Reverse Fixtures
    w = div.copy()
    random.shuffle(w)
    if len(w) % 2 == 1:
        w.append(None)
    n = len(w)
    d = list(range(n))
    mid = n // 2
    for i in range(n - 1):
        l1 = d[:mid]
        l2 = d[mid:]
        l2.reverse()
        round = []
        for j in range(mid):
            t1 = w[l1[j]]
            t2 = w[l2[j]]
            if j == 0 and i % 2 == 1:
                round.append((t1, t2))
            else:
                round.append((t2, t1))
        schedule[i+5] = schedule[i+5] + round
        # rotate list by n/2, leaving last element at the end
        d = d[mid:-1] + d[:mid] + d[-1:]
for i in Teams:
    random.shuffle(i)
random.shuffle(Teams)
ExtraSlate1M = [[i[j] for i in Teams] for j in range(5)]
ExtraSlate2M = [[i[(j+Teams.index(i))%5] for i in Teams] for j in range(5)]
for div in ExtraSlate1M: # Extra slates 1
    w = div.copy()
    random.shuffle(w)
    if len(w) % 2 == 1:
        w.append(None)
    n = len(w)
    d = list(range(n))
    mid = n // 2
    for i in range(n - 1):
        l1 = d[:mid]
        l2 = d[mid:]
        l2.reverse()
        round = []
        for j in range(mid):
            t1 = w[l1[j]]
            t2 = w[l2[j]]
            if j == 0 and i % 2 == 1:
                round.append((t2, t1))
            else:
                round.append((t1, t2))
        schedule[i+10] = schedule[i+10] + round
        # rotate list by n/2, leaving last element at the end
        d = d[mid:-1] + d[:mid] + d[-1:]
for div in ExtraSlate2M: # Extra Slates 2
    w = div.copy()
    random.shuffle(w)
    if len(w) % 2 == 1:
        w.append(None)
    n = len(w)
    d = list(range(n))
    mid = n // 2
    for i in range(n - 1):
        l1 = d[:mid]
        l2 = d[mid:]
        l2.reverse()
        round = []
        for j in range(mid):
            t1 = w[l1[j]]
            t2 = w[l2[j]]
            if j == 0 and i % 2 == 1:
                round.append((t2, t1))
            else:
                round.append((t1, t2))
        schedule[i+15] = schedule[i+15] + round
        # rotate list by n/2, leaving last element at the end
        d = d[mid:-1] + d[:mid] + d[-1:]
random.shuffle(schedule)

def playit(schedule, out, Tables, ends, rocks):
    for slate in schedule:
        rezzies = []
        for matchup in slate:
            if None not in matchup:
                rezzies.append(game(matchup[0], matchup[1], out, ends=ends, rocks=rocks))
        num = 0
        while num < len(rezzies):
            resultsDisplayer(out, rezzies[num:min(num+12, len(rezzies))])
            num += 12
        for div in Tables:
            div.standingsUpdate()
        AllTeams.standingsUpdateDIV()
        standingsDisplayer(out, Tables[0:3], 'NORTH')
        standingsDisplayer(out, Tables[3:8], 'SOUTH')
        standingsDisplayer(out, [AllTeams], 'ALL TEAMS')
    #Tournament
    playoffs = noneRemover(unseeder(tuple(list(AllTeams.df.iloc[:6, 0]) + [None]*4 + list(AllTeams.df.iloc[6:9, 0])))) # Super weird
    playoffPlayer(out, playoffs, [1, 1, 1, 1], [False, False, False, False], ends=ends, rocks=rocks)


def playoffPlayer(out, matchups, leng, seeded, ends, rocks): # just gotta be careful leng matches, this goes in everything
    R = len(leng)
    for roundN in range(R):
        sLeng = leng[roundN]
        slateD = findMatchups(matchups, R-roundN, [])
        slateM = list(slateD.keys())
        for pair in slateM:
            pair[0].pwins, pair[1].pwins = 0, 0
        need = (sLeng + 1) // 2
        bracket(seeder_full(matchups), out, leng=leng[roundN:])
        for gamenum in range(sLeng):
            rezzies = []
            for pair in slateM:
                if pair[0].pwins < need and pair[1].pwins < need:
                    if (seriesLoc[sLeng][gamenum] == 0 and seeded[roundN]) or \
                        (not seeded[roundN] and ((seriesLoc[sLeng][gamenum] == 0 and pair[0].seeder()>=pair[1].seeder()) or \
                                                    seriesLoc[sLeng][gamenum] == 1 and pair[0].seeder()<pair[1].seeder())): # lets pray
                        rezzies.append(game(pair[0], pair[1], out, finish=2, ends=ends, rocks=rocks, view='highlight'))
                    else:
                        rezzies.append(game(pair[1], pair[0], out, finish=2, ends=ends, rocks=rocks, view = 'highlight'))
                else:
                    pass # this is actually pass
            if rezzies:
                resultsDisplayer(out, rezzies, f'Round {roundN+1}-Game {gamenum+1}')
                bracket(seeder_full(matchups), out, leng=leng[roundN:])
        for pair in slateM:
            winner = pair[0] if pair[0].pwins == need else pair[1]
            path = slateD[pair]
            matchups = path_replacer(matchups, path, winner)
    checkpoint(f'{matchups} WINS THE CHAMPIONSHIP', out = out)



