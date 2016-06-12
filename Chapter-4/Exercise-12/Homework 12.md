

# **The Eleventh Homework**



## *Abstract*
	The problem chosen is Problem 4.16..
	We investigate the three body problem, using the Euler-Cromer method. 
	Besides, we construct a hypothetical solar system.
	Also, we generalize the model to cover arbitrary masses of Jupiter.
    We use Python to design the programs, which can realize the purpose of this assignment. 
    This article deals with the ideas for these problems, the programs ,and the results.

---

## *Introduction*
 - The motion of celestial objects has always aroused great curiosity in fields like astronomy and astrophysics. It is worth while to study a three body system, which has a chaotic behavior so that it cannot be solved analytically.
 - There are many dramatic phenomenon in the study of planetary motion in a three body system. Now consider a hypothetical, ideal celestial system consisting of sun, earth, and a pseudo Jupiter. All experience only the gravitation produced by the others. A few of the properties for different Jupiter mass are investigated here.

---

## *Body*
### 1. Requirement
 - Problem 4.16., 4.18., or 4.20..


### 2. Ideas
 - We take the average distance between earth and sun, namely 1 AU as the unit of length, and year as the unit of time.
 - We set the initial condition, including position and velocity according to observational data.
 - Then we list out the equations of motion in the center of mass frame according to the Newton Second law: <br>![](http://latex.codecogs.com/gif.latex?%5C%5C%5Cfrac%7Bd%5E%7B2%7D%5Cvec%7Br%7D_%7BE%7D%7D%7Bdt%5E%7B2%7D%7D%3D-%5Cfrac%7BGM_%7BS%7D%7D%7Br_%7BES%7D%5E%7B3%7D%7D%5Cvec%7Br%7D_%7BES%7D-%5Cfrac%7BGM_%7BJ%7D%7D%7Br_%7BEJ%7D%5E%7B3%7D%7D%5Cvec%7Br%7D_%7BEJ%7D%20%5C%5C%5Cfrac%7Bd%5E%7B2%7D%5Cvec%7Br%7D_%7BJ%7D%7D%7Bdt%5E%7B2%7D%7D%3D-%5Cfrac%7BGM_%7BS%7D%7D%7Br_%7BJS%7D%5E%7B3%7D%7D%5Cvec%7Br%7D_%7BJS%7D-%5Cfrac%7BGM_%7BE%7D%7D%7Br_%7BJE%7D%5E%7B3%7D%7D%5Cvec%7Br%7D_%7BJE%7D%20%5C%5C%5Cfrac%7Bd%5E%7B2%7D%5Cvec%7Br%7D_%7BS%7D%7D%7Bdt%5E%7B2%7D%7D%3D-%5Cfrac%7BGM_%7BE%7D%7D%7Br_%7BSE%7D%5E%7B3%7D%7D%5Cvec%7Br%7D_%7BSE%7D-%5Cfrac%7BGM_%7BJ%7D%7D%7Br_%7BSJ%7D%5E%7B3%7D%7D%5Cvec%7Br%7D_%7BSJ%7D)
 - On top of that, we compile the program and input parameter, namely the mass of the pseudo Jupiter, then we run the program to see the trajectory of these objects.


### 3. Programs
 - [Ex12.py](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Chapter-4/Exercise-12/Ex12.py)


### 4. Results
 - We run the program, and yield the trajectories of these three body problems for several disparate cases in a plane and in 3D: 
    1. Real case, normal Jupiter mass: <br> ![Ex12-1.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-4/Exercise-12/Ex12-1.png) <br> ![Ex12-2.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-4/Exercise-12/Ex12-2.png)
    2. Imaginary case, 10 times Jupiter mass: <br> ![Ex12-3.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-4/Exercise-12/Ex12-3.png) <br> ![Ex12-4.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-4/Exercise-12/Ex12-4.png)
    3. Imaginary case, 100 times Jupiter mass: <br> ![Ex12-5.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-4/Exercise-12/Ex12-5.png) <br> ![Ex12-6.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-4/Exercise-12/Ex12-6.png)
    4. Imaginary case, 1000 times Jupiter mass: <br> ![Ex12-7.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-4/Exercise-12/Ex12-7.png) <br> ![Ex12-8.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-4/Exercise-12/Ex12-8.png)
 
---

## *Conclusion*
 - As we can see from these graphs, in a three body system, earth exhibits a chaotic motion.
 - There is no chaotic behavior in this problem, if the mass of Jupiter is much less than that of sun, for example, below ten percent of sun mass.
 - When the mass of Jupiter become comparable with that of sun, the earth would swing between these two gigantic celestial objects in a chaotic way, while Jupiter and sun still rotate around each other regularly. Of course, they may fly away from each other if the initial speeds are large enough.
 - We can conclude that the earth rotate around the sun, with precession due to the gravity of Jupiter. Also, the precession become more obvious when the mass of the pseudo Jupiter increases. However, when the Jupiter mass become large enough, earth would be throw away due to sun and Jupiter's gravity or even collide with one of them.
    
---

## *Acknowledgment*
   The program part is based on the program of [2013301020099](https://github.com/guoxiaowhu/computationalphysics_N2013301020099/blob/master/three-body.py).


> Written with [StackEdit](https://stackedit.io/).
