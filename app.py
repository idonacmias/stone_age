


def main():
    players = [0,1,2]
    cards = [i for i in range(10)]

    while len(cards) > 3:
        assigned_phase()
        collecting_phase()
        change_first_palce_player(players)
        print(players)

def assigned_phase():
    pass

def collecting_phase():
    pass

def change_first_palce_player(players):
    players.insert(0, players.pop(-1))


if __name__ == '__main__':
    main()