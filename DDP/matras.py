# # 二枚貝ヘモグロビン(3g46) vs シアノバクテリアC-フィコシアニン(1gh0)
# ddp_a = 'MKTPLTEAVSVADSQGRFLSSTEIQVAFGRFRQAKAGLEAAKALTSKADSLISGAAQAVYNKFPYTTQM----QGPNYAADQRGKDKCARDIGYYLRMVTYCLIAGGTGPMDEYLIAGIDEINRTFELSPSWYIEALKYIKANHGLSGDAAVEANSYLDYAINALS'
# ddp_b = 'PSVYDAAAQLTAD-------------------VKKDLRDSWKVIGSDKKGNGVALMTTLFADNQETIGYFKRLGDVSQGMANDKLRGHSITLMYALQNF-IDQLDNPDDLVCVVEKFAVNHITRKISAAEFGKINGPIKKVLASKNFGDKYANAWAKLVAVVQAAL'
# matras_a = 'RFRQAKAGLEAAKALTSKADSLISGAAQAVYNKFPYTTQMQGPNYAAD-QRG-----KDKCARDIGYYLRMVTYCLIAG----GTGPMDEYLIAGIDEINRTFELSPSWYIEALKYIKANHGLSGDAAVEANSYLDYAINAL'
# matras_b = 'TADVKKDLRDSWKVIGSDKKGNGVALMTTLFADNQETI-----GYFKRLGDVSQGMANDKLRGHSITLMYALQNFIDQLDNPDDLVCVVEKFAVNHI-TRKISAAEFGKINGPIKKVLASKNFGDKYANAWAKLVAVVQAAL'
# 二枚貝ヘモグロビン(3g46) vs ヒトヘモグロビン(4hhb)
# ddp_a = 'VLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHF-DL-SHG-SAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLTSKYR'
# ddp_b ='PSVYDAAAQLTADVKKDLRDSWKVIGSDKKGNGVALMTTLFADNQETIGYFKRLGDVSQGMANDKLRGHSITLMYALQNFIDQL-DNPDDL-----VCVVEKFAVNHITRKISAAEFGKINGPIKKVLASKNFGDKYANAWAKL'
# matras_a = 'VLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFD-LSH--GSAQVKGHGKKVADALTNAVAHVD---DMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLT'
# matras_b = 'QLTADVKKDLRDSWKVIGSDKKGNGVALMTTLFADNQETIGYFKRLGDVSQGMANDKLRGHSITLMYALQNFIDQLDNPDDLVCVVEKFAVNHI-TRKISAAEFGKINGPIKKVLAS-KN--FGDKYANAWAKLVAVVQAA-L'
# ヒトヘモグロビン(4hhb) vs シアノバクテリアC-フィコシアニン(1gh0)
# ddp_a = 'VLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLTSKYR'
# ddp_b = 'MKTPLTEAVSVADSQGRFLSSTEIQVAFGRFRQAKAGLEAAKALTSKAD-SLISGAAQAV-YNKFPY----TTQMQGPNYAADQRGKDKCARDIGYYLRMVTYCLIAGGTGPMDEYLIAGIDEINRTFELSPSWYIEALKY'
# matras_a = 'SPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTK-----TYFPHFDLSHGSAQVKGHGKKVADALTNAVAH--VDDMPNA-LSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLT'
# matras_b = 'RFRQAKAGLEAAKALTSKADSLISGAAQAVYNKFPYTTQMQGPNYAADQRG---KDKCARDIGYYLRMVTYCLIAGGTGPMDEYLIAGIDEIN-RTFELSPSWYIEALKYIKANHG------LSGDAAVEANSYLDYAINALS'
# アズリン(4azu)とプラストシアニン(7pcy)
ddp_a = 'AAIVKLGGDDGSLAFVPNNITVG-AGESI-EFINNA--G---FPHNIV---------FDEDAVPAGV--------DADAISAEDYLNS-KGQTV----VRKLTTPGTYGVYCDPHSGAGMKMTITVQ'
ddp_b = 'AECSVDIQGNDQMQFNTNAITVDKSCKQFTVNLSHPGNLPKNVMGHNWVLSTAADMQGVVTDGMASGLDKDYLKPDDSRVIAHTKLIGSGEKDSVTFDVSKLKEGEQYMFFCTFPGHSALMKGTLTL'
matras_a = 'AAIVKLGGDDGSLAFVpNNITVGAGE-SIEFINNAG-------FpHNIVFDEDAVPAGV-----------------DADAISAEDYLN-SKGQTVVRK---LTTPGTYGVYCDP--HSGAGMKMTITVQ'
matras_b = 'ECSVDIQGN-DQMQFNTNAITVDKSCKQFTVNLSHPGNLPKNVMGHNWVLSTAADMQGVVTDGMASGLDKDYLKPDDSRVIAHTKLIGSGEKDSVTFDVSKLKEGEQYMFFCTFPGHSAL-MKGTLTLK'


matras_arrays = [matras_a,matras_b]
ddp_array = [ddp_a, ddp_b]

matras_ddp_match_and_unmatch_score = 0
matras_match_and_unmatch_score = 0
ddp_match_and_unmatch_score = 0
for ddp, matras in zip(ddp_array, matras_arrays):
    #ギャップの部分を除く
    if ddp[0] != '-' and ddp[1] != '-' and matras[0] != '-' and matras[1] != '-':
        # マトラスとDDPで共通のマッチミスマッチカラムについて
        # マトラスとDDPで共通のマッチカラム
        if ddp[0] == ddp[1] and matras[0] == matras[1] and ddp[0] == matras[0]:
            matras_ddp_match_and_unmatch_score += 1
        # マトラスとDDPで共通のミスマッチカラム
        elif ddp[0] != ddp[1] and matras[0] != matras[1] and ddp[0] == matras[0] and ddp[1] == matras[1]:
            matras_ddp_match_and_unmatch_score += 1
        # DDPだけで見られるマッチミスマッチカラム
        # DDPだけで見られるマッチカラム
        elif ddp[0] == ddp[1] and ddp != matras:
            ddp_match_and_unmatch_score += 1
        # DDPだけで見られるミスマッチカラム
        elif ddp[0] != ddp[1] and ddp != matras:
            ddp_match_and_unmatch_score += 1
        # matrasだけでみられるマッチミスマッチカラム
        # matrasだけで見られるマッチカラム
        elif matras[0] == matras[1] and ddp != matras:
            matras_match_and_unmatch_score += 1
        # matrasだけで見られるミスマッチカラム
        elif matras[0] != matras[1] and ddp != matras:
            matras_match_and_unmatch_score += 1

Jaccard = matras_ddp_match_and_unmatch_score/(matras_ddp_match_and_unmatch_score + matras_match_and_unmatch_score + ddp_match_and_unmatch_score)

print('マトラスとDDPで共通のマッチミスマッチカラム:', matras_ddp_match_and_unmatch_score)
print('マトラスだけでみられるマッチミスマッチカラム:', matras_match_and_unmatch_score)
print('DDPだけで見られるマッチミスマッチカラム:', ddp_match_and_unmatch_score)
print('Jaccardは:', Jaccard)


# 方針
# A=マトラスとDDPで共通のマッチミスマッチカラム
# B=マトラスだけでみられるマッチミスマッチカラム
# C=DDPだけで見られるマッチミスマッチカラム
# Jaccard=A/(A+B+C)
# マッチカラム＝同じアミノ酸がアラインメントされたカラム   AA
# ミスマッチカラム＝違ったアミノ酸がアラインメントされたカラム   AE
# ギャップカラム＝ギャップが入っているカラム     A-