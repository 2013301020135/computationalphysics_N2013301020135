
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


---

## *Acknowledgment*
   The program part is based on the program of [2013301020030](https://github.com/ZeganS/computationalphysics_N2013301020030/blob/master/Chapter1/ex1.py), and thanks him for helping me fixing some problems of my python plugins.


> Written with [StackEdit](https://stackedit.io/).
