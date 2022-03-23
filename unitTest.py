
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

if __name__ == '__main__':
    unittest.main()