def word(x):
    #تبدیل شمارش ها به دیکشنری
    counts = dict()
    #به هر فاصله که برسه اون رو یه کلمه حساب میکنه
    words = x.split(' ')
    
    for word in words:
        if word in counts:
            #شرط رو چک میکنه اگه کلمه قبلا باشه یدونه به تعداد موجودیتش اضافه میکنه
            counts[word] += 1
        else:
            #شرط رو چک میکنه اگه کلمه قبلا نباشه یدونه به تعداد موجودیتش اضافه میکنه
            counts[word] = 1
    return counts
print(word('dond del me whad do do'))