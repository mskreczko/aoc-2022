with open('data.txt', 'r') as f:
    points_for_shape = {
            'X': 1,
            'Y': 2,
            'Z': 3,
    }

    points_for_round_result = {
            'WIN': 6,
            'DRAW': 3,
            'LOSE': 0
    }

    matchups = {
            'A': ['Y', 'X', 'Z'], #[shape_to_win, shape_to_draw, shape_to_lose]
            'B': ['Z', 'Y', 'X'],
            'C': ['X', 'Z', 'Y'],
    }

    lines = f.read().splitlines()
    total = 0
    for ln in lines:
        oponnent_choice, player_choice = ln.split(' ')
        if oponnent_choice == 'A' and player_choice == 'Y':
            total += points_for_shape[player_choice] + points_for_round_result['WIN']
        elif oponnent_choice == 'B' and player_choice == 'Z':
            total += points_for_shape[player_choice] + points_for_round_result['WIN']
        elif oponnent_choice == 'C' and player_choice == 'X':
            total += points_for_shape[player_choice] + points_for_round_result['WIN']
        elif oponnent_choice == 'A' and player_choice == 'X' or oponnent_choice == 'B' and player_choice == 'Y' or oponnent_choice == 'C' and player_choice == 'Z':
            total += points_for_shape[player_choice] + points_for_round_result['DRAW']
        else:
            total += points_for_shape[player_choice] + points_for_round_result['LOSE']
    
    print(total) # part one solution

    total = 0
    for ln in lines:
        oponnent_choice, round_result = ln.split(' ')
        if round_result == 'X':
            total += points_for_shape[matchups[oponnent_choice][2]] + points_for_round_result['LOSE']
        elif round_result == 'Y':
            total += points_for_shape[matchups[oponnent_choice][1]] + points_for_round_result['DRAW']
        else:
            total += points_for_shape[matchups[oponnent_choice][0]] + points_for_round_result['WIN']

    print(total) # part two solution
