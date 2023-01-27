class payment:
    a = 10
    b = 20
    def __init__(self,price,name):
        self.__price = price
        self.name = name
        print(f'{name} ---> {price}')
        
    def print_discount_mob(self):
        print(f'congratulation you have {payment.a}% OFF')
    
    def print_discount_mat(self):
        print(f'you have {payment.b}% OFF')
        
    def set_fprice(self,discount):
        #discount = OFF \ fprice = final price
        if (discount == 'mobin'):
            self.__price = self.__price - int(self.__price * payment.a/100)
            self.print_discount_mob()
        if (discount == 'matin'):
            self.__price = self.__price - int(self.__price * payment.b/100)
            self.print_discount_mat()
    def get_fprice(self):
        #fprice = final price
        return f'pay --> {self.__price} tomans'
        
chips = payment(12000,'chips')
chips.set_fprice('matin')
print(chips.get_fprice())