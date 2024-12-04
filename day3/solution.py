from aoc_lib import file_to_array

def file_init(file_name):
    input_list = file_to_array(file_name)
    return input_list

def initialise_paths_flag(paths):
    paths_flag = {}
    for path in paths:
        paths_flag[path]=0
    return paths_flag

def text_parsing(instruction):
    static_paths = ["mul", "do", "don't"]
    paths = list(static_paths)
    path_flag = 0
    status_flag = 0
    patterns = []
    parameters = []
    current_path = ""
    current_parameter = ""
    for i in range(len(instruction)):
        # 2 Scenarios:
        # 1. If Status_Flag = 1
        #    Check if it's a number, if so add to a temp string
        #    else if it's a comma, add the number to a list
        #    else if it's a ), add the whole list into an action list
        #    if not, abort and re-init
        # 2. If Status_Flag = 0
        #    Check if it's in one of the pattern
        if status_flag == 1:
            if instruction[i].isnumeric():
                current_parameter+=instruction[i]
            elif instruction[i]==",":
                parameters.append(int(current_parameter))
                current_parameter=""
            elif instruction[i]==")":
                if current_parameter!="": 
                    parameters.append(int(current_parameter))
                    current_parameter = ""
                patterns.append({"action": current_path, "parameters": parameters})
                print({"action": current_path, "parameters": parameters})
                current_path = ""
                parameters = []
                current_parameter = ""
                status_flag = 0
            else:
                current_path = ""
                parameters = []
                current_parameter = ""
                status_flag = 0

        if status_flag == 0:
            if instruction[i]=="(":
                for path in paths:
                    if path_flag==len(path):
                        current_path = path
                        status_flag = 1
                path_flag=0
                paths = list(static_paths)
            else:
                to_be_removed = []
                for path in paths:
                    if path_flag >= len(path) or instruction[i]!=path[path_flag]:
                        to_be_removed.append(path)
                path_flag+=1
                for path in to_be_removed:
                    paths.remove(path)
                if paths == []:
                    paths = list(static_paths)
                    path_flag=0
    return patterns


def pattern_detection(instruction):
    patterns = []
    temp_left, temp_right = "", ""
    status_mul = ["m", "u", "l", "(", ",", ")"]
    status_flag = 0
    for i in range(len(instruction)):
        if instruction[i]==status_mul[status_flag]:
            status_flag+=1
            if status_flag==len(status_mul):
                patterns.append({"left": int(temp_left), "right": int(temp_right)})
                temp_left, temp_right, status_flag = "", "", 0
            continue
        if status_flag==4 and instruction[i].isnumeric():
            temp_left+=instruction[i]
            continue
        if status_flag==5 and instruction[i].isnumeric():
            temp_right+=instruction[i]
            continue
        temp_left, temp_right, status_flag = "", "", 0
    return patterns

def pattern_calculation(patterns):
    total = 0
    for i in patterns:
        total += i["left"] * i["right"]
    return total

def pattern_calculation_2(patterns):
    total = 0
    flag = True
    for i in patterns:
        if i["action"]=="do" and len(i["parameters"])==0:
            flag = True
        elif i["action"] =="don't" and len(i["parameters"])==0:
            flag = False
        elif flag == True and i["action"] == "mul" and len(i["parameters"])==2:
            total+=i["parameters"][0] * i["parameters"][1]
    return total

def part_1(file_name):
    instructions=file_init(file_name)
    patterns = []
    for i in instructions:
        patterns += pattern_detection(i)
    return pattern_calculation(patterns)

def part_2(file_name):
    instructions=file_init(file_name)
    patterns = []
    for i in instructions:
        patterns += text_parsing(i)
    return pattern_calculation_2(patterns)

print(part_2("day3/input.txt"))