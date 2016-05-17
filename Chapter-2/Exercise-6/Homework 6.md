

# **The Sixth Homework**



## *Abstract*
	We investigate the effects of both air drag and the reduced air density at high altitudes in order to reproduce the results in textbook for L1. 
    We generalize it to cover targets of different altitude including higher or lower than the cannon for L2.
    We use Python to design the programs, which can realize the purpose of this assignment. 
    This article deals with the ideas for these problems, the programs ,and the results.

---

## *Introduction*
 - Without air drag, the trajectory of a cannon shell would be a perfect parabola, and the maximum range occurs for a firing angle of 45°. However, when the air drag is considered, things are distinctly different: the maximum range would be a much smaller one with a firing angle about 37° .
 - Since the cannon shell could reach considerable high altitudes, we must be aware of the reduced air density. In this problem, we solved both the isothermal and adiabatic cases, and generalize the problem to cover targets at different altitudes.

---

## *Body*
### 1. Requirement
 - L1: Problem 2.9.;
 - L2: Problem 2.10. Advanced version (introducing wind resistance)------"Auxiliary Precise Striking System";
 - L3: Develop "Super Auxiliary Precise Striking System".


### 2. Ideas
 - We can write out the equations of motion for the cannon shell according to Newton's second law: <br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E%7B2%7Dx%7D%7Bdt%5E%7B2%7D%7D%3D-%5Cfrac%7BB_%7B2%7D%7D%7Bm%7Dvv_%7Bx%7D) <br> ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E%7B2%7Dy%7D%7Bdt%5E%7B2%7D%7D%3D-g-%5Cfrac%7BB_%7B2%7D%7D%7Bm%7Dvv_%7By%7D).
 - We also take the reduced air density at high altitudes into account. There are two mainstream models regard of this problem in statistical mechanics: isothermal ideal gas, and adiabatic approximation.
 - For isothermal ideal gas, the pressure `p` depends on altitudes according to <br>
![](http://latex.codecogs.com/gif.latex?p%28y%29%3Dp%280%29e%5E%7B%5E%7B-mgy/k_%7BB%7DT%7D%7D) <br>
Thus for the density: <br> ![](http://latex.codecogs.com/gif.latex?%5Crho%3D%5Crho_%7B0%7Dexp%28-y/y_%7B0%7D%29) <br> where ![](http://latex.codecogs.com/gif.latex?y_%7B0%7D%3Dk_%7BB%7DT/mg%5Capprox%201.0%5Ctimes10%5E%7B4%7D%5Ctextup%7Bm%7D), and ![](http://latex.codecogs.com/gif.latex?%5Crho_0) is the density at sea level. 
 - For adiabatic approximation, the density depends on altitudes according to <br> ![](http://latex.codecogs.com/gif.latex?%5Crho%3D%5Crho_%7B0%7D%281-%5Cfrac%7Bay%7D%7BT_%7B0%7D%7D%29%5E%7B%5Calpha%7D) <br> where ![](http://latex.codecogs.com/gif.latex?a%5Capprox6.5%5Ctimes10%5E%7B-3%7D%5Ctextup%7BK/m%7D) and ![](http://latex.codecogs.com/gif.latex?%5Calpha%5Capprox2.5) for air.
 - Since the drag force due to air resistance is proportional to the density, so for both models we have <br> ![](http://latex.codecogs.com/gif.latex?F_%7B%5Ctextup%7Bdrag%7D%7D%5E%7B*%7D%3D%5Cfrac%7B%5Crho%7D%7B%5Crho_%7B0%7D%7DF_%7B%5Ctextup%7Bdrag%7D%7D%28y%3D0%29).
 - Now we can get for isothermal ideal gas, the equations of motion become <br> ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E%7B2%7Dx%7D%7Bdt%5E%7B2%7D%7D%3D-%5Cfrac%7BB_%7B2%7D%7D%7Bm%7Dvv_%7Bx%7Dexp%28%5Cfrac%7B-y%7D%7By_%7B0%7D%7D%29) <br> ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E%7B2%7Dy%7D%7Bdt%5E%7B2%7D%7D%3D-g-%5Cfrac%7BB_%7B2%7D%7D%7Bm%7Dvv_%7By%7Dexp%28%5Cfrac%7B-y%7D%7By_%7B0%7D%7D%29).
 - Also, for adiabatic approximation, the equations of motion become <br> ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E%7B2%7Dx%7D%7Bdt%5E%7B2%7D%7D%3D-%5Cfrac%7BB_%7B2%7D%7D%7Bm%7Dvv_%7Bx%7D%281-%5Cfrac%7Bay%7D%7BT_%7B0%7D%7D%29%5E%7B%5Calpha%7D) <br> ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E%7B2%7Dy%7D%7Bdt%5E%7B2%7D%7D%3D-g-%5Cfrac%7BB_%7B2%7D%7D%7Bm%7Dvv_%7By%7D%281-%5Cfrac%7Bay%7D%7BT_%7B0%7D%7D%29%5E%7B%5Calpha%7D).
 - On top of that, we can use several numerical approaches including the simple Euler method and the Runge-Kutta method to yield the numerical solutions to these problems. The relating program is [ode.py](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Chapter-2/Exercise-6/ode.py).
 - Besides, for L2, there are two situations------the target higher or lower than the cannon. We define the altitude of the lower one of the cannon and the target as sea level, and the position of cannon as the origin in the horizontal plane. 
 - Then we design a program to scan through all possible firing angles and initial velocity in order to find the one which strikes the target precisely.
 - Also, we investigate how the firing velocity required to hit the target varies as the altitude of the target is varied.
 - We select several groups of target, and plot the trajectory of these cannon shells respectively, their firing angles and velocities are also given.


### 3. Programs
 - [Ex06-L1.py](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Chapter-2/Exercise-6/Ex06-L1.py)
 - [Ex06-L2.py](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Chapter-2/Exercise-6/Ex06-L2.py)


### 4. Results
 - In accord with the textbook, we set the initial velocity as 700m/s for L1.
 - For isothermal case, the maximum range is `26621.95m`, and the corresponding firing angle is `45.9°`:
 ![Ex6-L1-1.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-6/Ex6-L1-1.png)
 - For adiabatic case, the maximum range is `24735.75m`, and the corresponding firing angle is `43.9°`:
 ![Ex6-L1-2.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-6/Ex6-L1-2.png)
 - Without density correction, the maximum range is `22077.70m`, and the corresponding firing angle is `38.77°`:
 ![Ex6-L1-3.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-6/Ex6-L1-3.png)
 - We also perform the error analysis: ![Ex6-L1-4.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-6/Ex6-L1-4.png)
 - For L2, we define the cannon shell which strikes within `1m` from the target as successfully destroy the target.
 - We tried several disparate target, and list the data and trajectories below:
    1. (8000, 2000): firing angle `80.0°`, firing velocity `659.72m/s`. ![Ex6-L2-1.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-6/Ex6-L2-1.png)
    2. (10000, 2000): firing angle `75.5°`, firing velocity `610.48m/s`. ![Ex6-L2-2.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-6/Ex6-L2-2.png)
    3. (10000, 4000): firing angle `78.0°`, firing velocity `700.64m/s`. ![Ex6-L2-3.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-6/Ex6-L2-3.png)
    4. (8000, -2000): firing angle `80.0°`, firing velocity `605.76m/s`. ![Ex6-L2-4.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-6/Ex6-L2-4.png)
    5. (10000, -2000): firing angle `77.9°`, firing velocity `624.60m/s`. ![Ex6-L2-5.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-6/Ex6-L2-5.png)
    6. (10000, -4000): firing angle `79.0°`, firing velocity `626.46m/s`. ![Ex6-L2-6.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-6/Ex6-L2-6.png)

---

## *Conclusion*
 - As we can see from these graphs, the effects of air drag is dominant in the motion of cannon shell.
 - We can see from the charts that how we treat the air density at high altitudes have considerable effects on the trajectory of the cannon shell.
 - Just like the textbook and this passage indicates, the maximum range of a cannon shell with both air drag and density correction is approximately 20 km, which is in accord with reality.
 - The accuracy increases as time interval decrease. 
 - Besides, simple Euler method is more accurate than Runge-Kutta method in this case, and that is why I choose simple Euler method to solve this problem.
 - Also, compare the figures for L2, we find that the altitude of target has strong relation with the firing velocity.

---

## *Acknowledgment*
   The program part is based on the programs of [2013301020145](https://github.com/2013301020135/computational-physics_N2013301020145/tree/master/Exercise/Chapter%202).


> Written with [StackEdit](https://stackedit.io/).
