from typing import Tuple, List

natural_type = [
    'Rainforest',  # 雨林
    'Tropical forest',  # 热带森林
    'Grassland',  # 草原
    'Plain',  # 平原
    'Mountain',  # 山脉
    'Highland',  # 高地
    'River',  # 河流
    'Lake',  # 湖泊
    'Island',  # 岛屿
    'Ocean',  # 海洋
    'Wetland',  # 湿地
    # 'Other',
    'Not a ecosystem'
]

natural_geo_type = [
    'Geological Formations',  # 地理运动
    'Canyons and Gorges',  # 峡谷
    'Karst Landscapes',  # 喀斯特
    'Volcanic Landscapes',  # 火山
    'Geothermal Areas',  # 地热区
    # 'Other',
    'Not a geological landscapes'
]

problem_sets = {
    "natural_type": natural_type,
    "natural_geo_type": natural_geo_type
}


def gen_natural_questions(name: str):
    res = {}
    for k, v in problem_sets.items():
        problem = f"""Please choose one option\
        which can describe the world natural heritage best：：{name}\
         These options are：{v}"""
        res[k] = problem
    return res
