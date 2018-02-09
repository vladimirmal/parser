import pymorphy2


def get_form(text):
    morph = pymorphy2.MorphAnalyzer()
    result = morph.parse(text)[0]
    return result.normal_form

print(get_form('do'
               ))