from Game import *
# Make the teams

# NFC
NFCE = [
    Team('Eagles', 'PHI', [(0, 76, 84), (165, 172, 175)]),
    Team('Commanders', 'WSH', [(90, 20, 20), (255, 182, 18)]),
    Team('Cowboys', 'DAL', [(0, 53, 148), (134, 147, 151)]),
    Team('Giants', 'NYG', [(1, 35, 82), (163, 13, 45)])
]
NFCN = [ 
    Team('Lions', 'DET', [(0, 118, 182), (176, 183, 188)]),
    Team('Vikings', 'MIN', [(79, 38, 131), (255, 198, 47)]),
    Team('Packers', 'GB', [(24, 48, 40), (255, 184, 28)]),
    Team('Bears', 'CHI', [(11, 22, 42), (200, 56, 3)])
]
NFCS = [ 
    Team('Saints', 'NO', [(211, 188, 141), (16, 24, 31)]),
    Team('Falcons', 'ATL', [(167, 25, 48), (0, 0, 0)]),
    Team('Buccaneers', 'TB', [(213, 10, 10), (10, 10, 8)]),
    Team('Panthers', 'CAR', [(0, 133, 202), (16, 24, 32)])
]
NFCW = [ 
    Team('49ers', 'SF', [(170, 0, 0), (173, 153, 93)]),
    Team('Seahawks', 'SEA', [(0, 34, 68), (105, 190, 40)]),
    Team('Rams', 'LAR', [(0, 53, 148), (255, 163, 0)]),
    Team('Cardinals', 'ARI', [(151,35,63), (0,0,0)])
]
# AFC
AFCE = [
    Team('Bills', 'BUF', [(0, 51, 141), (198, 12, 48)]),
    Team('Patriots', 'NE', [(0, 34, 68), (198, 12, 48)]),
    Team('Dolphins', 'MIA', [(0, 142, 151), (252, 76, 2)]),
    Team('Jets', 'NYJ', [(18, 87, 64), (0, 0, 0)])
]
AFCN = [ 
    Team('Steelers', 'PIT', [(16, 24, 32), (255, 182, 18)]),
    Team('Ravens', 'BAL', [(26, 25, 95), (158, 124, 12)]),
    Team('Browns', 'CLE', [(49, 29, 0), (255, 60, 0)]),
    Team('Bengals', 'CIN', [(251, 79, 20), (0, 0, 0)])
]
AFCS = [ 
    Team('Colts', 'IND', [(0, 44, 95), (162, 170, 173)]),
    Team('Texans', 'HOU', [(3, 32, 47), (167, 25, 48)]),
    Team('Titans', 'TEN', [(12, 35, 64), (138, 141, 143)]),
    Team('Jaguars', 'JAX', [(0, 103, 120), (215, 162, 42)])
]
AFCW = [ 
    Team('Chiefs', 'KC', [(227, 24, 55), (255, 184, 28)]),
    Team('Chargers', 'LAC', [(0, 128, 198), (255, 194, 14)]),
    Team('Raiders', 'LV', [(0, 0, 0), (165, 172, 175)]),
    Team('Broncos', 'DEN', [(251, 79, 20), (0, 34, 68)])
]
bigDict = {
    'PHI': NFCE[0], 'WSH': NFCE[1], 'DAL': NFCE[2], 'NYG': NFCE[3],
    'DET': NFCN[0], 'MIN': NFCN[1], 'GB': NFCN[2], 'CHI': NFCN[3],
    'NO': NFCS[0], 'ATL': NFCS[1], 'TB': NFCS[2], 'CAR': NFCS[3],
    'SF': NFCW[0], 'SEA': NFCW[1], 'LAR': NFCW[2], 'ARI': NFCW[3],
    'BUF': AFCE[0], 'NE': AFCE[1], 'MIA': AFCE[2], 'NYJ': AFCE[3],
    'PIT': AFCN[0], 'BAL': AFCN[1], 'CLE': AFCN[2], 'CIN': AFCN[3],
    'IND': AFCS[0], 'HOU': AFCS[1], 'TEN': AFCS[2], 'JAX': AFCS[3],
    'KC': AFCW[0], 'LAC': AFCW[1], 'LV': AFCW[2], 'DEN': AFCW[3]
}

Tables = [
    Standings(NFCE, 'NFC East'),
    Standings(NFCN, 'NFC North'),
    Standings(NFCS, 'NFC South'),
    Standings(NFCW, 'NFC West'),
    Standings(AFCE, 'AFC East'),
    Standings(AFCN, 'AFC North'),
    Standings(AFCS, 'AFC South'),
    Standings(AFCW, 'AFC West')
]
NFC = Standings(NFCE+NFCN+NFCS+NFCW, 'NFC', dset=False)
AFC = Standings(AFCE+AFCN+AFCS+AFCW, 'AFC', dset=False)

# MAKE SCHEDULE
df = pandas.read_excel('NFL/NFL_Schedule_Grid_2023_awh.xlsx')
schedule = []
for weeknum in range(1, 19):
    cur = df[df.week == weeknum]
    slate = []
    for gamenum in range(len(cur)):
        slate.append((bigDict[cur.iloc[gamenum, 0]], bigDict[cur.iloc[gamenum, 2]]))
    schedule.append(slate)

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
        NFC.standingsUpdateDIV()
        AFC.standingsUpdateDIV()
        standingsDisplayer(out, Tables[0:4], 'NFC DIVISIONS')
        standingsDisplayer(out, Tables[4:8], 'AFC DIVISIONS')
        standingsDisplayer(out, [NFC, AFC], 'CONFERENCE STANDINGS')
    #Tournament
    playoffs = ( # SUPER BOWL
        noneRemover(unseeder(list(AFC.df.iloc[:7, 0]))), 
        noneRemover(unseeder(list(NFC.df.iloc[:7, 0])))
    )
    playoffPlayer(out, playoffs, [1, 1, 1, 1], [True, False, False, False], ends=ends, rocks=rocks)


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
    checkpoint(f'{matchups} WINS THE SUPER BOWL', out = out)