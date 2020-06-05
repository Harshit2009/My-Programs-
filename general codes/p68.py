tasks = open('todos.txt')
for chore in tasks:
    print(chore, end='')
    tasks.close()
