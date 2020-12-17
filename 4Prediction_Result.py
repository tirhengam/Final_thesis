__author__ = 'Saeideh Nazeri'
import loadPdbs as loadPdbs

# This script calculates Sensetivity, Specificity,Accuracy,F1 , MCC , PPV and FRR for each cluster in cross validation_
# Dataset and at the calculate the averageof 10 dataset
# cross_valiation_datasets_directory : dirHome/Prediction_Result/Cross_validation_dataset/
# this name must change base on window size(5,9.13,17) and rsa value(5or16) and grammar type (simple or complex)
# the results are available on dirHome + "Prediction_Result/
# possible filename just for psterior viterbi:
# prediction_post_rsa16_w17_complex
# prediction_post_rsa16_w13_complex
# prediction_post_rsa16_w9_complex
# prediction_post_rsa16_w5_complex
# prediction_post_rsa16_w17_simple
# prediction_post_rsa16_w13_simple
# prediction_post_rsa16_w9_simple
# prediction_post_rsa16_w5_simple

#change
name = "prediction_post_rsa16_w17_simple"

dirGeneral =loadPdbs.dirHome + "Prediction_Result/%s/" %name
import math
snAve = spAve = ppvAve = accAve = frrAve = mccAve = FIave= 0.0
handleRes = open(dirGeneral + name +".txt" , "w+")
handleRes.write("             sen     spe     acc     FI     mcc     ppv     frr\n")
for i in range(0 , 10):
    text = "test_24_" + str(i)
    print text
    # log_handle = open(dirGeneral+text+".txt" , "w+")
    len = nPA = iPA = nPP= iPP = tp = fp = tn =fn = FI = 0.0
    sn = sp = ppv = acc = frr = mcc = 0.0

    row = []
    for lineP in open(dirGeneral + text+".pred","r+"):
        if lineP.startswith("N") | lineP.startswith("I"):
            len = len+1
            row = lineP.rstrip().split("\t")
            # print row[1] , row[0]
            if row[0] == "N":
                nPA=nPA+1
            if row[1] == "N":
                nPP=nPP+1
            if row[0] == "I":
                iPA=iPA+1
            if row[1] == "I":
                iPP=iPP+1
            if (row[0] == "I") & (row[1] == "I"):
                tp=tp+1
            if (row[0] == "N") & (row[1] == "N"):
                tn=tn+1
            if (row[0] == "I") & (row[1] == "N"):
                fn=fn+1
            if (row[0] == "N") & (row[1] == "I"):
                fp=fp+1

    sn= tp/(tp+fn)
    sp= tp/(tp+fp)
    ppv=tp/(tp+fn)
    acc=(tp+tn)/(tp+fn+tn+fp)
    frr= fp/(fp+tn)
    mcc=((tp*tn)-(fp*fn))/(math.sqrt((tp+fn)*(tp+fp)*(tn+fp)*(tn+fn)))
    FI = (2*sp*sn) / (sp+sn)
    line = "dataset%2d   %.2f    %.2f    %.2f    %.2f    %.2f    %.2f    %.2f" %(i,sn , sp , acc , FI , mcc , ppv ,frr)
    print line
    handleRes.write(line+'\n')
    snAve = snAve + sn
    spAve = spAve + sp
    ppvAve = ppvAve + ppv
    accAve = accAve + acc
    frrAve = frrAve + frr
    mccAve = mccAve + mcc
    FIave = FIave + FI

    print "sn= " + "%.2f" % sn
    print "sp= " + "%.2f" % sp
    print "FI= "+ "%.2f" % FI
    print "ppv= "+ "%.2f" % ppv
    print "acc= "+ "%.2f" % acc
    print "frr= "+ "%.2f" % frr
    print "mcc= "+ "%.2f" % mcc




print "--------AVERAGE---------------"
print "sn= " + "%.2f" % (snAve/10.0)
print "sp= " + "%.2f" % (spAve/10.0)
print "FI= " + "%.2f" % (FIave/10.0)
print "ppv= "+ "%.2f" % (ppvAve/10.0)
print "acc= "+ "%.2f" % (accAve/10.0)
print "frr= "+ "%.2f" % (frrAve/10.0)
print "mcc= "+ "%.2f" % (mccAve/10.0)
line = "Average     %.2f    %.2f    %.2f    %.2f    %.2f    %.2f    %.2f" %(snAve/10.0 , spAve/10.0 , accAve/10.0 ,
                                                                FIave/10.0 , mccAve/10.0 , ppvAve /10.0,frrAve/10.0)

print line
handleRes.write(line+'\n')

