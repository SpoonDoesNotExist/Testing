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