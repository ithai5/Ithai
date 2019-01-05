# On this program you can play "Rock Scissors Paper".
# in the start you should choose how many rounds would you like to play
# Enjoy!

import random


moves = ['rock', 'paper', 'scissors']


class Player:
    def human_player(self):
        human_move = input('Choose your weapon: ').lower()
        while human_move not in moves:
            human_move = input('Typing mistake, please try again: ').lower()
        return human_move


class RockCpu:
    def move(self):
        return "rock"


class RandomCpu:
    def move(self):
        return random.choice(moves)


class ReflectCpu:
    def move(self, list):
        # last player move
        try:
            return list[-1][1]
        except Exception:
            return RandomCpu.move(self)


class CycleCpu:
    def move(self, round_history):
        # last computer moves
        try:
            last_move = round_history[-1][2]
            if last_move == 'rock':
                return 'paper'
            elif last_move == "paper":
                return 'scissors'
            else:
                return 'rock'
        except Exception:
            return RandomCpu.move(self)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self, computer):
        human = self.p1.human_player()
        print(f"Player 1: {human}  Computer: {computer}")
        if beats(human, computer):
            print("Player 1 wins")
            self.p1_score += 1
            return ["player",  human, computer]
        elif beats(cpu, human):
            print("Computer Wins")
            self.p2_score += 1
            return ["cpu", human, computer]
        else:
            print("It's a tie")
            return ["tie", human, computer]

    def play_game(self):
            round_history = []
            # saving the history of the game in case
            # that I would like to make others strategies
            game_style = input("which style would you like to play against?\n"
                               "[any type]- Random Computer "
                               "  [1]- Always Rock\n"
                               "[2]- Reflect Computer"
                               "                   [3]- Cycle Computer\n")
            rounds = input('How many rounds would you like to play? ')
            while type(rounds) is not int:
                try:
                    rounds = int(rounds)
                except Exception:
                    rounds = input('Type a number please ')
            print('Game start!')
            for round in range(rounds):
                if game_style == "1":
                    computer = RockCpu.move(self)
                elif game_style == "2":
                    computer = ReflectCpu.move(self, round_history)
                elif game_style == "3":
                    computer = CycleCpu.move(self, round_history)
                else:
                    computer = RandomCpu.move(self)
                print(f' Round {round+1}:')
                round_history.append(self.play_round(computer))
                print(f"You got {self.p1_score} Computer got {self.p2_score}")
            if self.p1_score > self.p2_score:
                print("The winner is YOU")
            elif self.p1_score < self.p2_score:
                print(' The winner is the computer ')
            else:
                print('It is a Tie, play again to see who is the winner!')


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
