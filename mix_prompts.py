from typing import Tuple, List

mixed_type = [
    'Cultural Landscapes with Natural Features',  # 带有自然特色的文化遗产
    'Historical Cities with Surrounding Natural Landscapes',  # 自然环绕的历史建筑
    'Cultural and Natural Heritage within the Same Area',  # 同位的文化自然遗产
    'Cultural and Natural Sites Associated with Historic Events',  # 伴有历史事件的混合遗产
    'Cultural Landscapes with Biodiversity',  # 生物多样性的文化景观
    # 'Other',
    'Historic City Centers with Natural Surroundings'  # 历史悠久的市中心和自然环境
]

problem_sets = {
    "mixed_type": mixed_type
}


def gen_mixed_questions(name: str):
    res = {}
    for k, v in problem_sets.items():
        problem = f"""Please choose one option which can describe the world mixed heritage best：：{name}\
         These options are：{v}"""
        res[k] = problem
    return res
