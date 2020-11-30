# -*- coding: utf-8 -*-
# sample = ['AGT','AGCTT']

sample = [
    'ASLNGTLMQYFEWYMPNDGQHWKRLQNDSAYLAEHGITAVWIPPAYKGTSQDDVGYGAYDLYDLGEFHQKGTVRTKYGTKAINSLHSRDINVYGDVVINHKGGADATEYVTAVEVDPADRNRVTSGEQRIKAWTHFQFPGRGSTYSDFKWYWYHFDGTDWDESRKLNRIYKFQGKAWDWEVSNENGNYDYLMYADIDYDHPDVTAEIKRWGTWYANELQLDGFRLDAVKHIKFSFLRDWVNHVREKTGKEMFTVAEYWQNDLGALENYLNKTNFNHSVFDVPLHYQFHAASTQGGGYDMRKLLNGTVVSKHPVKAVTFVDN',
    'ASLNGTLMQYFEWYMPNDGQHWKRLQNDSAYLAEHGITAVWIPPAYKGTSQDDVGYGAYDLYDLGEFHQKGTVRTKYGTKGELQSAINSLHSRDINVYGDVVINHKGGADATEYVTAVEVDPADRNRVTSGEQRIKAWTHFQFPGRGSTYSDFKWYWYHFDGTDWDESRKLNRIYKFQGKAWDWEVSNENGNYDYLMYADIDYDHPDVTAETWYANELQLDGFRLDAVKHIKFSFLRDWVNHVREKTGKEMFTVAEYWQNDLGALENYLNKTNFNHSVFDVPLHYQFHAASTQGGGYDMRKLLNGTVVSKHPVKAVTFVDN'
]
# sample = [
#     'MVTTFVALYDYESRTETDLSFKKGERLQIVNNTEGDWWLAHSLSTGQTGYIPSNYVAPSDSIQAEEWYFGKITRRESERLLLNAENPRGTFLVRESETTKGAYCLSVSDFDNAKGLNVKHYKIRKGQTGYIPSDVGYGAYDLYDLGEFHQKGTLDSGGFYITSRTQFNSLQQLVAYYSKHADGLCHRLTTVCPTSKPQTQGLAKDAWEIPRESLRLEVKLGQGCFGEVWMGTWNGTTRVAIKTLKPGTMSPEAFLQEAQVMKKLRHEKLVQLYAVVSEEPIYIVTEYMSKGSLLDFLKGETGKYLRLPQLVDMAAQIASGMAYVERMNYVHRDLRAANILVGENLVCKVADFGLARLIEDNEYTARQGAKFPIKWTAPEAALYGRFTIKSDVWSFGILLTELTTKGRVPYPGMVNREVLDQVERGYRMPCPPECPESLHDLMCQCWRKEPEERPTFEYLQAFLEDYFTSTEPQYQPGENL',
#     'AMVTTFVALYDYESRTETDLSFKKGELQIVNNTEGDWWLAHSPPGQTGYIPSDVGYGAYDLYDLGEFHQKGTVRRESERLLLELQSAINSLHSRINVYGDVVINHKGGADATEYVTAVEVDPADRNRVTSGEQRIKAWTHFQFPGRGSTYSDFKWYWYHFDGCPTKPQTQGLAKDAWEIPRESVSNENGNYDYLMADIDYDHPDVTVAIKTLKPGTMSPEAFLQAQVMKKHIKFSFLRDWNHVREKTGKEMFTVAEGSLLDFLKGETGKYLRLPTNFNHSVFDVPLHYQFHAASTQGGGYDMRKLLNGENLVCKVKAVTFVDNHDTQPGQSLESTVQTWFKPLAYAFILTREAGYPQIFYGDMYGTKIPALKHKIEPILKARKQYAYGAQHDYFDHGASQRYPGMVNREVLDVERGYRMITDGPGGTKRMYVGQNAGETWHDITGNRSDSVVINAEGWGDYFTSTEPQYPGENLR'
# ]
PAM_amino = ['C','S','T','P','A','G','N','D','E','Q','H','R','K','M','I','L','V','F','Y','W']
PAM_score = [[12],
            [0,2],
            [-2,0,3],
            [-3,1,0,5],
            [-2,1,1,1,2],
            [-3,1,0,-1,1,5],
            [-4,1,0,-1,0,0,2],
            [-5,0,0,-1,0,1,2,4],
            [-5,0,0,-1,0,0,1,3,4],
            [-5,-1,-1,0,0,-1,1,2,2,4],
            [-3,-1,-1,0,-1,-2,2,1,1,3,6],
            [-4,0,-1,0,-2,-3,0,-1,-1,1,2,6],
            [-5,0,0,-1,-1,-2,1,0,0,1,0,3,5],
            [-5,-2,-1,-2,-1,-3,-2,-3,-2,-1,-2,0,0,5],
            [-2,-1,0,-2,-1,-3,-2,-2,-2,-2,-2,-2,-2,2,5],
            [-6,-3,-2,-3,-2,-4,-3,-4,-3,-2,-2,-3,-3,4,2,6],
            [-2,-1,0,-1,0,-1,-2,-2,-2,-2,-2,-2,-2,2,4,2,4],
            [-4,-3,-3,-5,-4,-5,-4,-5,-5,-5,-2,-4,-5,0,1,2,-1,9],
            [0,-3,-3,-5,-3,-5,-2,-4,-4,-4,0,-4,-4,-2,-1,-1,-2,7,10],
            [-8,-2,-5,-6,-6,-7,-4,-7,-7,-5,-3,2,-3,-4,-2,-2,-6,0,0,17]
            ]
# PAM_score[長い方][短い方]で検索

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
    print('アライメント後：')
    RES_0 = ''.join(res[0])
    RES_1 = ''.join(res[1])
    print(RES_0)
    print("*"*180)
    print(RES_1)
    # print(join(res[0]))
    # print(join(res[1]))

def  make_optimal_path(arg, node_data, aminos):
    next_node = arg[-1][-1]
    route_path = []
    if type(next_node) == list:
        for i in next_node:
            route_path.extend([i])
    else:
        route_path = [next_node]

    next_node = None
    while next_node != [1]:
        all_ways = []
        for route in route_path:
            if type(route) == int:
                route = [route]
            last = route[-1]
            next_node = arg[last//node_data['width']][last%node_data['width'] - 1]
            if type(next_node) == int:
                next_node = [next_node]
            new_one = [route]*len(next_node) #[[7],[7]]
            append_one = list(zip(new_one, next_node))# [([17, 4], 16), ([17, 4], 10)]
            for a in append_one:
                all_ways.append(a[0] + [a[1]])

        route_path = all_ways
    if type(all_ways[0]) == list: #複数経路がある場合
        way = all_ways[0]
        way.reverse()
        way.append(node_data['max_node_num'])
        alignment_result(way, aminos)
        # for way in all_ways:
        #     way.reverse()
        #     way.append(node_data['max_node_num'])
        #     alignment_result(way, aminos)
    else:
        all_ways.reverse()
        all_ways.append(node_data['max_node_num'])
        alignment_result(all_ways, aminos)


def check_score_and_prenode(arg, aminos): # ["最大スコア", "ノード番号", ["左スコア", "斜スコア", "上スコア"]]
    width = len(arg[0])
    amino_height = aminos[0] 
    amino_width = aminos[1]
    max_node = (len(amino_height)+ 1)*(len(amino_width) + 1)
    node_data = {'width': len(aminos[1]) + 1,'height': len(aminos[0]) + 1,'max_node_num': max_node}
    the_arg = arg[1:] 
    rows_counter = 1
    for mono_array in the_arg: # [-6,None,None,None,None]
        rows_counter = rows_counter + 1
        simple_counter = 0
        for arr in mono_array: # -6
            this_number = width*(rows_counter-1) + simple_counter + 1
            if arr == None: # rows_counterが    横, simple_counterが縦
                left = arg[rows_counter - 1][simple_counter - 1]
                diagonal = arg[rows_counter - 2][simple_counter - 1]
                top = arg[rows_counter - 2][simple_counter]

                # PAMのスコアを使う
                index_a = amino_height[rows_counter - 2]
                index_b = amino_width[simple_counter - 1]
                index_a_number = PAM_amino.index(index_a)
                index_b_number = PAM_amino.index(index_b)
                if index_a_number >= index_b_number:
                    gap = PAM_score[index_a_number][index_b_number]
                else:
                    gap = PAM_score[index_b_number][index_a_number]
                # ここまで

                if (left[2][0] is None) and (left[2][1] is None):
                    from_left = None
                elif left[2][0] is None:
                    from_left = left[2][1] - 10
                elif left[2][1] is None:
                    from_left = left[2][0] - 2
                else:
                    from_left = max(left[2][0] - 2, left[2][1] - 10)

                if (top[2][1] is None) and (top[2][2] is None):
                    from_top = None
                elif top[2][1] is None:
                    from_top = top[2][2] - 2
                elif top[2][2] is None:
                    from_top = top[2][1] - 10
                else:
                    from_top = max(top[2][1] - 10, top[2][2] - 2)
                pre_d = [from_left, diagonal[0] + gap, from_top] # [左からのスコア, 斜めからのスコア,  上からのスコア]
                pre_a = [x for x in pre_d if x is not None] #スコアの中からNoneを排除
                max_val = max(pre_a) #最大スコア
                if pre_d.count(max_val) != 1: # 複数からの経路の時
                    if pre_d[0] == pre_d[1] == pre_d[2]: # 左・斜め・上
                        number = [this_number - 1, this_number - width, this_number - width - 1]
                    elif pre_d[1] == pre_d[2]: # 斜め・上
                        number = [this_number - width, this_number - width - 1]
                    elif pre_d[0] == pre_d[2]: # 左・上
                        number = [this_number - 1, this_number - width]
                    elif pre_d[0] == pre_d[1]:
                       number = [this_number - 1, this_number - width - 1]
                else: # 単数からの経路の時
                    if pre_d.index(max_val) == 0:# 左から
                        number = this_number - 1
                    elif pre_d.index(max_val) == 1: # 斜めから
                        number = this_number - width - 1
                    elif pre_d.index(max_val) == 2: # 上から
                        number = this_number - width

                d = [max_val, number, pre_d]# ["最大スコア", "ノード番号", ["左スコア", "斜スコア", "上スコア"]]
                arg[rows_counter - 1][simple_counter]= d # 当ノードに上の情報を再代入
            simple_counter = simple_counter + 1

    big_arg = [] # ノードの情報だけを抽出
    total_score = arg[-1][-1][0]
    print("================================ここまでの総計スコアは:", total_score, "です==========================================")
    for ar in arg:
        node_score_arg = []
        for a in ar:
            node_score_arg.extend([a[1]])
        big_arg.extend([node_score_arg])
    arg = big_arg
    # print(node_data)
    print(arg)
    make_optimal_path(arg, node_data, aminos)


def make_array(arg):
    arg1 = list(arg[0])
    arg2 = list(arg[1])
    # print('アライメント前：')
    # print(arg1)
    # print(arg2)
    arg_amino = [arg1, arg2]
    l = [None] * len(arg2)
    width = len(arg2) + 1
    simple_array = []
    counter = 0
    col_counter =  1 - width
    for i in range(len(arg1) + 1):
        num = [[counter * -3, col_counter, [None, None, None]]]
        num.extend(l)
        simple_array.append(num)
        counter = counter + 1
        col_counter = col_counter + width 
        
    # 配列に初期のギャップを入れる
    first = simple_array[0]
    counter = 0
    first_array = [] 
    row_counter = 0  
    for i in first:
        i = [counter * -3, row_counter, [None, None, None]]
        first_array.append(i)
        counter = counter + 1
        row_counter = row_counter + 1
    simple_array[0] = first_array
    # for i in simple_array:
    #     print(i)
    check_score_and_prenode(simple_array, arg_amino)

make_array(sample)