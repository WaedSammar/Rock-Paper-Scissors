import random

moves = ["rock", "paper", "scissors"]


class Player:
    def move(self):
        return "rock"

    def learn(self, move1, move2):
        pass


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Enter your move (rock, paper, or scissors):").lower()
            if move in moves:
                return move
            print("Invalid move! Please try again.")


class RockPlayer(Player):
    def move(self):
        return "rock"


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        self.last = None

    def move(self):
        if self.last is None:
            return random.choice(moves)
        return self.last

    def learn(self, move1, move2):
        self.last = move2


class CyclePlayer(Player):
    def __init__(self):
        self.last = None

    def move(self):
        if self.last is None:
            return random.choice(moves)
        return moves[(moves.index(self.last) + 1) % 3]

    def learn(self, move1, move2):
        self.last = move1


def beats(one, two):
    return (
        (one == "rock" and two == "scissors")
        or (one == "scissors" and two == "paper")
        or (one == "paper" and two == "rock")
    )


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player one: {move1}  Player two: {move2}")
        if beats(move1, move2):
            print("player one win this round!")
            self.score1 += 1
        elif beats(move2, move1):
            print("player tow win this round!")
            self.score2 += 1
        else:
            print("It's a tie")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(
            f"""Score: Player one: {self.score1}
        \nPlayer two: {self.score2}"""
        )
        return True

    def play_game(self):
        print("Game start!")
        s = input("Do you want to play 1 round or 3 rounds? ")
        if s == "3":
            for round in range(3):
                print(f"\nRound {round + 1}: ")
                self.play_round()
        elif s == "1":
            print("\nRound 1: ")
            self.play_round()
        else:
            print("Please choose valid a input :)")
            start()
        print(
            f"""\nFinal Score: Player one: {
              self.score1}\nPlayer tow:{self.score2}"""
        )

        if self.score1 > self.score2:
            print("Player one win the game!")
        elif self.score1 < self.score2:
            print("Player tow win the game!")
        else:
            print("The game is tie!")


def intro():
    print(
        """Welcome in rock paper scissors game
    \nOur game have 1 round or 3 rounds\nWish you the
     best go ahead to the game"""
    )
    print(
        """Do you want to play\n1- Reflect Game\n
    2- Cycle Game\n3- Rock Game\n4- Random Player?"""
    )
    res = input("Please choose 1, 2, 3 or 4: ")
    return res


def start():
    if __name__ == "__main__":
        res = intro()
        if res == "1":
            print("\nTest ReflectPlayer Vs HumanPlayer")
            game = Game(ReflectPlayer(), HumanPlayer())
            game.play_game()
        elif res == "2":
            print("\nTest CyclePlayer Vs HumanPlayer")
            game = Game(CyclePlayer(), HumanPlayer())
            game.play_game()
        elif res == "3":
            print("\nTest RockPlayer Vs HumanPlayer")
            game = Game(RockPlayer(), HumanPlayer())
            game.play_game()
        elif res == "3":
            print("\nTest RandomPlayer Vs HumanPlayer")
            game = Game(RandomPlayer(), HumanPlayer())
            game.play_game()
        else:
            print("Please choose a valid input :)")
            start()


start()
