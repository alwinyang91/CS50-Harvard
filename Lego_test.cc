#include <iostream>
#include <stdlib.h>
#include <string>
#include <map>
#include <vector>

using namespace std;

/*********************************************************
 * IMPORTANT NOTES:
 * 1) You are not expected to have to read or understand all of this code
 * 2) You may use any existing language features, libraries, etc.
 * 3) You may take time-saving shortcuts - but try to verbally indicate the "proper" way to do it
 * 4) You may ask for help with anything - syntax, available library methods, where in the code X happens, etc.
 * 5) You may compile & run, add print statements, and change things as much as you'd like.
 */



/**
 * The three moves you can throw in Rock, Paper, Scissors.
 * Rock beats scissors.
 * Scissors beats paper.
 * Paper beats rock.
 */
enum RPSMove {
    ROCK,
    SCISSORS,
    PAPER
};

/**
 * Return true iff move A beats move B.
 */
static bool handIsBetter(RPSMove a, RPSMove b) {
    return ((a+1)%3) == b;
}


/**
 * A bot interface for playing Rock, Paper, Scissors.
 */
class Bot {
public:
    virtual ~Bot() {}

    /**
     * An identifier for what type of bot this is.
     */
    virtual string name() const = 0;

    /**
     * Returns this bot's next throw against the current opponent.
     */
    virtual RPSMove makeMove() = 0;

    /**
     * Invoked prior to a series of games with a new opponent.
     */
    virtual void onNewOpponent() {}

    /**
     * Invoked after each hand against an opponent, indicating what move the opponent made.
     */
    virtual void onHandPlayed(RPSMove opponentsMove) {}
};


/**
 * Class for receiving information about what happens during the tournament.
 */
class TournamentObserver {
public:
    virtual ~TournamentObserver() {}

    /**
     * Invoked after a series of games are played between two bots.
     */
    virtual void onGamesPlayed(const Bot& botA, const Bot& botB, int winsA, int winsB) = 0;
};

/**
 * Runs a rock paper scissors tournament between a set of bots.
 */
class Tournament {
public:
    Tournament(vector<Bot*> bots)
        : _bots(std::move(bots)) {
    }

    /**
     * Adds an observer to be notified when events happen in the tournament.
     */
    void addObserver(TournamentObserver* observer) {
        _observers.push_back(observer);
    }

    /**
     * Plays through the tournament, having each bot play against the others in a round-robin format.
     */
    void playTournament() {
        static int numGames = 1000;
        // Go through each unique pair of bots.
        for (size_t i = 0; i < _bots.size(); ++i) {
            for (size_t j = i + 1; j < _bots.size(); ++j) {

                // Play the games.
                pair<int, int> wins = playGames(*_bots[i], *_bots[j], numGames);

                // Send the results to any observers.
                for (auto* observer : _observers) {
                    observer->onGamesPlayed(*_bots[i], *_bots[j], wins.first, wins.second);
                }
            }
        }
    }

private:
    /**
     * Plays a series of games between these two bots, returning how many times each bot won.
     */
    pair<int, int> playGames(Bot& playerA, Bot& playerB, int numGames) {
        pair<int, int> wins;
        playerA.onNewOpponent();
        playerB.onNewOpponent();
        
        for (int i = 0; i < numGames; ++i) {
            RPSMove moveA = playerA.makeMove();
            RPSMove moveB = playerB.makeMove();
            if (handIsBetter(moveA, moveB)) {
                wins.first++;
            } else if (handIsBetter(moveB, moveA)) {
                wins.second++;
            }

            playerA.onHandPlayed(moveB);
            playerB.onHandPlayed(moveA);
        }

        return wins;
    }

    vector<Bot*> _bots;
    vector<TournamentObserver*> _observers;
};

/**
 * Stores and displays the outcome of a tournament - who won, and what happened.
 */
class TournamentResults : public TournamentObserver {
public:

    /**
     * Adds the results of a set of games between two bots to these results.
     * winsA is the number of times botA beat botB.
     * winsB is the number of times botB beat botA.
     */
    void onGamesPlayed(const Bot& botA, const Bot& botB, int winsA, int winsB) override {
        _botWins[botA.name()] += winsA;
        _botLosses[botA.name()] += winsB;
        
        _botWins[botB.name()] += winsB;
        _botLosses[botB.name()] += winsA;
    }

    /**
     * Prints a summary of the tournament results to the console.
     */
    void printToConsole() {
        printf("%20s | %7s | %7s | %4s\n", "Name", "Wins", "Losses", "Overall");
        printf("--------------------------------------------------\n");
        for (const auto& entry : _botWins) {
            auto botName = entry.first;

            printf("%20s | %7d | %7d | %4d\n", botName.c_str(), _botWins[botName], _botLosses[botName], _botWins[botName] - _botLosses[botName]);
        }
    }

private:
    // Stores total wins across the tournament for each bot, by name.
    map<string, int> _botWins;

    // Stores total losses across the tournament for each bot, by name.
    map<string, int> _botLosses;
};

/**
 * A bot that randomly chooses what to play each hand.
 */
class RandomBot : public Bot {
public:
    string name() const override {
        return "RandomBot";
    }
    RPSMove makeMove() override {
        return (RPSMove)(rand() % 3);
    }
};

/**
 * A bot that always picks the same move every hand.
 */
class OneMoveBot : public Bot {
public:
    OneMoveBot(RPSMove move) : _move(move) {
    }

    string name() const override {
        return "OneMoveBot";
    }

    RPSMove makeMove() override {
        return _move;
    }

private:
    RPSMove _move;
};


/**
 * A bot that tracks which hand their opponent has played the most, and plays
 * the hand that will beat that.
 *
 * e.g. if their opponent has played more rock than anything else, it will play paper.
 */
class BasicStatsBot : public Bot {
public:
    string name() const override {
        return "BasicStatsBot";
    }

    RPSMove makeMove() override {
        // Find the most played move.
        RPSMove mostPlayedMove = ROCK;
        int mostPlayedMoveCount = 0;
        for (const auto& cnt : _playedCounts) {
            if (cnt.second > mostPlayedMoveCount) {
                mostPlayedMove = cnt.first;
                mostPlayedMoveCount = cnt.second;
            }
        }

        // Find the counter to the most played move.
        for (int i = 0; i < 3; ++i) {
            if (handIsBetter((RPSMove)i, mostPlayedMove)) {
                // Found the counter, return it.
                return (RPSMove)i;
            }
        }

        throw "This should be impossible!";
    }

    void onNewOpponent() override {
        _playedCounts.clear();
    }

    void onHandPlayed(RPSMove opponentsMove) override {
        _playedCounts[opponentsMove]++;
    }

private:
    map<RPSMove, int> _playedCounts;
};

int main() {
    // Initialize our list of bots.
    RandomBot randomBot;
    OneMoveBot scissorsBot(SCISSORS);
    BasicStatsBot basicStatsBot;

    // Setup our tournament.
    {
        Tournament tourny({&randomBot, &scissorsBot, &basicStatsBot});
        
        // Keep track of results.
        TournamentResults results;
        tourny.addObserver(&results);
        
        // Play the tournament.
        tourny.playTournament();
        
        // Print out the results.
        results.printToConsole();
    }
}
