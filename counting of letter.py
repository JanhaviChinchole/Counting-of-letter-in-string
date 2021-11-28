z="Pune is well known for historical reasons"
d={}
for letter in z:
    if letter not in d.keys():
        d[letter]=1
    else:
        d[letter]=d[letter]+1
print(d)

