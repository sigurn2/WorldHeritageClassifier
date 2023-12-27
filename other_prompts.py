#  this prompt is aim to sort natural heritages into three types: tangible, intangible and cultural landscape ( mixin )

def gen_nat_sort(name: str):

    return f'''Which type can describe {name} best? Choose one option from tangible/intangible/cultural landscape
    (cultural landscape is the mix of tangible and intangible), your answer should be few words.
    '''
