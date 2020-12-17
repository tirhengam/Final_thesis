__author__ = 'Saeideh Nazeri'

# This script Generates the files in dirhome/Bound_unbound_RSA_measure_Chains/
# format of file:  PDB_name # Chain_name # Residue_number # RSA_value_in_Bound_satet # RSA_value_in_UnBound_satet # incresing_sign(++)

from Bio.PDB import *
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Residue import *
from datetime import datetime
import shutil
import loadPdbs as loadPdbs
import os
import sys

dirGeneral= loadPdbs.dirHome+"Proteins/"
dirBound= loadPdbs.dirHome+"Bound_unbound_RSA_measure_Chains/"

def f_get_dssp(pdb_name ,structure):
    chain1_count=0
    model= structure[0]
    pdb_path=loadPdbs.f_get_dir(pdb_name)
    dssp = DSSP(model, pdb_path+pdb_name+".pdb")
    print "DSSP created for" + pdb_name+"\n"
    handlelog.write("DSSP created for" + pdb_name+"\n")
    return dssp

def f_pdb_to_chains(pdb_name,path,chain_name):
    name=pdb_name[0:5]
    path_name = "%s_%c.pdb" % (name ,chain_name)
    filenameNew=path+path_name
    if(os.path.isfile(filenameNew)):
        print filenameNew+ "Already Exist"+"\n"
        handlelog.write(filenameNew+ "Already Exist"+"\n")
        return 1;

    handle = open(filenameNew , "a+")
    filename = path+pdb_name+".pdb"
    for line in open(filename):
        if line.startswith("ATOM"):
            chain = line[21]
            if chain == chain_name:
                handle.write(line)

    handle.close()
    print path_name + " created"+"\n"
    handlelog.write(path_name + " created"+"\n")
    return 2



def f_get_chain_dssp(pdb_name, path,chain_name):
    name=pdb_name[0:4]
    pdb_chain_name = "%s_%c.pdb" % (name ,chain_name)
    p=PDBParser()
    structure=p.get_structure('X',path+pdb_chain_name)
    model= structure[0]
    dssp = DSSP(model, path+pdb_chain_name)
    print "DSSP created for " + pdb_chain_name+"\n"
    handlelog.write("DSSP created for " + pdb_chain_name+"\n")
    return dssp

def f_generate_file(pdbName):

    loadPdbs.f_dowload_pdb(pdbName)
    struct = loadPdbs.f_get_Structure(pdbName)
    dsspStruct= f_get_dssp(pdbName,struct)
    path = loadPdbs.f_get_dir(pdbName)

    fileName = pdbName+"_table.txt"
    handle = open(dirBound+fileName , "w+")
    print fileName +" created"+"\n"
    handlelog.write(fileName +" created"+"\n")
    for model in struct.get_list():
        chains = model.get_list()
        e= ' '.join(str(x) for x in chains)
        handlelog.write(e+"\n")
        k=0
        for i in range(len(chains)):
            chain = chains[i]
            chainName = str(chain)
            f_pdb_to_chains(pdbName,path,chainName[10])
            dssp_chain =f_get_chain_dssp(pdbName,path,chainName[10])

            j=0
            #print type(j)
            rsa=0
            for resiu in chain.get_list():
                try:
                    #print ("the amount of k is:%d" %k)
                    list_pdb=list(dsspStruct)[k]
                    print list_pdb
                    for item in list_pdb:
                        if(isinstance(item ,Residue)):
                            resname = item.resname
                            seq =  ' '.join (str(t) for t in item.id)
                            print "seq:" + seq
                        if(isinstance(item , int)):
                            rsaStr= str(item)
                            rsa= item


                    print ("the amount of j is:%d" %j)
                    try:
                        list_pdb_chain = list(dssp_chain)[j]
                        for item2 in list_pdb_chain:
                            if(isinstance(item2 , int)):
                                rsaChain= str(item2)
                                rsa2= item2

                    except IndexError:
                        e = sys.exc_info()[0]
                        print "%s" % e
                        line = "%s   %c   %8s   %4s  k=%d  j=%d" %(pdbName ,chainName[10] ,seq, resname,k,j)
                        handlelog.write("IndexError on(j loop): " +line+"\n")
                        break;

                    if(rsa>rsa2):
                        sign="--"
                    elif(rsa<rsa2):
                        sign = "++"
                    else:
                        sign="  "

                    line = "%s   %c   %8s   %4s   %4s   %4s  %4s" %(pdbName ,chainName[10] ,seq, resname,rsaStr,rsaChain,sign)
                    handle.write(line+'\n')
                    print line
                    j=j+1
                    k=k+1

                except IndexError:
                    line = "%s   %c   %8s   %4s  k=%d  j=%d" %(pdbName ,chainName[10] ,seq, resname,k,j)
                    handlelog.write("IndexError on(k loop): " +line +"\n")
                    break;


    handle.close()


strDateTime=str(datetime.now())
handlelog = open(dirBound+"log_file.txt" , "w+")
handlelog.write(strDateTime+"\n")
for lineP in open(dirGeneral+"pdb_final4.txt" ,"r+"):
     pdb_name = lineP[0:4]
     #print pdb_name
     handlelog.write("PDB Name:   "+lineP.rstrip()+".pdb\n")
     f_generate_file(pdb_name)
     handlelog.write("-"*60+"\n")
handlelog.close

# i=0
# for lineP in open(dirGeneral+"/results/log_file.txt" ,"r+"):
#     if lineP.startswith("PDB Name:"):
#         i=i+1
# print str(i)
# lineF = open(dirGeneral+"pdb_final.txt" ,"r+")
# searchlines = lineF.readlines()
# lineF.close()
# for line1 in enumerate(searchlines):
#     list1 = list(line1)
#     for item in list1:
#         if(isinstance(item , str)):
#             pdb = item
#
#     i=0
#     for  line2 in open(dirGeneral+"pdb_final.txt" , "r+"):
#          if(line2 ==pdb):
#              i+=1
#              if(i>1):
#                  print line2



