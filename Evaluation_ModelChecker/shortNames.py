import re

filename = "Spec2.nusmv"
filename2 = "Spec2_short_Names.nusmv"

with open(filename) as f:
    s = f.read()
    s = s.replace('(', '( ')
    s = s.replace(')', ' )')
    # s = s.replace('!', '! ')
    s = s.replace(',', ' , ')

    m = re.findall('(?<= )([a-zA-Z0-9_]+(?:_[a-zA-Z0-9_]+))*(?<! )', s)
    # m = m + re.findall('(?<=,)(?:_[a-zA-Z0-9_]+)*(?<! )', s)
    # m = re.findall('(?<=!)(?:_[a-zA-Z0-9_]+)*(?<! )', s)
    # m = re.findall('(?<= )(?:_[a-zA-Z0-9_]+)*(?<! )', s)


    # m = re.search('/(?<=[ (!\n])[a-zA-Z0-9_]*[_][a-zA-Z0-9_]*(?<![ \n)])/gm', s)


    if m:
        table = dict()
        counter = 0
        m.sort(key = len, reverse = True)

        print('Array Length: ' + str(len(m)))

        for x in m:
            if table.get(x) == None:
                table[x] = counter
                counter = counter + 1
       
        print('Dictionary Length: ' + str(counter))

        for key in table:
            s = s.replace(key, '_' + str(table.get(key)) + '_')

        with open(filename2, 'w') as f2:
            f2.write(s)