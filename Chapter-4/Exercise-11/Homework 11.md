

# **The Eleventh Homework**



## *Abstract*
	The problem chosen is Problem 4.7..
	We investigate the double star system, using the Euler-Cromer method. 
	Besides, we construct a hypothetical solar system.
	Also, we generalize the model to cover arbitrary masses of the two objects.
    We use Python to design the programs, which can realize the purpose of this assignment. 
    This article deals with the ideas for these problems, the programs ,and the results.

---

## *Introduction*
 - There are many different situations in the study of planetary motion. Now consider a hypothetical, ideal celestial system consisting of two planets. Both experience only the gravitation produced by the other one. A few of the properties are investigated here.
 - The motion of celestial objects has always aroused great curiosity in fields like astronomy and astrophysics. It is worth while to study a two body system, which could be solved both analytically and numerically.

---

## *Body*
### 1. Requirement
 - Problem 4.7., 4.9., or 4.11..


### 2. Ideas
 - We take the average distance between earth and sun, namely 1 AU as the unit of length, and year as the unit of time.
 - Then we list out the equations of motion in the rest frame according to the Newton Second law: <br>![](http://latex.codecogs.com/gif.latex?%5Coverrightarrow%7Bv_c%7D%3D%5Cfrac%7Bm_1%5Coverrightarrow%7Bv_%7B10%7D%7D&plus;m_2%5Coverrightarrow%7Bv_%7B20%7D%7D%7D%7Bm_1&plus;m_2%7D%3Dconst) <br> ![](http://latex.codecogs.com/gif.latex?%5Coverrightarrow%7Br_c%7D%3D%5Cfrac%7Bm_1%5Coverrightarrow%7Br_1%7D&plus;m_2%5Coverrightarrow%7Br_2%7D%7D%7Bm_1&plus;m_2%7D%3D%5Coverrightarrow%7Br_%7Bc0%7D%7D&plus;%5Coverrightarrow%7Bv_c%7Dt)
 - Similarly, we have that in the center-of-mass frame: <br> ![](http://latex.codecogs.com/gif.latex?%5C%5C%5Coverrightarrow%7Br_%7B1%7D%7D%3D%5Coverrightarrow%7Br_c%7D&plus;%5Coverrightarrow%7Br_%7B1c%7D%7D%20%5C%5C%5Coverrightarrow%7Br_%7B2%7D%7D%3D%5Coverrightarrow%7Br_c%7D-%5Cfrac%7Bm_1%7D%7Bm_2%7D%5Coverrightarrow%7Br_%7B1c%7D%7D)  
 - In differential equations form we have: <br> ![](http://latex.codecogs.com/gif.latex?%5C%5C%5Cfrac%7B%5Cmathrm%7Bd%7D%20x_%7B1c%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3Dv_%7Bx1c%7D%2C%5Cfrac%7B%5Cmathrm%7Bd%7D%20v_%7Bx1c%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Calpha%20%5Cfrac%7Bx_%7B1c%7D%7D%7B%28x%7B_%7B1c%7D%7D%5E%7B2%7D&plus;y%7B_%7B1c%7D%7D%5E%7B2%7D%29%5E%7B3/2%7D%7D%20%5C%5C%5Cfrac%7B%5Cmathrm%7Bd%7D%20y_%7B1c%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3Dv_%7By1c%7D%2C%5Cfrac%7B%5Cmathrm%7Bd%7D%20v_%7By1c%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Calpha%20%5Cfrac%7By_%7B1c%7D%7D%7B%28x%7B_%7B1c%7D%7D%5E%7B2%7D&plus;y%7B_%7B1c%7D%7D%5E%7B2%7D%29%5E%7B3/2%7D%7D) <br> In which for simplicity, we denote: <br> ![](http://latex.codecogs.com/gif.latex?%5Calpha%20%3D-%5Cfrac%7BGm_2%7D%7B%281&plus;%5Cfrac%7Bm_1%7D%7Bm_2%7D%29%5E2%7D)
 - Thus we get the calculation subroutine: <br> ![](http://latex.codecogs.com/gif.latex?%5C%5Cv_%7Bx1c%2Ci&plus;1%7D%3Dv_%7Bx1c%2Ci%7D&plus;%5Calpha%20%5Cfrac%7Bx_%7B1c%2Ci%7D%7D%7B%28x%7B_%7B1c%2Ci%7D%7D%5E%7B2%7D&plus;y%7B_%7B1c%2Ci%7D%7D%5E%7B2%7D%29%5E%7B3/2%7D%7D%20dt%20%5C%5Cv_%7By1c%2Ci&plus;1%7D%3Dv_%7By1c%2Ci%7D&plus;%5Calpha%20%5Cfrac%7By_%7B1c%2Ci%7D%7D%7B%28x%7B_%7B1c%2Ci%7D%7D%5E%7B2%7D&plus;y%7B_%7B1c%2Ci%7D%7D%5E%7B2%7D%29%5E%7B3/2%7D%7Ddt%20%5C%5Cx_%7B1c%2Ci&plus;1%7D%3Dx_%7B1c%2Ci%7D&plus;v_%7Bx1c%2Ci&plus;1%7Ddt%20%5C%5Cy_%7B1c%2Ci&plus;1%7D%3Dy_%7B1c%2Ci%7D&plus;v_%7By1c%2Ci&plus;1%7Ddt)  
 - We denote the initial condition as: <br> ![](http://latex.codecogs.com/gif.latex?%5Coverrightarrow%7Bv_%7B10%7D%7D%2C%5Coverrightarrow%7Br_%7B10%7D%7D%2C%5Coverrightarrow%7Bv_%7B20%7D%7D) 
 - Finally, we compile the program and input some parameters such as the masses of two objects, the initial position, and initial velocity, then we run the program to see the trajectory of these planets.


### 3. Programs
 - [Ex11-1.py](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Chapter-4/Exercise-11/Ex11-1.py)
 - [Ex11-2.py](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Chapter-4/Exercise-11/Ex11-2.py)


### 4. Results
 - We run the program, and yield the trajectories of these two planets for several disparate cases: 
    1. Equal mass, low initial speed: <br> ![Ex11-1.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-4/Exercise-11/Ex11-1.png) <br> ![Ex11-2.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-4/Exercise-11/Ex11-2.png)
    2. Equal mass, medium initial speed: <br> ![Ex11-3.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-4/Exercise-11/Ex11-3.png) <br> ![Ex11-4.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-4/Exercise-11/Ex11-4.png)
    3. Equal mass, high initial speed: <br> ![Ex11-5.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-4/Exercise-11/Ex11-5.png) <br> ![Ex11-6.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-4/Exercise-11/Ex11-6.png)
    4. Twice mass, medium initial speed: <br> ![Ex11-7.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-4/Exercise-11/Ex11-7.png) <br> ![Ex11-8.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-4/Exercise-11/Ex11-8.png)
    5. Gigantic mass, medium initial speed: <br> ![Ex11-9.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-4/Exercise-11/Ex11-9.png) <br> ![Ex11-10.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-4/Exercise-11/Ex11-10.png)
 - We also draw out the trajectories of these two planets under different initial velocity, while all other conditions remain the same, to make a comparison: 
    1. Near mass: <br> ![Ex11-11.gif](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-4/Exercise-11/Ex11-11.gif)
    2. Incomparable mass: <br> ![Ex11-12.gif](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-4/Exercise-11/Ex11-12.gif)
 
---

## *Conclusion*
 - As we can see from these graphs, in a double star system, the two stars almost rotate around each other, while the center of mass goes along a straight line.
 - There is no chaotic behavior in this problem, it could be solved analytically.
 - When the mass of one star is much greater than the other, the sun would almost stay still, while the planet rotate around the sun with precession.
 - If the initial speed is too large, the planet may escape the gravity of the other, and break this double star system.
    
---

## *Acknowledgment*
   The program part is based on the program of [2013301020076](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/tree/master/ex11).


> Written with [StackEdit](https://stackedit.io/).
