from aoc_lib import file_to_map

def file_init(filename: str):
    return file_to_map(filename)

def detect_letter(word_map, x, y, next_letters, direction=[]) -> int:
    if len(next_letters) == 0:
        return 1
    next_letter = next_letters[0]
    x_limit = len(word_map[y])
    y_limit = len(word_map)
    match_count = 0
    if len(direction)==0:
        for x_step in [-1, 0, 1]:
            for y_step in [-1, 0, 1]:
                if (x_step!=0 or y_step !=0) and x+x_step in range(x_limit) and y+y_step in range(y_limit) and word_map[y+y_step][x+x_step]==next_letter:
                    match_count += detect_letter(word_map, x+x_step, y+y_step, next_letters[1:], direction=[x_step, y_step]) 
    else:
        if x+direction[0] in range(x_limit) and y+direction[1] in range(y_limit) and word_map[y+direction[1]][x+direction[0]]==next_letter:
            match_count += detect_letter(word_map, x+direction[0], y+direction[1], next_letters[1:], direction=direction) 
    return match_count

def detect_m_s_match(x, y):
    match_status=0
    # print(x,y)
    if x=="M" and y=="S":
        match_status=1
    if x=="S" and y=="M":
        match_status=1
    return match_status

def detect_x_mas(word_map, x, y) -> int:
    match_count = 0
    x_limit = len(word_map[y])
    y_limit = len(word_map)
    if x+1 in range(x_limit) and y+1 in range(y_limit) and x-1 in range(x_limit) and y-1 in range(y_limit):
        match_count+=detect_m_s_match(word_map[y+1][x+1], word_map[y-1][x-1])
        match_count+=detect_m_s_match(word_map[y-1][x+1], word_map[y+1][x-1])
    # if match_count == 2:
        # print(x, y)
    return int(match_count==2)

def sol_1(filename: str):
    word_map = file_init(filename)
    print(word_map)
    xmas_count = 0
    for y in range(len(word_map)):
        for x in range(len(word_map[y])):
            if word_map[y][x]=="X":
                xmas_count += detect_letter(word_map, x, y, ["M", "A", "S"])
    return xmas_count

def sol_2(filename: str):
    word_map = file_init(filename)
    print(word_map)
    xmas_count = 0
    for y in range(len(word_map)):
        for x in range(len(word_map[y])):
            if word_map[y][x]=="A":
                print("A", x, y)
                xmas_count += detect_x_mas(word_map, x, y)
    return xmas_count

print(sol_2("day4/input.txt"))








