import random
from enum import IntEnum
from abc import ABC, abstractmethod

'''
-------------------------- IMPORTANT NOTES FOR CANDIDATES -------------------------
# 1) You are not expected to have to read or understand all of this code
# 2) You may use any existing language features, libraries, etc.
# 3) You may take time-saving shortcuts - but try to verbally indicate the "proper" way to do it
# 4) You may ask for help with anything - syntax, available library methods, where in the code X happens, etc.
# 5) You may compile & run, add print statements, and change things as much as you'd like.
------------------------------------------------------------------------------------
'''

'''
# The three moves you can throw in Rock, Paper, Scissors.
# Rock beats scissors.
# Scissors beats paper.
# Paper beats rock.
'''
class RPSMove(IntEnum):
    ROCK = 0
    SCISSORS = 1
    PAPER = 2

def handIsBetter(A, B):
    '''Return true iff move A beats move B.'''
    return (A+1)%3 == B


class Bot(ABC):
    '''A bot interface for playing Rock, Paper, Scissors.'''
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod    
    def makeMove(self):
        pass
    
    @abstractmethod
    def name(self):
        pass
    
    def onNewOpponent(self):
        pass
    
    def onHandPlayed(self, opponentsMove):
        pass

    
class randomBot(Bot):
    '''A bot that randomly chooses what to play each hand.'''
    def __init__(self):
        pass
    
    def name(self):
        return 'randomBot'
    
    def makeMove(self):
        selection = random.randint(0, len(RPSMove) - 1)
        action = RPSMove(selection)
        return action

class randomBot_2(Bot):
    '''A bot that randomly chooses what to play each hand.'''
    #20% rock, 30% paper, 50% scissors
    def __init__(self):
        pass
    
    def name(self):
        return 'randomBot_2'
    
    def makeMove(self):
        random_num = random.randint(0, 9)
        if random_num < 2:
            action = RPSMove(0)
        elif 2 <= random_num < 5:
            action = RPSMove(2)
        else:
            action = RPSMove(1)
        # selection = random.randint(0, len(RPSMove) - 1)

        # action = RPSMove(selection)
        return action


class oneMoveBot(Bot):
    '''A bot that always picks the same move every hand.'''
    def __init__(self, move):
        self.move = move
    
    def name(self):
        return 'oneMoveBot'
    
    def makeMove(self):
        action = RPSMove(self.move)
        return action

    
class basicStatsBot(Bot):
    '''
    A bot that tracks which hand their opponent has played the most, and plays the hand that will beat that.
    e.g. if their opponent has played more rock than anything else, it will play paper.
    '''
    def __init__(self):
        pass
    
    def name(self):
        return 'basicStatsBot'
    
    def makeMove(self):
        # Find the most played move.
        mostPlayedMoveCount = 0
        mostPlayedMove = 0
        for k, v in self.playedCounts.items():
            if v > mostPlayedMoveCount:
                mostPlayedMove = k
                mostPlayedMoveCount = v
                        
        # Find the counter to the most played move.
        for i in range(3):
            if handIsBetter(i, mostPlayedMove):
                return RPSMove(i)
    
    def onNewOpponent(self):
        self.playedCounts = {0:0, 1:0, 2:0}
    
    def onHandPlayed(self, opponentsMove):
        self.playedCounts[opponentsMove] += 1

    
class TournamentResults():
    '''Stores and displays the outcome of a tournament - who won, and what happened.'''
    
    def __init__(self, bots):

        keys = [bots[i].name() for i in range(len(bots))]
        self.botWins = dict(zip(keys, [0]*len(bots)))
        self.botLosses = dict(zip(keys, [0]*len(bots)))
        self.botTie = dict(zip(keys, [0]*len(bots)))
    
    def onGamesPlayed(self, botA, botB, winsA, winsB, winsAB):
        '''
        Adds the results of a set of games between two bots to these results.
        winsA is the number of times botA beat botB.
        winsB is the number of times botB beat botA.
        '''
        
        self.botWins[botA.name()] += winsA
        self.botLosses[botA.name()] += winsB
        self.botWins[botB.name()] += winsB
        self.botLosses[botB.name()] += winsA
        self.botTie[botA.name()] += winsAB
        self.botTie[botB.name()] += winsAB
      
    def printToConsole(self):
        '''Prints a summary of the tournament results to the console.'''
        
        print("{:20s} | {:7s} | {:7s} | {:7s} | {:4s}".format("Name", "Wins", "Losses", "Tie", "Overall"))
        print("---------------------------------------------------------------------\n")
        for i in range(len(self.botWins)):
            botName = list(self.botWins.keys())[i]
            print("{:20s} | {:7d} | {:7d} | {:7d} | {:4d}".format(
                            botName, 
                            self.botWins[botName], 
                            self.botLosses[botName], 
                            self.botTie[botName],
                            self.botWins[botName]-self.botLosses[botName]
                            ))

                                               
class Tournament():
    '''Runs a rock paper scissors tournament between a set of bots.'''
    
    def __init__(self, bots):
        self.bots = bots
        
        self.TournamentObserver = TournamentResults(bots)
               
    def _playGames(self, playerA, playerB, play_times): 
        '''Plays a series of games between these two bots, returning how many times each bot won.'''
        
        wins = [0, 0, 0] # [A win, B win]
        playerA.onNewOpponent()
        playerB.onNewOpponent()
        print("---------")
        print(f"{playerA.name()} v.s. {playerB.name()}:")
        # range(1000)
        for i in range(play_times):
            moveA = playerA.makeMove()
            moveB = playerB.makeMove()

            if handIsBetter(moveA, moveB):
                wins[0] += 1
                print(f"{playerA.name()}: A wins")
            elif handIsBetter(moveB, moveA):
                wins[1] += 1
                print(f"{playerB.name()}: B wins")
            else:
                wins[2] += 1
                print(f"Tie")
            
            playerA.onHandPlayed(moveB)
            playerB.onHandPlayed(moveA)

        return wins
         
    def playTournament(self, play_times):
        '''Plays through the tournament, having each bot play against the others in a round-robin format.'''
        
        bot_size = len(self.bots)
        
        # Go through each unique pair of bots.
        for i in range(bot_size):
            for j in range(i+1,bot_size):                
                # Play the games.
                wins = self._playGames(self.bots[i], self.bots[j], play_times)
                # Send the results to any observers.
                self.TournamentObserver.onGamesPlayed(self.bots[i], self.bots[j], wins[0], wins[1], wins[2])
                
        self.TournamentObserver.printToConsole()
        
          
def main():
    play_times_2 = 10
    RandomBot = randomBot()
    OneMoveBot = oneMoveBot(RPSMove.SCISSORS)
    BasicStatsBot = basicStatsBot()
    RandomBot_2 = randomBot_2()

    # Setup our tournament.
    bots = [RandomBot, OneMoveBot, BasicStatsBot, RandomBot_2]
    # tourny = Tournament(bots)
    tourny_2 = Tournament(bots)

    # Play the tournament.
    # tourny.playTournament(play_times)
    tourny_2.playTournament(play_times_2)


    
if __name__ == "__main__":
    main()
