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
    file = "back.xlsx"
    wb = openpyxl.load_workbook(file)
    sheet = wb.active

    header_row = sheet[1]
    header_dict = {cell.value: cell.column_letter for cell in header_row}
    target_column = 'S'
    attrs = [cell.value for cell in sheet[target_column][1:]]
    content = f'''
    You are an expert about world heritage
    I will give you a list {attrs}
    You should do my orders step by step
    1. summarize these values and divide them into some abstract types
    2. use a scientific way to merge them into more reasonable types and reduce the redundancy
    3. use a scientific way to merge them into more reasonable types and make sure every option is exclusive, 
    options should be in a slice 
    You should return me a python map, this map contain the full data mapping between original data and the new type
'''
    prompt = {"role": "user", "content": content}
    c = client.chat.completions.create(
        messages=[prompt],
        model='gpt-3.5-turbo'
    )
    print(c.choices[0].message.content)
    print("fin")


