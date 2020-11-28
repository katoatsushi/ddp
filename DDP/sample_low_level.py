amino_a = [
    ['V', 0, 0, 1],
    ['L', 0, 0, 2],
    ['S', 0, 0, 3],
    ['A', 0, 0, 4],
    ['A', 0, 0, 5]
]

amino_b = [
    ['V', 0, 0, 2],
    ['L', 0, 0, 4],
    ['S', 0, 0, 6],
    ['P', 0, 0, 8],
    ['A', 0, 0, 10]
]

# amino_aの3番目とamino_bの3番目がマッチと仮定する
def check_score_and_prenode(arg, aminos):
    width = len(arg[0])
    amino_height = aminos[0] # ['A','G','T']
    amino_width = aminos[1] # ['A','G','C','T']
    max_node = (len(amino_height)+ 1)*(len(amino_width) + 1)
    the_arg = arg[1:] 
    rows_counter = 1
    for mono_array in the_arg: # [-6,None,None,None,None]
        rows_counter = rows_counter + 1
        simple_counter = 0
        for arr in mono_array: # -6
            this_number = width*(rows_counter-1) + simple_counter + 1
            if arr == None:
                # 最大スコアと移動前のノードを決める 
                # rows_counter　が横, simple_counterが縦
                left = arg[rows_counter - 1][simple_counter - 1]
                if type(left) == list:
                    left = left[0]
                top = arg[rows_counter - 2][simple_counter]
                if type(top) == list:
                    top = top[0]
                diagonal = arg[rows_counter - 2][simple_counter - 1]
                if type(diagonal) == list:
                    diagonal = diagonal[0]
                if amino_height[rows_counter - 2] == amino_width[simple_counter - 1]:
                    gap = 1 #　一致した時
                else:
                    gap = -2 #　一致していない時
                score_array = [left-3, top-3, diagonal + gap]
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


def first(amino_a, amino_b):
    a_num = 3
    a_last = len(amino_a) - a_num
    b_num = 3
    b_last = len(amino_b) - b_num
    print('a_numは', a_num, 'b_numは', b_num, 'a_lastは', a_last, 'b_lastは', b_last)
    arg1 = [x[0] for x in amino_a]
    arg2 = [y[0] for y in amino_b]
    print(arg1[a_num-1])
    print(arg2[b_num-1])
    matrix_num = [[a_num, b_num], [a_last, b_last]]

    arg_amino = [arg1, arg2]
    l = [None] * len(arg2)
    simple_array = []
    counter = 0
    for i in range(len(arg1) + 1):
        num = [counter * -4]
        num.extend(l)
        simple_array.append(num)
        counter = counter + 1
    first = simple_array[0]
    counter = 0
    first_array = []
    for i in first:
        i = counter*-4
        first_array.append(i)
        counter = counter + 1
    simple_array[0] = first_array
    for i in simple_array:
        print(i)
    print("%"*200)
    first = []
    counter = 0
    for i in simple_array:
        if not counter >= b_num:
            first.append(i[0:a_num])
        counter = counter + 1
    print(first)
    print("*"*300)
    second = []
    counter = 0
    for i in simple_array:
        if not counter < b_num:
            second.append(i[a_num:])
        counter = counter + 1
    print(second)


first(amino_a, amino_b)
