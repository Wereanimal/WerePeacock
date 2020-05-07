f = open('./Documentation.md')
translation_table = open('./translate.md', 'w')
import string
tmp = []
i = 0
a = string.ascii_lowercase + string.ascii_uppercase
print(a)
for x in f.readlines()[:51]:
    tmp.append(x[0] + '-' + a[i] + '\n')
    print(i)
    i += 1

translation_table.writelines(tmp)
