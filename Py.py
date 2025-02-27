class computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling price: {}". format(self.__maxprice) )

    def setmaxprice(self,price):
        self.__maxprice = price

computer1 = computer()
computer1.sell()
computer1.__maxprice = 5000
computer1.sell()
computer1.setmaxprice(5000)
computer1.sell()