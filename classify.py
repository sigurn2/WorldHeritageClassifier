from openai import Client
import openpyxl
import winsound

attr_list = [
    """ 
A: Preservation of traditional crafts and cultural traditions
B: Cultural significance and recognition
C: Skilled craftsmanship and heritage preservation
D: Unique cultural identity and tradition
E: Artistic expression and significance
F: Contribution to cultural value and recognition
G: Showcasing of cultural heritage
H: Intrinsic cultural significance
I: Unique architectural and artistic value
    """
]
pos = "AS"
if __name__ == '__main__':
    import yaml

    with open('config.yml', 'r') as yaml_file:
        config = yaml.safe_load(yaml_file)
        client = Client(
            api_key=config['credentials']['api_key'],
            base_url="https://api.chatanywhere.com.cn/v1",

            max_retries=3
        )
    file = "heritage.xlsx"
    wb = openpyxl.load_workbook(file)
    sheet = wb.active

    header_row = sheet[1]
    header_dict = {cell.value: cell.column_letter for cell in header_row}
    heritages = [cell.value for cell in sheet['C'][1:]]
    for k, heritage in enumerate(heritages):
        posi = openpyxl.utils.column_index_from_string(pos)
        cell = sheet.cell(row=2 + k, column=posi)
        content = f'''
        You are an expert about world heritage
        I will give you a list {attr_list}
        You should choose a appropriate option for this heritage: {heritage}
        The answer must a simple letter that I gave you
        Example: A
        '''
        prompt = {"role": "user", "content": content}
        c = client.chat.completions.create(
            messages=[prompt],
            model='gpt-3.5-turbo'
        )
        ans = c.choices[0].message.content
        cell.value = ans
        print(ans)
    wb.save("heritage.xlsx")
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    print("fin")
