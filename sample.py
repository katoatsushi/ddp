# ATOM      2  CA  MET A   1     -10.276 -58.943 -23.782  1.00110.10           C  
# ANISOU    2  CA  MET A   1    13157  15430  13247  -5692    930    958       C  
 
# ATOM     10  CA  GLY A   2      -9.448 -56.511 -26.618  1.00 97.72           C  
# ANISOU   10  CA  GLY A   2    10419  15122  11590  -5215    106   1191       C 

# ATOM     14  CA  ARG A   3      -9.584 -53.334 -24.511  1.00 88.33           C  
# ANISOU   14  CA  ARG A   3     9104  13627  10832  -4348    540   2112       C 

#入力
input_array_a = [
    [A,[-10.276, -58.943, -23.782]],
    [GLY,[-9.448, -56.511, -26.618]],
    [ARG,[ -9.584, -53.334, -24.511]],
]

input_array_b = [
    [A,[-10.276, -58.943, -23.782]],
    [GLY,[-9.448, -56.511, -26.618]],
    [ARG,[ -9.584, -53.334, -24.511]],
]

def ddp(input_array_a , input_array_b)
    return res

from pdb import 6xb5

f = open('../pdb/6xb5.pdb', 'r', encoding='UTF-8')