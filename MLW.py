from Game import *
# Make the teams

NLt = [
    Team('Eastern Eagles', 'EAS', [(209, 206, 2), (40, 197, 224)]), # Yellow, Light Blue
    Team('Downtown Dbacks', 'DOW', [(158, 158, 108), (0, 0, 0)]), # Beige, Black
    Team('Midwest Mallards', 'MID', [(12, 138, 12), (209, 206, 2)]), # Green, Yellow
    Team('Great Lakes Gators', 'GLG', [(3, 121, 163), (0, 0, 0)]) # Blue, Black (I don't think they ever play in away strip)
]

ALt = [
    Team('Western Wildcats', 'WES', [(60, 2, 92), (160, 160, 160)]), # Purple, Gray
    Team('Pacific Predators', 'PAC', [(0, 0, 0), (255,215,0)]), # Black, Gold
    Team('Coastal Cobras', 'COA', [(150, 8, 8), (40, 197, 224)]), # Red, Light Blue (Never Use it)
    Team('Metro Magic', 'MET', [(133, 2, 173), (40, 197, 224)]) # Like a lighter purple, light blue
]

Teams = [NLt, ALt]

Tables = [Standings(NLt, 'National League'), Standings(ALt, 'American League')]

schedule = [ # I'm just gonna do this the hard way. This is the real 2023 schedule
    [ # SLATE 1
        (NLt[0], NLt[2]), (NLt[2], NLt[0]), (NLt[0], NLt[2]), # EAS v MID
        (ALt[0], ALt[2]), (ALt[2], ALt[0]), (ALt[0], ALt[2]), # WES v COA
        (ALt[1], NLt[1]), (NLt[1], ALt[1]), (ALt[1], NLt[1]), # PAC v DOW
        (ALt[3], NLt[3]), (NLt[3], ALt[3]), (ALt[3], NLt[3])  # MET v GLG
    ],
    [ # SLATE 2
        (NLt[2], ALt[0]), (ALt[0], NLt[2]), (NLt[2], ALt[0]), # MID v WES
        (ALt[2], NLt[3]), (NLt[3], ALt[2]), (ALt[2], NLt[3]), # COA v GLG
        (NLt[1], NLt[0]), (NLt[0], NLt[1]), (NLt[1], NLt[0]), # DOW v EAS
        (ALt[1], ALt[3]), (ALt[3], ALt[1]), (ALt[1], ALt[3])  # PAC v MET
    ],
    [ # SLATE 3
        (NLt[1], NLt[3]), (NLt[3], NLt[1]), (NLt[1], NLt[3]), # DOW v GLG
        (NLt[2], ALt[1]), (ALt[1], NLt[2]), (NLt[2], ALt[1]), # MID v PAC
        (ALt[3], ALt[0]), (ALt[0], ALt[3]), (ALt[3], ALt[0]), # MET v WES
        (NLt[0], ALt[2]), (ALt[2], NLt[0]), (NLt[0], ALt[2])  # EAS v COA
    ],
    [ # SLATE 4
        (NLt[2], NLt[1]), (NLt[1], NLt[2]), (NLt[2], NLt[1]), # MID v DOW
        (NLt[3], NLt[0]), (NLt[0], NLt[3]), (NLt[3], NLt[0]), # GLG v EAS
        (ALt[0], ALt[1]), (ALt[1], ALt[0]), (ALt[0], ALt[1]), # WES v PAC
        (ALt[3], ALt[2]), (ALt[2], ALt[3]), (ALt[3], ALt[2])  # MET v COA
    ],
    [ # SLATE 5
        (NLt[3], NLt[2]), (NLt[2], NLt[3]), (NLt[3], NLt[2]), # GLG v MID
        (NLt[1], ALt[3]), (ALt[3], NLt[1]), (NLt[1], ALt[3]), # DOW v MET
        (ALt[2], ALt[1]), (ALt[1], ALt[2]), (ALt[2], ALt[1]), # COA v PAC
        (ALt[0], NLt[0]), (NLt[0], ALt[0]), (ALt[0], NLt[0])  # WES v EAS
    ]
]

def playit(schedule, out, Tables, ends, rocks):
    for slate in schedule:
        rezzies = []
        for matchup in slate:
            if None not in matchup:
                rezzies.append(game(matchup[0], matchup[1], out, ends=ends, rocks=rocks))
                for div in Tables: # for mlw only cuz in series
                    div.standingsUpdate()
        num = 0
        while num < len(rezzies):
            resultsDisplayer(out, rezzies[num:min(num+12, len(rezzies))])
            num += 12
        standingsDisplayer(out, Tables, f'SLATE {schedule.index(slate)+1}')
    #Tournament
    playoffmatchups = ( 
        (Tables[0].df.iloc[0, 0], (Tables[0].df.iloc[1, 0], Tables[0].df.iloc[2, 0])), 
        (Tables[1].df.iloc[0, 0], (Tables[1].df.iloc[1, 0], Tables[1].df.iloc[2, 0]))
    )
    playoffPlayer(out, playoffmatchups, leng = [3, 3, 5], seeded = [True, True, False], ends=ends, rocks=rocks)


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
    checkpoint(f'{matchups} WINS THE TITLE', out = out)