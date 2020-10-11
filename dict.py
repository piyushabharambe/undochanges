dict={'Hardware':[11,12,13,14,15,16,17,18,19],
'Software':[21,22,23,24,25,26,27,28,29],
'Electronics':[31,32,33,34,35,36,37,38,39]
}
print(dict)
for i in  dict:
  print(dict[i][4])
for i,j in dict.items():
    print(i,"has",j)