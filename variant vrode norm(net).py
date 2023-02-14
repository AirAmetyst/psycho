import csv
data = []
with open('correct.csv', 'r', newline='',  encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            data.append(";".join(row))
c = 1
results = []
answers = {"Полностью согласен":7,"Кое в чем не согласен":3, "Ни то  ни другое":4,"Согласен":6,"Не согласен":2, "Кое в чем согласен":5, "Полностью не согласен":1  }
'''
for i in data[3:]:
    goal = 0
    analysis = 0
    plan = 0
    selfcontrol = 0
    correction = 0
    will = 0
    t = i.split(';')
    for j in range(185,223):
        if j-185 in [0,2,5,6,7,9,13,15,21,24,26,30,33,38]:
            goal += answers[t[j]]
        if j-185 in [1,4,6,10,15,16,17,22,27,31,32,35,36,37]:
            analysis += answers[t[j]]
        if j-185 in [2,11,17,22,23,26,27,28,33,35,36]:
            plan += answers[t[j]]
        if j-185 in [1,2,12,15,16,17,18,22,27,29,30,32,33,35,37]:
            selfcontrol += answers[t[j]]
        if j-185 in [4,8,13,14,20,24,25,26,31,34]:
            correction += answers[t[j]]
        if j-185 in [3,5,6,7,13,17,19,26,30,38,26,30,33,38]:
            will += answers[t[j]]
    results.append((((goal+42)/0.84)+((analysis+42)/0.84)+((plan+33)/0.66)+((selfcontrol+45)/0.9)+((correction+30)/0.6)+((will+30)/0.6))/6)
'''
for i in data[3:]:
    goal = 0
    analysis = 0
    plan = 0
    selfcontrol = 0
    correction = 0
    will = 0
    t = i.split(';')
    for j in range(159, 184):
        if j - 159 in [1, 3, 7, 10]:
            goal += answers[t[j]]
        if j - 159 in [6, 13, 17, 19, 24]:
            analysis += answers[t[j]]
        if j - 159 == 22:
            analysis += abs(answers[t[j]] - 8)
        if j - 159 in [0, 4, 9, 14, 20]:
            plan += abs(answers[t[j]] - 8)
        if j - 159 in [2, 5, 12, 16, 23]:
            selfcontrol += answers[t[j]]
        if j - 159 in [15, 18, 21]:
            correction += answers[t[j]]
        if j - 159 in [8, 11]:
            will += answers[t[j]]
    results.append(goal + analysis + plan + selfcontrol + correction + will)
print(results)
# for i in results:
#     print(i)
# print(len(results))