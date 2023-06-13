from player import player
from houses import houses
from bord import bord



def main(houses, number_of_players):
    players = [player.copy() for _ in range(number_of_players)]
    civilization_cards = [i for i in range(10)]
    house_pille_size = len(houses) // number_of_players
    houses = tuple(houses[i * house_pille_size:house_pille_size * (1 + i)] for i in range(number_of_players))
    print(houses)
    
    while len(civilization_cards) > 3 and is_pile_full(houses):
        assigned_phase(players, number_of_players)
        collecting_phase()
        feeding_phase()
        change_first_palce_player(players)
        print(houses[1].pop())

def is_pile_full(houses):
    if [] not in houses:
        return True

def assigned_phase(players,number_of_players):
    corent_player = 0
    while tribe_members_lefts_to_place(players):
        assigned_tribe_member_to_task(players[corent_player])
        switch_player(corent_player, number_of_players)

def tribe_members_lefts_to_place(players):
    return sum([player['tribe_members'] for player in players]) > 0

def assigned_tribe_member_to_task(corent_player):
    tribe_members_in_task = choose_task()
    corent_player['tribe_members'] -= tribe_members_in_task

def choose_task():
    tasks = {'oction house':None,
             'oction civilization_card':None,
             'gather resources':None,
             'buy_huose':None}
    return 1    

def switch_player(corent_player, number_of_players):
    if corent_player == number_of_players - 1:
        corent_player = 0

    else:
        corent_player += 1

def collecting_phase():
    pass

def feeding_phase():
    pass

def change_first_palce_player(players):
    players.insert(0, players.pop(-1))


if __name__ == '__main__':
    main(houses, number_of_players=2)
