class Category:
    name = ''
    name_list = []
    ledger = []
    total_depo = 0
    total_withdraw = 0
    total_balance = 0
    total_transfer = 0
    def __init__(self, nam):
        self.name = nam
        self.name_list.append(self.name)
    def deposit(self, amount, description = False):
        self.total_depo += float(amount)
        if description:
            self.ledger.append({"amount": float(amount), "description": description})
        else:
            self.ledger.append({"amount": float(amount), "description": ""})

    def withdraw(self, amount, description = False):
        if self.check_funds(amount):
            self.total_withdraw += float(amount)
            if self.total_withdraw > self.total_depo:
                self.total_withdraw -= float(amount)
                return False
            else:
                if description:
                    self.ledger.append({"amount": -(float(amount)), "description": description})
                else:
                    self.ledger.append({"amount": -(float(amount)), "description": ""})
                return True

    def get_balance(self):
        self.total_balance = self.total_depo - self.total_withdraw
        return self.total_balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            if category in self.name_list:
                self.total_withdraw += float(amount)
                if self.total_withdraw > self.total_depo:
                    self.total_withdraw -= float(amount)
                    return False
                else:
                    self.ledger.append({"amount": -(float(amount)), "description": f"Transfer to {category.name}"})
                    category.ledger.append({"amount": float(amount), "description": f"Transfer from {self.name}"})
                    return True

    def check_funds(self, amount):
        if amount > self.total_balance:
            return False
        else:
            return True





def create_spend_chart(categories):