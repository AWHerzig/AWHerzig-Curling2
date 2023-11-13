from DirWide import *
# like DirWide2 btw but button specific cuz shit gets funky
# And the startup is here

def buttons(out, title, options, retop=True):
    if len(options) > 8:
        raise ValueError('Can only do 8 buttons at a time')
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                spot = pygame.mouse.get_pos()
                if 100 <= spot[0] <= 900 and 100 <= spot[1] <= 600:
                    run = False
            if event.type == pygame.QUIT:
                pygame.quit()
        out.fill(WhiteC)
        text('Click on option to make selection', (500, 25), 15, out)
        text(title, (500, 75), 32, out)
        #Start Lines
        # Core 4
        pygame.draw.line(out, BlackC, (100, 100), (100, 600))
        pygame.draw.line(out, BlackC, (100, 100), (900, 100))
        pygame.draw.line(out, BlackC, (900, 600), (100, 600))
        pygame.draw.line(out, BlackC, (900, 600), (900, 100))
        # Vertical Splits
        pygame.draw.line(out, BlackC, (300, 100), (300, 600))
        pygame.draw.line(out, BlackC, (500, 100), (500, 600))
        pygame.draw.line(out, BlackC, (700, 100), (700, 600))
        # Horizontal Split
        if len(options) > 4:
            pygame.draw.line(out, BlackC, (100, 350), (900, 350))
        #End Lines
        #Start Text
        for block in range(len(options)):
            text(options[block], (200 + 200*(block%4), 350 if len(options) <= 4 else 175 + 350*(block//4)), 32, out)
        pygame.display.update()
    grid = (spot[0]-100)//200, int(spot[1] > 350) if len(options) > 4 else 0
    ind = grid[0] + 4*grid[1]
    return options[ind] if retop else ind

pygame.init()

out = pygame.display.set_mode(screen)
pygame.display.set_caption('CURLING')
kill = False

checkpoint('WELCOME TO CURLING', (500, 300), 40, out)
leaguePick = buttons(out, 'League Option', ['States', 'MLW'])
