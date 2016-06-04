

# **The Eighth Homework**



## *Abstract*
	We investigate the nonlinear pendulum, using the Euler-Cromer method. 
	The relationship between the amplitude and period is given numerically.
	Besides, we give an qualitatively argument to support our results.
    We use Python to design the programs, which can realize the purpose of this assignment. 
    This article deals with the ideas for these problems, the programs ,and the results.

---

## *Introduction*
 - A simple pendulum can be regarded as a particle with mass m connected by a light string to a rigid support.
 - It is convenient to consider the components of these forces parallel and perpendicular to the string.
 - According to the equation of motion, we can get the calculation subroutine using Euler-Cromer method.

---

## *Body*
### 1. Requirement
 - Investigate the nonlinear pendulum;
 - Use the Euler-Cromer method or another suitable method to give the numerical relationship between the amplitude and the period;
 - Give an intuitive argument supporting the results.


### 2. Ideas
 - We can write out the equations of motion for the nonlinear pendulum according to Newton's second law and the textbook: <br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E%7B%5E%7B2%7D%20%7D%5Ctheta%7D%7Bdt%5E%7B2%7D%7D%3D-%5Cfrac%7Bg%7D%7Bl%7D%5Csin%5Ctheta) <br> 
 - Then we can list out the calculation subroutine: <br> ![](http://latex.codecogs.com/gif.latex?%5Comega_%7Bi&plus;1%7D%3D%5Comega_%7Bi%7D-%5Cfrac%7Bg%7D%7Bl%7D%5Csin%5Ctheta%20_%7Bi%7Ddt) <br> ![](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta%20_%7Bi%7D&plus;%5Comega_%7Bi%7Ddt)
 - In this problem, we suppose the mass of the nonlinear pendulum as `1kg`, the length of the pendulum as `1m`.
 - We also set the acceleration due to gravity as `9.794m/s^2`, which is the experimental value of Wuhan.


### 3. Programs
 - [Ex08-1.py](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Chapter-3/Exercise-8/Ex08-1.py)
 - [Ex08-2.py](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Chapter-3/Exercise-8/Ex08-2.py)


### 4. Results
 - We run the program, which numerically yields the value of theta as a function of time for various amplitudes: <br> ![Ex8-1.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-3/Exercise-8/Ex8-1.png)
 - The relationship can be seen from the corresponding graph: <br> ![Ex8-2.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-3/Exercise-8/Ex8-2.png)
 - And here is the specific data which indicates the relationship between the amplitude and the period: <br> ![Ex8-3.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-3/Exercise-8/Ex8-3.png)
 - Period as a function of amplitude:  <br> ![Ex8-4.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-3/Exercise-8/Ex8-4.png)
 
    
---

## *Conclusion*
 - As we can see from these graphs, the larger the amplitude is, the longer the period.
 - To verify this qualitatively, we compare this nonlinear pendulum with the linear one. We can see that the restoring force of the nonlinear one is smaller, thus the acceleration would be smaller, as a result, the moving time would be longer, leading to a longer period.
    
---

## *Acknowledgment*
   The program part is based on the program of [2013301510086](https://github.com/newton2ndlaw/computationalphysics_N2013301510086/tree/master/Homework8).


> Written with [StackEdit](https://stackedit.io/).
