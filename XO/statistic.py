plr1win = 0
plr1loo = 0
plr2win = 0
plr2loo = 0
compwin = 0
comploo = 0



stat = {
    'Player 1': {
        'Win': plr1win,
        'Loose': plr1loo},
    'Player 2': {
        'Win': plr2win,
        'Loose': plr2loo},
    'Computer': {
        'Win': compwin,
        'Loose': comploo}
}


def printstat(stat):
    print(f"""
        ----------------------------------
        |           | Победа | Поражения |
        ----------------------------------
        | Игрок 1   |   {stat['Player 1']['Win']}   |     {stat['Player 1']['Loose']}      |
        |--------------------------------|
        | Игрок 2   |   {stat['Player 2']['Win']}   |     {stat['Player 2']['Loose']}      |
        |--------------------------------|
        | Компьютер |   {stat['Computer']['Win']}   |     {stat['Computer']['Loose']}      |
        ----------------------------------

""")


