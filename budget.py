class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0

        for transaction in self.ledger:
            amount = transaction["amount"]
            description = transaction["description"]
            items += f"{description[:23]:23}{amount:7.2f}\n"
            total += amount

        output = title + items + f"Total: {total:.2f}"
        return output


def create_spend_chart(categories):
    total_withdrawals = 0
    category_withdrawals = {}

    for category in categories:
        withdrawals = 0
        for transaction in category.ledger:
            if transaction["amount"] < 0:
                withdrawals -= transaction["amount"]
        total_withdrawals += withdrawals
        category_withdrawals[category.name] = withdrawals

    percentages = {}
    for category, withdrawals in category_withdrawals.items():
        percentage = withdrawals / total_withdrawals * 100
        percentages[category] = int(percentage // 10) * 10

    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3d}| "
        for category in categories:
            if percentages[category.name] >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    max_category_length = max(len(category.name) for category in categories)
    for i in range(max_category_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "
        if i != max_category_length - 1:
            chart += "\n"

    return chart
