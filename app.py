from Player import Player


def main():
    players = [Player() for _ in range(3)]
    cards = [i for i in range(10)]

    while len(cards) > 3:
        assigned_phase(players)
        collecting_phase()
        change_first_palce_player(players)
        print(players)

def assigned_phase(players):
    corent_player = 0
    len_players = len(players)
    while tribe_members_lefts_to_place(players):
        assigned_tribe_member_to_task(players[corent_player])
        switch_player(corent_player, len_players)

def tribe_members_lefts_to_place(players):
    return sum([player.tribe_members for player in players]) > 0

def assigned_tribe_member_to_task(corent_player):
    tribe_members_in_task = choose_task()
    corent_player.tribe_members -= tribe_members_in_task

def choose_task():
    pass    

def switch_player(corent_player, len_players):
    if corent_player == len_players - 1:
        corent_player = 0

    else:
        corent_player += 1

def collecting_phase():
    pass

def change_first_palce_player(players):
    players.insert(0, players.pop(-1))


if __name__ == '__main__':
    main()