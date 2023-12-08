# Name:  Mahin Ganesan
# Net UD: mg4ccz

import pandas as pd
import numpy as np

class Die():
    """
    A class that creates a "Die" object, or any variable with n results and weights 
    for each result that can a numeric or character value. The object can be fair, with 
    equal weights, or unfair, with unequal weights and the object can be "rolled" many times.
    """
    def __init__(self,faces):
        """
        Initializes the class, taking an array of faces as a parameter, 
        raises an error if input is not an array or if there are 
        duplicate values in the array. Initializes weights to be 1.0 
        and saves weights and faces in a data frame.
        """
        if not isinstance(faces,np.ndarray):
            raise TypeError("Input is not a numpy array.")
        if len(faces) != len(np.unique(faces)):
            raise ValueError("Duplicate values in array.")
        self.faces = faces
        self.weights = np.ones_like(faces,dtype=float)
        self.die_df = pd.DataFrame(self.weights,index=self.faces)

    def change_weight(self,face,weight):
        """
        Changes the weight of a single face based on an inputted face and weight value.
        Raises an error if the value is not a face in the array or if value is not numeric.
        """
        if face not in self.faces:
            raise IndexError("Face value not found.")
        if not isinstance(weight, (int, float)):
            raise TypeError("Input is not an numeric value.")
        self.die_df.loc[face,0] = weight
    def roll(self,nrolls=1):
        """
        Rolls the die object, default is one roll. Returns a list of the 
        outcomes of the roll.
        """
        probs = self.weights/sum(self.weights)
        outcomes = np.random.choice(self.faces,nrolls,p=probs)
        return outcomes
    def show_state(self):
        """
        Returns a copy of the die data frame with faces and weights for each face.
        """
        return self.die_df.copy()


class Game():
        """
        Creates the Game class, which takes in one or more dice and rolls the dice
        based on the form of the Game (number of rolls) using the play function.
        """
        def __init__(self,dice):
            """
            Takes in one parameter, a list of dice and creates a private
            data frame to store the results of playing a Game.
            """
            self.dice = dice
            self.play_result_wide_df = pd.DataFrame()
        def play(self,rolls):
            """
            Rolls the dice a given number of times and saves the result in 
            a data frame.
            """
            roll_df = {}
            for i,die in enumerate(self.dice):
                roll_df[i] = die.roll(rolls)
            self.play_result_wide_df = pd.DataFrame(roll_df)
        def play_results(self,form = 'wide'):
            """
            Shows the results of the play method in either a wide or narrow form
            and raises an error if the input provided is not either of these two.
            """
            if form != 'wide' and form != 'narrow':
                raise ValueError("Invalid Option, must use between forms narrow and wide.")
            elif form == 'wide':
                return self.play_result_wide_df.copy()
            else:
                narrow_play_result_df = pd.DataFrame(self.play_result_wide_df.unstack().reset_index())
                narrow_play_result_df.columns = ['Die Number', 'Roll Number', 'Outcomes']
                narrow_play_result_df = narrow_play_result_df[['Roll Number','Die Number','Outcomes']]
                return narrow_play_result_df
            

class Analyzer():
        """
        Uses the results of a game to conduct different analyses on the game's results.
        """
        def __init__(self,game):
            """
            Takes a Game as an input and throws an error if the object provided is not 
            a Game object. Gets the results of the game.
            """
            if not isinstance(game, Game):
                raise ValueError("Value provided is not a Game object.")
            self.game = game
            self.game_results = game.play_results()
        def jackpot(self):
            """
            Calculates the number of times a roll had all the same faces and
            returns this number as an integer.
            """
            jackpotct = 0
            for r in range(len(self.game_results)):
                roll = self.game_results.iloc[r]
                isJackpot = True
                lastDie = roll.iloc[0]
                for i in range(len(roll)):
                    die = roll.iloc[i]
                    if die != lastDie:
                        isJackpot = False
                        break
                    lastDie = die
                if isJackpot:
                    jackpotct += 1 
            return jackpotct   
        
        def face_cts_per_roll(self):
            """
            Returns a data frame with number of times each face was rolled 
            in a Game.
            """
            face_cts = []
            for val in range(len(self.game_results)):
                face_counts = self.game_results.iloc[val].value_counts()
                face_cts.append(face_counts)
            return pd.DataFrame(face_cts, index=range(1, len(self.game_results) + 1)).fillna(0).astype(int)
                              
        def combination_ct(self):
            """
            Returns a data frame of the number of occurrences of each unique set of faces rolled
            based on a Game.
            """
            countSets = {}
            for r in range(len(self.game_results)):
                #print(self.game_results.iloc[r])
                roll = self.game_results.iloc[r]
                newSet = tuple()
                for i in range(len(roll)):
                    dieval = roll.iloc[i]
                    newSet += (dieval,)
                    # print("newSet", newSet)
                    # print("dieval ", dieval, " for roll: ", r)
                combination = tuple(sorted(list(newSet)))
                # print("combination for roll: ", r, combination)
                if combination in countSets:
                    countSets[combination] += 1
                else:
                    countSets[combination] = 1

            df = pd.DataFrame.from_dict(countSets, orient='index', columns=['Count'])
            df.index = pd.MultiIndex.from_tuples(df.index)
            #print(countSets)
            #print(df)

            return df
        
        def permutation_ct(self):
            """
            Returns a data frame of the number of occurrences of each unique set of faces rolled
            in the order they were rolled in based on a Game.
            """           
            countSets = {}
            for r in range(len(self.game_results)):
                #print(self.game_results.iloc[r])
                roll = self.game_results.iloc[r]
                combination = tuple()
                for i in range(len(roll)):
                    dieval = roll.iloc[i]
                    combination += (dieval,)
                if combination in countSets:
                    countSets[combination] += 1
                else:
                    countSets[combination] = 1

            df = pd.DataFrame.from_dict(countSets, orient='index', columns=['Count'])
            #level_names = [f'Die{i + 1}' for i in range(num_dice)]
            df.index = pd.MultiIndex.from_tuples(df.index)
            #print(countSets)
            #print(df)

            return df
                

