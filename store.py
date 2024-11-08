from models import Product, User


class Store:
    def __init__(self):
        self.products = dict()
        self.users = list()


    def add_product(self, product, amount=1):
        try :
            self.products[product] = self.products.get(product, 0) + amount
            print(f"'{product}' add to market")
        except :
            print(f"{product} does not added to market!")


    def remove_product(self, product, amount=1):
        if product in self.products :
            if amount <= self.products[product]:
                self.products[product] -= amount
                if self.products[product] == 0 :
                    del self.products[product]
            else:
                print(f"you can not delete '{product}' from market")
        else :
            print(f"'{product}' wan not found in market")


    def add_user(self, username):
        if username in self.users :
            return None
        else :
            self.users.append(username)
            return username
        

    def get_total_asset(self):
        # total_asset = 0
        # for product in self.products.keys() :
        #     price_product = product.price * self.products.values()
        # total_asset += price_product
        # return total_asset

        total_asset = 0
        for product , amount in self.products.items() :
            total_asset += product.price * amount
        return total_asset

    def get_total_profit(self):
        profit = 0
        for product , sold_amount in self.products.items() :
            profit += product.price * sold_amount
            total_profit = self.get_total_asset() - profit
        return total_profit 

    # def get_comments_by_user(self, user):
    #     pass

    # def get_inflation_affected_product_names(self):
    #     pass

    # def clean_old_comments(self, date):
    #     pass

    # def get_comments_by_bought_users(self, product):
    #     pass



store = Store()
product_1 = Product("lobtop" , price=2500 , category="digital")
product_2 = Product("phone" , price=1300 , category="digital")
product_3 = Product("watch" , price=700 , category="digital")

store.add_product(product_1, 2) 
store.add_product(product_2 , 10)
store.add_product(product_3 , 7)

print("----------------------------")
print(store.get_total_asset())
print("----------------------------")

store.remove_product(product_1 , 1)
store.remove_product(product_3 , 4)


# store.add_product("tablet" , 7)
# store.add_product("phone" , 10)
# store.add_product("watch" , 6)
print("----------------------------")
# store.remove_product("loptop" , 3)
# store.remove_product("watch" , 4)
# store.remove_product("TV" , 4)

print(store.get_total_asset())
print("----------------------------")
print(store.get_total_profit())
print("----------------------------")

print(store.products)