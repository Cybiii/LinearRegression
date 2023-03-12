import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csvLS")

def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].years
        y = points.iloc[i].salary

        m_gradient += -(2/n) * x * (y - (m_now*x + b_now))
        b_gradient += -(2/n) * (y - (m_now*x + b_now)) 

    m = m_now - m_gradient*L
    b = b_now - b_gradient*L
    
    return m, b

m = 0
b = 0
L = 0.0001
iterations = 1000

for i in range(iterations):
    m, b = gradient_descent(m,b,data,L)
    
    if (i % 10 == 0):
        plt.scatter(data.years,data.salary, color = "black")
        plt.plot(list(range(0,12)), [m*x + b for x in range(0,12)], color = "blue")
        plt.show(block = False)
        plt.pause(0.2)
        plt.close("Figure 1")
        tempm = round(m,2)
        tempb = round(b,2)
        print('The equation is: y = {}x + {}'.format(tempm,tempb))





