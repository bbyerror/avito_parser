
def build_a_link(choises:dict) -> str:
    """linkbuilder_func
    """
    link = 'https://www.avito.ru/'
    location = choises.get('location')
    base = choises.get('base')
    keywords = choises.get('keywoards')
    range_by = choises.get('range_by')

    if location:
        link += location+'/'
    if base:
        link += base
        link += '?cd=1'
    if keywords:
        link += 'q='+'+'.join([i for i in keywords.split()])
    if range_by and range_by in ['cheep', 'date']:
        if range_by == 'cheep':
            link += '&s=1'
        else:
            link += '&s=104'
    return link

'''all_choises={'location':{'all_regions':'all', #локация
                         'moscow': 'moskva',
                         'stPetersburg_i_lo':'sankt_peterburg_i_lo',
                         'sebastopol': 'sevastopol',
                         'rostov': 'rostovskaya_oblast',
                         'krasnodar': 'krasnodar'},
             'base': {'transport': 'transport', #группа товаров   
                      'nedvizhimost': 'nedvizhimost',
                      'job': 'rabota',
                      'uslugi': 'predlozheniya_uslug',
                      'for_home': 'dlya_doma_i_dachi',
                      'electronics': 'bytovaya_elektronika',
                      'noutbuki': 'noutbuki'},         
             'keywoards': '', #ключевые слова
             'range_by':['default','cheep','date']}#способ отображения'''