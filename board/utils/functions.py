def pos_to_string(pos):
    row = pos[0]
    col = pos[1]
    return chr(97 + col) + str(row + 1)

def string_to_pos(str):
    letter = str[0]
    digit = int(str[1])
    return (digit - 1, ord(letter) - 97)
