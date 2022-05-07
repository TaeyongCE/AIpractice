import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x>0, dtype= np.int)


def OR(x1,x2):
    bias = -0.4
    w = np.array([0.5,0.5])
    x = np.array([x1,x2])

    z = np.sum(w*x) + bias

    if z > 0: return 1
    else : return 0

def NOR(x1,x2):
    bias = 0.4
    w = np.array([-0.5,-0.5])
    x = np.array([x1,x2])

    z = np.sum(w*x) + bias

    if z > 0: return 1
    else : return 0

def AND(x1,x2):
    bias = -0.6
    w = np.array([0.5,0.5])
    x = np.array([x1, x2])

    z = np.sum(w*x) + bias

    if z>0: return 1
    else : return 0

def NAND(x1,x2):
    bias = 0.6
    w = np.array([-0.5,-0.5])
    x = np.array([x1, x2])

    z = np.sum(w*x) + bias

    if z>0: return 1
    else : return 0

def XOR(x1,x2):
    a = NAND(x1,x2)
    b = OR(x1,x2)
    c = AND(a,b)
    return c

def XNOR(x1,x2):
    a = NAND(x1,x2)
    b = OR(x1,x2)
    c = NAND(a,b)
    return c

def QUIZ3(x1,x2):
    bias = -0.4
    w = np.array([0.5,0])
    x = np.array([x1,x2])
    z = np.sum(w*x) + bias

    if z > 0: return 1
    else : return 0


print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))

print(XNOR(0,0))
print(XNOR(0,1))
print(XNOR(1,0))
print(XNOR(1,1))

print(XOR(0,0))
print(XOR(0,1))
print(XOR(1,0))
print(XOR(1,1))

print(QUIZ3(0,0))
print(QUIZ3(0,1))
print(QUIZ3(1,0))
print(QUIZ3(1,1))
