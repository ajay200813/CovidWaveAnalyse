CovidList = []
x = 0
y = int(input('How many days of data are you giving:  '))
while x < y:
    usrinput = int(input('Number for list:  '))
    if usrinput < 0:
        print('You have entered an invalid number please try again')
        exit()
    CovidList.append(usrinput)
    x += 1
FirstTime = True
index = 0
CovidWaves = 0
IfLastWasWave = False
for num in CovidList:
    if index == 2:
        FirstTime = False
    if FirstTime == True:
        prevNum = num
        index = 2
    if num < prevNum:
        if IfLastWasWave == True:
            prevNum = num
            index += 1
            IfLastWasWave = False
            continue
        CovidWaves += 1
        print('Wave No.{}'.format(CovidWaves))
        prevNum = num
        index += 1
        IfLastWasWave = True
        continue
    if num > prevNum:
        prevNum = num
        index += 1
        IfLastWasWave = False
        continue
print('Total Waves are {}...'.format(CovidWaves))








