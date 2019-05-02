import csv
import math


class Speed():
    def __init__(self):
        self.dataset1 = {}
        self.dataset2 = {}


    def readDataset1(self):
        with open('dataset1.txt') as fp:
            fp = csv.reader(fp, delimiter = ',')
            line_count = 0
            for row in fp:
                # row will be list of words separated by delimiter
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    self.dataset1[row[0]] = float(row[1])
                    line_count += 1
        return self.dataset1

    def readDataset2(self):
        with open('dataset2.txt') as fp:
            fp = csv.reader(fp, delimiter = ',')
            line_count = 0
            for row in fp:
                # row will be list of words separated by delimiter
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    self.dataset2[row[0]] = float(row[1])
                    line_count += 1
        return self.dataset2

def getSpeed():
    s = Speed()
    d1 = s.readDataset1()
    d2 = s.readDataset2()
    g = 9.8
    res = {}
    for dinasour in d1:
        if dinasour in d2:
            res[dinasour] = ((d2[dinasour]/d1[dinasour])-1)* math.sqrt(d1[dinasour] * g)
    res = sorted(res.items(), key=lambda x: x[1], reverse= True)
    for dino in res:
        print(dino[0])


if __name__ == "__main__":
    getSpeed()