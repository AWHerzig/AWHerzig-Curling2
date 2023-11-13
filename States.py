from Game import *
# Make the teams

PacificT = [
    Team('Hawaii', 'HI ', [(200, 16, 46), (160, 160, 160)]), # Red, Gray
    Team('Guam', 'GU ', [(199, 27, 53), (0, 139, 232)]), # Red, Light Blue
    Team('Am Samoa', 'AS ', [(13, 133, 214), (189, 16, 33)]), # Light Blue, Red
    Team('N Mar Islands', 'NMI', [(0, 51, 161), (177, 180, 179)]), # Blue, Gray. 
    Team('California', 'CA ', [(0, 132, 61), (181, 129, 80)]), # Green, light brown
    Team('Oregon', 'OR ', [(4, 106, 57), (255, 235, 15)]), # Green, Yellow
    Team('Alaska', 'AK ', [(15, 32, 75), (255, 184, 18)]) # Dark Blue, Yellow
]
SouthwestT = [
    Team('Arizona', 'AZ ', [(191, 10, 48), (62, 192, 204)]), # Red, Light Blue
    Team('New Mexico', 'NM ', [(255, 217, 0), (191, 10, 49)]), # Yellow, Red
    Team('Nevada', 'NV ', [(0, 51, 160), (0, 132, 62)]), # Blue, Green
    Team('Kansas', 'KS ', [(0, 37, 105), (255, 255, 0)]), # Blue, Yellow
    Team('Texas', 'TX ', [(0, 32, 91), (191, 13, 63)]), # Blue, Red
    Team('Oklahoma', 'OK ', [(0, 114, 207), (179, 153, 93)]), # Light Blue, kinda like a yellowy brown
    Team('Utah', 'UT ', [(1, 45, 106), (229, 24, 55)]) # Blue, Red
]
MountainT = [
    Team('Montana', 'MT ', [(0, 42, 134), (255, 219, 15)]), # Blue, Yellow
    Team('Wyoming', 'WY ', [(191, 10, 49), (0, 40, 104)]), # Red, Blue
    Team('Idaho', 'ID ', [(255, 232, 53), (134, 227, 255)]), # Yellow, Light Blue
    Team('North Dakota', 'ND ', [(0, 42, 134), (255, 209, 43)]), # Blue, Yellow
    Team('South Dakota', 'SD ', [(0, 115, 168), (255, 196, 0)]), # Light Blue, Yellow
    Team('Colorado', 'CO ', [(0, 40, 104), (160, 160, 160)]), # Blue, Gray
    Team('Washington', 'WA ', [(0, 132, 88), (255, 214, 32)]) # Green, Yellow
]
MidwestT = [
    Team('Minnesota', 'MN ', [(78, 38, 131), (179, 181, 183)]), # Purple, Gray
    Team('Wisconsin', 'WI ', [(0, 71, 27), (255, 184, 18)]), # Green, Yellow
    Team('Nebraska', 'NE ', [(199, 42, 42), (200, 200, 200)]), # Red, Gray
    Team('Indiana', 'IN ', [(0, 44, 95), (213, 160, 15)]), # Blue, Yellow
    Team('Illinois', 'IL ', [(190, 10, 46), (255, 231, 15)]), # Red, Yellow
    Team('Michigan', 'MI ', [(0, 118, 182), (200, 16, 47)]), # Light Blue, Red
    Team('Iowa', 'IA ', [(10, 31, 98), (216, 0, 36)]) # Blue, Red
]
BibleT = [
    Team('Mississippi', 'MS ', [(194, 31, 50), (234, 171, 34)]), # Red, Yellow
    Team('Louisiana', 'LA ', [(211, 188, 141), (0, 68, 123)]), # Saints, Blue
    Team('Arkansas', 'AR ', [(191, 10, 48), (0, 40, 104)]), # Red, Blue
    Team('Tennessee', 'TN ', [(204, 0, 0), (0, 45, 101)]), # Red, Blue
    Team('Alabama', 'AL ', [(177, 0, 32), (160, 160, 160)]), # Red, Gray
    Team('Kentucky', 'KY ', [(0, 0, 102), (49, 161, 127)]), # Blue, Blue-Green
    Team('Missouri', 'MO ', [(171, 6, 53), (0, 75, 141)]) # Red, Blue
]
SoutheastT = [
    Team('Florida', 'FL ', [(250, 70, 22), (0,48,135)]), # Orange, Blue
    Team('Puerto Rico', 'PR ', [(233, 34, 41), (58, 94, 171)]), # Red, Blue
    Team('US Virgin Isl', 'UVI', [(166, 0, 50), (244, 198, 61)]), # Red, Yellow
    Team('Georgia', 'GA ', [(167, 25, 49), (0, 0, 0)]), # Red, Black
    Team('South Carolina', 'SC ', [(0, 51, 102), (160, 160, 160)]), # Blue, Gray
    Team('North Carolina', 'NC ', [(0, 40, 104), (191, 10, 49)]), # Blue, Red
    Team('Virginia', 'VA ', [(35, 45, 75), (229, 114, 0)]) # UVA blue and orange
]
MidAtlT = [
    Team('Ohio', 'OH ', [(193, 19, 60), (0, 29, 90)]), # Red, Blue
    Team('Pennsylvania', 'PA ', [(0, 0, 0), (255, 184, 18)]), # Black and Gold lol
    Team('New York', 'NY ', [(0, 56, 168), (206, 17, 39)]), # Blue, Red
    Team('Maryland', 'MD ', [(234, 172, 0), (223, 71, 1)]), # Yellow, Orange
    Team('Washington DC', 'DC ', [(232, 27, 58), (160, 160, 160)]), # Red, Gray
    Team('Deleware', 'DE ', [(0, 83, 159), (255, 221, 49)]), # Blue, Yellow
    Team('West Virginia', 'WV ', [(0, 55, 118), (160, 160, 160)]) # Blue, Gray
]
NortheastT = [
    Team('Vermont', 'VT ', [(90, 133, 98), (255, 204, 51)]), # Green, Yellow
    Team('New Hampshire', 'NH ', [(0, 42, 134), (239, 175, 14)]), # Blue, Yellow
    Team('Connecticut', 'CT ', [(18, 150, 18), (180, 0, 180)]), # Green, Purple lets get crazy
    Team('Rhode Island', 'RI ', [(160, 160, 160), (254, 199, 0)]), # Gray, Yellow
    Team('Massachusetts', 'MA ', [(0, 131, 72), (230, 165, 0)]), # Green, Yellow
    Team('Maine', 'ME ', [(0, 0, 102), (255, 204, 0)]), # Blue, Yellow
    Team('New Jersey', 'NJ ', [(255, 201, 102), (204, 0, 0)]) # like a light yellow, Red
]

Teams = [PacificT, SouthwestT, MountainT, MidwestT, BibleT, SoutheastT, MidAtlT, NortheastT]

Tables = [
    Standings(PacificT, 'Pacific'),
    Standings(SouthwestT, 'Southwest'),
    Standings(MountainT, 'Mountain'),
    Standings(MidwestT, 'Midwest'),
    Standings(BibleT, 'Bible'),
    Standings(SoutheastT, 'Southeast'),
    Standings(MidAtlT, 'Mid-Atlantic'),
    Standings(NortheastT, 'Northeast')
]

schedule = [[]]*(len(Teams[0]))
for div in Teams:
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

"""
for i in schedule:
    print(schedule.index(i))
    for j in i:
        print(*j)
"""

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
        standingsDisplayer(out, Tables[0:4], 'WESTERN')
        standingsDisplayer(out, Tables[4:8], 'EASTERN')
    #Tournament
    playoffmatchups = ( # No idea if this works
        (
            (
                (Tables[0].df.iloc[0, 0], (Tables[1].df.iloc[1, 0], Tables[1].df.iloc[2, 0])), 
                (Tables[1].df.iloc[0, 0], (Tables[0].df.iloc[1, 0], Tables[0].df.iloc[2, 0]))
            ),
            (
                (Tables[2].df.iloc[0, 0], (Tables[3].df.iloc[1, 0], Tables[3].df.iloc[2, 0])), 
                (Tables[3].df.iloc[0, 0], (Tables[2].df.iloc[1, 0], Tables[2].df.iloc[2, 0]))
            )
        ),
        (
            (
                (Tables[4].df.iloc[0, 0], (Tables[5].df.iloc[1, 0], Tables[5].df.iloc[2, 0])), 
                (Tables[5].df.iloc[0, 0], (Tables[4].df.iloc[1, 0], Tables[4].df.iloc[2, 0]))
            ),
            (
                (Tables[6].df.iloc[0, 0], (Tables[7].df.iloc[1, 0], Tables[7].df.iloc[2, 0])), 
                (Tables[7].df.iloc[0, 0], (Tables[6].df.iloc[1, 0], Tables[6].df.iloc[2, 0]))
            )
        )
    )
    playoffPlayer(out, playoffmatchups, leng = [1, 3, 3, 3, 5], seeded = [True, True, False, False, False], ends=ends, rocks=rocks)


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
                    if seriesLoc[sLeng][gamenum] == 0:
                        rezzies.append(game(pair[0], pair[1], out, finish=2, ends=ends, rocks=rocks))
                    else:
                        rezzies.append(game(pair[1], pair[0], out, finish=2, ends=ends, rocks=rocks))
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
    

