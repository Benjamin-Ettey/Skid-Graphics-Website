# import openpyxl as xl
# wb=xl.load_workbook('transaction.xlsx')
# sheet=wb[Sheet1]
# cell=sheet.cell(1, 1)
# print(cell.value)

class Person:
    def __init__(self,names):
        self.names=names

    def name(self):
        print(f'Firstname: {self.names}')

your_name=Person('Benjamin')
print(your_name.name())



