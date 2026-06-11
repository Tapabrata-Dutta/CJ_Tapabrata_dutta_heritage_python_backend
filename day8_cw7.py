inventory = ['Pen', 'Notebook', 'Eraser', 'Scale']
search = 'Stapler'


for item in inventory:
    if item == search:
        print(f'{search} found!')
        break
else:
    print(f'{search} not found in inventory.')
