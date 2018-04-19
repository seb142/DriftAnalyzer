import os

path = '/home/sebastian/moa-release-2017.06b'
print(os.getcwd())
print('__________')
os.chdir(path)
print(os.getcwd())
print('__________')


def evaluate(w,fx_to_fy,noise):

    for i in range(1,11):
        print('iteration:', i)
        os.system('java -cp moa.jar -javaagent:sizeofag-1.0.0.jar moa.DoTask "EvaluatePrequential -l (drift.SingleClassifierDrift -d EDDM) -s (ArffFileStream -f /home/sebastian/PythonProjects/NoiseMaker/dataset/ClassNoise/gradual/%snoise/GradualW%s%sNoise%sN%s.arff) -i 40000 -f 1 -d /home/sebastian/PythonProjects/NoiseMaker/Evaluations/GradualW%s%sNoise%sN%s.csv"'%(fx_to_fy,w,fx_to_fy,noise,i,w,fx_to_fy,noise,i))


evaluate(3000,'F1F2',0.5)
evaluate(3000,'F1F2',1)
evaluate(3000,'F1F2',1.5)


evaluate(3000,'F3F10',0.5)
evaluate(3000,'F3F10',1)
evaluate(3000,'F3F10',1.5)






'''
for i in range(1,11):
    print('iteration:', i)
    os.system('java -cp moa.jar -javaagent:sizeofag-1.0.0.jar moa.DoTask "EvaluatePrequential -l drift.SingleClassifierDrift -s (ArffFileStream -f /home/sebastian/PythonProjects/NoiseMaker/dataset/ClassNoise/abrupt/f1f2noise/noise1/AbruptW1F1F2Noise1.0N%s.arff) -i 40000 -f 1 -d /home/sebastian/PythonProjects/NoiseMaker/Evaluations/AbruptW1F1F2Noise1.0N%d.csv"'%(i,i))
#os.chdir('/moa-release-2017.06b')

for i in range(1,11):
    print('iteration:', i)
    os.system('java -cp moa.jar -javaagent:sizeofag-1.0.0.jar moa.DoTask "EvaluatePrequential -l drift.SingleClassifierDrift -s (ArffFileStream -f /home/sebastian/PythonProjects/NoiseMaker/dataset/ClassNoise/abrupt/f1f2noise/noise15/AbruptW1F1F2Noise1.5N%d.arff) -i 40000 -f 1 -d /home/sebastian/PythonProjects/NoiseMaker/Evaluations/AbruptW1F1F20Noise1.5N%d.csv"'%(i,i))
#os.chdir('/moa-release-2017.06b')

for i in range(1,11):
    print('iteration:', i)
    os.system('java -cp moa.jar -javaagent:sizeofag-1.0.0.jar moa.DoTask "EvaluatePrequential -l drift.SingleClassifierDrift -s (ArffFileStream -f /home/sebastian/PythonProjects/NoiseMaker/dataset/ClassNoise/abrupt/f5f6noise/noise05/AbruptW1F5F6Noise0.5N%d.arff) -i 40000 -f 1 -d /home/sebastian/PythonProjects/NoiseMaker/Evaluations/AbruptW1F5F6Noise0.5N%d.csv"'%(i,i))
#os.chdir('/moa-release-2017.06b')

for i in range(1,11):
    print('iteration:', i)
    os.system('java -cp moa.jar -javaagent:sizeofag-1.0.0.jar moa.DoTask "EvaluatePrequential -l drift.SingleClassifierDrift -s (ArffFileStream -f /home/sebastian/PythonProjects/NoiseMaker/dataset/ClassNoise/abrupt/f5f6noise/noise1/AbruptW1F5F6Noise1.0N%d.arff) -i 40000 -f 1 -d /home/sebastian/PythonProjects/NoiseMaker/Evaluations/AbruptW1F5F6Noise1.0N%d.csv"'%(i,i))
#os.chdir('/moa-release-2017.06b')
print("3")

for i in range(1,11):
    print('iteration:', i)
    os.system('java -cp moa.jar -javaagent:sizeofag-1.0.0.jar moa.DoTask "EvaluatePrequential -l drift.SingleClassifierDrift -s (ArffFileStream -f /home/sebastian/PythonProjects/NoiseMaker/dataset/ClassNoise/abrupt/f5f6noise/noise15/AbruptW1F5F6Noise1.5N%d.arff) -i 40000 -f 1 -d /home/sebastian/PythonProjects/NoiseMaker/Evaluations/AbruptW1F5F6Noise1.5N%d.csv"'%(i,i))
#os.chdir('/moa-release-2017.06b')
print("4")

for i in range(1,11):
    print('iteration:', i)
    os.system('java -cp moa.jar -javaagent:sizeofag-1.0.0.jar moa.DoTask "EvaluatePrequential -l drift.SingleClassifierDrift -s (ArffFileStream -f /home/sebastian/PythonProjects/NoiseMaker/dataset/ClassNoise/abrupt/f3f10noise/noise05/AbruptW1F3F10Noise0.5N%d.arff) -i 40000 -f 1 -d /home/sebastian/PythonProjects/NoiseMaker/Evaluations/AbruptW1F3F10Noise0.5N%d.csv"'%(i,i))
#os.chdir('/moa-release-2017.06b')
print("5")

for i in range(1,11):
    print('iteration:', i)
    os.system('java -cp moa.jar -javaagent:sizeofag-1.0.0.jar moa.DoTask "EvaluatePrequential -l drift.SingleClassifierDrift -s (ArffFileStream -f /home/sebastian/PythonProjects/NoiseMaker/dataset/ClassNoise/abrupt/f3f10noise/noise1/AbruptW1F3F10Noise1.0N%d.arff) -i 40000 -f 1 -d /home/sebastian/PythonProjects/NoiseMaker/Evaluations/AbruptW1F3F10Noise1.0N%d.csv"'%(i,i))
#os.chdir('/moa-release-2017.06b')
print("6")

for i in range(1,11):
    print('iteration:', i)
    os.system('java -cp moa.jar -javaagent:sizeofag-1.0.0.jar moa.DoTask "EvaluatePrequential -l drift.SingleClassifierDrift -s (ArffFileStream -f /home/sebastian/PythonProjects/NoiseMaker/dataset/ClassNoise/abrupt/f3f10noise/noise15/AbruptW1F3F10Noise1.5N%d.arff) -i 40000 -f 1 -d /home/sebastian/PythonProjects/NoiseMaker/Evaluations/AbruptW1F3F10Noise1.5N%d.csv"'%(i,i))
'''