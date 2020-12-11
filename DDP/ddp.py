import low_level_scoring_matrix
import set_data
import hight_level_dp


amino_a = set_data.put_amino_position(f1)
amino_b = set_data.put_amino_position(f2)
hight_level_scoring_matrix = low_level_scoring_matrix.init(amino_a, amino_b)