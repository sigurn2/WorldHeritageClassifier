from openai import Client
import openpyxl
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
    target_column = 'S'
    attrs = [cell.value for cell in sheet[target_column][1:]]
    content = f'''
    I will give you a list, please summarize these values and divide them into some abstract types
    {attrs}
    '''
    prompt = {"role": "user", "content": content}
    c = client.chat.completions.create(
        messages=[prompt],
        model='gpt-3.5-turbo'
    )
    print(c.choices[0].message.content)
    print("fin")


