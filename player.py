__author__ = 'Ondrej Prenek'


class MyPlayer:
    """ Hrac nejdrive spolupracuje, pote se prizpusobi """


    # class Myplayer can be created with 1 or 2 arguments
    def __init__(self, payoff_matrix, number_of_iterations=0):
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.opponent_move_history = []
        self.playCounter = 0

    # Save opponents move into variable opponent_move
    def record_opponents_move(self, opponent_move=""):
        self.opponent_move = opponent_move

        if self.opponent_move != "":
            self.opponent_move_history.append(self.opponent_move)

    # Method check find out if in array is more defects than num variable
    def defectCheck(self, arr, num):
        if sum(arr) > num:
            return True
        else:
            return False

    #Method "move" returns  a Boolean type
    def move(self):
        bothCoop = self.payoff_matrix[0][0][0] #4
        oppDefect= self.payoff_matrix[0][1][0] #1
        onlyMeDefect = self.payoff_matrix[0][1][1] #6
        bothDefect = self.payoff_matrix[1][1][0] #2
        bigArr = self.opponent_move_history[6:]
        shortArr = self.opponent_move_history

        #Finding out,whether is better to cooperate
        if bothDefect>bothCoop:
            return True
        if bothCoop>=bothDefect and oppDefect>=bothCoop:
            return False
        if bothCoop>bothDefect  and onlyMeDefect>oppDefect:
            ##When num of iters  is  UKNOWN
            if self.number_of_iterations ==0:
                #First round of game/ No opp. move history
                if len(self.opponent_move_history) == 0:
                    return False
                #First round of the game up to seventh round of the game
                if (len(self.opponent_move_history) >= 1) and (len(self.opponent_move_history) < 6):
                    if MyPlayer.defectCheck(self, shortArr, 1):
                        return False
                    return True
                #Seventh round of game and more
                else:
                  while(sum(bigArr)==0):
                    return False
                return True


            ##When num of iterations is KNOWN
            else:
                # while it isn't last iteration(round) of the game
                while self.playCounter != self.number_of_iterations - 1:
                    #First round of game/ No opp. move history
                    if len(self.opponent_move_history) == 0:
                        self.playCounter += 1
                        return False
                    #First round of the game up to seventh round of the game
                    if (len(self.opponent_move_history) >= 1) and (len(self.opponent_move_history) < 6):
                        if MyPlayer.defectCheck(self, shortArr, 1):
                            self.playCounter += 1
                            return True
                        self.playCounter += 1
                        return False
                    #Seventh round of game and more
                    else:
                        while(sum(bigArr)==0):
                            self.playCounter+=1
                            return False
                        self.playCounter+=1
                        return True

                return True
        #When it's last round of the game
        else:
            return True

    def play(self):
        return self.decision
