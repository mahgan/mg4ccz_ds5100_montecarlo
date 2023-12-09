# mg4ccz_ds5100_montecarlo

## Project Description

In this project includes modules Montecarlo and Montecarlo_test which creates a Die, Game, and Analyzer class that computes analytics for die rolls within games with user-specified parameters and tests it.


## Metadata

Install and import the package montecarlo. Within the package montecarlo is a montecarlo module, which contains the classes necessary. This includes a Die, Game, and Analyzer class. The package also contains unittest classes for each of the three classes, which ensures the classes and their methods are done correctly.


## Synopsis

To import the Die class, you can run "from montecarlo.montecarlo import Die", provided you have installed the montecarlo package. You can call the Die class by making an numpy array of face values, either integers or strings, and putting it in Die() as a parameter. For example, if you had an array of faces called "faces", you would call the Die class with die1 = Die(faces). 

To import the Game class, you can run "from montecarlo.montecarlo import Game", provided you have installed the montecarlo package. You can call the Game class by making a list of dice and putting it in Game() as a parameter. For example, if you had a list of dice called "die1" and "die2, you would call the class with game1 = Game([die1,die2]).

To import the Analyzer class, you can run "from montecarlo.montecarlo import Analyzer", provided you have installed the montecarlo package. You can call the Analyzer class by taking in a Game object as a parameter. For example, if you had a Game called game1, you would call the class with analyzer1 = Analyzer(game1)


## Classes and Methods

Die Class
    __init__(faces)
    change_weight(face,weight)
    roll(nrolls)
    show_state()

Game Class
    __init__(dice)
    play(rolls)
    play_results(form = 'wide')

Analyzer Class
    __init__(game)
    jackpot()
    face_cts_per_roll()
    combination_ct()
    permutation_ct()