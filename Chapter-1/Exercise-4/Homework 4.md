

# **The Forth Homework**



## *Abstract*
    The problem chosen is 1.1, the velocity of a freely falling object. 
    We use Python to design the programs, which can realize the purpose of this assignment. 
    Besides, this program is a general one which not only can solve this specific problem, 
    but also can handle this sort of problem with different initial velocity and time.
    This article deals with the ideas for these problems, the programs ,and the results.

---

## *Introduction*
 - Numerical method has been widely used as an approximation of the exact solution of an ordinary equation. To determine how well this approximation is, it is of great significance for us to determine errors of Euler Methods-how far the Euler solution found deviate from the exact solution. 
 - In this assignments, two factors-step length and the equation itself-have been discussed to show how they influence the deviation. Also, a way to approximately estimate the errors is included and illustrated using Problem 1 of chapter 1.

---

## *Body*
### 1. Requirement
 - Calculate `v` as a function of `t`;
 - Repeat the calculation for several different values of the time step;
 - Compare the results with the exact solution to `dv/dt=-g`;
 - Verify that for this case the Euler method gives the exact result.


### 2. Ideas
 - Numerical Method is a particularly useful approach to solve an initial value problem. Take the free falling problem as an example, which is <br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdv%7D%7Bdt%7D%3D-g) <br>
with `g` being the acceleration due to gravity and initial velocity ![](http://latex.codecogs.com/gif.latex?v_%7B0%7D%3D0). <br>
The numerical approach to this problem is based on the Taylor expansion for `v(t)` at `t=0`, <br>
![](http://latex.codecogs.com/gif.latex?v%28t%29%3Dv%280%29&plus;v%7B%7D%27%280%29t&plus;%5Cfrac%7Bv%7B%7D%27%27%280%29%7D%7B2%21%7Dt%5E2&plus;...). 
 - If we take t to be small enough, it is always a good approximation to simply consider only the first two terms, leaving us with <br>
![](http://latex.codecogs.com/gif.latex?v%28t%29%5Capprox%20v%280%29&plus;v%7B%7D%27%280%29t). <br>
Similarlly by expanding `v(t)` at time `t`, we can esitimate the value of ![](http://latex.codecogs.com/gif.latex?v%28t&plus;%5CDelta%20t%29) at ![](http://latex.codecogs.com/gif.latex?t%7B%7D%27%3Dt&plus;%5CDelta%20t) to be <br>
![](http://latex.codecogs.com/gif.latex?v%28t&plus;%5CDelta%20t%29%3Dv%28t%29&plus;v%7B%7D%27%28t%29%5CDelta%20t%3Dv%28t%29-g%5CDelta%20t). <br>
 - Therefore, by repeatedly applying this method, we can estimate the value of the velocity at time ![](http://latex.codecogs.com/gif.latex?t%3D%5CDelta%20t%2C2%5CDelta%20t%2C3%5CDelta%20t%2C...) <br>
 - From latter discussion, we will see that the Euler solution of the free falling problem is actually the exact solution, which is the result of the first derivative of `v(t)` being constant and thus the second (and higher) derivative of it being zero.
 - To estimate how well Euler solution approaches the real solution, a comparison between the Euler solution and the exact solution is made in this assignment.
 - We select three different values of time step including `dt=0.5s`, `dt=0.2s`, `dt=0.05s`, to investigate the influence of time step length.


### 3. Programs
 - [Ex04.py](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Chapter-1/Exercise-4/Ex04.py)


### 4. Results
 - Time step `dt=0.5s`:
 ![Ex4-1.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-1/Exercise-4/Ex4-1.png)
 - Time step `dt=0.2s`:
 ![Ex4-2.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-1/Exercise-4/Ex4-2.png)
 - Time step `dt=0.05s`:
 ![Ex4-3.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-1/Exercise-4/Ex4-3.png)


---

## *Conclusion*
 - As we can see from these graphs, all the dots calculate according to the Euler method are precisely located on the analytical solution curve.
 - We can conclude from the data printed by the program that in this case, no matter how long the time step is, are exactly the exact results.
 - Since the Euler method always yield the exact results in this case, the time step length makes no difference in the results at all.

---

## *Acknowledgment*
   The program part is based on the program of [2013301020030](https://github.com/ZeganS/computationalphysics_N2013301020030/blob/master/Chapter1/ex1.py), and thanks him for helping me fixing some problems of my python plugins.


> Written with [StackEdit](https://stackedit.io/).
