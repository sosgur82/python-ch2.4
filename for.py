# for 반복문

a = ['cat', 'dog', 'cow']
for animal in a:
    print(animal)

l = [('둘리', 10), ('마이콜', 20), ('도우넛', 30)]
for t in l:
    print('이름:%s, 나이:%d' % t)

for name, age in l:
    print('이름:{0}, 나이:{1}'.format(name, age))


for i in range(10):
    print(i, end=' ')
else:
    print()

s=0
for i in range(1, 11):
    s+= i
print(s)


#break
for i in range(10):
    if i>5:
        break
else:
    print('else called')
print('done')

# continue
for i in range(10):
    if i <= 5:
        continue

    print(i, end=' ')

else:
    print()

# 역삼각형(중첩 for문)
for i in range(10, 0, -1):
    for j in range(0, i):
        print('*', end='')

    print()

for i in range(10, 0, -1):
    print('*' * i)

# 삼각형
for i in range(0, 10):
    for j in range(0, i+1):
        print('*', end='')

    print()
