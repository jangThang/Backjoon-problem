croatia = input()
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in alphabet:
    croatia = croatia.replace(i, 'C')
print(len(croatia))
