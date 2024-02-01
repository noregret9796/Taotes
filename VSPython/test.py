import tabula
from collections import defaultdict
df = tabula.read_pdf('rptReprintPO.pdf', output_format="json", pages='all')
dic = defaultdict(lambda: defaultdict(str))
dic2 = defaultdict(int)
idx = 0
curitem = ""
for page in range(len(df)) :
    for row in range(len(df[page]['data'])) :  #row is list
        if len(df[page]['data'][row]) == 6 :
            #0:quantity/UOM 1:ITEM# 2:Des   3:CS PK 4:Unit Price    5:Extended
            qt = df[page]['data'][row][0]['text']
            uom = qt[-2:]
            qt = qt[:-3]
            item = df[page]['data'][row][1]['text']
            des = df[page]['data'][row][2]['text']
            cs = df[page]['data'][row][3]['text']
            unit = df[page]['data'][row][4]['text']
            ext = df[page]['data'][row][5]['text']
        if len(df[page]['data'][row]) == 7 :
            #0:quantity/UOM 1:ITEM# 2:Des   3:CS PK 4:Unit Price    5:Extended
            qt = df[page]['data'][row][0]['text']
            uom = df[page]['data'][row][1]['text']
            item = df[page]['data'][row][2]['text']
            des = df[page]['data'][row][3]['text']
            cs = df[page]['data'][row][4]['text']
            unit = df[page]['data'][row][5]['text']
            ext = df[page]['data'][row][6]['text']
        if unit == 'TOTAL' :
            dic['sum']['TOTAL'] = ext
        elif qt =='' and item =='' and cs == '' and unit == '' and ext == '' :
            #dic[idx-1]['DESCRIPTION'] += des
            dic[curitem]['DESCRIPTION'] += des
        elif ext != '' :
            curitem = item
            dic[curitem]['QUANTITY'] = qt
            dic[curitem]['UOM'] = uom
            dic[curitem]['ITEM #'] = item
            dic[curitem]['DESCRIPTION'] = des
            dic[curitem]['CS PK'] = cs
            dic[curitem]['UNIT PRICE'] = unit
            dic[curitem]['EXTENDED'] = ext
            dic2[curitem] = cs
            # dic[idx]['QUANTITY'] = qt
            # dic[idx]['UOM'] = uom
            # dic[idx]['ITEM #'] = item
            # dic[idx]['DESCRIPTION'] = des
            # dic[idx]['CS PK'] = cs
            # dic[idx]['UNIT PRICE'] = unit
            # dic[idx]['EXTENDED'] = ext
            # idx += 1
print(dic)
print(dic2)