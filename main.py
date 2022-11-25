from random import randint, choice

SIZE_N = randint(5, 20)
SIZE_M = randint(5, 20)

def check_state(char_x, char_y, char_sign,
                enemy_x, enemy_y,
                exit_x, exit_y):
    win_condition = char_x == exit_x and char_y == exit_y
    loss_condition = char_x == enemy_x and char_y == enemy_y

    if win_condition:
        char_sign = 'W'
        print(f'You Won in {turns} turns!')
    elif loss_condition:
        char_sign = 'L'
        print(f'You Lost in {turns} turns!')

    return char_sign, win_condition or loss_condition



def generate_map(char_x, char_y, char_sign,
                 enemy_x, enemy_y, enemy_sign,
                 exit_x, exit_y, exit_sign,
                 size_n=SIZE_N, size_m=SIZE_M):

    world_map = []

    for j in range(size_m):
        row = []

        for i in range(size_n):
            row.append(' ')

        world_map.append(row)


    world_map[enemy_y][enemy_x] = enemy_sign
    world_map[exit_y][exit_x] = exit_sign
    world_map[char_y][char_x] = char_sign

    return world_map


def move(direction, x, y, size_n=SIZE_N, size_m=SIZE_M):
    if direction == 'u' and y > 0:
        y -= 1
    elif direction == 'd' and y < size_m - 1:
        y += 1
    elif direction == 'l' and x > 0:
        x -= 1
    elif direction == 'r' and x < size_n - 1:
        x += 1

    return x, y


char_x = randint(0, SIZE_N - 1)
char_y = randint(0, SIZE_M - 1)
char_sign = 'X'

enemy_x = randint(0, SIZE_N - 1)
enemy_y = randint(0, SIZE_M - 1)
enemy_sign = 'E'

exit_x = randint(0, SIZE_N - 1)
exit_y = randint(0, SIZE_M - 1)
exit_sign = 'O'

turns = 0

while True:
    char_sign, end_flag = check_state(char_x, char_y, char_sign,
                                        enemy_x, enemy_y,
                                        exit_x, exit_y)


    world_map = generate_map(char_x, char_y, char_sign,
                             enemy_x, enemy_y, enemy_sign,
                             exit_x, exit_y, exit_sign)

    print(world_map)
    if end_flag:
        break


    direction = input('Enter direction (u / d / l / r ): ')
    char_x, char_y = move(direction, char_x, char_y)

    enemy_direction = choice('udlr')
    enemy_x, enemy_y = move(enemy_direction, enemy_x, enemy_y)

    turns += 1
