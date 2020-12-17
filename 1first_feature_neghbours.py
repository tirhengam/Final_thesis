__author__ = 'Saeideh Nazeri'

# This script Generates the files in .dirHome/1first_feature_neghbours/
# Neighbour of each residues in 12 Angestrom imaginary spehre ordered by distance
# format of generated file
# pdbName_chainName # Residue_Number # Ineteracting?orNo # list_of_neighbours_base_on_window_size


from Bio.PDB import *
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Residue import *
from datetime import datetime
import shutil
import os
import subprocess
import sys
from operator import itemgetter
import loadPdbs as loadPdbs

# change
Window = 9

dirGeneral = loadPdbs.dirHome + "Proteins/"
dirFasta = loadPdbs.dirHome + "Fasta/"
dirNeighbour = loadPdbs.dirHome + "1first_feature_neghbours/"

def get_key3(item):
    return item[3]


def get_key2(item):
    return item[2]


def get_key1(item):
    return item[1]


def get_key0(item):
    return item[0]


def r(x):
    return {
        'ALA': 'A',
        'ARG': 'R',
        'ASN': 'N',
        'ASP': 'D',
        'ASX': 'B',
        'CYS': 'C',
        'GLN': 'Q',
        'GLU': 'E',
        'GLX': 'Z',
        'GLY': 'G',
        'HIS': 'H',
        'ILE': 'I',
        'LEU': 'L',
        'LYS': 'K',
        'MET': 'M',
        'PHE': 'F',
        'PRO': 'P',
        'SER': 'S',
        'THR': 'T',
        'TRP': 'W',
        'TYR': 'Y',
        'UNK': ' ',
        'VAL': 'V',
        'HOH': 'O',
        ' MG': 'O',
        'GDP': 'O',
        'SO4': 'O'
    }[x]





def f_surface_file(pdbName):
    loadPdbs.f_dowload_pdb(pdbName)
    struct = loadPdbs.f_get_Structure(pdbName)
    path = loadPdbs.f_get_dir(pdbName)


    for model in struct.get_list():
        chains = model.get_list()
        e = ' '.join(str(x) for x in chains)
        handlelog.write(e+"\n")
        k = 0
        for i in range(len(chains)):
            chain = chains[i]
            chainName = str(chain)
            chain1 = model[chainName[10]]
            lenChain = len(chain)
            # change
            casta_fname = pdbName+"_"+chainName[10]+".int.surf16.fasta"
            if os.path.exists(dirFasta+"rsa16/"+casta_fname):
                with open(dirFasta+"rsa16/"+casta_fname, "r") as handle_surface:
                    handlelog.write(casta_fname+"found\n")
                    surface_data = handle_surface.readlines()

                fileName = pdbName+"_"+chainName[10] +"_rsa16_w9.txt"
                handle = open(dirNeighbour+"orderd_nearest_Res16_w9/"+fileName, "w+")
                print fileName + " created"+"\n"
                handlelog.write(fileName + " created"+"\n")

                print "the surface data is:"+ str(surface_data[2])
                lenLoop = len(surface_data[2])
                print lenLoop

                chainRange = []
                for resiu1 in chain.get_list():
                    resStr = str(resiu1).split(" ")
                    if resStr[2].startswith("het"):
                        hetem = resStr[2].split("=")
                        if hetem[1] == '':
                            seqRes = resStr[4].split("=")
                            seqRes2 = resStr[5].split("=")
                            if seqRes2[1] == '':
                                chainRange.append(seqRes[1])


                j1 = 0
                j2 = 0

                for j1 in range(lenLoop):
                    mindif = 0.0
                    list_tple = []
                    list_tple_window = []
                    tpl = ()
                    dif = []
                    pdb_indexes = []
                    surface_indexes = []
                    try :
                        index1 = int(chainRange[j1])
                        residue1 = chain[index1]
                        if residue1.has_id("CA"):
                                ca1 = residue1["CA"]
                    except IndexError:
                            continue

                    for j2 in range(lenLoop):
                        if j1 != j2:
                            try:
                                index2 = int(chainRange[j2])
                                residue2 = chain[index2]

                                if residue2.has_id("CA"):
                                    ca2 = residue2["CA"]

                                dist = ca1-ca2
                                if (dist<12.0)&(surface_data[2][j1] == 'S')&(surface_data[2][j2] == 'S'):
                                    # pdb_indexes[chainRange[j2]]= r(residue2.get_resname())
                                    # casta_indexes[j2] = round (dist , 2)
                                    #print j1 , j2 , index1 ,index2 , surface_data[1][j1] , surface_data[1][j2]
                                    tpl = r(residue2.get_resname()), index2, j2, round(dist, 2)
                                    list_tple.append(tpl)
                                    pdb_indexes.append(index2)
                                    surface_indexes.append(j2)
                                    if len(list_tple) <= Window:
                                        list_tple_window.append(tpl)
                                    elif len(list_tple) > Window:
                                        for j3 in range(len(list_tple_window)):
                                            dif[j3] = tpl[3] - list_tple_window[j3][3]
                                            if mindif > dif[j3]:
                                                mindif = dif[j3]
                                                flag=1
                                                loc=j3
                                        if flag == 1:
                                            list_tple_window[loc] = tpl

                            except IndexError:
                                continue

                    if list_tple_window:

                        # feild4 = ",".join(str(item[1]) for item in list_tple_window)
                        handlelog.write(str(sorted(list_tple_window , key =get_key3))+"\n")
                        feild5 = ",".join(str(item[2]) for item in sorted(list_tple_window , key =get_key3))
                        # feild6 = ",".join(str(item[0]) for item in list_tple_window)
                        # feild7 = ",".join(str(item[3]) for item in sorted(list_tple_window , key =get_key3))
                        # line1 = "%6s\t%3d\t%3s\t%c\t%s\t%s\t%s\t%s" %(pdbName+"_"+chainName[10], index1, j1, r(residue1.get_resname()), feild4, feild5 , feild6 , feild7)
                        line1 = "%s\t%d\t%c\t%s" % (pdbName+"_"+chainName[10], j1,  surface_data[3][j1], feild5 )
                        handle.write(line1+"\n")
                        print line1
                        # print sorted(list_tple_window)
                    # print len(list_tple_window)
                    #print sorted(list_tple , key = get_key)
                    # print len(list_tple)
                handle.close()

            else:
                handlelog.write(casta_fname +"not found !!!!\n")




strDateTime = str(datetime.now())
# change
handlelog = open(dirNeighbour+"orderd_nearest_Res16_w9/log.txt" , "w+")
handlelog.write(strDateTime+"\n")
for lineP in open(dirGeneral+"pdb_final.txt" ,"r+"):
     pdb_name = lineP[0:4]
     #print pdb_name
     handlelog.write("PDB Name:   "+lineP.rstrip()+".pdb\n")
     f_surface_file(pdb_name)
     handlelog.write("-"*60+"\n")
handlelog.close

subprocess.call(['speech-dispatcher'])
subprocess.call(['spd-say', '"Surface generated"'])

