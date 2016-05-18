

# **The Seventh Homework**



## *Abstract*
	We investigate the effects of backspin on batted ball for L1. 
	Besides, we generalize it to consider the situation of no spin, and also the effect of tailwind or headwind.  
    We visualize it to come up with the requirement for L2.
    Both the programs are general enough that we can set any parameters we like.
    That is to say, variable such as initial velocity, batting angle, angular velocity, wind speed, and even baseball type are all adjustable.
    We use Python to design the programs, which can realize the purpose of this assignment. 
    This article deals with the ideas for these problems, the programs ,and the results.

---

## *Introduction*
 - The equations of motion for baseball are very similar to that of cannon shell. However, they mainly distinguish at two points: there is no need to consider reduced air density for baseball, and their drag coefficients are disparate functions of velocity for each type of baseball.
 - Also, since baseball is light and its speed is not so fast, we must take the wind speed in account, including both tailwind and headwind.
 - Nevertheless, as the problem suggests, our main purpose is model the effect of spin. As we shall see later, due to Magnus force, spin would play a significant role in the motion of a batted ball.

---

## *Body*
### 1. Requirement
 - L1: Problem 2.19.;
 - L2: Visualize the motion of cannon shell or baseball using vpython.


### 2. Ideas
 - We can write out the equations of motion for the batted ball according to Newton's second law: <br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdx%7D%7Bdt%7D%3Dv_%7Bx%7D) <br> ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdy%7D%7Bdt%7D%3Dv_%7By%7D) <br> ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdv_%7Bx%7D%7D%7Bdt%7D%3D-%5Cfrac%7BB_%7B2%7D%7D%7Bm%7Dvv_%7Bx%7D-%5Cfrac%7BS_%7B0%7D%7D%7Bm%7Dv_%7Bx%7D%5Comega) <br> ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bdv_%7By%7D%7D%7Bdt%7D%3D-%5Cfrac%7BB_%7B2%7D%7D%7Bm%7Dvv_%7By%7D&plus;%5Cfrac%7BS_%7B0%7D%7D%7Bm%7Dv_%7By%7D%5Comega-g)
 - We also write out the drag coefficient function for each type of baseball:
    1. Rough baseball: <br> ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7BB_%7B2%7D%7D%7Bm%7D%3D%5Cleft%280.0013&plus;%5Cfrac%7B0.0084%7D%7B1&plus;e%5E%7B%5Cfrac%7B%28x-21%29%7D%7B2.5%7D%7D%7D%5Cright%29%5Cleft%284-%5Cfrac%7B3-e%5E%7B0.5%28x-39%29%7D%7D%7B1&plus;e%5E%7B0.5%28x-39%29%7D%7D%5Cright%29)
    2. Normal baseball: <br> ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7BB_%7B2%7D%7D%7Bm%7D%3D0.0039&plus;%5Cfrac%7B0.0058%7D%7B1&plus;e%5E%7B%5Cfrac%7B%28x-35%29%7D%7B5%7D%7D%7D)
    3. Smooth baseball: <br> ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7BB_%7B2%7D%7D%7Bm%7D%3D0.0013&plus;%5Cfrac%7B0.0084%7D%7B1&plus;e%5E%7B%5Cfrac%7B%28x-65%29%7D%7B4%7D%7D%7D)
 - In this problem, we suppose the initial height as `1.5m`, which is almost the practical value.
 - We set angular velocity as `2000rpm` according to the problem.
 - We set wind speed as `10mph` per level, that is to say, wind speed level `1` is `10mph`, level `2` is `20mph`, and so on.
 - Since our focus is the effect of backspin, there is no need to construct a three-dimension coordinate system, so a two-dimension coordinate system is enough. 
 - Then, we set the initial velocity around `45m/s`, which is about the velocity of batted ball bat by a good player.
 - To make the result more practical, we take the batted angle to be approximately `40°`.
 - Besides, for L2, we generalize the program so that we could visualize the movement of a batted ball with arbitrary angular velocity vector. Of course, the batted angle and initial velocity are also adjustable.
 - Also, we investigate some interesting phenomenons produced under some special statistics.
 - We select several groups of data, and visualize the trajectory of these batted balls by Vpython respectively, their batted angles, initial velocities, along with angular velocity vectors are also given.


### 3. Programs
 - [Ex07-L1.py](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Chapter-2/Exercise-7/Ex07-L1.py)
 - [Ex07-L2.py](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Chapter-2/Exercise-7/Ex07-L2.py)


### 4. Results
 - In accord with the textbook, we set the angular velocity of spin as 2000rpm for L1.
 - We tried several disparate groups of parameters for L1, and list the data and trajectories below, for each figure, we consider all the four situations including no spin or backspin and tailwind or headwind:
    1. Rough baseball, Initial velocity `45m/s`, batting angle `35°`, wind level `1`. The distance of batted ball with tailwind and backspin is `180m`, that with headwind and backspin is `168m`, that with tailwind and nospin is `156m`, and that with headwind and nospin is `134m`. <br> ![Ex7-L1-1.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-7/Ex7-L1-1.png)
    2. Rough baseball, Initial velocity `45m/s`, batting angle `45°`, wind level `1`. The distance of batted ball with tailwind and backspin is `152m`, that with headwind and backspin is `170m`, that with tailwind and nospin is `155m`, and that with headwind and nospin is `155m`. <br> ![Ex7-L1-2.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-7/Ex7-L1-2.png)
    3. Normal baseball, Initial velocity `45m/s`, batting angle `35°`, wind level `1`. The distance of batted ball with tailwind and backspin is `123m`, that with headwind and backspin is `101m`, that with tailwind and nospin is `112m`, and that with headwind and nospin is `93m`. <br> ![Ex7-L1-3.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-7/Ex7-L1-3.png)
    4. Normal baseball, Initial velocity `45m/s`, batting angle `45°`, wind level `1`. The distance of batted ball with tailwind and backspin is `123m`, that with headwind and backspin is `92m`, that with tailwind and nospin is `116m`, and that with headwind and nospin is `89m`. <br> ![Ex7-L1-4.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-7/Ex7-L1-4.png)
    5. Smooth baseball, Initial velocity `45m/s`, batting angle `35°`, wind level `1`. The distance of batted ball with tailwind and backspin is `120m`, that with headwind and backspin is `90m`, that with tailwind and nospin is `109m`, and that with headwind and nospin is `83m`. <br> ![Ex7-L1-5.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-7/Ex7-L1-5.png)
    6. Smooth baseball, Initial velocity `45m/s`, batting angle `45°`, wind level `1`. The distance of batted ball with tailwind and backspin is `121m`, that with headwind and backspin is `86m`, that with tailwind and nospin is `114m`, and that with headwind and nospin is `83m`. <br> ![Ex7-L1-6.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-7/Ex7-L1-6.png)
    7.  Normal baseball, Initial velocity `50m/s`, batting angle `35°`, wind level `1`. The distance of batted ball with tailwind and backspin is `140m`, that with headwind and backspin is `117m`, that with tailwind and nospin is `127m`, and that with headwind and nospin is `109m`. <br> ![Ex7-L1-7.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-7/Ex7-L1-7.png)
    8. Normal baseball, Initial velocity `50m/s`, batting angle `35°`, wind level `2`. The distance of batted ball with tailwind and backspin is `154m`, that with headwind and backspin is `106m`, that with tailwind and nospin is `140m`, and that with headwind and nospin is `101m`. <br> ![Ex7-L1-8.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-7/Ex7-L1-8.png)
 - And for L2, we also tried several groups of parameters to investigate the behavior of the batted ball, and visualize their motions by Vpython:
    1. Initial velocity `100mph`, batting angle `35°`, angular velocity vector `(20,-20,20)`. <br> ![Ex7-L2-1.gif](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-7/Ex7-L2-1.gif)
    2. Initial velocity `120mph`, batting angle `35°`, angular velocity vector `(20,-20,20)`. <br> ![Ex7-L2-2.gif](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-7/Ex7-L2-2.gif)
    3. Initial velocity `100mph`, batting angle `45°`, angular velocity vector `(20,-20,20)`. <br> ![Ex7-L2-3.gif](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-7/Ex7-L2-3.gif)
    4. Initial velocity `100mph`, batting angle `35°`, angular velocity vector `(20,-20,300)`. <br> ![Ex7-L2-4.gif](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-2/Exercise-7/Ex7-L2-4.gif)
    
---

## *Conclusion*
 - As we can see from these graphs, the type of baseball has dramatic effect on the range of a batted ball.
 - Generally speaking, batted ball travels further under tailwind than headwind, but according to the function of drag coefficient (rough ball), under some specific circumstance, it is also possible for a baseball to travel further under headwind than tailwind. Figure Ex7-L1-2 is a good example of this.
 - Also, the effect of wind speed and direction depends greatly on other parameters such as angular velocity, initial velocity, baseball type, and so on.
 - Just like the textbook and this passage indicates, commonly the maximum range of a batted ball of normal type by an excellent player is around `120m`, which is in accord with reality.
 - We can infer from figure Ex7-L2-4 that when angular velocity is large enough at some proper component, it is possible for the ball to turn back and form a spiral trajectory.
 - For smooth ball and rough ball, which drag coefficient would reach a relative small value under specific condition, proper parameters could yield a extremely far range more than `200m`.

---

## *Acknowledgment*
   The program part for L1 is based on the program of [2013301510017](https://github.com/mma2101/computationalphysics_N2013301510017/blob/master/Chapter_2/homework07_L1_2.19.py) and the program for L2 is based on the program of [2013301020145](https://github.com/chenfeng2013301020145/computational-physics_N2013301020145/blob/master/Exercise/Chapter%202/chapter2.19_visual.py).


> Written with [StackEdit](https://stackedit.io/).
