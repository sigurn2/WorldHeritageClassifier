from openai import Client
import openpyxl

attr_list = ["Ancient and Prehistoric Architecture",
             "Classical and European Architectural Styles (includes Renaissance, Baroque, Gothic, Romanesque, Byzantine, Roman)",
             "Islamic and Middle Eastern Architecture",
             "Colonial and Industrial Revolution Architecture",
             "Asian Architectural Styles",
             "South American and Mesoamerican Architecture",
             "Polynesian and Pacific Island Architecture",
             "African and Native American Architecture",
             "Norse and Icelandic Architecture",
             "Art and Cave Paintings"]
pos = "S"
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
        You should choose a appropriate attribute for this heritage: {heritage}
        Your answer is one option, just shut the fuck up and tell me your choice
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
    print("fin")
