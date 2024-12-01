from aoc_lib import file_to_array
from collections import Counter

def split_into_two_libs(input_list):
    list_a = []
    list_b = []
    for i in input_list:
        if i=="":
            continue
        line_split = i.split("  ")
        list_a.append(int(line_split[0]))
        list_b.append(int(line_split[1]))
    return list_a, list_b

def calculate_difference(list_a, list_b):
    if len(list_a)!=len(list_b):
        raise AttributeError
    difference = 0
    for i in range(len(list_a)):
        difference += abs(list_a[i]-list_b[i])
    return difference

def file_init(file_name):
    input_list = file_to_array(file_name)
    list_a, list_b = split_into_two_libs(input_list)
    return list_a, list_b

def calculate_similarity(counter_a: Counter, counter_b: Counter):
    similarity_score = 0
    for i in counter_a.keys():
        if i in counter_b.keys():
            similarity_score += i*counter_a[i]*counter_b[i]
    return similarity_score

def solution_1(file_name):
    list_a, list_b = file_init(file_name)
    list_a.sort()
    list_b.sort()
    return calculate_difference(list_a, list_b)

def solution_2(file_name):
    list_a, list_b = file_init(file_name)
    counter_a = Counter(list_a)
    counter_b = Counter(list_b)
    print(counter_a, counter_b)
    return calculate_similarity(counter_a, counter_b)

print(solution_2("day1/input.txt"))