"""
https://projecteuler.net/problem=54
"""
from treys import Card, Evaluator

from src.utils import timer


@timer
def problem54():
    player1_wins = 0
    evaluator = Evaluator()
    with open("p054_poker.txt", "r") as f:
        hands = f.readline()
        while hands:
            hands = [card[0] + card[1].lower() for card in hands.split()]
            player1_hand = [Card.new(card) for card in hands[:5]]
            player2_hand = [Card.new(card) for card in hands[5:]]
            if evaluator.evaluate([], player1_hand) < evaluator.evaluate([], player2_hand):
                player1_wins += 1
            hands = f.readline()
    return player1_wins


if __name__ == "__main__":
    print(problem54())
