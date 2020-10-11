x={'key1':1,'key2':3,'key3':2}
y={'key1':1,'key2':2}
for (i,j) in set(x.items())& set(y.items()):
    print(i,":",j,"is present in both x and y")