import os.path
import webbrowser
import os
from fpdf import FPDF
from core_classes import Bill, Flatmate


class pdfReport:
    """
    class that generates the pdf report stating the names of the flatmates,
    the period,and how much each of them has to pay.

    """
    def __init__(self, filename):
        self.filename = filename
    def generate(self, flatmate1, flatmate2, bill):

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        pdf.image("files/house.png",w=30,h=30)
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=3)
        pdf.set_font(family='Times',size=14,style='B')
        pdf.cell(w=100, h=40, txt="Period: ", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate1.pays(bill,flatmate2),2)), border=0, ln=1)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate2.pays(bill, flatmate1),2)), border=0, ln=1)
        pdf.output(f"files/{self.filename}")
        webbrowser.open('file://'+os.path.realpath(f"files/{self.filename}"))

        #NOTE: os.chdir("files") --> changes the directory of the pdf created to files folder.

a=float(input("enter the bill amount: "))
b=str(input("enter the month and year of the bill "))
c=input("enter name of flatmate1 ")
d=input("enter name of flatmate2 ")
e=int(input(f"enter no of days {c} lived in the house "))
f=int(input(f"enter no of days {d} lived in the house "))
the_bill= Bill(a, b)
flatmate1= Flatmate(name=c, days_in_house=e)
flatmate2= Flatmate(name=d, days_in_house=f)
print(c,"pays: ",flatmate1.pays(the_bill,flatmate2))
print(d,"pays: ",flatmate2.pays(the_bill,flatmate1))
pdf_report=pdfReport(f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1,flatmate2,bill=the_bill)
