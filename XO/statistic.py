
stat = {
    'Player 1': {
        'Win': 0,
        'Loose': 0},
    'Player 2': {
        'Win': 0,
        'Loose': 0},
    'Computer': {
        'Win': 0,
        'Loose': 0}
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


