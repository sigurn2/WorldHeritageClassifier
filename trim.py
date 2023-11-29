import re


def trim_longitude_latitude(s: str):
    pattern = r'([NS]\d{1,2}(?:\.\d+)?\s\d{1,2}(?:\.\d+)?\s\d{1,2}(?:\.\d+)?)\s([EW]\d{1,3}(?:\.\d+)?\s\d{1,2}(?:\.\d+)?\s\d{1,2}(?:\.\d+)?)'
    match = re.search(pattern, s)
    if match:
        return match.group()
    else:
        return 'undefined'


if __name__ == '__main__':
    import openpyxl

    file = "heritage.xlsx"
    wb = openpyxl.load_workbook(file)
    sheet = wb.active
    for cell in sheet['E'][1:]:
        cell.value = trim_longitude_latitude(cell.value)
    wb.save(file)
    wb.close()
