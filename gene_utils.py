class Genestring:
  """Class and methods to hold and compute information about a gene string"""

  def __init__(self,stringrep):
    self.stringrep = stringrep
    self.stringlist = stringrep.split()

  def printstring(self):
    """Method to print the original string"""
    print(self.stringrep)

  def printstringlist(self):
    """Method to print the string list"""
    print(self.stringlist)

  def listtostring(a):
    a_as_string = ''.join(a)
    return a_as_string

class Genemethods:
  """Class to compare genestrings etc I guess"""

  def __init__(self):
    self.geneset = set()

  def printoffset(a,b,offset):
    if offset >=0:
      a.printstring()
      print("print " + str(offset) + " spaces before next string")
      b.printstring()
    else:
      print("print " + str(-offset) + " spaces before next string")
      a.printstring()
      b.printstring()
      
  def printoffsetlist(a,b,offset):
    if offset >=0:
      print(a)
      print(b)
    else:
      print(a)
      print(b)
