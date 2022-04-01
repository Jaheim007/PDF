from fpdf import FPDF
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QAbstractItemView
from Widget.pdf import Ui_MainWindow
from Widget.table import PDF
import sqlite3

class AccountPage_PDF(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.register_btn.clicked.connect(self.enregister)
        self.saveuser_btn.clicked.connect(self.usersave)
        self.refresh_btn.clicked.connect(self.refreshitems)
        self.open_pdf_btn.clicked.connect(self.table)
        
    def enregister(self):
        self.stackedWidget.setCurrentWidget(self.page_2)
        self.show()
    
    def usersave(self):  
        if self.cmdp.text() != self.mdp.text():       
            QMessageBox.warning(self, "Error", "Le mot de passe ne correspond pas")
            
            self.nom.clear()
            self.prenom.clear()
            self.email.clear()
            self.mdp.clear()
            self.cmdp.clear()
        
        elif self.nom.text() == "" or  self.prenom.text() == "" or self.email.text() == "":       
            QMessageBox.warning(self, "Error", "Veuillez saisir vos infomations")
            
            self.nom.clear()
            self.prenom.clear()
            self.email.clear()
            self.mdp.clear()
            self.cmdp.clear()
           
        else:
            db = sqlite3.connect("database.db")
            global diction
            
            diction ={
                "nom" : self.nom.text(),
                "prenom": self.prenom.text(), 
                "email": self.email.text(),
                "mdp" : self.mdp.text(),
                "cmdp" : self.cmdp.text()
            }
            
            cursor = db.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS data(
                    Nom text, 
                    Prenom text,
                    Email text,
                    Mdp text,
                    Cmdp text
                )""")
            cursor.execute("INSERT INTO data VALUES(:nom, :prenom, :email, :mdp, :cmdp)", diction)
            db.commit()
            db.close()
            
            self.nom.clear()
            self.prenom.clear()
            self.email.clear()
            self.mdp.clear()
            self.cmdp.clear()
            
            self.stackedWidget.setCurrentWidget(self.page)
            self.show()
    
    def refreshitems(self):      
        opendata = sqlite3.connect("database.db")
        datacursor = opendata.cursor()
        commands = '''SELECT * FROM data'''
        exe = datacursor.execute(commands).fetchall()
   
        
        self.tableWidget.setRowCount(0)
        
        for row_number, row_data in enumerate(exe):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def table(self):
        # dictin ={
        #         "nom" : ["Jason", "Jaheim"],
        #         "prenom": [self.prenom.text()], 
        #         "email": [self.email.text()],
        #         "mdp" : [self.mdp.text()],
        #         "cmdp" : [self.cmdp.text()]
        #     }     
        opendata = sqlite3.connect("database.db")
        datacursor = opendata.cursor()
        commands = '''SELECT * FROM data'''
        exe = datacursor.execute(commands)
        donnes = exe.fetchall()
        for rows in donnes:     
            dictin= {
                "nom": rows[0], 
                "prenom":rows[1], 
                "email" : rows[2], 
                "mdp" : rows[3],
                "cmdpe" : rows[4]
            }
        print(rows)
        # dictin = {"nom" : donnes}
        pdf = PDF()
        pdf.add_page()
        pdf.set_font("Times", size=10)
        
        pdf.create_table(table_data= dictin, title='Liste Des Personnes', cell_width='even')
        pdf.ln()
        pdf.output('test.pdf')  
        
                
    # def openpdf(self): 
    #     diction ={
    #             "nom" : self.nom.text(),
    #             "prenom": self.prenom.text(), 
    #             "email": self.email.text(),
    #             "mdp" : self.mdp.text(),
    #             "cmdp" : self.cmdp.text()
    #     }    
        
    #     pdf = FPDF(orientation='P', unit='mm', format='A4')
    #     pdf.add_page()
    #     pdf.set_font("Arial" ,size=20)  
    #     line_height = pdf.font_size * 2.5
    #     col_width = pdf.epw / 5
    #     for row in diction:    
    #         for data in row: 
    #             pdf.multi_cell(col_width, line_height, data, border=1, ln=3, max_line_height=pdf.font_size)    
    #         pdf.ln(line_height)
    #     pdf.output('test1.pdf','F')        
   
    
       