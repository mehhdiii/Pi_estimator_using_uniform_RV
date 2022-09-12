
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
def random_generator():
    return np.random.uniform(0, 1)


def pi_estimator():
    allx = []
    ally = []

    TOTAL_POINTS = 1000.0
    inside_circle_count = 0
    for i in range(int(TOTAL_POINTS)):
        x = random_generator()
        y = random_generator()
        r = (x**2+y**2)**0.5
        if r<=1:
            inside_circle_count+=1
        
        
        allx.append(x)
        ally.append(y)
    
    figure, axes = plt.subplots() 
    cc = plt.Circle(( 0 , 0 ), 1, color='r' )
    axes.add_patch(matplotlib.patches.Rectangle((0, 0), 1, 1))

    axes.set_aspect( 1 ) 
    axes.add_artist( cc ) 
    plt.plot(allx, ally, 'go')

    pi_estimate = 4 * inside_circle_count/TOTAL_POINTS
    print('estimated pi =', pi_estimate)
    
    plt.show()



pi_estimator()