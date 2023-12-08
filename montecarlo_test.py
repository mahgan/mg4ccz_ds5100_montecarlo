import unittest
import pandas as pd
import numpy as np
from montecarlo import Die


class TestDie(unittest.TestCase):
    def test_init(self):
        faces = np.array([1,2,3,4,5,6])
        die1 = Die(faces)
        self.assertTrue(isinstance(die1.faces,np.ndarray))
        self.assertTrue(isinstance(die1.die_df,pd.DataFrame))

    def test_change_weight(self):
        faces = np.array([1,2,3,4,5,6])
        die1 = Die(faces)
        die1.change_weight(6,3)
        expected = 3
        self.assertEqual(die1.weights[5],expected)

    def test_roll(self):
        faces = np.array([1,2,3,4,5,6])
        die1 = Die(faces)
        expected = 3
        self.assertEqual(len(die1.roll(3)),expected)

    def test_show_state(self):
        faces = np.array([1,2,3,4,5,6])
        die1 = Die(faces)   
        df_copy = die1.show_state()
        self.assertTrue(isinstance(df_copy, pd.DataFrame))



from montecarlo import Game

class TestGame(unittest.TestCase):
    def test_init(self):
        faces = np.array([1,2,3,4,5,6])
        die1 = Die(faces)
        faces2 = np.array([1,2])
        die2 = Die(faces2)
        game1 = Game([die1,die2])
        self.assertTrue(isinstance(game1.dice, list))

    def test_play(self):
        faces = np.array([1,2,3,4,5,6])
        die1 = Die(faces)  
        faces2 = np.array([1,2])
        die2 = Die(faces2)
        game1 = Game([die1,die2])   
        game1.play(6)       
        expected = 6
        self.assertTrue(isinstance(game1.play_results(), pd.DataFrame))
        self.assertEqual(len(game1.play_results()),expected) 

    def test_play_results(self):
        faces = np.array([1,2,3,4,5,6])
        die1 = Die(faces)  
        faces2 = np.array([1,2])
        die2 = Die(faces2)
        game1 = Game([die1,die2])   
        game1.play(6)  
        results = game1.play_results()
        self.assertTrue(isinstance(results, pd.DataFrame))
        expected = list(range(len(game1.dice)))
        self.assertEqual(list(results.columns), expected)



from montecarlo import Analyzer

class TestAnalyzer(unittest.TestCase):
    def test_init(self):
        faces = np.array([1,2,3,4,5,6])
        die1 = Die(faces)  
        faces2 = np.array([1,2])
        die2 = Die(faces2)
        game1 = Game([die1,die2])   
        game1.play(6)  
        analyzer1 = Analyzer(game1)
        self.assertTrue(isinstance(analyzer1, Analyzer))

    def test_jackpot(self):
        faces = np.array([1,2,3,4,5,6])
        die1 = Die(faces)  
        faces2 = np.array([1,2])
        die2 = Die(faces2)
        game1 = Game([die1,die2])   
        game1.play(6)  
        analyzer1 = Analyzer(game1)
        jackpotct = analyzer1.jackpot()
        maxjackpotct = 6
        self.assertTrue(isinstance(jackpotct, int))
        self.assertLessEqual(jackpotct, maxjackpotct)

    def test_face_cts_per_roll(self):
        faces = np.array([1,2,3,4,5,6])
        die1 = Die(faces)  
        faces2 = np.array([1,2])
        die2 = Die(faces2)
        game1 = Game([die1,die2])   
        game1.play(6)  
        analyzer1 = Analyzer(game1)
        face_cts_df = analyzer1.face_cts_per_roll()
        self.assertTrue(isinstance(face_cts_df, pd.DataFrame))

    def test_combination_ct(self):
        faces = np.array([1,2,3,4,5,6])
        die1 = Die(faces)  
        faces2 = np.array([1,2])
        die2 = Die(faces2)
        game1 = Game([die1,die2])   
        game1.play(6)  
        analyzer1 = Analyzer(game1)
        combination_counts_df = analyzer1.combination_ct()
        self.assertTrue(isinstance(combination_counts_df, pd.DataFrame))
        self.assertTrue(isinstance(combination_counts_df.index, pd.MultiIndex))
    
    def test_permutation_ct(self):
        faces = np.array([1,2,3,4,5,6])
        die1 = Die(faces)  
        faces2 = np.array([1,2])
        die2 = Die(faces2)
        game1 = Game([die1,die2])   
        game1.play(6)  
        analyzer1 = Analyzer(game1)
        permutation_counts_df = analyzer1.permutation_ct()
        self.assertTrue(isinstance(permutation_counts_df, pd.DataFrame))
        self.assertTrue(isinstance(permutation_counts_df.index, pd.MultiIndex))





if __name__ == '__main__':
    
    unittest.main(verbosity=3)