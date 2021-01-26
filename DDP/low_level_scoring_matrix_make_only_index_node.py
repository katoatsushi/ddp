# -*- coding: utf-8 -*
import math
import decimal
import itertools
import numpy as np

# low level scoreing matrix　を作成する際にマッチしていると仮定したノードに初期スコア25を入力し、
# DPして最適パスを求め、総スコアを指定したノードに代入しhight level score　を作る

amino_a = [
    ['V', 1, 2, 1],
    ['L', 3, 1, 2],
    ['S', 1, 4, 3],
    ['A', 1, 2, 4],
    ['A', 5, 3, 5]
]

amino_b = [
    ['A', 2, 2, 2],
    ['B', 3, 5, 4],
    ['C', 2, 1, 6],
    ['D', 9, 6, 8],
    ['E', 12, 15, 10]
]

gap = -4

def measure_the_distance(arg1, arg2):
    x_1 = abs(arg1[0][1] - arg1[1][1])**2
    y_1 = abs(arg1[0][2] - arg1[1][2])**2
    z_1 = abs(arg1[0][3] - arg1[1][3])**2

    x_2 = abs(arg2[0][1] - arg2[1][1])**2
    y_2 = abs(arg2[0][2] - arg2[1][2])**2
    z_2 = abs(arg2[0][3] - arg2[1][3])**2
    distance_1 = math.sqrt(x_1 + y_1 + z_1)
    distance_2 = math.sqrt(x_2 + y_2 + z_2)
    dis = distance_2 - distance_1
    if dis < 0:
        dis = -dis
    dis = float(format(dis, '.2f'))
    dis = 50.0/(dis+5.0)
    return dis

def check_score_and_prenode(index, first_input, first_or_not):
    index_a = index[0]
    index_b = index[1]
    lange = first_input[0]
    arg = first_input[2]
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
                    left = left[0]
                if type(top) == list:
                    top = top[0]
                if type(diagonal) == list:
                    diagonal = diagonal[0]
                tap = measure_the_distance([amino_height[rows_counter-2], index_b], [amino_width[simple_counter - 1], index_a])
                score_array = [left + gap, top + gap, diagonal + tap]
                max_score = max(score_array)
                if type(max_score) == list: # 経路が複数ある場合は最初の経路だけを取得する
                    if max_score[0] == max_score[1] == max_score[2]:
                        number = [this_number - 1, this_number - width, this_number - width - 1]
                        arg[rows_counter - 1][simple_counter]= [max_score, number]
                    elif max_score[0] == max_score[1]:
                        number = [this_number - 1, this_number - width]
                        arg[rows_counter - 1][simple_counter]= [max_score, number]
                    elif max_score[0] == max_score[2]:
                        number = [this_number - 1, this_number - width - 1]
                        arg[rows_counter - 1][simple_counter]= [max_score,number]
                    elif max_score[1] == max_score[2]:
                        number = [this_number - width, this_number - width - 1]
                        arg[rows_counter - 1][simple_counter]= [max_score, number]
                else:
                    if score_array.index(max_score) == 0: # 左から来た時
                        number = this_number - 1
                        arg[rows_counter - 1][simple_counter]= [max_score, number]
                    elif score_array.index(max_score) == 1:  # 上から来た時
                        number = this_number - width
                        arg[rows_counter - 1][simple_counter]= [max_score, number]
                    elif score_array.index(max_score) == 2: # 斜めから来た時
                        number = this_number - width - 1
                        arg[rows_counter - 1][simple_counter] = [max_score, number]
            simple_counter = simple_counter + 1

    final_score = list(itertools.chain.from_iterable(arg))[-1]
    return final_score

def make_array(arg):
    arg1 = list(arg[1])
    arg2 = list(arg[0])
    arg_amino = [arg1, arg2]
    l = [None] * len(arg2)
    simple_array = []
    counter = 0
    for i in range(len(arg1)+1):
        num = [counter * -4]
        num.extend(l)
        simple_array.append(num)
        counter = counter + 1
    # 配列に初期のギャップを入れる
    first = simple_array[0]
    counter = 0
    first_array = []
    for i in first:
        i = counter*-4
        first_array.append(i)
        counter = counter + 1
    simple_array[0] = first_array
    return simple_array


def first(amino_a, amino_b, a_num, b_num, first_func_counter):
    width_max = len(amino_a)
    height_max = len(amino_b)

    a_last = len(amino_a) - a_num
    a_index = amino_a[a_num-1]
    b_last = len(amino_b) - b_num
    b_index = amino_b[b_num-1]

    index = [a_index, b_index]
    arg1 = [x[0] for x in amino_a]
    arg2 = [y[0] for y in amino_b]
    matrix_num = [[a_num, b_num], [a_last, b_last]]
    
    total_score = 0
    first_or_not = True
    if (a_num != 1) and (b_num != 1):      
        first_arg1 = [x[0] for x in amino_a[:a_num-1]]
        first_arg2 = [y[0] for y in amino_b[:b_num-1]]
        first_objs = [first_arg1, first_arg2]
        res = make_array(first_objs)
        first_input = [{"width":[1, a_num], "height":[1, b_num]},[amino_a[:a_num], amino_b[:b_num]], res]
        final_score = check_score_and_prenode(index, first_input, first_or_not)
        total_score += final_score[0]
        total_score += 25

    first_or_not = False
    if (a_num != width_max) and (b_num != height_max):
        first_arg1 = [x[0] for x in amino_a[a_num:]]
        first_arg2 = [y[0] for y in amino_b[b_num:]]
        first_objs = [first_arg1, first_arg2]
        res = make_array(first_objs)
        second_input = [{"width":[a_num, len(amino_a)], "height":[b_num, len(amino_a)]},[amino_a[a_num:], amino_b[b_num:]], res]
        final_score = check_score_and_prenode(index, second_input, first_or_not)
        total_score += final_score[0]

    print(width_max * height_max, ":", first_func_counter)
    return total_score

def init(amino_a, amino_b):
    low_level_score_matrixs = np.zeros((len(amino_b),len(amino_a)))
    width_max = len(amino_a)
    height_max = len(amino_b)
    main_counter = 0
    first_func_counter = 0
    for i_w in range(width_max+1):
        for i_h in range(height_max+1):
            if (i_w != 0) and (i_h != 0):
                a_num = i_w
                b_num = i_h
                # 各ノードにスコア情報を足していく
                low_level_score_matrixs[b_num -1][a_num -1] = first(amino_a, amino_b, a_num, b_num, first_func_counter)
                print(low_level_score_matrixs)
                main_counter = main_counter + 1
                first_func_counter += 1
    total = np.sum(low_level_score_matrixs)
    # print(low_level_score_matrixs)
    return low_level_score_matrixs

# init(amino_a, amino_b)
