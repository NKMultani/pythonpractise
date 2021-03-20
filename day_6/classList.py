class Mobile:
    def __init__(self, model, price, brand, storageInGb):
        self.model = model
        self.price = price
        self.brand = brand
        self.storageInGb = storageInGb


iphone = Mobile("iphone12pro", 1199.00, "apple", 128)
samsung = Mobile("s10", 559.00, "samsung", 64)
nokia = Mobile("nokia11", 399.00, "nokia", 32)
motorola = Mobile("moto15", 485.00, "moto", 16)

mobiles = [iphone, samsung, nokia, motorola]


for mobile in mobiles:
    print(mobile.model)
    print(mobile.price)
    print(mobile.brand)
    print(mobile.storageInGb)
    print("--------------------")



