class Bill:
    """
    object that contains data abt bill i.e. total amt,period of bill
    """
    def __init__(self, amount, period):
        self.amount=amount
        self.period=period


class Flatmate:
    """
    Creates flatmate persons who lives in the flat and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name
    def pays(self, bill,flatmate2):
        weight=self.days_in_house/(self.days_in_house+flatmate2.days_in_house)
        to_pay=round(bill.amount*weight)
        return to_pay