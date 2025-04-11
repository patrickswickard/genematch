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
