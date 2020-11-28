# import set_data
# f1 = open('../pdb/3wtg.pdb', 'r')
# f2 = open('../pdb/4yu3.pdb', 'r')
# set_data.put_amino_position(f1)
# set_data.put_amino_position(f2)
amino_a = [
    ['V', -21.416, 13.35, 2.482],
    ['L', -18.312, 15.566, 2.993],
    ['S', -19.386, 19.108, 3.808],
    ['A', -18.071, 22.178, 1.946],
    ['A', -16.079, 22.95, 5.09]
    # ['D', -14.683, 19.381, 4.988]
    # ['K', -13.581, 19.855, 1.338]
    # ['T', -11.863, 23.2, 2.029]
    # ['N', -10.119, 21.645, 5.05]
    # ['T', -8.864, 18.598, 3.238]
]

amino_b = [
    ['V', -29.16, 16.657, -19.435],
    ['L', -25.799, 17.814, -18.077],
    ['S', -25.81, 19.732, -14.786],
    ['P', -23.197, 22.517, -14.093],
    ['A', -21.293, 19.951, -11.954]
    # ['D', -21.356, 17.746, -15.126]
    # ['K', -19.988, 20.654, -17.166]
    # ['T', -17.257, 21.468, -14.502]
    # ['N', -16.293, 17.74, -14.548]
    # ['L', -16.106, 17.375, -18.318]
]
aminos = [amino_a, amino_b]

def make_array(arg):
    arg1 = [x[0] for x in arg[0]]
    arg2 = [y[0] for y in arg[1]]
    print('アライメント前：', arg1, arg2)
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
    print(simple_array)
    print("%"*200)

make_array(aminos)

#def set_low_level_scoring_matrix(amino_a, amino_b):



