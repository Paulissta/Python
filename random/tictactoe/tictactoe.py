__author__ = 'Bruno Santos'


def clear(rows):
    print "\n" * rows


class TileType:
    X = [1, "X"]
    O = [-1, "O"]
    SPACE = [0, " "]

    def __init__(self, _value):
        self.__value = _value

    def getvalue(self):
        return self.__value[0]

    def gettext(self):
        return str(self.__value[1])


class Tile:
    def __init__(self, _value):
        # Set the value of tile
        self.__value = _value

    def __repr__(self):
        # Return the string based in the tile value #
        return str(self.__value.gettext())

    def getvalue(self):
        return self.__value

    def setvalue(self, _value):
        self.__value = _value


class Player:
    __name, __value = None, TileType(TileType.SPACE)

    def __init__(self, _name, _value):
        # Set the player's name e his value
        self.__name = _name
        self.__value = _value

    def __repr__(self):
        # Return the player's name only
        return self.__name

    def getvalue(self):
        return self.__value

    def setvalue(self, _value):
        self.__value = _value

    def getname(self):
        return self.__name

    def setname(self, _name):
        self.__name = _name


class Field:

    __tiles = []

    def __init__(self, tiles):
        # Set the array of tiles
        self.__tiles = tiles

    def __repr__(self):
        # Return the formatted field #
        out = "-" * 25 + "\n"
        for i in range(len(self.__tiles)):
            cols = len(self.__tiles[i])
            for j in range(cols):
                out += "|" + " " * 7
            out += "|\n|"
            for j in range(cols):
                out += " " * 3 + str(self.__tiles[i][j])
                out += " " * 3 + "|"
            out += "\n"
            for j in range(cols):
                out += "|" + " " * 7
            out += "|\n"
            out += "-" * 25 + "\n"
        return out

    def makemove(self, row, col, _value):
        """

        :param row: chosen tile's row
        :param col: chosen tile's column
        :param _value: value to be inserted in tile
        :return: :raise Exception: Throws an exception if don't exist the chosen tile
        """
        try:
            if TileType(TileType.X).getvalue() != self.__tiles[row][col].getvalue()\
                    and TileType(TileType.O).getvalue() != self.__tiles[row][col].getvalue():
                self.__tiles[row][col].setvalue(_value)
                return True
            return False
        except:
            raise Exception("Choice a valid tile!")

    def verifyvictory(self):
        """


        :rtype : int
        """
        for i in range(len(self.__tiles)):
            # Verify if the whole row have the same value #
            if abs(sum(tile.getvalue().getvalue() for tile in self.__tiles[i])) == 3:
                return self.__tiles[i][0].getvalue()
            # Verify if the whole column have the same value #
            for j in range(len(self.__tiles[i])):
                if abs(sum(row[j].getvalue().getvalue() for row in self.__tiles)) == 3:
                    return self.__tiles[0][j].getvalue()
        # Verify if the whole principal diagonal have the same value #
        if abs(sum(self.__tiles[i][i].getvalue().getvalue() for i in range(len(self.__tiles)))) == 3:
            return self.__tiles[0][0].getvalue()
        # Verify if the whole secondary diagonal have the same value #
        if abs(sum(self.__tiles[i][len(self.__tiles) - 1 - i].getvalue().getvalue() for i in range(len(self.__tiles)))) == 3:
            return self.__tiles[0][len(self.__tiles) - 1].getvalue()
        # Return 0 for non-finished game
        return TileType.SPACE


def main():
    # Init the field #
    field = Field([[Tile(TileType(TileType.SPACE)) for j in range(3)] for i in range(3)])

    # Init the players #
    players = [Player(raw_input("Enter the first player's name:\n"), TileType(TileType.X)),
               Player(raw_input("Enter the second player's name:\n"), TileType(TileType.O))]

    turn = 0
    winner = TileType.SPACE

    while turn < 9 and winner == TileType.SPACE:
        # Draw the actual state field #
        print field

        while True:
            try:
                # Subtracts 1 for the correct programming array's row #
                row = int(raw_input("Enter the desired tile's row: ")) - 1

                if row < 1 or row > 3:
                    raise Exception("")

                # Subtracts 1 for the correct programming array's col #
                col = int(raw_input("Enter the desired tile's col: ")) - 1

                if col < 1 or col > 3:
                    raise Exception("")

                break
            except Exception, e:
                print "\nEnter valid numbers!\n"

        try:
            # Verify if is a valid choice #
            if field.makemove(row, col, players[turn % 2].getvalue()):
                try:
                    winner = field.verifyvictory()
                except Exception, e:
                    print "Erro 2: %s" % e.message
                    continue
            else:
                # Alert that is an already chosen tile #
                print "Choice a empty tile!"
                continue
        except Exception, e:
            # Show the "makemove"'s exception #
            print "Erro 1: %s" % e.message
            continue

        clear(20)
        turn = 1 + int(turn)

    print str(field) + "\n"

    for player in players:
        if player.getvalue() == winner:
            print "The winner is %s!!" % player.getname()
            winner = "a"
    if str(winner) != "a":
        print "You tied!!"

main()