historical_period = [  # 历史和时期
    'Prehistory',
    'Ancient history',
    'Post-classical history',
    'Modern history',
    # 'Other'
]

culture_type = [  # 文化类型
    'Archaeological Sites',  # 考古学
    'Architectural Heritage',  # 建筑学
    'Historic Urban Heritage',  # 古代城市
    'Cultural Landscapes',  # 文化景观
    # 'Other',
    'Cultural Heritage Sites of Memory'  # 有纪念意义的

]


culture_value = [  # iter 1  文化价值
    'Folk culture',  # 民俗文化
    'ethnic customs',  # 民族风情
    'religious ceremonies'  # 肃穆的宗教仪式
]

cultural_building_type = [  # 建筑类型
    'Building group',  # 建筑群
    'Castle',  # 城堡
    'Church',  # 教堂
    'Residential',  # 住宅
    'Palace',  # 宫殿
    'Municipal building',  # 市政建筑
    # 'Other',
    'Not a building'
]

building_style = [  # 建筑风格
    'Gothic',  # 哥特
    'Renaissance and Baroque',  # 文艺复兴和巴洛克
    # 'Classic',  # 古典
    'Moorish',  # 摩尔
    'Colonial',  # 殖民
    'Buddhist',  # 佛教
    'Modernist',  # 现代
    'Islamic',  # 伊斯兰
    'Cave',  # 洞穴
    # 'Other',
    'Not a building'
]

remain_type = [  # 遗址类型
    'Cemeteries and tombs',  # 墓地和墓穴
    'City ruins',  # 城市遗址
    'Industry ruins',  # 工业遗址
    'Mining sites',  # 矿场遗址
    'Religious sites',  # 宗教遗址
    'Cave sites',  # 洞窟遗址
    # 'Other'
    'Not a remain'
]

landscape = [  # 文化景观类别
    'Agricultural',  # 农业
    "Park",  # 公园和庭院
    "Roads or transport",  # 道路和交通运输
    # 'Other',
    'Not a landscape'
]

problem_sets = {
    "historical_period": historical_period,
    "culture_type": culture_type,
    "building_type": cultural_building_type,
    "building_style": building_style,
    "remain_type": remain_type,
    "landscape": landscape,
}


def gen_cultural_questions(name: str) :
    res = {}
    for k, v in problem_sets.items():
        problem = f"""Please choose one option\
        which can describe the world cultural heritage best from {",".join(v)}\
         These options are：{v}"""
        res[k] = problem
    return res

