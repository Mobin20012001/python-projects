c1 = 0
c2 = 0
for i in range(5):
    a = int(input('insert number 1 or 2: '))

    if a == 1:
        c1 = c1 + 1
    if a == 2:
        c2 = c2 + 1
    print(f'"number {i + 1}')
print(f'amir {c1}')
print(f'mosi {c2}')
