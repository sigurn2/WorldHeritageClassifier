import asyncio
import time

import openpyxl
import yagmail
from openai import AsyncOpenAI

## iteration1
architecture_style = '''find an appropriate architectural style can summarize this heritage '''
architecture_period = '''find an appropriate architectural period can summarize this heritage '''
architecture_texture = '''Tell me what are the main building materials of this world cultural heritage site'''
architecture_method = '''find an appropriate building method can summarize this heritage'''
architecture_achievement = '''summarize this heritage most important architecture achievement'''
architecture_function = '''find a function from religious, political, or social purposes that can summarize this 
heritage'''
architecture_ornamentation = '''Architecture encompasses the visual and aesthetic qualities of a structure, including 
its colors, textures, ornamentation, and decorative elements. Introduce this heritage's ornamentation'''
architecture_ingenuity = '''architecture within world cultural heritage sites often reflects the 
technological advancements and innovative solutions developed by ancient civilizations. The use of advanced construction
 techniques, sophisticated engineering systems, and artistic craftsmanship demonstrates the ingenuity and technical 
 expertise of the past. summarize this heritage's most important ingenuity '''
# iteration2
architectural_distinct_features = "What are the distinct architectural features of the world cultural heritage site? "
architectural_reflection = "How does the architecture of the site reflect the cultural history and influences of the region?"
architectural_innovation = "Are there any specific indicators of architectural excellence or innovation at the site? "
architectural_reservation = "How has the site's architecture been preserved or restored over time?"
arts_traditional = "What traditional performing arts are associated with the world cultural heritage site?"
arts_reflection = "How do the performing arts at the site reflect the cultural identity and values of the community?"
arts_mastery = "Are there any specific indicators of the performing arts' historical significance or mastery at the site?"
arts_preservation = "How has the site contributed to the preservation and promotion of traditional performing arts?"
arts_tourist = "Do the performing arts at the site attract visitors and contribute to its cultural significance?"
intangible_practices = "What intangible cultural practices or traditions are recognized and celebrated at the world cultural heritage site?"
intangible_contribution = "How does the intangible cultural heritage at the site contribute to the cultural identity and diversity of the community?"
intangible_authenticity = "Are there any specific indicators of the intangible cultural heritage's authenticity or traditional knowledge at the site?"
intangible_safeguarding = "How has the site ensured the safeguarding and transmission of its intangible cultural heritage?"
intangible_role = ("What is the role that the intangible cultural heritage at the site play in its recognition as a "
                   "world cultural heritage?")
traditional_crafts = "What traditional crafts or artisanal skills are associated with the world cultural heritage site? "
traditional_reflection = "How do these traditional crafts showcase the cultural heritage and craftsmanship of the community?"
traditional_uniqueness = "Are there any specific indicators of the quality, uniqueness, or traditional techniques used in the crafts at the site?"
traditional_preservation = "How has the site supported the preservation and promotion of traditional crafts?"
traditional_contribution = "What does the traditional crafts at the site contribute to its recognition as a world cultural heritage?"

problem_set = {
    # "architecture_style": architecture_style,
    # "architecture_period": architecture_period,
    # "architecture_texture": architecture_texture,
    # "architecture_method": architecture_method,
    # "architecture_achievement": architecture_achievement,
    # "architecture_function": architecture_function,
    # "architecture_ornamentation": architecture_ornamentation,
    # "architecture_ingenuity": architecture_ingenuity,
    # iteration2
    # "architectural_distinct_features": architectural_distinct_features,
    # "architectural_reflection": architectural_reflection,
    # "architectural_innovation": architectural_innovation,
    "architectural_reservation": architectural_reservation,
    # "arts_traditional": arts_traditional,
    # "arts_reflection": arts_reflection,
    # "arts_mastery": arts_mastery,
    # "arts_preservation": arts_preservation,
    # "arts_tourist": arts_tourist,
    # "intangible_practices": intangible_practices,
    # "intangible_contribution": intangible_contribution,
    # "intangible_authenticity": intangible_authenticity,
    # "intangible_safeguarding": intangible_safeguarding,
    # "intangible_role": intangible_role,
    # "traditional_crafts": traditional_crafts,
    # "traditional_reflection": traditional_reflection,
    # "traditional_uniqueness": traditional_uniqueness,
    # "traditional_preservation": traditional_preservation,
    # "traditional_contribution": traditional_contribution
}


def architecture_generator():
    return problem_set


async def process_entity(client, text, heritage):
    prompt = f"""
    Your task is to analyze the attributes of world heritage.
    Heritage: ```{heritage}```
    Classify task: ```{text}```
    Output limitations:
    1. Return the most concise answer less than 5 words
    """

    #  removed If you can't find a proper option, provide an answer without quotes.
    prompt = {"role": "user", "content": prompt}
    c = await call_openai(client, prompt)
    answer = c.choices[0].message.content
    return answer.strip('.').lower()


async def process_heritage(client, heritage, header_dict, i, sheet, wb):
    prompts = architecture_generator()
    for attr, prompt in prompts.items():
        answer = await process_entity(client, prompt, heritage)
        # print(f"{i} finished")
        position = header_dict[attr]  # Get the insert position
        position = openpyxl.utils.column_index_from_string(position)
        cell = sheet.cell(row=2 + i, column=position)
        cell.value = answer
        wb.save("heritage.xlsx")


async def call_openai(client, s):
    c = await client.chat.completions.create(
        messages=[s],
        model='gpt-3.5-turbo'
    )
    return c


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
    for i, heritage in enumerate(heritages):
        sort_ = sorts[i]
        if 'cultural' in sort_:
            task = process_heritage(client, heritage, header_dict, i, sheet, wb)
            tasks.append(task)

    await asyncio.gather(*tasks)

    wb.close()
    print("fin")
    yag = yagmail.SMTP(user="sigurn7979@gmail.com", password='1250476871LDQ', host='smtp.gmail.com')
    yag.send(to=['sigurn7979@gmail.com'], subject='FIN', contents=['FIN'])


asyncio.run(main())

