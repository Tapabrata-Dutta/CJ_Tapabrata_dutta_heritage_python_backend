tasks = ['backup', 'encrypt', 'send', 'archive']


for task in tasks:
    if task == 'encrypt':
        pass    # TODO: implement encryption later
    else:
        print(f'Executing task: {task}')
