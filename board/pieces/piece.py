class Piece:
    def __init__(self, is_white):
        self.is_white = is_white

    def print_symbol(self):
        if self.is_white:
            return self.symbol.upper()
        return self.symbol