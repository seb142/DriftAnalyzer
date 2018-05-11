import csv
from decimal import Decimal
from decimal import InvalidOperation

def checkIfDrift(row_number, width):
    halfWidth = width/2
    if(row_number == (10000-halfWidth) or row_number == (20000-halfWidth) or row_number == (30000-halfWidth)):
        return True
    else:
        return False
def checkIfonWindowEdge(row_number, width):
    halfWidth = width / 2
    if(row_number == (10000-halfWidth+600) or row_number == (20000-halfWidth+600) or row_number == (30000-halfWidth+600) or row_number == (40000-halfWidth+600) or row_number == (50000-halfWidth+600) or row_number == (60000-halfWidth+600) or row_number == (70000-halfWidth+600)):
        return True
    else:
        return False

def withinWindow(row_number,width):
    halfWidth = width / 2
    if(row_number > (10000-halfWidth) and row_number < (10000-halfWidth+600) or row_number > (20000-halfWidth) and row_number < (20000-halfWidth+600) or row_number > (30000-halfWidth) and row_number < (30000-halfWidth+600) or row_number > (40000-halfWidth) and row_number < (40000-halfWidth+600) or row_number > (50000-halfWidth) and row_number < (50000-halfWidth+600) or row_number > (60000-halfWidth) and row_number < (60000-halfWidth+600) or row_number > (70000-halfWidth) and row_number < (70000+halfWidth+600)):
        return True
    else:
        return False

def outsideWindow(row_number,width):
    halfWidth = width / 2
    if(row_number > (10000-halfWidth+600) and row_number < (20000-halfWidth) or row_number > (20000-halfWidth+600) and row_number < (30000-halfWidth) or row_number > (30000-halfWidth+600) and row_number < (40000-halfWidth) or row_number > (40000-halfWidth+600) and row_number < (50000-halfWidth) or row_number > (50000-halfWidth+600) and row_number < (60000-halfWidth) or row_number > (60000-halfWidth+600) and row_number < (70000-halfWidth)):
        return True
    else:
        return False

class DriftAnalyzer():

    def __init__(self, number, fxtofx, method, width,percent):
        #if(percent == '1.0'):
            #percent = '1'
        with open('/home/sebastian/PythonProjects/NoiseMaker/Evaluations/GradualClassNoise/%s/gradualW%s%sNoise%s/GradualW%s%sNoise%sN%s.csv'%(method,width,fxtofx,percent,width,fxtofx,percent, number)) as input_csv:
            print('/home/sebastian/PythonProjects/NoiseMaker/Evaluations/GradualClassNoise/%s/GradualW%s%s%s%s.csv'%(method,width,fxtofx,method, number))
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
                if(detection >= 1):
                    print("Detektering", row_number)


                if(checkIfDrift(row_number,width)):
                    #print('Row: ', row[0], ', Drift detection: ', row[10])
                    drift_identified = False
                    FN_idientified = False

                if(detection >= 1 and row_number >= 1000-(width/2)):
                    if(withinWindow(row_number,width) and drift_identified == False):
                        true_positive += detection
                        print('Row: ', row_number, ', Drift detection: ', detection, 'True positive')
                        drift_identified = True

                    elif(withinWindow(row_number,width) and drift_identified == True):
                        false_positive += 1
                        print('Row: ', row_number, ', Drift detection: ', detection, 'False positive1')

                    elif(outsideWindow(row_number,width)):
                        false_positive += 1
                        print('Row: ', row_number, ', Drift detection: ', detection, 'False positive2')

                if(checkIfonWindowEdge(row_number,width) and row_number >= 1000-width/2 and drift_identified == False and FN_idientified == False):
                    FN_idientified = True
                    false_negative += 1
                    print('Row: ', row_number, ', Drift detection: ', row[10], 'False negative')

        print("true_positive: ", true_positive, "false_positives: ", false_positive, "false_negatives: ", false_negative)

        with open('%sNoise%sPerf.csv'%(method,percent), 'a') as newFile:
            newFileWriter = csv.writer(newFile)
            newFileWriter.writerow([true_positive, false_positive, false_negative])



