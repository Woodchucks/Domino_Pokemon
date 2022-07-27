class Dominos:

    @staticmethod
    def dominos_algorithm(dominos, iterations):
        dominos = list(dominos)

        for iteration in range(iterations):
            dominos_standing_idx = [idx for (idx, item) in enumerate(dominos) if item == "|"][1:-1]
            dominos_to_turn_right_idx = [idx for idx in dominos_standing_idx
                                         if dominos[idx-1] == '/' if dominos[idx+1] != '\\']
            dominos_to_turn_left_idx = [idx for idx in dominos_standing_idx
                                        if dominos[idx+1] == '\\' if dominos[idx-1] != '/']

            for idx in dominos_to_turn_right_idx:
                dominos[idx] = '/'
            for idx in dominos_to_turn_left_idx:
                dominos[idx] = '\\'

        return ''.join(dominos)

    @staticmethod
    def reverse_dominos(dominos, iterations):
        dominos = list(dominos)
        idx_to_stand_up = []

        def stand_up(state):
            for iteration in range(iterations):
                [idx_to_stand_up.append(idx) for (idx, item) in enumerate(dominos)
                    if item == f'{state}' if dominos[idx - 1] == f'{state}' if dominos[idx + 1] != f'{state}']

        stand_up('/')
        stand_up('\\')

        for idx in idx_to_stand_up:
            dominos[idx] = '|'

        return ''.join(dominos)
