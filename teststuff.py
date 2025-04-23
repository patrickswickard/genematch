import gene_utils

#a_testvalue = "RGBYYYGBBGYB"
#b_testvalue = "GBRGBYYBYBR"

#a_testvalue = "GYRGRBBYBGBRGBYYBYBR"
#b_testvalue = "GBRGBYYBYBRGBRYRGY"
                
a_testvalue = "GCAGATTCTGTAGTCCTCTA"
b_testvalue = "GTAGTCCTCTAGTACAGC"


a = gene_utils.Genestring(a_testvalue)
b = gene_utils.Genestring(b_testvalue)

a.printstring()
b.printstring()

gene_utils.Genemethods.printoffset(a,b,-3)

#print("******************************")

gene_utils.Genemethods.printoffsetlist(a,b,-3)

a_genelist = [char for char in a.stringrep]
b_genelist = [char for char in b.stringrep]

a_genestring = ''.join(a_genelist)
b_genestring = ''.join(b_genelist)

#print('hi')
#print(a_genelist)
#print(b_genelist)
#print(a_genestring)
#print(b_genestring)

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

#for i in range(-3,4):
#  printoffset(a_genestring,b_genestring,i)

#print(a_genestring[0])




def reverse_string(s):
  """Reverses a string using slicing."""
  return s[::-1]

def complement_string(s):
  """Complements a string using clumsy crappy code, maybe improve this...now with degenerate bases!"""
  newstring = ''
  for i in s:
    match i:
      case 'A':
        newstring += 'T'
      case 'T':
        newstring += 'A'
      case 'C':
        newstring += 'G'
      case 'G':
        newstring += 'C'
      case 'U':
        newstring += 'A'
      case 'W':
        newstring += 'W'
      case 'S':
        newstring += 'S'
      case 'M':
        newstring += 'K'
      case 'K':
        newstring += 'M'
      case 'R':
        newstring += 'Y'
      case 'Y':
        newstring += 'R'
      case 'B':
        newstring += 'V'
      case 'D':
        newstring += 'H'
      case 'H':
        newstring += 'D'
      case 'V':
        newstring += 'B'
      case 'N':
        newstring += 'N'
      case '-':
        newstring += '-'
      case _:
        newstring += '_'
  return newstring

def calcsim(a,b,offset):
  totalmatch = 0
  #print('offset is ' + str(offset))
  length_of_a = len(a)
  length_of_b = len(b)
  #print(length_of_a)
  #print(length_of_b)
  for i in range(0,length_of_a):
    a_index = i
    b_index = i - offset
    if a_index >= 0 and a_index < length_of_a and b_index >= 0 and b_index < length_of_b:
      #print(str(a_index) + ' a index vs b index ' + str(b_index))
      #print(a[a_index] + '---' + b[b_index])
      if a[a_index] == b[b_index]:
        totalmatch += 1
  #print('Total matches: ' + str(totalmatch))
  #printoffset(a,b,offset)
  return totalmatch

def find_best_offset(a_genestring,b_genestring):
  length_of_a_genestring = len(a_genestring) + 1
  length_of_b_genestring = len(b_genestring) + 1
  biggest_possible = max(length_of_a_genestring,length_of_b_genestring)
  b_genestring_reverse = reverse_string(b_genestring)
  b_genestring_complement = complement_string(b_genestring)
  b_genestring_revcomp = reverse_string(complement_string(b_genestring))
  bestoffset = -biggest_possible
  bestmatch = 0
  for i in range(-biggest_possible,biggest_possible):
    thismatch = calcsim(a_genestring,b_genestring,i)
    if thismatch > bestmatch:
      bestoffset = i
      bestmatch = thismatch
  return {"best_offset": bestoffset, "best_match": bestmatch}

b_genestring_reverse = reverse_string(b_genestring)
b_genestring_complement = complement_string(b_genestring)
b_genestring_revcomp = reverse_string(complement_string(b_genestring))

print("Let us do some calculations...")
print("Finding best match for " + str(a_genestring) + ' and ' + str(b_genestring))
solution1 = find_best_offset(a_genestring, b_genestring)
print('Best offset turns out to be ' + str(solution1))
best_offset1= solution1['best_offset']
best_match1= solution1['best_match']
printoffset(a_genestring,b_genestring,best_offset1)

solution2 = find_best_offset(a_genestring, b_genestring_reverse)
print('Best offset in reverse turns out to be ' + str(solution2))
best_offset2= solution2['best_offset']
best_match2= solution2['best_match']
printoffset(a_genestring,b_genestring_reverse,best_offset2)

solution3 = find_best_offset(a_genestring, b_genestring_complement)
print('Best offset in complement turns out to be ' + str(solution3))
best_offset3= solution3['best_offset']
best_match3= solution3['best_match']
printoffset(a_genestring,b_genestring_complement,best_offset3)

solution4 = find_best_offset(a_genestring, b_genestring_revcomp)
print('Best offset in reverse complement turns out to be ' + str(solution4))
best_offset4= solution4['best_offset']
best_match4= solution4['best_match']
printoffset(a_genestring,b_genestring_revcomp,best_offset4)
