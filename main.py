import asyncio
import os

import openpyxl
from openai import AsyncOpenAI
from tqdm import tqdm


async def call_openai(client, s):
    c = await client.chat.completions.create(
        messages=[s],
        model='gpt-3.5-turbo'
    )
    return c


async def process_entity(client, text):
    prompt = f"""
    Your task is to analyze the attributes of world heritages.
    Classify task: ```{text}```
    Output limitations:
    1. Less than 5 words
    2. 回答最简结果，并且不包含符号，单词首字母大写
    """

    #  removed If you can't find a proper option, provide an answer without quotes.
    prompt = {"role": "user", "content": prompt}
    c = await call_openai(client, prompt)
    answer = c.choices[0].message.content
    return answer.strip('.').lower()


def question_generator(type_: str, name: str) -> dict:
    problems = {}
    if 'cultural' in type_:
        from cultural_prompts import gen_cultural_questions
        problems = gen_cultural_questions(name)
    if 'natural' in type_:
        from natural_prompts import gen_natural_questions
        problems = gen_natural_questions(name)
    if 'mixed' in type_:
        from mix_prompts import gen_mixed_questions
        problems = gen_mixed_questions(name)
    return problems


async def process_heritage(client, heritage, sort_, header_dict, i, sheet, wb):
    prompts = question_generator(sort_, heritage)  # Generate prompts
    for attr, prompt in prompts.items():
        answer = await process_entity(client, prompt)
        # print(f"{i} finished")
        position = header_dict[attr]  # Get the insert position
        position = openpyxl.utils.column_index_from_string(position)
        cell = sheet.cell(row=2 + i, column=position)
        cell.value = answer
        wb.save("heritage.xlsx")


async def main():
    import yaml
    with open('config.yml', 'r') as yaml_file:
        config = yaml.safe_load(yaml_file)
    client = AsyncOpenAI(
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
    sorts = [cell.value for cell in sheet['D'][1:]]

    tasks = []
    for i, heritage in enumerate(tqdm(heritages)):
        sort_ = sorts[i]
        task = process_heritage(client, heritage, sort_, header_dict, i, sheet,wb)
        tasks.append(task)

    await asyncio.gather(*tasks)

    wb.close()


asyncio.run(main())
