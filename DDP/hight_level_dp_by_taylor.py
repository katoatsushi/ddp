# -*- coding: utf-8 -*
import low_level_scoring_matrix
import set_data
import drms
import csv

# 処理
# アズリン(4azu)とプラストシアニン(7pcy)の検証(position　128の行まで)
# f1 = open('../pdb/4azu.pdb', 'r')
# f2 = open('../pdb/7pcy.pdb', 'r')
# f1_length = [2,128]
# f2_length = [0,99]
# # 二枚貝ヘモグロビン(3g46) vs ヒトヘモグロビン(4hhb)
# f1 = open('../pdb/3g46.pdb', 'r')
# f2 = open('../pdb/4hhb.pdb', 'r')
# f1_length = [9, 146]
# f2_length = [1, 137]
# # 二枚貝ヘモグロビン(3g46) vs シアノバクテリアC-フィコシアニン(1gh0)
# f1 = open('../pdb/3g46.pdb', 'r')
# f2 = open('../pdb/1gh0.pdb', 'r')
# f1_length = [11, 147]
# f2_length = [30, 161]
# # ヒトヘモグロビン(4hhb) vs シアノバクテリアC-フィコシアニン(1gh0)
# f1 = open('../pdb/4hhb.pdb', 'r')
# f2 = open('../pdb/1gh0.pdb', 'r')
# f1_length = [3, 137]
# f2_length = [30, 162]

# amino_a = set_data.put_amino_position(f1)
# amino_b = set_data.put_amino_position(f2)

amino_a, strings_a = set_data.matras_put_amino_position(f1, f1_length)
amino_b, strings_b = set_data.matras_put_amino_position(f2, f2_length)

print(strings_a)
print(strings_b)

def alignment(aminos, result_array):
    amino_a = aminos[0]
    amino_b = aminos[1]
    alignment_s = []
    alignment_l = []
    counter_s = 0
    counter_l = 0
    for i in result_array:
        if i == 'OK':
            alignment_s.append(amino_a[counter_s])
            alignment_l.append(amino_b[counter_l])
            counter_s = counter_s + 1
            counter_l = counter_l + 1
        elif i == 'R': 
            alignment_s.append('-')
            alignment_l.append(amino_b[counter_l])
            counter_l = counter_l + 1
        elif i == 'D':
            alignment_l.append('-')
            alignment_s.append(amino_a[counter_s])
            counter_s = counter_s + 1
    alignment = [alignment_s, alignment_l]
    return alignment

def alignment_result(node_num_array, aminos):
    result_array = []
    pre_node = node_num_array[0]
    counter = 0
    width = len(aminos[1]) + 1
    for i in node_num_array:
        gap = node_num_array[counter + 1] - i
        if gap == 1:
            result_array.append("R")
        elif gap == width:
            result_array.append("D")
        else:
            result_array.append("OK")
        pre_node = i
        counter = counter + 1
        if (counter + 1) == len(node_num_array):
            break
    res = alignment(aminos, result_array)
    RES_0 = ''.join(res[0])
    RES_1 = ''.join(res[1])
    print(RES_0)
    print(RES_1)
    print('アライメント後：', res)
    drms.distancebased_root_mean_square_deviation(amino_a, amino_b, res)


def  make_optimal_path(arg, max_node, aminos):
    flatten_div_array = []
    for mini_arg in arg:
        for i in mini_arg:
            flatten_div_array.append(i)
    # 3元配列から2元配列に変換
    last = flatten_div_array[-1]
    main_array = [last[1]]
    while type(flatten_div_array[last[1]-1]) == list:
        last = flatten_div_array[last[1]-1]
        main_array.append(last[1])
    main_array.reverse()
    main_array.append(max_node)
    #print(main_array)
    alignment_result(main_array, aminos)

def check_score_and_prenode(arg, aminos):
    width = len(arg[0])
    amino_height = aminos[0] # ['A','G','T']
    amino_width = aminos[1] # ['A','G','C','T']
    max_node = (len(amino_height)+ 1)*(len(amino_width) + 1)
    the_arg = arg[1:] 
    rows_counter = 0
    for mono_array in arg: # [-6,None,None,None,None]
        rows_counter = rows_counter + 1
        simple_counter = 0
        for arr in mono_array: # -6
            this_number = width*(rows_counter-1) + simple_counter + 1
            if arr == None:
                left = arg[rows_counter - 1][simple_counter - 1]
                if type(left) == list:
                    left = left[0]
                top = arg[rows_counter - 2][simple_counter]
                if type(top) == list:
                    top = top[0]
                diagonal = arg[rows_counter - 2][simple_counter - 1]
                if type(diagonal) == list:
                    diagonal = diagonal[0]
                tap = hight_level_scoring_matrix[rows_counter - 2][simple_counter - 1]
                score_array = [left-3, top-3, diagonal + tap]
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
                        arg[rows_counter - 1][simple_counter]= [max_score, number]
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
    make_optimal_path(arg, max_node, aminos)

def make_array(arg):
    arg1 = list(arg[0])
    arg2 = list(arg[1])
    #print('アライメント前：', arg1, arg2)
    arg_amino = [arg1, arg2]
    l = [None] * len(arg2)
    simple_array = []
    counter = 0
    for i in range(len(arg1) + 1):
        num = [counter * -3]
        num.extend(l)
        simple_array.append(num)
        counter = counter + 1
    # 配列に初期のギャップを入れる
    first = simple_array[0]
    counter = 0
    first_array = []
    for i in first:
        i = counter*-3
        first_array.append(i)
        counter = counter + 1
    simple_array[0] = first_array
    
    check_score_and_prenode(simple_array, arg_amino)

 

hight_level_scoring_matrix = low_level_scoring_matrix.init(amino_a, amino_b)
print("hight_level_scoring_matrix is")
print(hight_level_scoring_matrix)

filename = 'hight_level.csv'
# ファイル，1行目(カラム)の作成
with open(filename, 'w') as f:
    writer = csv.writer(f)
    for i in hight_level_scoring_matrix:
        writer.writerow(i)

arg1 = [x[0] for x in amino_a]
arg2 = [y[0] for y in amino_b]
sample = [arg2, arg1]
make_array(sample)
# print(response)


