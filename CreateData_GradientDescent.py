#!/usr/bin/env python
# coding=utf-8

import random

if __name__ == '__main__':
    a = 5
    b = 10
    with open('GradientDescent_Data.txt', 'w') as f:
        for i in range(1000):
            x = random.random()*100
            x = float('%.2f' % x)
            y = a*x+b+(1 if random.random() > 0.5 else -1)*(random.random()*30)
            y = float('%.2f' % y)
            f.write(f'{x},{y}\n')
