# -*- coding: utf-8 -*
import math
import decimal
import itertools

amino_a = [
    ['V', 0, 0, 1],
    ['L', 0, 0, 2],
    ['S', 0, 0, 3],
    ['A', 0, 0, 4],
    ['A', 0, 0, 5]
]

amino_b = [
    ['A', 0, 0, 2],
    ['B', 0, 0, 4],
    ['C', 0, 0, 6],
    ['D', 0, 0, 8],
    ['E', 0, 0, 10]
]
gap = -4

def measure_the_distance(arg1, arg2):
    # print("---------arg 1---------")
    # print(arg1)
    # print("---------arg 2---------")
    # print(arg2)
    x_1 = abs(arg1[0][1]**2 - arg1[1][1]**2)
    y_1 = abs(arg1[0][2]**2 - arg1[1][2]**2)
    z_1 = abs(arg1[0][3]**2 - arg1[1][3]**2)
    x_2 = abs(arg2[0][1]**2 - arg2[1][1]**2)
    y_2 = abs(arg2[0][2]**2 - arg2[1][2]**2)
    z_2 = abs(arg2[0][3]**2 - arg2[1][3]**2)
    distance_1 = math.sqrt(x_1 + y_1 + z_1)
    distance_2 = math.sqrt(x_2 + y_2 + z_2)
    dis = distance_2 - distance_1
    if dis < 0:
        dis = -dis
    # print("===============dis is ==========")
    # print(distance_1, distance_2, dis)
    # print("%"*100)
    dis = float(format(dis, '.2f'))
    ## dis = decimal.Decimal((format(dis, '.2f')))
    # print(type(dis))
    return dis
    

def find_path(height, width, arg):
    print('============arg==========')
    print(arg)
    start = arg[-1][-1][1]
    height = len(height)
    width = len(width)
    goal = (height)*(width)
    print(max_node)
    print("========== height and width =============")
    print('height is :', height, 'width is :', width)
    new_array = [[0] * width] * height
    print("========== new araay is =============")
    print(new_array)
    new_array[-1][-1] = arg[-1][-1][0]
    #print(new_array[-1][-1])
    
    next_is = start
    while type(next_is) != list:
        q = start//width
        mod = start%width
        next_is = arg[q][mod-1]
        nex_score = next_is[0]
        next_node = next_is[1]
        new_array[q][mod-1] = nex_score
    print(new_array)


def check_score_and_prenode(first_input, low_level_score_matrix):
    print("&"*100)
    print(first_input)
    arg = first_input[2]
    print("arg"*100)
    print(arg)
    width = len(arg[0])
    amino_height = first_input[1][1] # ['A','G','T']
    amino_width = first_input[1][0] # ['A','G','C','T']
    max_node = (len(amino_height)+ 1)*(len(amino_width) + 1)
    the_arg = arg[1:] 
    rows_counter = 1
    for mono_array in the_arg: 
        simple_counter = 0
        rows_counter = rows_counter + 1
        for arr in mono_array: # -6
            this_number = width*(rows_counter-1) + simple_counter + 1
            if arr == None:
                left = arg[rows_counter - 1][simple_counter - 1]
                top = arg[rows_counter - 2][simple_counter]
                diagonal = arg[rows_counter - 2][simple_counter - 1]
                if type(left) == list:
                    print("aaaaaaaaaaaaaa")
                    left = left[0]
                if type(top) == list:
                    top = top[0]
                if type(diagonal) == list:
                    diagonal = diagonal[0]
                print(top, left,diagonal)
                tap = measure_the_distance([amino_height[rows_counter-2], amino_height[-1]], [amino_width[simple_counter - 1], amino_width[-1]])
                score_array = [left + gap, top + gap, diagonal + tap]
                max_score = max(score_array)
                if type(max_score) == list: # 経路が複数ある場合は最初の経路だけを取得する
                    if max_score[0] == max_score[1] == max_score[2]:
                        number = [this_number - 1, this_number - width, this_number - width - 1]
                        arg[rows_counter - 1][simple_counter]= [max_score, [this_number,number]]
                    elif max_score[0] == max_score[1]:
                        number = [this_number - 1, this_number - width]
                        arg[rows_counter - 1][simple_counter]= [max_score, [this_number,number]]
                    elif max_score[0] == max_score[2]:
                        number = [this_number - 1, this_number - width - 1]
                        arg[rows_counter - 1][simple_counter]= [max_score, [this_number,number]]
                    elif max_score[1] == max_score[2]:
                        number = [this_number - width, this_number - width - 1]
                        arg[rows_counter - 1][simple_counter]= [max_score, [this_number,number]]
                else:
                    if score_array.index(max_score) == 0: # 左から来た時
                        number = this_number - 1
                        arg[rows_counter - 1][simple_counter]= [max_score, [this_number,number]]
                    elif score_array.index(max_score) == 1:  # 上から来た時
                        number = this_number - width
                        arg[rows_counter - 1][simple_counter]= [max_score, [this_number,number]]
                    elif score_array.index(max_score) == 2: # 斜めから来た時
                        number = this_number - width - 1
                        arg[rows_counter - 1][simple_counter] = [[max_score, tap], [this_number,number]]
                        print("this is gooooood", tap)
                        print('Node', this_number, "to", number)
            simple_counter = simple_counter + 1
    
    final_score = list(itertools.chain.from_iterable(arg))[-1]
    print("final score is:", final_score)
    print(arg)
    #find_path(amino_height, amino_width, arg)


def first(amino_a, amino_b):
    low_level_score_matrix = [[0]*len(amino_a)]*len(amino_b)
    a_num = 4
    a_last = len(amino_a) - a_num
    b_num = 3
    b_last = len(amino_b) - b_num
    #print('a_num', a_num, 'b_num', b_num, '::::::::a_last', a_last, 'b_last', b_last)
    arg1 = [x[0] for x in amino_a]
    arg2 = [y[0] for y in amino_b]
    print("マッチしているのはこの2つ")
    print(arg1[a_num-1])
    print(arg2[b_num-1])
    matrix_num = [[a_num, b_num], [a_last, b_last]]

    arg_amino = [arg1, arg2]
    l = [None] * len(arg2)
    simple_array = []
    counter = 0
    for i in range(len(arg1) + 1):
        num = [counter * -4.0]
        num.extend(l)
        simple_array.append(num)
        counter = counter + 1
    first = simple_array[0]
    counter = 0
    first_array = []
    for i in first:
        i = counter*-4.0
        first_array.append(i)
        counter = counter + 1
    simple_array[0] = first_array
    # for i in simple_array:
    #     print(i)
    # print("%"*200)
    first = []
    counter = 0
    for i in simple_array:
        if not counter >= b_num:
            first.append(i[0:a_num])
        counter = counter + 1
    first_input = [[[1, a_num], [1, b_num]],[amino_a[:a_num], amino_b[:b_num]], first]
    # print(first)
    # print("*"*100)
    second = []
    counter = 0
    for i in simple_array:
        if not counter < b_num:
            second.append(i[a_num:])
        counter = counter + 1
    # print(second)
    # print("!"*100)
    print(first_input)
    print(low_level_score_matrix)
    check_score_and_prenode(first_input, low_level_score_matrix)


first(amino_a, amino_b)
