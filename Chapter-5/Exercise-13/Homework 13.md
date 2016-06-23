

# **The Thirteenth Homework**



## *Abstract*
	We write two programs which solve the capacitor problem using the Jacobi method and the SOR algorithm respectively.
	Then we investigate the number of iterations for a fixed accuracy. 
	Besides, we study it as a function of the number of grid elements and compare these two means.
    We use Python to design the programs, which can realize the purpose of this assignment. 
    This article deals with the ideas for these problems, the programs ,and the results.

---

## *Introduction*
 - In numerical linear algebra, the Jacobi method (or Jacobi iterative method) is an algorithm for determining the solutions of a diagonally dominant system of linear equations. Each diagonal element is solved for, and an approximate value is plugged in. The process is then iterated until it converges. This algorithm is a stripped-down version of the Jacobi transformation method of matrix diagonalization. The method is named after Carl Gustav Jacob Jacobi.

---

## *Body*
### 1. Requirement
 - Problem 5.3., 5.7., or 5.16..


### 2. Ideas
 - The potential obeys Laplace's equation, we can solve this partial differential equation using relaxation method.
 - Thus we can list out: ![](http://latex.codecogs.com/gif.latex?%5CDelta%20V%3D0) or <br> ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2V%7D%7B%5Cpartial%20x%5E2%7D&plus;%5Cfrac%7B%5Cpartial%5E2V%7D%7B%5Cpartial%20y%5E2%7D&plus;%5Cfrac%7B%5Cpartial%5E2V%7D%7B%5Cpartial%20z%5E2%7D%3D0)
 - And when it comes to calculation, we have: <br> ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2V%7D%7B%5Cpartial%20x%5E2%7D%5Capprox%5Cfrac%7BV%28i&plus;1%2Cj%2Ck%29&plus;V%28i-1%2Cj%2Ck%29-2V%28i%2Cj%2Ck%29%7D%7B%28%5CDelta%20x%29%5E%7B2%7D%7D) <br> which in this case reduce to <br> ![](http://latex.codecogs.com/gif.latex?V%28i%2Cj%29%3D%5Cfrac%7B1%7D%7B4%7D%5Cleft%5BV%28i&plus;1%2Cj%29&plus;V%28i-1%2Cj%29&plus;V%28i%2Cj&plus;1%29&plus;V%28i%2Cj-1%29%5Cright%5D)


### 3. Programs
 - [Ex13-1.py](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Chapter-5/Exercise-13/Ex13-1.py)
 - [Ex13-2.py](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Chapter-5/Exercise-13/Ex13-2.py)
 - [Ex13-3.py](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Chapter-5/Exercise-13/Ex13-3.py)


### 4. Results
 - We run the program, and yield the contours, and distribution graph in 3D of electric potential, and vector figure of electric field by Jacobi method: <br> ![Ex13-1.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-5/Exercise-13/Ex13-1.png) <br> ![Ex13-2.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-5/Exercise-13/Ex13-2.png)<br> ![Ex13-1.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-5/Exercise-13/Ex13-3.png)
 - Then we do the same thing using the program of SOR algorithm: <br> ![Ex13-4.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-5/Exercise-13/Ex13-4.png) <br> ![Ex13-5.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-5/Exercise-13/Ex13-5.png)<br> ![Ex13-6.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-5/Exercise-13/Ex13-6.png)
 - Finally, a comparison between these two method and the number of iterations that each requires as a function of the number of grid elements are given: <br> ![Ex13-1.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-5/Exercise-13/Ex13-7.png)
 
---

## *Conclusion*
 - Three methods are all appliable for this problem.
 - When it comes to the number of iterations for a fixed accuracy, we have that the Jacobi method is proportional to the number of grid elements, and SOR algorithm is proportional to its square.
 - Also, comparing the convergent speeds of these three different methods, we have SOR algorithm is the fastest, GS method is the second fastest, while Jacobi method is the slowest.
     
---

## *Acknowledgment*
   The program part is based on the program of [2013301020099](https://github.com/guoxiaowhu/computationalphysics_N2013301020099).

> Written with [StackEdit](https://stackedit.io/).
