from fpdf import FPDF
import os
import webbrowser


class PdfReport:
    """
    Creates a PDF file that contains data about the roommates (like their names and
    amount due) and the billing period.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        roommate_1_pays = str(round(roommate1.pays(bill, roommate2), 2))
        roommate_2_pays = str(round(roommate1.pays(bill, roommate1), 2))
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("files/house.png", w=30, h=30)

        # Add the title of the page
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Roommates Bill', border=0, align='C', ln=1)

        # Add the billing period label and value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Add the names and due amount of roommates
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=roommate1.name, border=0)
        pdf.cell(w=150, h=25, txt=roommate_1_pays, border=0, ln=1)

        # Add the names and due amount of roommates
        pdf.cell(w=100, h=25, txt=roommate2.name, border=0)
        pdf.cell(w=150, h=25, txt=roommate_2_pays, border=0, ln=1)

        pdf.output(self.filename)
        webbrowser.open("file://" + os.path.realpath(self.filename))
