from Game import *

if modePick != '2-player':
    if leaguePick == 'States':
        from States import *
    elif leaguePick == 'MLW':
        from MLW import * 
    elif leaguePick == 'NFL':
        from NFL import *
    elif leaguePick == 'Soccer':
        from Soccer import *
    else:
        raise ValueError('Not built yet')

#game(SouthwestT[0], SouthwestT[2], out = out, view=True) # This is for testing



if modePick == '1-Player':
    divPick = buttons(out, 'Which Division?', [i.name for i in Tables], retop=False)
    teamPick = buttons(out, 'Which Team?', [i for i in Teams[divPick]])
    teamPick.controlled = True
    teamPick.Xacc, teamPick.Yacc, teamPick.Cacc = 0, 0, 0
elif modePick == '2-player':
    if l1 == 'States':
        from States import Tables as Teams1
    elif l1 == 'MLW':
        from MLW import Tables as Teams1
    elif l1 == 'NFL':
        from NFL import Tables as Teams1
    elif l1 == 'Soccer':
        from Soccer import Tables as Teams1
    divPick = buttons(out, 'PLAYER 1 Which Division?', [i.name for i in Teams1], retop=False)
    Team1 = buttons(out, 'PLAYER 1 Which Team?', [i for i in Teams1[divPick].df.Team])
    Team1.controlled = True
    Team1.Xacc, Team1.Yacc, Team1.Cacc = 10, 10, 10
    if l2 == 'States':
        from States import Tables as Teams2
    elif l2 == 'MLW':
        from MLW import Tables as Teams2
    elif l2 == 'NFL':
        from NFL import Tables as Teams2
    elif l2 == 'Soccer':
        from Soccer import Tables as Teams2
    divPick = buttons(out, 'PLAYER 2 Which Division?', [i.name for i in Teams2], retop=False)
    Team2 = buttons(out, 'PLAYER 2 Which Team?', [i for i in Teams2[divPick].df.Team])
    Team2.controlled = True
    Team2.Xacc, Team2.Yacc, Team2.Cacc = 10, 10, 10
else:
    teamPick = 'No team selected'
endsPick = buttons(out, 'How many ends per game?', list(range(1, 9)))
rocksPick = buttons(out, 'How many stones per end?', list(range(1, 9)))
#SouthwestT[2].controlled = True
#game(SouthwestT[3], SouthwestT[2], out, True, 2, 2, finish=1)
#print(leaguePick, modePick, divPick, teamPick, endsPick, rocksPick, sep='\n')
if modePick != '2-player':
    playit(schedule, out, Tables, endsPick, rocksPick)
else:
    game(Team1, Team2, out, True, endsPick, rocksPick)
    checkpoint(f'{Team1 if Team1.wins > 0 else Team2} WINS', out=out)
checkpoint('It Stopped', (500, 300), 40, out)






