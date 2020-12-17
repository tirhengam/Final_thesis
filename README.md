for full version please visit: 
https://sourceforge.net/projects/predict-of-protein-interactins/files/


# Final_thesis
PREDICTION OF PROTEINPROTEIN INTERACTION SITES WITH A NEW PROBABILISTIC METHOD
presentation file in directory: presentation_saeideh_nazeri.pdf

The manual of using the scripts and generating file

first: change the home directory in loadPdbs.py file : 
dirHome= "/home/hengam/PycharmProjects/Protein_Interaction_Prediction/" to your own path on computer

Second: make or download all the folders you see in sourcefourge to the dirctory you created : 
the names of folders :  1first_feature_neghbours , 2second_feature_sable , Bound_unbound_RSA_measure_Chains , Fasta , Grammer , Input_Dataset , Prediction_Result , Proteins , PSSM_for_each_protein , Server_scripts


Third : run the python scripts th this order: (to finally rech to standard input dataset for all winow sizes and RSA value)
	you can skip this part and easily use the sample provided in Input_Dataset for RSA 16 and window size 5
	the files that are generated are quiet huge the total need 12 GIG free on your computer
	
	0Bound_unbound_RSA_measure_Chains.py
	1first_feature_neghbours.py
	2second_feature_sable.py
	3Input_Dataset.py


fourth : RUN server scripts for train and test , THe access to GRH-CRF server is needed 
         you can ask it from : http://www.biocomp.unibo.it/  professror Martelli
	

fifth : Run the 4Prediction_Result.py to see the results for each data set 
	The already calculated results are available at forlder /Prediction_Result

Good Luck
Saeideh Nazeri 
for any question feel free to contact by : saeideh.nazeri@studio.unibo.it





