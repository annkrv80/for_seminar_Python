data = set('привет любимая')
my_dictcomp = {i: ord(i) for i in data}
print(my_dictcomp)
dict_iter = iter(my_dictcomp.items())
for _ in range(5):
    print(next(dict_iter))
