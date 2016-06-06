

# **The Fifth Homework**



## *Abstract*
	The problem chosen is 1.2, the displacement of a horizontally uniform moving object. 
    We use Python to design the programs, which can realize the purpose of this assignment. 
    Besides, this program is a general one which not only can solve this specific problem, 
    but also can handle this sort of problem with different initial displacement, velocity, and time.
    This article deals with the ideas for these problems, the programs ,and the results.

---

## *Introduction*
 - Numerical method has been widely used as an approximation of the exact solution of an ordinary equation. To determine how well this approximation is, it is of great significance for us to determine errors of Euler Methods-how far the Euler solution found deviate from the exact solution. 
 - In this assignments, two factors-step length and the equation itself-have been discussed to show how they influence the deviation. Also, a way to approximately estimate the errors is included and illustrated using Problem 2 of chapter 1.

---

## *Body*
### 1. Requirement
 - Calculate `x` as a function of `t`.
 - Compare the results with the exact solution to `dx/dt=v`.


### 2. Ideas
 - Numerical Method is a particularly useful approach to solve an initial value problem. Take the uniform motion problem as an example, which is <br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdx%7D%7Bdt%7D%3Dv) <br>
with `v` being the velocity and initial displacement ![](http://latex.codecogs.com/gif.latex?x_%7B0%7D%3D0). <br>
The numerical approach to this problem is based on the Taylor expansion for `x(t)` at `t=0`, <br>
![](http://latex.codecogs.com/gif.latex?x%28t%29%3Dx%280%29&plus;x%7B%7D%27%280%29t&plus;%5Cfrac%7Bx%7B%7D%27%27%280%29%7D%7B2%21%7Dt%5E2&plus;...). 
 - If we take t to be small enough, it is always a good approximation to simply consider only the first two terms, leaving us with <br>
![](http://latex.codecogs.com/gif.latex?x%28t%29%5Capprox%20x%280%29&plus;x%7B%7D%27%280%29t). <br>
Similarlly by expanding `x(t)` at time `t`, we can esitimate the value of ![](http://latex.codecogs.com/gif.latex?x%28t&plus;%5CDelta%20t%29) at ![](http://latex.codecogs.com/gif.latex?t%7B%7D%27%3Dt&plus;%5CDelta%20t) to be <br>
![](http://latex.codecogs.com/gif.latex?x%28t&plus;%5CDelta%20t%29%3Dx%28t%29&plus;x%7B%7D%27%28t%29%5CDelta%20t%3Dx%28t%29+v%5CDelta%20t). <br>
 - Therefore, by repeatedly applying this method, we can estimate the value of the displacement at time ![](http://latex.codecogs.com/gif.latex?t%3D%5CDelta%20t%2C2%5CDelta%20t%2C3%5CDelta%20t%2C...) <br>
 - From latter discussion, we will see that the Euler solution of the uniform motion problem is actually the exact solution, which is the result of the first derivative of `x(t)` being constant and thus the second (and higher) derivative of it being zero.
 - To estimate how well Euler solution approaches the real solution, a comparison between the Euler solution and the exact solution is made in this assignment.
 - We select three different values of time step including `dt=0.5s`, `dt=0.2s`, `dt=0.05s`, to investigate the influence of time step length.


### 3. Programs
 - [Ex05.py](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Chapter-1/Exercise-5/Ex05.py)


### 4. Results
 - Time step `dt=0.5s`:
 ![Ex5-1.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-1/Exercise-5/Ex5-1.png)
 - Time step `dt=0.2s`:
 ![Ex5-2.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-1/Exercise-5/Ex5-2.png)
 - Time step `dt=0.05s`:
 ![Ex5-3.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-1/Exercise-5/Ex5-3.png)

---

## *Conclusion*
 - As we can see from these graphs, all the dots calculate according to the Euler method are precisely located on the analytical solution curve.
 - We can conclude from the data printed by the program that in this case, no matter how long the time step is, are exactly the exact results.
 - Since the Euler method always yield the exact results in this case, the time step length makes no difference in the results at all.

---

## *Acknowledgment*
   This homework is completely original. Thanks 2013301020145 for answering my questions about the usage of matplotlib.


> Written with [StackEdit](https://stackedit.io/).
