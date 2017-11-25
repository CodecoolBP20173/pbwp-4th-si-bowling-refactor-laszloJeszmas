def score(game):
    #print(game)
    result = 0
    frame = 1
    in_first_half = True # I should understan what is this.
    for throw in range(len(game)):
        if game[throw] == '/':
            result += get_value(game[throw]) - last
        else:
            result += get_value(game[throw])
        if frame < 10 and get_value(game[throw]) == 10:
            if game[throw] == '/':
                result += get_value(game[throw+1])
            elif game[throw].lower() == 'x':
                if game[throw+2] != '/':
                    result += get_value(game[throw+1])
                result +=  get_value(game[throw+2])

        if in_first_half == False:
            frame += 1
        in_first_half = not in_first_half
        if game[throw].lower() == 'x':
            in_first_half = True
            frame += 1
        last = get_value(game[throw])
    return result


def get_value(char):
    if char in map(str, range(1, 10)):
        return int(char)
    elif char.lower() == 'x' or char == '/': #Is it sure that it won't ever get an error if it want to lower non-alphabetical symbols?
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
