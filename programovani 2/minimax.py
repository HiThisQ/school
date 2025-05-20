hrac1 = 1
hrac2 = -1

win = 1
lose = -1

max_value = 2
min_value = -2

def maxPlay(odehraneTahy=[], pozadovanySoucet=10, mnozinaTahu=[2,3]):
    if is_terminal(odehraneTahy, pozadovanySoucet):
        return utility(odehraneTahy, pozadovanySoucet, hrac2)
    max_game_value = min_value
    for tah in mnozinaTahu:
        odehraneTahy.append(tah)
        actual_game_value = min_play(odehraneTahy, pozadovanySoucet, mnozinaTahu)
        odehraneTahy.pop()

        if actual_game_value > max_game_value:
            max_game_value = actual_game_value
    return max_game_value



def minPlay(odehraneTahy, pozadovanySoucet, mnozinaTahu):
    if is_terminal(odehraneTahy, pozadovanySoucet):
        return utility(odehraneTahy, pozadovanySoucet, hrac1)
    min_game_value = max_value
    for tah in mnozinaTahu:
        odehraneTahy.append(tah)
        actual_game_value = max_play(odehraneTahy, pozadovanySoucet, mnozinaTahu)

def min_play(odehraneTahy, pozadovanySoucet, mnozinaTahu):
    


def is_terminal(odehraneTahy, pozadovanySoucet):
    if sum(odehraneTahy) >= pozadovanySoucet:
        return True
    else:
        return False

def utility(odehraneTahy, pozadovanySoucet, hralHrac):



