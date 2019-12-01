from openpyxl import load_workbook
import os

class getting_credentials:
    def get_values(self):
        excel_path = os.path.join('D:\GitHub\Eko_Mobile_Automation\Config\credentials.xlsx')
        self.wb = load_workbook(excel_path)
        self.sheet_name = self.wb['admin']
        user_name = self.sheet_name['A2'].value
        password = self.sheet_name['B2'].value
        return user_name, password

