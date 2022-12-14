pieces = {
    "Q": {
        "name": "Queen",
        "symbol": "Q",
        "value": 9,
        "jump": False,
        "straight": 8,
        "diagonal": 8,
    },
    "K": {
        "name": "King",
        "symbol": "K",
        "value": 100,
        "jump": False,
        "straight": 1,
        "diagonal": 1,
    },
    "R": {
        "name": "Rook",
        "symbol": "R",
        "value": 5,
        "jump": False,
        "straight": 8,
        "diagonal": 0,
    },
    "B": {
        "name": "Bishop",
        "symbol": "B",
        "value": 3,
        "jump": False,
        "straight": 0,
        "diagonal": 8,
    },
    "N": {
        "name": "Knight",
        "symbol": "N",
        "value": 3,
        "jump": True,
        "straight": 1,
        "diagonal": 2,
        "straight2": 2,
        "diagonal2": 1,
    },
    "P": {
        "name": "Pawn",
        "symbol": "P",
        "value": 1,
        "jump": False,
        "straight": 1,
        "diagonal": 1,
        "first_move": 2,
        "first_move_taken_White": {
            "1": False,
            "2": False,
            "3": False,
            "4": False,
            "5": False,
            "6": False,
            "7": False,
            "8": False,
        },
        "first_move_taken_Black": {
            "1": False,
            "2": False,
            "3": False,
            "4": False,
            "5": False,
            "6": False,
            "7": False,
            "8": False,
        },
    },
}

score = {
    "player_one": 0,
    "player_two": 0,
}

en_passant_check = {
    "en_passant": False,
}

castling_check = {
    "castling": True,
}

player_turn = {
    "player_one": True,
    "count": 0,
    "player_one_check": False,
    "player_two_check": False,
    "memory": [[]],
}