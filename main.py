from random import randint, choice

SIZE_N = randint(10, 30)
SIZE_M = randint(10, 30)


def check_state(objects):
    for obj in objects:
        if obj['type'] == 'char':
            char = obj
        elif obj['type'] == 'portal':
            portal = obj
        elif obj['type'] == 'enemy':
            loss_condition = char['x'] == obj['x'] and char['y'] == obj['y']
            if loss_condition:
                char['sign'] = 'L'
                print(f'You Lost in {turns} turns!')
                break

    win_condition = char['x'] == portal['x'] and char['y'] == portal['y']

    if win_condition:
        char['sign'] = 'W'
        print(f'You Won in {turns} turns!')

    return win_condition or loss_condition


def generate_enemies(count):
    enemies = []
    for _ in range(count):
        enemy = {'x': randint(0, SIZE_N - 1),
                 'y': randint(0, SIZE_M - 1),
                 'sign': 'E',
                 'type': 'enemy'}
        enemies.append(enemy)

    return enemies


def generate_map(objects, size_n=SIZE_N, size_m=SIZE_M):
    world_map = []

    for j in range(size_m):
        row = []

        for i in range(size_n):
            row.append(' ')

        world_map.append(row)

    for obj in objects:
        world_map[obj['y']][obj['x']] = obj['sign']

    return world_map


def move(direction, obj, size_n=SIZE_N, size_m=SIZE_M):
    if direction == 'u' and obj['y'] > 0:
        obj['y'] -= 1
    elif direction == 'd' and obj['y'] < size_m - 1:
        obj['y'] += 1
    elif direction == 'l' and obj['x'] > 0:
        obj['x'] -= 1
    elif direction == 'r' and obj['x'] < size_n - 1:
        obj['x'] += 1


def print_map(world_map):
    for row in world_map:
        print(f'| {" | ".join(row)} | ')


char = {'x': randint(0, SIZE_N - 1),
        'y': randint(0, SIZE_M - 1),
        'sign': 'X',
        'type': 'char'}


portal = {'x': randint(0, SIZE_N - 1),
          'y': randint(0, SIZE_M - 1),
          'sign': 'O',
          'type': 'portal'}

enemies = generate_enemies(10)

objects = [char, portal] + enemies

turns = 0

while True:
    end_flag = check_state(objects)

    world_map = generate_map(objects)

    print_map(world_map)

    if end_flag:
        break

    for obj in objects:
        direction = ''

        if obj['type'] == 'char':
            direction = input('Enter direction (u / d / l / r ): ')
        elif obj['type'] == 'enemy':
            direction = choice('udlr')

        move(direction, obj)

    turns += 1
