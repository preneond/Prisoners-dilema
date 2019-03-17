__author__ = 'Ondrej Prenek'



class MyPlayer:
    ''''''

    # class Myplayer can be created with 1 or 2 arguments
    def __init__(self, payoff_matrix, number_of_iterations=0):
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations

    # Save oponnents move into variable opponent_move
    def record_opponents_move(self, opponent_move):
        self.opponent_move = opponent_move


    def move(self):
        import random
        return random.choice([True,False])

    def play(self):
        return self.decision
