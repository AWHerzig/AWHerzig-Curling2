from Game import *


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
else:
    teamPick = 'No team selected'
endsPick = buttons(out, 'How many ends per game?', list(range(1, 9)))
rocksPick = buttons(out, 'How many stones per end?', list(range(1, 9)))
#SouthwestT[2].controlled = True
#game(SouthwestT[3], SouthwestT[2], out, True, 2, 2, finish=1)
#print(leaguePick, modePick, divPick, teamPick, endsPick, rocksPick, sep='\n')
playit(schedule, out, Tables, endsPick, rocksPick)
checkpoint('It Stopped', (500, 300), 40, out)






