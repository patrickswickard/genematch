import gene_utils

a = gene_utils.Genestring("RGBYYYGBBGYB")
b = gene_utils.Genestring("GBRGBYYBYBR")

a.printstring()
b.printstring()

gene_utils.Genemethods.printoffset(a,b,-3)

print("******************************")

gene_utils.Genemethods.printoffsetlist(a,b,-3)

a_genelist = [char for char in a.stringrep]
b_genelist = [char for char in b.stringrep]

a_genestring = ''.join(a_genelist)
b_genestring = ''.join(b_genelist)

print('hi')
print(a_genelist)
print(b_genelist)
print(a_genestring)
print(b_genestring)

print('**********************')

def printoffset(a,b,offset):
  offsetstring = ''
  for i in range(abs(offset)):
    offsetstring += '_'
  if offset >=0:
    print(a)
    print(offsetstring + b)
  else:
    print(offsetstring + a)
    print(b)
  print('----------------------------')

for i in range(-3,4):
  printoffset(a_genestring,b_genestring,i)

print(a_genestring[0])

def calcsim(a,b,offset):
  totalmatch = 0
  print('offset is ' + str(offset))
  length_of_a = len(a)
  length_of_b = len(b)
  print(length_of_a)
  print(length_of_b)
  for i in range(0,length_of_a-1):
    a_index = i
    b_index = i + offset
    if a_index >= 0 and a_index < length_of_a and b_index >= 0 and b_index < length_of_b:
      print(str(a_index) + ' a index vs b index ' + str(b_index))
      print(a[a_index] + '---' + b[b_index])
      if a[a_index] == b[b_index]:
        totalmatch += 1
  print('Total matches: ' + str(totalmatch))
  printoffset(a,b,offset)
  return totalmatch

bestoffset = -20
bestmatch = 0
for i in range(-20,20):
  thismatch = calcsim(a_genestring,b_genestring,i)
  if thismatch > bestmatch:
    bestoffset = i
    bestmatch = thismatch

print('Best offset turns out to be ' + str(bestoffset) + ' with ' + str(bestmatch) + ' total matches')
