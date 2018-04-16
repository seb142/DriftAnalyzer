import DriftAnalyzer

fxtofx = 'F1F2'
method = 'DDM'
percent = '1.0'

for i in range(1,31):
    print("iteration:",i)
    DriftAnalyzer.DriftAnalyzer(i,fxtofx,method,percent)

fxtofx = 'F5F6'
for i in range(1,31):
    print("iteration:",i)
    DriftAnalyzer.DriftAnalyzer(i,fxtofx,method,percent)

fxtofx = 'F3F10'
for i in range(1,31):
    print("iteration:",i)
    DriftAnalyzer.DriftAnalyzer(i,fxtofx,method,percent)