from player import player
from houses import houses


def main(houses):
    players = [player.copy() for _ in range(3)]
    advence_cards = [i for i in range(10)]
    house_pille_size = len(houses) // len(players)
    houses = tuple(houses[i * house_pille_size:house_pille_size * (1 + i)] for i in range(len(players)))
    while len(advence_cards) > 3 or is_houses_pile_not_empty():
        assigned_phase(players)
        collecting_phase()
        change_first_palce_player(players)
        print(players)

def is_houses_pile_not_empty():
    if 0 in (len(houses_pille) for house__pille in houses):
        return True

def assigned_phase(players):
    corent_player = 0
    len_players = len(players)
    while tribe_members_lefts_to_place(players):
        assigned_tribe_member_to_task(players[corent_player])
        switch_player(corent_player, len_players)

def tribe_members_lefts_to_place(players):
    return sum([player['tribe_members'] for player in players]) > 0

def assigned_tribe_member_to_task(corent_player):
    tribe_members_in_task = choose_task()
    corent_player['tribe_members'] -= tribe_members_in_task

def choose_task():
    return 1    

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
    main(houses)
