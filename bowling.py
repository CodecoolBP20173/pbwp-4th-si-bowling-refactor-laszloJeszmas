def score(game):
    MAX_POINT = 10
    LAST_FRAME = 10
    result = 0
    frame = 1
    in_first_half = True  # I should understan what is this.
    for throw in range(len(game)):
        result += get_value(game[throw])
        if game[throw] == '/':
            result -= last
        if frame < LAST_FRAME and get_value(game[throw]) == MAX_POINT:
            if game[throw] == '/':
                result += get_value(game[throw+1])
            elif game[throw].lower() == 'x':
                if game[throw+2] != '/':
                    result += get_value(game[throw+1])
                result += get_value(game[throw+2])
        frame, in_first_half = first_half(in_first_half, frame, game, throw)
        last = get_value(game[throw])
    return result


def get_value(char):
    if char in map(str, range(1, 10)):
        return int(char)
    elif char.lower() == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()


def first_half(in_first_half, frame, game, throw):
        if in_first_half is False:
            frame += 1
        in_first_half = not in_first_half
        if game[throw].lower() == 'x':
            in_first_half = True
            frame += 1
        return frame, in_first_half
