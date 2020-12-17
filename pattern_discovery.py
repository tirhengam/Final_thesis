__author__ = 'hengam'



from Bio.PDB import *
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Residue import *
from datetime import datetime
import shutil
import os
import sys
import subprocess
import loadPdbs as loadPdbs

dirFasta = loadPdbs.dirHome + "Fasta/rsa16/"
dirPattern = loadPdbs.dirHome + "Pattern/"
zero_str = str((" %.2f" % 0.00)*20)
# change rsa(5 or 16) win(5 , 9 , 13 , 17)
rsa = 16
win = 17
Window = win+1

surface_path=loadPdbs.dirHome +"1first_feature_neghbours/orderd_nearest_Res%d_w%d/" %(rsa,win)
surface_suffix = "_rsa%d_w%d.txt" % (rsa,win)

Cluster_path = loadPdbs.dirHome + "Prediction_Result/Cross_validation_dataset/"

def f_pattern_neighbour(pdbName , handle):
    fasta_fname = pdbName+".int.surf16.fasta"
    fasta_handle = open(dirFasta + fasta_fname)
    p_lines = fasta_handle.readlines()
    #list_pssm = []
    # change
    for s_lines in open(surface_path + pdbName + surface_suffix):
        s_line_list = s_lines.split("\t")
        p_line_list = p_lines[3]
        current_res = int(s_line_list[1])
        near_res = s_line_list[3].rstrip().split(",")
        near_res.insert(0 , s_line_list[1].rstrip())
        # log_handle.write(str(near_res)+'\n')
        # print near_res
        i = 0

        print  p_line_list
        print s_line_list[3]
        s_line_detail=[]
        for index in range(len(near_res)):
            rsa_index = int(near_res[index])
            #print rsa_index , p_line_list[rsa_index]
            s_line_detail.append(p_line_list[rsa_index])

        print s_line_detail
        str3 = "  ".join(s_line_detail)
        print str3
        line = "%s    %s   %s   %s                   %s" %(s_line_list[0],s_line_list[1],s_line_list[2], s_line_list[3] ,str3)
        handle.write(line+'\n')








strDateTime = str(datetime.now())

for i in range(0 , 1):
    # change
    # test = "test" + str(i)
    # print test
    test = "train" + str(i)
    print test

    for lineP in open(Cluster_path+test , "r+"):
         pdb_name = lineP[0:6]
         # print pdb_name
         result_fname = pdb_name+".pat"
         res_handle = open(dirPattern+result_fname , "w+")
         f_pattern_neighbour(pdb_name , res_handle)
         res_handle.close()



for i in range(0 , 1):
    # change
    test = "test" + str(i)
    print test
    # test = "train" + str(i)
    # print test

    for lineP in open(Cluster_path+test , "r+"):
         pdb_name = lineP[0:6]
         # print pdb_name
         result_fname = pdb_name+".pat"
         res_handle = open(dirPattern+result_fname , "w+")
         f_pattern_neighbour(pdb_name , res_handle)
         res_handle.close()




subprocess.call(['speech-dispatcher'])        #start speech dispatcher
subprocess.call(['spd-say', '"the file generation  finshed"'])