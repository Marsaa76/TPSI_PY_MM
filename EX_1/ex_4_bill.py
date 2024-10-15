from datetime import date  # Import date class to work with today's date

class Bill:
    def __init__(self, client, amount, bill_date):
        self.client = client
        self.amount = amount
        self.bill_date = bill_date

    def display_bill(self):
        return (f"Bill for {self.client}:\n"
                f"Amount: €{self.amount}\n"
                f"Date: {self.bill_date}")

    @classmethod
    def create_bill_with_today(cls, client, amount):
        # Use today's date
        today = date.today().strftime("%Y-%m-%d")
        return cls(client, amount, today)

bill1 = Bill.create_bill_with_today("Ferrero", 5200)
print(bill1.display_bill())

bill2 = Bill.create_bill_with_today("Agenzia delle Entrate", 3500)
print(bill2.display_bill())