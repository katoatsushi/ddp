one_string_aminos = {'GLY':'G','ALA':'A','SER':'S',
    'THR':'T','PRO':'P','VAL':'V',
    'LEU':'L','ILE':'I','PHE':'F',
    'TYR':'Y','TRP':'W','ASP':'D',
    'ASN':'N','GLU':'E','GLN':'Q',
    'HIS':'H','LYS':'K','ARG':'R',
    'MET':'M','CYS':'C'}

# f1 = open('../pdb/3wtg.pdb', 'r')
# f2 = open('../pdb/4yu3.pdb', 'r')

# アズリン(4azu)とプラストシアニン(7pcy)の検証(position　128の行まで)
f1 = open('../pdb/4azu.pdb', 'r')
f2 = open('../pdb/7pcy.pdb', 'r')
f1_length = [2,128]
f2_length = [0,98]
# 二枚貝ヘモグロビン(3g46) vs ヒトヘモグロビン(4hhb)
f1 = open('../pdb/3g46.pdb', 'r')
f2 = open('../pdb/4hhb.pdb', 'r')
f1_length = [9, 146]
f2_length = [1, 137]
# 二枚貝ヘモグロビン(3g46) vs シアノバクテリアC-フィコシアニン(1gh0)
f1 = open('../pdb/3g46.pdb', 'r')
f2 = open('../pdb/1gh0.pdb', 'r')
f1_length = [11, 147]
f2_length = [30, 161]
# ヒトヘモグロビン(4hhb) vs シアノバクテリアC-フィコシアニン(1gh0)
f1 = open('../pdb/4hhb.pdb', 'r')
f2 = open('../pdb/1gh0.pdb', 'r')
f1_length = [3, 137]
f2_length = [30, 162]



def put_amino_position(f):
    res = []
    number_array = []
    for i in f:
        one_atom_date = i.split()
        if (one_atom_date[0] == 'ATOM') and (one_atom_date[2] == 'CA') and (one_atom_date[4] == 'A'): 
            x = float(one_atom_date[6])
            y = float(one_atom_date[7])
            z = float(one_atom_date[8])
            if not one_atom_date[5] in number_array:
                # AASPとBSAPのように2つある場合以下の処理
                if len(one_atom_date[3]) == 4:
                    amino_base = list(one_atom_date[3])
                    amino_base.pop(0)
                    amino_base = ''.join(amino_base)
                    amino = one_string_aminos[amino_base]
                    number_array.append(one_atom_date[5])
                    res.append([amino, x, y, z])
                else:
                    number_array.append(one_atom_date[5])
                    res.append([one_string_aminos[one_atom_date[3]], x, y, z])
    # for r in res:
    #     print(r)
    return res


def matras_put_amino_position(f, length):
    protein_strings = []
    res = []
    number_array = []
    for i in f:
        one_atom_date = i.split()
        if (one_atom_date[0] == 'ATOM') and (one_atom_date[2] == 'CA') and (one_atom_date[4] == 'A'):
            if length[0] -1 < int(one_atom_date[5]) and int(one_atom_date[5]) < length[1] + 1:
                x = float(one_atom_date[6])
                y = float(one_atom_date[7])
                z = float(one_atom_date[8])
                if not one_atom_date[5] in number_array:
                    # AASPとBSAPのように2つある場合以下の処理
                    if len(one_atom_date[3]) == 4:
                        amino_base = list(one_atom_date[3])
                        amino_base.pop(0)
                        amino_base = ''.join(amino_base)
                        amino = one_string_aminos[amino_base]
                        number_array.append(one_atom_date[5])
                        res.append([amino, x, y, z])
                        protein_strings.append(amino)
                    else:
                        number_array.append(one_atom_date[5])
                        res.append([one_string_aminos[one_atom_date[3]], x, y, z])
                        protein_strings.append(one_string_aminos[one_atom_date[3]])
    protein_strings = ''.join(protein_strings)
    return res, protein_strings

# f_1 = put_amino_position(f1)
# f_2 = put_amino_position(f2)

f_1, strings1 = matras_put_amino_position(f1, f1_length)
f_2, strings2 = matras_put_amino_position(f2, f2_length)
# print(strings1)
# print(strings2)