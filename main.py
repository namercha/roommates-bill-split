from room import Bill, Roommate
from reports import PdfReport


amount = float(input("Hello, please enter the bill amount: "))
period = input("What is the billing period? Example: December 2022. ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} live in the house during the billing period? "))

name2 = input("What is the name of the roommate? ")
days_in_house2 = int(input(f"How many days did {name2} live in the house during the billing period? "))

the_bill = Bill(amount, period)
roommate1 = Roommate(name1, days_in_house1)
roommate2 = Roommate(name2, days_in_house2)

print(f"{roommate1.name} pays: ", roommate1.pays(the_bill, roommate2))
print(f"{roommate2.name} pays: ", roommate2.pays(the_bill, roommate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(roommate1, roommate2, the_bill)
