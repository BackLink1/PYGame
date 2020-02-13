class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __gt__(self, other):
    	print(str(index) + '  '+ other.cont[:index])
    for index in range(len(other.cont)+1):1git
    	result = other.cont[:index] + ">" + self.cont
    	result += ">" + other.cont[index:]
    print(result)

spam = SpecialString("fdsfdsfds")
eggs = SpecialString("eggs")
eggs > spam
