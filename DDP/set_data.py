one_string_aminos = {'GLY':'G','ALA':'A','SER':'S',
    'THR':'T','PRO':'P','VAL':'V',
    'LEU':'L','ILE':'L','PHE':'F',
    'TYR':'Y','TRP':'W','ASP':'D',
    'ASN':'N','GLU':'E','GLN':'Q',
    'HIS':'H','LYS':'K','ARG':'R',
    'MET':'M','CYS':'C'}

# f1 = open('../pdb/3wtg.pdb', 'r')
# f2 = open('../pdb/4yu3.pdb', 'r')

def put_amino_position(f):
    res = []
    for i in f:
        one_atom_date = i.split()
        if (one_atom_date[0] == 'ATOM') and ((one_atom_date[2] == 'CA')): 
            amino = one_string_aminos[one_atom_date[3]]
            x = float(one_atom_date[6])
            y = float(one_atom_date[7])
            z = float(one_atom_date[8])
            res.append([amino, x, y, z])
    print("*"*300)
    for i in res:
        print(i)
        #print(len(res))
    return res

# put_amino_position(f1)
# put_amino_position(f2)