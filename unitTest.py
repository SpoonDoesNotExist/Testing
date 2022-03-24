
class UpAndDown:

  def __compare(self, a,b,rule):
    a=len(a)
    b=len(b)
    if rule==1:
      return a<=b
    return a>=b


  def arrange(self,string)->str:
    if type(string)!=str:
        return None


    words = string.lower().split()

    if len(words)<2:
      return string

    if len(words[0])>len(words[1]):
      words[0],words[1]=words[1],words[0]


    rule=1

    for i in range(1,len(words)-1):
      if not self.__compare(words[i+1],words[i],rule):
        words[i],words[i+1]=words[i+1],words[i]

      rule=(rule+1)%2

    for i in range(1,len(words),2):
      words[i]=words[i].upper()

    return " ".join(words)

up_down=UpAndDown()

import unittest


class TestUpAndDown(unittest.TestCase):

    def test_Empty_EmptyReturned(self):
        res=up_down.arrange("")
        self.assertEqual(res,"")

    def test_OneWord_OneWordLowerReturned(self):
        self.assertEqual(up_down.arrange("hello"),"hello")

    def test_LongShort_ShortLongReturned(self):
        self.assertEqual(up_down.arrange("hello world"),"hello WORLD")

    def test_MoreThan2Words_EveryEvenLowerReturned(self):
        self.assertEqual(up_down.arrange("hello test mad world"),"test HELLO mad WORLD")

    def test_EqualLength_InitialOrderReturned(self):
        self.assertEqual(up_down.arrange("hello tests world"),"hello TESTS world")

    def test_NotAString_NoneReturned(self):
        self.assertEqual(up_down.arrange(1),None)

    def test_ManyWords1_CorrectUpAndDownReturned(self):
        self.assertEqual(up_down.arrange("one two three four filve six"),"one THREE two FILVE six FOUR")

    def test_ManyWords2_CorrectUpAndDownReturned(self):
        self.assertEqual(up_down.arrange("one two three four filve six seven eight nine ten"),"one THREE two FILVE six SEVEN four EIGHT ten NINE")
    
    def test_ManyWordsWithDigits_CorrectUpAndDownReturned(self):
        self.assertEqual(up_down.arrange("one two three 4 filve 6"),"one THREE 4 FILVE 6 TWO")

    def test_OnlyDigits1_CorrectUpAndDownReturned(self):
        self.assertEqual(up_down.arrange("11 2 33 4 555 6"),"2 11 4 555 6 33")

    def test_OnlyDigits2_CorrectUpAndDownReturned(self):
        self.assertEqual(up_down.arrange("1 2 3 4 5 6 7 8 9"),"1 2 3 4 5 6 7 8 9")

    def test_OnlyDigits3_CorrectUpAndDownReturned(self):
        self.assertEqual(up_down.arrange("1 2 3 4 5 6 7 8 9"),"1 2 3 4 5 6 7 8 9")

    def test_SpecialSymbolsNewLine_CorrectUpAndDownReturned(self):
        self.assertEqual(up_down.arrange("on\n\ne tw\no three\n \nfour"),"e ON o THREE tw FOUR")

    def test_ClosedSingleCommas_CorrectUpAndDownReturned(self):
        self.assertEqual(up_down.arrange("one 'two' 'three' ''"),"one 'THREE' '' 'TWO'")

    def test_SpecialSymbolsOther_CorrectUpAndDownReturned(self):
        self.assertEqual(up_down.arrange("one$ t#wo) ' th@r+e-e &"),"one$ T#WO) ' TH@R+E-E &")

    def test_LargeWords1000000000_CorrectUpAndDownReturned(self):
        size=1000000000
        string=" ".join("w"*size for i in range(5))
        result_string=" ".join(("w" if i%2==0 else "W")*size for i in range(5))
        self.assertEqual(up_down.arrange(string),result_string)

    def test_LargeString100000_CorrectUpAndDownReturned(self):
        size=100000
        string=" ".join("w"*7 for i in range(size))
        result_string=" ".join(("w" if i%2==0 else "W")*7 for i in range(size))
        self.assertEqual(up_down.arrange(string),result_string)

    def test_LargeString100000000_CorrectUpAndDownReturned(self):
        size=100000000
        string=" ".join("w"*7 for i in range(size))
        result_string=" ".join(("w" if i%2==0 else "W")*7 for i in range(size))
        self.assertEqual(up_down.arrange(string),result_string)
    
    def test_DoubleSpace_CorrectUpAndDownReturned(self):
        self.assertEqual(up_down.arrange("one two three  four"),"one THREE two FOUR")

    def test_ManyMultipleSpace_CorrectUpAndDownReturned(self):
        self.assertEqual(up_down.arrange("one     two   three     four five     six"),"one THREE two FOUR six FIVE")

if __name__ == '__main__':
    unittest.main()