#  trim the output into standard

import openpyxl
from shutil import copyfile

pos = "AF"
if __name__ == '__main__':

    file = "heritage.xlsx"
    wb = openpyxl.load_workbook(file)
    sheet = wb.active

    header_row = sheet[1]
    header_dict = {cell.value: cell.column_letter for cell in header_row}
    heritages = [cell.value for cell in sheet['C'][1:]]
    for k, heritage in enumerate(heritages):
        posi = openpyxl.utils.column_index_from_string(pos)
        cell = sheet.cell(row=2 + k, column=posi)
        v = str(cell.value)
        index = v.rfind(":")
        if index != -1:
            letter = v[index - 1]
            # if letter.islower():
            #     print(v, letter)
            # print(v,letter)
            print(letter)
            if letter.islower():
                continue
            cell.value = letter
    wb.save("heritage.xlsx")
    print("fin")
    copyfile("heritage.xlsx", "bak.xlsx")
