class Bill:
    """
    Object that contains the data about a mill, like the total amount and
    the billing period.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Roommate:
    """
    Creates a roommate person who lives in the house and pays their portion
    of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        pass


class PdfReport:
    """
    Creates a PDF file that contains data about the roommates (like their names and
    amount due) and the billing period.
    """

    def __init__(self, filename):
        self.name = filename

    def generate(self, roommate1, roommate2, bill):
        pass
