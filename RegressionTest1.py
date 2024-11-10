import pandas as pd
import matplotlib.pyplot as plt

xandys = pd.read_csv("data.csv")

m = 0
b = 20000
LearningRate = 0.0001
Iterations = 1000

def linearregression(m1, b1, LearningRate, xandys):

    gradientm = 0 
    gradientb = 0

    n = len(xandys)

    for i in range(n):
        x = xandys.iloc[i].years
        y = xandys.iloc[i].salary

        gradientm = gradientm + -(2/n)*(x)*(y - m1*x - b1)
        gradientb = gradientb + -(2/n)*(y - m1*x - b1)

    m = m1 - gradientm*LearningRate
    b = b1 - gradientb*LearningRate

    return m, b

for i in range(Iterations):
    m, b = linearregression(m, b, LearningRate, xandys)

    if (i % 10 == 0):
        plt.scatter(xandys.years,xandys.salary, color = "black")
        plt.plot(list(range(0,12)), [m*x + b for x in range(0,12)], color = "purple")
        plt.show(block = False)
        plt.pause(0.00001)
        plt.close("Figure 1")
        tempm = round(m,5)
        tempb = round(b,5)
        print('The equation is: y = {}x + {}'.format(tempm,tempb))