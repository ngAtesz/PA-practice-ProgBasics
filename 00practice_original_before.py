import math

s = 7
a = int(s/s)
b = int(s/s)+1
c = int(s/s)+2
d = int(s/s)+3
e = int(s/s)+4
f = int(s/s)+5
g = s
x = [a, b, c, d, e, f, g]  # list from 1 to 7

print('Our list is '+str(s)+' long.')
print('It have the following items: ')
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

k = 0

if x[0]//2 <= 2:
    k += 1
if x[1]//2 <= 2:
    k += 1
if x[2]//2 <= 2:
    k += 1
if x[3]//2 <= 2:
    k += 1
if x[4]//2 <= 2:
    k += 1
if x[5]//2 <= 2:
    k += 1
if x[6]//2 <= 2:
    k += 1

print('From the', str(s), 'items, there is ' + str(k) + ' items which are dividible by 2 maximum 2 times')
