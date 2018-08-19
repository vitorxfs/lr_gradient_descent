import math
import Tkinter
import matplotlib.pyplot as plt
from numpy import *

def plot(p):
    n = len(p)

    q = []
    r = []

    for i in range(n): #putting X values into q[] and Y values into r[]
        q.append(p[i][0]) 
        r.append(p[i][1])

           
    '''PLOTTING THE DATA'''


    plt.plot(q, r, 'ro') #plotting the points of the input

    return sorted(q)

    #plotting the line found
    


def compute_error(b, m, p):

    totalError = 0

    for i in range(0, len(p)):
        x = p[i][0]
        y = p[i][1]

        totalError += ((m * x + b) - y) **2
        #totalError += (y- ((m * x) + b)) ** 2

    return totalError / float(len(p))


def step_gradient(b_current, m_current, points, learning_rate):
    b_gradient = 0
    m_gradient = 0

    N = float(len(points))

    for i in range(0, len(points)):
        x = points[i][0]
        y = points[i][1]

        b_gradient += (2/N) * (((m_current * x) + b_current) - y)
        m_gradient += (2/N) * x * (((m_current * x) + b_current) - y)

    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)


    return [new_b, new_m]


def gradient_descent_run(p, starting_b, starting_m, learning_rate, num_iterations, s):
    b = starting_b
    m = starting_m

    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(p), learning_rate)
        plt.plot([s[0], s[-1]], [m*s[0] + b, m*s[-1] + b])

    return [b, m]




def run():
    #p = [ [1,3], [2,6], [3,7], [4,10], [5,10], [6,12] ] #data used for test - it will be changed by a file
    #p = [[80,220], [100,180], [120,140], [140,125], [160,95]] #- another amount of data

    p = genfromtxt("data.csv", delimiter=",") #opening data file

    learning_rate = 0.0001
    iterations = 1000

    initial_b = 0
    initial_m = 0

    s = plot(p)

    print 'starting gd at b = {0}, m = {1}, error = {2}'.format(initial_b, initial_m, compute_error(initial_b, initial_m, p))

    [b, m] = gradient_descent_run(p, initial_b, initial_m, learning_rate, iterations, s)

    print 'ending point at b = {0}, m = {1}, error = {2}'.format(b, m, compute_error(b, m, p))

    plt.show()


if __name__ == "__main__": #defining a main function
    run()