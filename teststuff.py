import genestring 

a = genestring.Genestring("RGBYYYGBBGYB")
b = genestring.Genestring("GBRGBYYBYBR")

a.printstring()
b.printstring()

genestring.Genemethods.printoffset(a,b,-3)

print("******************************")

genestring.Genemethods.printoffsetlist(a,b,-3)

a_genelist = [char for char in a.stringrep]
b_genelist = [char for char in b.stringrep]

a_genestring = ''.join(a_genelist)
b_genestring = ''.join(b_genelist)

print('hi')
print(a_genelist)
print(b_genelist)
print(a_genestring)
print(b_genestring)
