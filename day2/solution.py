from aoc_lib import file_to_array

def file_ingestion(file_name):
    matrix = file_to_array(file_name)
    return [i.split() for i in matrix]

def safe_detection(line):
    if len(line)==0:
        return 0
    direction = int(line[0])>int(line[1])
    for i in range(len(line)-1):
        if (int(line[i])>int(line[i+1]))==direction and 1<=abs(int(line[i])-int(line[i+1]))<=3:
            continue
        # print(f"Stopped at {line[i]} {line[i+1]}, full line {line}")
        return 0
    return 1

def safe_detection_with_fault_tolerance(line):
    if len(line)==0:
        return 0
    fault_flag = 0
    direction = int(line[0])>int(line[1])
    for i in range(len(line)-1):
        if fault_flag==1:
            fault_flag = 2
            continue
        if (int(line[i])>int(line[i+1]))==direction and 1<=abs(int(line[i])-int(line[i+1]))<=3:
            continue
        if i!=0 and safe_detection(line[0:i-1]+line[i:])==1:
            print(f"Tolerated, {line[0:i-1]+line[i:]}, original {line}")
            return 1
        if safe_detection(line[0:i]+line[i+1:])==1:
            print(f"Tolerated, {line[0:i]+line[i+1:]}, original {line}")
            return 1
        if i!=len(line)-1 and safe_detection(line[0:i+1]+line[i+2:]):
            print(f"Tolerated, {line[0:i+1]+line[i+2:]}, original {line}")
            return 1
        print(f"Not Tolerated, {line}")
        return 0
    print(f"Valid, {line}")
    return 1

def sol_1(file_name):
    matrix = file_ingestion(file_name)
    counter = 0
    for i in matrix:
        counter+=safe_detection(i)
    return counter

def sol_2(file_name):
    matrix = file_ingestion(file_name)
    counter = 0
    for i in matrix:
        counter+=safe_detection_with_fault_tolerance(i)
    return counter

print(sol_2("day2/input.txt"))