__author__ = 'Saeideh Nazeri'
# This script download pdb files from PDB and load PDB file to memory
# The functions are used in other scripts because for calculating the distance_
# betwwen two residue the pdb must be loaded to memory


from Bio.PDB import *
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Residue import *
from datetime import datetime
import shutil
#import 0Bound_unbound_RSA_measure_Chains.py as Bound
import os
import sys


#update this path base on the directory on your computer
dirHome= "/home/hengam/PycharmProjects/Protein_Interaction_Prediction/"
dirGeneral= dirHome+"Proteins/"
dirBound= dirHome+"0Bound_unbound_RSA_measure_Chains/"

# def f_dowload_pdb(pdb_name):
#     print "in download pdb " + pdb_name
#     Bound.handlelog.write("in download pdb " + pdb_name)
#     p=PDBList()
#     p.retrieve_pdb_file(pdb_name)
#
#
# def f_pdb_dir(pdb_name):
#     pdbPath=pdb_name[1:3]
#     pdbPath.lower();
#     print "pdbPath :" + pdbPath+"\n"
#     Bound.handlelog.write("pdbPath :" + pdbPath+"\n")
#     structName="pdb%s.ent" % pdb_name.lower()
#     print "structName:" + structName+"\n"
#     Bound.handlelog.write("structName:" + structName+"\n")
#     structDir="%s/%s" % (pdbPath.lower() , structName)
#     if(os.path.isfile(dirGeneral+structDir)):
#         newPath="%s/%s/%s.pdb" %(dirGeneral, pdbPath.lower(),pdb_name)
#         shutil.copy2(dirGeneral+structDir ,newPath)
#         print newPath +" Created"+"\n"
#         Bound.handlelog.write(newPath +" Created"+"\n")
#     print "structDir is: " +dirGeneral+structDir+"\n"
#     Bound.handlelog.write("structDir is: " +dirGeneral+structDir+"\n")
#     return dirGeneral+structDir
#
# def f_get_dir(pdb_name):
#     pdbPath=pdb_name[1:3]
#     pdbpath2= pdbPath.lower()+"/";
#     print "get dir is: "+ dirGeneral+ pdbpath2+"\n"
#     Bound.handlelog.write("get dir is: "+ dirGeneral+ pdbpath2+"\n")
#     return dirGeneral+ pdbpath2
#
# def f_get_Structure(pdb_name):
#     p=PDBParser()
#     dir2 = f_pdb_dir(pdb_name)
#     structure=p.get_structure('X', dir2)
#     print "Structure created for " + pdb_name+"\n"
#     Bound.handlelog.write("Structure created for " + pdb_name+"\n")
#     return structure