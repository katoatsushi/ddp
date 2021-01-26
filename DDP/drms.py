import math

def distancebased_root_mean_square_deviation(amino_a, amino_b, ddp):
    print("*"*200)
    amino_a_after = ddp[1]
    amino_b_after = ddp[0]
    # print("amino_a_after is:", amino_a_after)
    # print("amino_b_after is:", amino_b_after)
    # print("amino_a is:", amino_a)
    # print("amino_b is:", amino_b)
    length = len(ddp[0])
    amino_a_counter = 0
    amino_b_counter = 0
    amino_a_new = []
    amino_b_new = []
    for i in range(length):
        if  (amino_a_after[i] != "-") and (amino_b_after[i] != "-"):
            x_y_z_a = [amino_a[amino_a_counter][1], amino_a[amino_a_counter][2], amino_a[amino_a_counter][3]]
            amino_a_new.extend([[amino_a_after[i], x_y_z_a]])
            x_y_z_b = [amino_b[amino_b_counter][1], amino_b[amino_b_counter][2], amino_b[amino_b_counter][3]]
            amino_b_new.extend([[amino_b_after[i], x_y_z_b]]) 
            amino_a_counter += 1
            amino_b_counter += 1   
        elif (amino_a_after[i] == "-") and (amino_b_after[i] != "-"):
            amino_b_counter += 1
        elif (amino_a_after[i] != "-") and (amino_b_after[i] == "-"):
            amino_a_counter += 1 
    # print(amino_a_new)
    # print(amino_b_new)

    # 更新
    length = len(amino_a_new)
    total_distance = 0
    for i in range(length):
        from_a = amino_a_new[i]
        from_b = amino_b_new[i]
        # print('*i is', i,from_a, from_b)
        for j in range(length):
            if i < j:
                to_a = amino_a_new[j]
                to_b = amino_b_new[j]
                # print('j is', j,to_a,to_b)
                da = math.sqrt((from_a[1][0] - to_a[1][0])**2 + (from_a[1][1] - to_a[1][1])**2 + (from_a[1][2] - to_a[1][2])**2)
                db = math.sqrt((from_b[1][0] - to_b[1][0])**2 + (from_b[1][1] - to_b[1][1])**2 + (from_b[1][2] - to_b[1][2])**2)
                # d = (db - da)**2
                total_distance += (db - da)**2
    total_distance = math.sqrt((total_distance*2)/(length*(length-1)))
    print("DRMS is:", total_distance)
