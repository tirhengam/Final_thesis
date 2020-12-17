__author__ = 'Saeideh Nazeri'

# This script Generates the files in .dirHome/2second_feature_sable/
# Sable value for each residue on the surface

import loadPdbs as loadPdbs

dirGeneral= loadPdbs.dirHome
dirSable= loadPdbs.dirHome + "2second_feature_sable/"

def max_rsa(x):
    return {
        'ALA': 121.0,
        'ARG': 265.0,
        'ASN': 187.0,
        'ASP': 187.0,
        'CYS': 148.0,
        'GLN': 214.0,
        'GLU': 214.0,
        'GLY': 97.0,
        'HIS': 216.0,
        'ILE': 195.0,
        'LEU': 191.0,
        'LYS': 230.0,
        'MET': 203.0,
        'PHE': 228.0,
        'PRO': 154.0,
        'SER': 143.0,
        'THR': 163.0,
        'TRP': 264.0,
        'TYR': 255.0,
        'VAL': 165.0,
        'GLX': 100.0,
        'ASX': 100.0,
        'UNK': 100.0,
        'HOH': 100.0,
        ' MG': 100.0,
        'GDP': 100.0,
        'SO4': 100.0
    }[x]

# sable_handle = open(dirGeneral+"0sable/"+pdb_name+".norm.sable")
error_handle = open(dirGeneral+"indexError.txt" ,"w+")
for lineP in open(dirGeneral+"names.txt", "r+"):
    pdb_name = lineP[0:6]
    print(pdb_name)
    i = 0
    sable_handle = open(dirGeneral+"0sable/"+pdb_name+".norm.sable","r")
    sable_lines = sable_handle.readlines()
    with open(dirGeneral+"0RSA/"+pdb_name+"_rsa.txt" , 'r+') as rsa_old:
         with open(dirSable+"empirical/"+pdb_name+"_rsa_emp.txt" , 'w+') as rsa_new:
            for line in rsa_old:
                line_list = line.rstrip().split("  ")

                while '' in line_list:
                    line_list.remove('')
                print line_list
                max_allowed = max_rsa(line_list[3])
                try:
                    value4 = int(line_list[4])/max_allowed-float(sable_lines[i].rstrip())
                    value5 = int(line_list[5])/max_allowed-float(sable_lines[i].rstrip())


                    # if value4 < 0.00:
                    #     value4 = 0.00
                    # if value5 < 0.00:
                    #     value5 =0.00
                    if value4 > 1.0 :
                        value4 = 1.0
                    if value5 > 1.0:
                        value5 = 1.0

                    line_list[4] = "%.2f" % (value4)
                    line_list[5] = "%.2f" % (value5)
                    # line_list.insert(6 ,  "%.2f" %value4)
                    # line_list.insert(7 ,  "%.2f" %value5)
                    # line_list.insert(8 ,sable_lines[i].rstrip())
                    new_line = "   " .join(line_list)
                    rsa_new.write(new_line+"\n")
                    i+=1
                    print new_line

                except IndexError:
                    error_handle.write(pdb_name + " " + str(i)+'\n')
                    value4 = int(line_list[4])/max_allowed
                    value5 = int(line_list[5])/max_allowed

                    # if value4 < 0.00:
                    #     value4 = 0.00
                    # if value5 < 0.00:
                    #     value5 = 0.00
                    if value4 > 1.0 :
                        value4 = 1.0
                    if value5 > 1.0:
                        value5 = 1.0

                    line_list[4] = "%.2f" % (value4)
                    line_list[5] = "%.2f" % (value5)
                    # line_list.insert(6 ,  "%.2f" %value4)
                    # line_list.insert(7 ,  "%.2f" %value5)
                    # line_list.insert(8 ,sable_lines[i].rstrip())
                    new_line = "   " .join(line_list)
                    rsa_new.write(new_line+"\n")
                    i+=1
                    print new_line

error_handle.close