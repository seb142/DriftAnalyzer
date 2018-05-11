import DriftAnalyzer


width = 1000

fxtofx = 'F1F2'
method = 'EDDM'
percent = '1.5'

for i in range(1,11):
    print("iteration:",i)
    DriftAnalyzer.DriftAnalyzer(i,fxtofx,method,width,percent)

fxtofx = 'F3F10'
for i in range(1,11):
    print("iteration:",i)
    DriftAnalyzer.DriftAnalyzer(i,fxtofx,method,width,percent)

fxtofx = 'F1F2'
method = 'DDM'
percent = '1.5'

for i in range(1,11):
    print("iteration:",i)
    DriftAnalyzer.DriftAnalyzer(i,fxtofx,method,width,percent)

fxtofx = 'F3F10'
for i in range(1,11):
    print("iteration:",i)
    DriftAnalyzer.DriftAnalyzer(i,fxtofx,method,width,percent)

fxtofx = 'F1F2'
method = 'STEPD'
percent = '1.5'

for i in range(1,11):
    print("iteration:",i)
    DriftAnalyzer.DriftAnalyzer(i,fxtofx,method,width,percent)

fxtofx = 'F3F10'
for i in range(1,11):
    print("iteration:",i)
    DriftAnalyzer.DriftAnalyzer(i,fxtofx,method,width,percent)

width = 3000

fxtofx = 'F1F2'
method = 'EDDM'
percent = '1.5'

for i in range(1,11):
    print("iteration:",i)
    DriftAnalyzer.DriftAnalyzer(i,fxtofx,method,width,percent)

fxtofx = 'F3F10'
for i in range(1,11):
    print("iteration:",i)
    DriftAnalyzer.DriftAnalyzer(i,fxtofx,method,width,percent)

fxtofx = 'F1F2'
method = 'DDM'
percent = '1.5'

for i in range(1,11):
    print("iteration:",i)
    DriftAnalyzer.DriftAnalyzer(i,fxtofx,method,width,percent)

fxtofx = 'F3F10'
for i in range(1,11):
    print("iteration:",i)
    DriftAnalyzer.DriftAnalyzer(i,fxtofx,method,width,percent)

fxtofx = 'F1F2'
method = 'STEPD'
percent = '1.5'

for i in range(1,11):
    print("iteration:",i)
    DriftAnalyzer.DriftAnalyzer(i,fxtofx,method,width,percent)

fxtofx = 'F3F10'
for i in range(1,11):
    print("iteration:",i)
    DriftAnalyzer.DriftAnalyzer(i,fxtofx,method,width,percent)



