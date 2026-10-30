class shopping_list:
    def __init__(self,shopping_list):
        self.shopping_list = shopping_list

    def item_count(self):
        return len(self.shopping_list)

    def total_price(self):
        total = 0
        for price in self.shopping_list.values():
            total += price
        return total