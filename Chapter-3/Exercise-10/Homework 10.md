

# **The Tenth Homework**



## *Abstract*
	We investigate the Lorenz model, using the Euler-Cromer method. 
	Besides, we construct the phase-space plots for the Lorenz problem in various regimes.
    We use Python to design the programs, which can realize the purpose of this assignment. 
    This article deals with the ideas for these problems, the programs ,and the results.

---

## *Introduction*
 - Lorenz was studying the basic equations of fluid mechanics, which are known as the Navier-Stokes equations and which can be regarded as Newton’s law written in a form appropriate to a fluid. 
 - The specific situation he considered was the Rayleigh-Benard problem, which concerns a fluid in a container whose top and bottom surfaces are held at different temperatures. 
 - Indeed, he grossly simplified the problem as he reached to the so-called Lorenz equations, or equivalently, the Lorenz model, which provided a major contribution to the modern field of physics.

---

## *Body*
### 1. Requirement
 - L1: Problem 3.26.;
 - L2: Problem 3.29 or 3.31.;
 - L3: Perform a 3D exhibition of above problems using Vpython.


### 2. Ideas
 - Lorenz considered the greatly simplified version of the Navier-Stokes equations as: <br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%5Cfrac%7Bdx%7D%7Bdt%7D%3D%5Csigma%28y-x%29%5C%5C%5Cfrac%7Bdy%7D%7Bdt%7D%3D-xz&plus;rx-y%5C%5C%5Cfrac%7Bdz%7D%7Bdt%7D%3Dxy-bz) <br> 
 -  Thus we get the calculation subroutine: <br> ![](http://latex.codecogs.com/gif.latex?%5C%5Cx_%7Bi&plus;1%7D%3Dx_%7Bi%7D&plus;%5Csigma%28y_%7Bi%7D-x_%7Bi%7D%29dt%5C%5Cy_%7Bi&plus;1%7D%3Dy_%7Bi%7D&plus;%5Cleft%28-x_%7Bi%7Dz_%7Bi%7D&plus;rx_%7Bi%7D-y_%7Bi%7D%5Cright%29dt%5C%5Cz_%7Bi&plus;1%7D%3Dz_%7Bi%7D&plus;%5Cleft%28x_%7Bi%7Dy_%7Bi%7D-bz_%7Bi%7D%5Cright%29dt)
 - In this problem, we follow the custom and adopt  `σ=10` and `b=8/3`.
 - The parameter `r` is a measure of the temperature difference between the top and the bottom of the fluid. In fact, it plays the role analogous to the drive amplitude.


### 3. Programs
 - [Ex10-L1-1.py](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Chapter-3/Exercise-10/Ex10-L1-1.py)
 - [Ex10-L1-2.py](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Chapter-3/Exercise-10/Ex10-L1-2.py)


### 4. Results
 - We run the program, and yield the variation of the Lorenz variable `y` and `z` as a function of time for these required cases: <br> ![Ex10-L1-1.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-3/Exercise-10/Ex10-L1-1.png) <br> ![Ex10-L1-2.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-3/Exercise-10/Ex10-L1-2.png)
 - We also draw out the phase-space plot in xOy plane, xOz plane, and yOz plane respectivly: <br> ![Ex10-L1-3.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-3/Exercise-10/Ex10-L1-3.png) <br> ![Ex10-L1-4.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-3/Exercise-10/Ex10-L1-4.png) <br> ![Ex10-L1-5.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-3/Exercise-10/Ex10-L1-5.png)
 - Besides, a 3D phase-space plot is presented: <br> ![Ex10-L1-6.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-3/Exercise-10/Ex10-L1-6.png)
 - To be more specific, the phase-space plot of yOz when `x=0`, and that of xOz when `y=0` are given, both acquired when `r=25`: <br> ![Ex10-L1-7.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-3/Exercise-10/Ex10-L1-7.png) <br> ![Ex10-L1-8.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-3/Exercise-10/Ex10-L1-8.png)
 - Furthermore, we reconstruct the above plots when `r=35`: <br> ![Ex10-L1-9.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-3/Exercise-10/Ex10-L1-9.png) <br> ![Ex10-L1-10.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-3/Exercise-10/Ex10-L1-10.png)
 
    
---

## *Conclusion*
 - As we can see from these graphs, the Lorenz model has a chaotic characteristic. To be more precise, it become chaotic when `r` appraoches 25.
 - Our phase-space plots are more precise and vivid than the text book, and they are in accord with each other.
    
---

## *Acknowledgment*
   The program part is based on the program of [2013301020076](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/tree/master/ex10_ch3.26).


> Written with [StackEdit](https://stackedit.io/).
