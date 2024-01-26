from openai import Client
import openpyxl



target_column = "AS"
target = 'traditional_contribution'



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


    attrs = [cell.value for cell in sheet[target_column][1:]]
    content = f'''
    You are an expert about world heritage
    I will give you a list {attrs}， their theme is {target}
    Limitation: options less than 26
    You should do my orders step by step
    1. summarize these values and divide them into some abstract types
    2. use a scientific way to merge them into more reasonable types and reduce the redundancy
    3. use a scientific way to merge them into more reasonable types and make sure every option is exclusive
    Your answer should like:
    A: Engineering innovation
'''
    prompt = {"role": "user", "content": content}
    c = client.chat.completions.create(
        messages=[prompt],
        model='gpt-3.5-turbo'
    )
    print(c.choices[0].message.content)
    print("fin")


