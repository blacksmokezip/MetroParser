ENCODING = 'utf-8'

TIME_DELAY = 3

CITIES = {
    'moscow': (
        'body > div.dialog-root > div > div > div'
        ' > div.receipt-order > div:nth-child(1)'
        ' > div.pickup > div.pickup__select > div:nth-child(1)'
        ' > div > div.multiselect__content-wrapper'
        ' > ul > li:nth-child(1) > span'
    ),
    'saint_petersburg': (
        'body > div.dialog-root > div > div > div'
        ' > div.receipt-order > div:nth-child(1)'
        ' > div.pickup > div.pickup__select > div:nth-child(1)'
        ' > div > div.multiselect__content-wrapper'
        ' > ul > li:nth-child(23) > span'
    ),
}

ALL_CENTERS = {
    'moscow': {
        'Leningradskaya_71': (
            'body > div.dialog-root > div > div > div > div.receipt-order'
            ' > div:nth-child(1) > div.pickup > div.pickup__select'
            ' > div:nth-child(2) > div > div.multiselect__content-wrapper'
            ' > ul > li:nth-child(1) > span > span'

        ),
        'ProspectMira_211': (
            'body > div.dialog-root > div > div > div > div.receipt-order'
            ' > div:nth-child(1) > div.pickup > div.pickup__select'
            ' > div:nth-child(2) > div > div.multiselect__content-wrapper'
            ' > ul > li:nth-child(2) > span > span'
        ),
        'Doroznaya_1': (
            'body > div.dialog-root > div > div > div > div.receipt-order'
            ' > div:nth-child(1) > div.pickup > div.pickup__select'
            ' > div:nth-child(2) > div > div.multiselect__content-wrapper'
            ' > ul > li:nth-child(3) > span > span'
        ),
        # 'Ryabinova_59': None,
        # 'Dmitrovskoe_165B': None,
        # 'Proshlakova_14': None,
        # 'MKAD_104': (
        #     'body > div.dialog-root > div > div > div > div.receipt-order'
        #     ' > div:nth-child(1) > div.pickup > div.pickup__select >'
        #     ' div:nth-child(2) > div > div.multiselect__content-wrapper'
        #     ' > ul > li:nth-child(7) > span > span'
        # ),
        # 'Shosseinaya_2B': None,
        # 'Moskovskiy_34': None,
        # 'Skladochnaya_1': None,
        # 'Dubrovskaya_13A': None,
        # 'Borovskoe_10A': (
        #     'body > div.dialog-root > div > div > div > div.receipt-order'
        #     ' > div:nth-child(1) > div.pickup > div.pickup__select >'
        #     ' div:nth-child(2) > div > div.multiselect__content-wrapper >'
        #     ' ul > li:nth-child(12) > span > span'
        # ),
    },
    'saint_petersburg': {
        'Comendantskiy_3': (
            'body > div.dialog-root > div > div > div > div.receipt-order'
            ' > div:nth-child(1) > div.pickup > div.pickup__select'
            ' > div:nth-child(2) > div > div.multiselect__content-wrapper'
            ' > ul > li:nth-child(1) > span > span'
        ),
        'Kosygina_4': (
            'body > div.dialog-root > div > div > div > div.receipt-order'
            ' > div:nth-child(1) > div.pickup > div.pickup__select'
            ' > div:nth-child(2) > div > div.multiselect__content-wrapper'
            ' > ul > li:nth-child(2) > span'
        ),
        'Pulkovskoe_23': (
            'body > div.dialog-root > div > div > div > div.receipt-order'
            ' > div:nth-child(1) > div.pickup > div.pickup__select'
            ' > div:nth-child(2) > div > div.multiselect__content-wrapper'
            ' > ul > li:nth-child(3) > span'
        ),
    }
}
