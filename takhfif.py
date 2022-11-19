buy = 100
if buy < 100:
    off = buy * 0.05
    cost = buy - off
    print(f'thats your off: {off:.0f}')
    print(f'you should pay: {cost:.0f} tomans')
elif buy >= 100 and buy < 200:
    off = buy * 0.10
    cost = buy - off
    print(f'thats your off: {off:.0f}')
    print(f'you should pay: {cost:.0f} tomans')
else:
    off = buy * 0.20
    cost = buy - off
    print(f'thats your off: {off:.0f}')
    print(f'you should pay: {cost:.0f} tomans')