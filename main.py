import sys 
# from fpdf import FPDF
from PyQt5.QtWidgets import QApplication, QMainWindow
from Widget.resume import AccountPage_PDF
 
def main():
    app = QApplication(sys.argv)
    home = AccountPage_PDF()
    home.show()
    app.exec_()

# def openpdf():     
#     pdf = FPDF(orientation='P', unit='mm', format='A4')
#     pdf.add_page()
#     pdf.output('test.pdf','F')
#     pdf.set_font("Arial", size="20")
#     pdf.text(50,50, txt="Hello World")


if __name__ == '__main__':
    main()
