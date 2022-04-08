import upAndDown
import unittest

my_db=MyDatabase()

class TestUpAndDown(unittest.TestCase):

    def test_GetByCorrectIndex_CorrectRow(self):
        res=my_db.get(1)
        self.assertEqual(res[1],"test HELLO mad WORLD")
    
    def test_GetByCorrectIndexList_CorrectRows(self):
        res=my_db.get([3,5,7])
        true_answers=[
            ['one two three four filve six','one THREE two FILVE six FOUR'],
            ['in_1','out_1'],
            ['in_3','out_3'],
        ]
        for i in range(3):
            if not list(res.iloc[i])==true_answers[i]:
                self.assertEqual('',' ')
        self.assertEqual('','')


    def test_GetByIncorrectIndex1_ValueError(self):
        with pytest.raises(ValueError):
            res=my_db.get(-141)

    def test_GetByIncorrectIndex2_ValueError(self):
        with pytest.raises(ValueError):
            res=my_db.get(44252552141)
    
    def test_GetByIncorrectIndexList_ValueError(self):
        with pytest.raises(ValueError):
            res=my_db.get([0,4,100000,-41344])


if __name__ == '__main__':
    unittest.main()