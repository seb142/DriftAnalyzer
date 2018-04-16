import os


path = '/home/sebastian/moa-release-2017.06b'
print(os.getcwd())
print('__________')
os.chdir(path)
print(os.getcwd())
print('__________')

for i in range(1,31):
    print('iteration:', i)
    os.system('java -cp moa.jar -javaagent:sizeofag-1.0.0.jar moa.DoTask "EvaluatePrequential -l (drift.SingleClassifierDrift -d (STEPD -r 100)) -s (ArffFileStream -f /home/sebastian/PythonProjects/NoiseMaker/dataset/abrupt/f1f2noise/noise05/AbruptW1F1F2Noise0.5N%d.arff) -i 40000 -f 1 -d /home/sebastian/PythonProjects/NoiseMaker/Evaluations/AbruptW1F1F2Noise0.5N%dDDM.csv"'%(i,i))
#os.chdir('/moa-release-2017.06b')

for i in range(1,31):
    print('iteration:', i)
    os.system('java -cp moa.jar -javaagent:sizeofag-1.0.0.jar moa.DoTask "EvaluatePrequential -l (drift.SingleClassifierDrift -d (STEPD -r 100)) -s (ArffFileStream -f /home/sebastian/PythonProjects/NoiseMaker/dataset/abrupt/f1f2noise/noise1/AbruptW1F1F2Noise1.0N%d.arff) -i 40000 -f 1 -d /home/sebastian/PythonProjects/NoiseMaker/Evaluations/AbruptW1F1F2Noise1.0N%dDDM.csv"'%(i,i))
#os.chdir('/moa-release-2017.06b')

for i in range(1,31):
    print('iteration:', i)
    os.system('java -cp moa.jar -javaagent:sizeofag-1.0.0.jar moa.DoTask "EvaluatePrequential -l (drift.SingleClassifierDrift -d (STEPD -r 100)) -s (ArffFileStream -f /home/sebastian/PythonProjects/NoiseMaker/dataset/abrupt/f1f2noise/noise15/AbruptW1F1F2Noise1.5N%d.arff) -i 40000 -f 1 -d /home/sebastian/PythonProjects/NoiseMaker/Evaluations/AbruptW1F1F20Noise1.5N%dDDM.csv"'%(i,i))
#os.chdir('/moa-release-2017.06b')

for i in range(1,31):
    print('iteration:', i)
    os.system('java -cp moa.jar -javaagent:sizeofag-1.0.0.jar moa.DoTask "EvaluatePrequential -l (drift.SingleClassifierDrift -d (STEPD -r 100)) -s (ArffFileStream -f /home/sebastian/PythonProjects/NoiseMaker/dataset/abrupt/f5f6noise/noise05/AbruptW1F5F6Noise0.5N%d.arff) -i 40000 -f 1 -d /home/sebastian/PythonProjects/NoiseMaker/Evaluations/AbruptW1F5F6Noise0.5N%dDDM.csv"'%(i,i))
#os.chdir('/moa-release-2017.06b')

for i in range(1,31):
    print('iteration:', i)
    os.system('java -cp moa.jar -javaagent:sizeofag-1.0.0.jar moa.DoTask "EvaluatePrequential -l (drift.SingleClassifierDrift -d (STEPD -r 100)) -s (ArffFileStream -f /home/sebastian/PythonProjects/NoiseMaker/dataset/abrupt/f5f6noise/noise1/AbruptW1F5F6Noise1.0N%d.arff) -i 40000 -f 1 -d /home/sebastian/PythonProjects/NoiseMaker/Evaluations/AbruptW1F5F6Noise1.0N%dDDM.csv"'%(i,i))
#os.chdir('/moa-release-2017.06b')

for i in range(1,31):
    print('iteration:', i)
    os.system('java -cp moa.jar -javaagent:sizeofag-1.0.0.jar moa.DoTask "EvaluatePrequential -l (drift.SingleClassifierDrift -d (STEPD -r 100)) -s (ArffFileStream -f /home/sebastian/PythonProjects/NoiseMaker/dataset/abrupt/f5f6noise/noise15/AbruptW1F5F6Noise1.5N%d.arff) -i 40000 -f 1 -d /home/sebastian/PythonProjects/NoiseMaker/Evaluations/AbruptW1F5F6Noise1.5N%dDDM.csv"'%(i,i))
#os.chdir('/moa-release-2017.06b')

for i in range(1,31):
    print('iteration:', i)
    os.system('java -cp moa.jar -javaagent:sizeofag-1.0.0.jar moa.DoTask "EvaluatePrequential -l drift.SingleClassifierDrift -s (ArffFileStream -f /home/sebastian/PythonProjects/NoiseMaker/dataset/abrupt/f3f10noise/noise05/AbruptW1F3F10Noise0.5N%d.arff) -i 40000 -f 1 -d /home/sebastian/PythonProjects/NoiseMaker/Evaluations/AbruptW1F3F10Noise0.5N%dDDM.csv"'%(i,i))
#os.chdir('/moa-release-2017.06b')

for i in range(1,31):
    print('iteration:', i)
    os.system('java -cp moa.jar -javaagent:sizeofag-1.0.0.jar moa.DoTask "EvaluatePrequential -l drift.SingleClassifierDrift -s (ArffFileStream -f /home/sebastian/PythonProjects/NoiseMaker/dataset/abrupt/f3f10noise/noise10/AbruptW1F3F10Noise1.0N%d.arff) -i 40000 -f 1 -d /home/sebastian/PythonProjects/NoiseMaker/Evaluations/AbruptW1F3F10Noise1.0N%dDDM.csv"'%(i,i))
#os.chdir('/moa-release-2017.06b')

for i in range(1,31):
    print('iteration:', i)
    os.system('java -cp moa.jar -javaagent:sizeofag-1.0.0.jar moa.DoTask "EvaluatePrequential -l drift.SingleClassifierDrift -s (ArffFileStream -f /home/sebastian/PythonProjects/NoiseMaker/dataset/abrupt/f3f10noise/noise15/AbruptW1F3F10Noise1.5N%d.arff) -i 40000 -f 1 -d /home/sebastian/PythonProjects/NoiseMaker/Evaluations/AbruptW1F3F10Noise1.5N%dDDM.csv"'%(i,i))
#os.chdir('/moa-release-2017.06b')