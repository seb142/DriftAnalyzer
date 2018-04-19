import csv
from decimal import Decimal
from decimal import InvalidOperation

class DriftAnalyzer():

    def __init__(self, number, fxtofx, method, percent):
        with open('/home/sebastian/PythonProjects/NoiseMaker/Evaluations/AbruptClassNoise/%s/abrupt%sNoise%s/AbruptW1%sNoise%sN%s.csv'%(method,fxtofx,percent,fxtofx,percent,number)) as input_csv:
            #print('/home/sebastian/PythonProjects/NoiseMaker/Evaluations/%s/abrupt%sNoise%s/AbruptW1%sNoise%sN%s.csv'%(method,fxtofx,percent,fxtofx,percent,number))
            readCSV = csv.reader(input_csv, delimiter=',')
            true_positive = 0
            false_positive = 0
            false_negative = 0
            next(readCSV, None)
            FN_idientified = False
            drift_identified = False


            for row in readCSV:
                try:
                    row_number = Decimal(row[0])
                    detection = Decimal(row[10])
                except(InvalidOperation, IndexError):
                    break

                if(row_number % 2500 == 0):
                    #print('Row: ', row[0], ', Drift detection: ', row[10])
                    drift_identified = False
                    FN_idientified = False

                if(detection == 1 and row_number >= 2500):
                    if(row_number%2500<100 and drift_identified == False):
                        print('Row: ', row_number, ', Drift detection: ', detection, 'True positive')
                        drift_identified = True
                        true_positive += 1

                    elif(row_number%2500<100 and drift_identified == True):
                        print('Row: ', row_number, ', Drift detection: ', detection, 'False positive')
                        false_positive += 1

                    elif(row_number%2500>100):
                        print('Row: ', row_number, ', Drift detection: ', detection, 'False positive')
                        false_positive += 1

                if(row_number%2500 ==100 and row_number >= 2500 and drift_identified == False and FN_idientified == False):
                    FN_idientified = True
                    print('Row: ', row_number, ', Drift detection: ', row[10], 'False negative')
                    false_negative += 1

        print("true_positive: ", true_positive, "false_positives: ", false_positive, "false_negatives: ", false_negative)

        with open('%sNoise%sPerf.csv'%(method,percent), 'a') as newFile:
            newFileWriter = csv.writer(newFile)
            newFileWriter.writerow([true_positive, false_positive, false_negative])
