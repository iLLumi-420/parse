with open('text_to_parse.txt', 'r') as file:
    raw_data = file.read()

lines = raw_data.splitlines()

data= [['State', 'Abbre.', 'Postal_Code']]
for line in lines[6:]:

    values = line.split() 

    state = values[0]
    abbr = values[1]
    postal = values[2]

    data.append([state, abbr, postal])

    if len(values) == 6:
        state = values[3]
        abbr = values[4]
        postal = values[5]
        data.append([state, abbr, postal])

print(data)
