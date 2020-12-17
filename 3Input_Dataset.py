__author__ = 'Saeideh Nazeri'
# this script generates Input data for CRH-CRF Server
# format of Input Dataset(refer to presentation slide 12,13):
# PSSM of neighbour residues with maximum length of window size # average of sable difference for window size # Interacting or No
# These datasets are devided to 10 clusters because of the method 10_fold_cross_validation
# cross_valiation_datasets_directory : dirHome/Prediction_Result/Cross_validation_dataset/

from Bio.PDB import *
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Residue import *
from datetime import datetime
import shutil
import os
import sys
import subprocess
import loadPdbs as loadPdbs

dirPssm = loadPdbs.dirHome + "PSSM_for_each_protein/"
dirRSA = loadPdbs.dirHome + "2second_feature_sable/empirical/"
zero_str = str((" %.2f" % 0.00)*20)
# change rsa(5 or 16) win(5 , 9 , 13 , 17)
rsa = 16
win = 17
Window = win+1


Input_Dataset_path = loadPdbs.dirHome +"Input_Dataset/pssm_rsa%d_w%d/" % (rsa , win)
pssm_suffix = "_%dse_w%d_pssm.txt" % (rsa , win)
surface_path=loadPdbs.dirHome +"1first_feature_neghbours/orderd_nearest_Res%d_w%d/" %(rsa,win)
surface_suffix = "_rsa%d_w%d.txt" % (rsa,win)

Cluster_path = loadPdbs.dirHome + "Prediction_Result/Cross_validation_dataset/"

def f_pssm_sorted_file(pdbName):
    pssm_fname = pdbName+".pssm"
    pssm_handle = open(dirPssm + pssm_fname)
    p_lines = pssm_handle.readlines()
    rsa_fname = pdb_name+"_rsa_emp.txt"
    rsa_handle = open(dirRSA + rsa_fname)
    r_lines = rsa_handle.readlines()
    #list_pssm = []
    # change
    for s_lines in open(surface_path + pdbName + surface_suffix):
        s_line_list = s_lines.split("\t")
        si_falg = s_line_list[2]
        current_res = int(s_line_list[1])
        near_res = s_line_list[3].rstrip().split(",")
        near_res.insert(0 , s_line_list[1].rstrip())
        # log_handle.write(str(near_res)+'\n')
        # print near_res
        i = 0
        index_list = 0
        # r_line_list = r_lines[current_res].split("   ")
        # delta_rsa = float(r_line_list[5])
        # print delta_rsa
        # r_line_list = []
        delta_rsa = 0.0
        for index in range(len(near_res)):
            rsa_index = int(near_res[index])
            # print r_lines[rsa_index-1]
            r_line_list = r_lines[rsa_index].split("   ")
            delta_rsa = delta_rsa + float(r_line_list[5])
            aligned=[]
            index_list = int(near_res[index]) + 3
            p_lines_strip = p_lines[index_list].rstrip().split(" ")
            while '' in p_lines_strip:
                p_lines_strip.remove('')
            for x in range(22, 42):
                aligned.append( "%.2f" % (int(p_lines_strip[x])/100.0))

            result = " ".join(aligned)

            # log_handle.write(str(p_lines_strip[0:2]))
            # log_handle.write(result+'\n')
            log_handle.write(result+" ")
            res_handle.write(result+" ")
            #list_pssm.insert(i, result)
            i += 1
        if i < Window:
            for x in range(0, Window-i):
                log_handle.write(zero_str+" ")
                res_handle.write(zero_str+" ")
                i += 1
        # print(delta_rsa/win+1)
        res_handle.write( "%.2f" % (delta_rsa/(float(len(near_res)))) + " ")
        log_handle.write("%.2f" % (delta_rsa/(float(len(near_res)))) + " ")
        res_handle.write(si_falg +"\n")
        log_handle.write(si_falg +"\n")
        #list_pssm.insert(i, si_falg)
        #line = "  ,  ".join(list_pssm[x] for x in range(len(list_pssm)))
        #print line
        #res_handle.write(line+"\n")
        i=0;
        # delta_rsa = 0.0

strDateTime = str(datetime.now())

for i in range(0 , 10):
    # change
    # test = "test" + str(i)
    # print test
    test = "train" + str(i)
    print test
    log_handle = open(Input_Dataset_path+test+pssm_suffix , "w+")
    for lineP in open(Cluster_path+test , "r+"):
         pdb_name = lineP[0:6]
         # print pdb_name
         result_fname = pdb_name+pssm_suffix
         res_handle = open(Input_Dataset_path+result_fname , "w+")
         f_pssm_sorted_file(pdb_name)
         res_handle.close()
         log_handle.write("\n")
    log_handle.close()

for i in range(0 , 10):
    # change
    test = "test" + str(i)
    print test
    # test = "train" + str(i)
    # print test
    log_handle = open(Input_Dataset_path+test+pssm_suffix , "w+")
    for lineP in open(Cluster_path+test , "r+"):
         pdb_name = lineP[0:6]
         # print pdb_name
         result_fname = pdb_name+pssm_suffix
         res_handle = open(Input_Dataset_path+result_fname , "w+")
         f_pssm_sorted_file(pdb_name)
         res_handle.close()
         log_handle.write("\n")
    log_handle.close()


subprocess.call(['speech-dispatcher'])        #start speech dispatcher
subprocess.call(['spd-say', '"the file generation  finshed"'])



