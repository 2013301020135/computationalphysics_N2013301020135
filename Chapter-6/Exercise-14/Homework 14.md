

# **The Fourteenth Homework**



## *Abstract*
	Wave propagating along a string is an interesting question involving the time evolution of a dynamical system.
	The linearity is confirmed in the program that two Gaussian waves propagates independently with their speed and shape unruffled.
    We use Python to design the programs, which can realize the purpose of this assignment. 
    This article deals with the ideas for these problems, the programs ,and the results.

---

## *Introduction*
 - The homogeneity and additivity properties together are called the superposition principle. It can be shown that additivity implies homogeneity in all cases where α is rational; this is done by proving the case where α is a natural number by mathematical induction and then extending the result to arbitrary rational numbers. If f is assumed to be continuous as well, then this can be extended to show homogeneity for any real number α, using the fact that rationals form a dense subset of the reals.
 - In physics, a wave packet (or wave train) is a short "burst" or "envelope" of localized wave action that travels as a unit. A wave packet can be analyzed into, or can be synthesized from, an infinite set of component sinusoidal waves of different wave numbers, with phases and amplitudes such that they interfere constructively only over a small region of space, and destructively elsewhere. Each component wave function, and hence the wave packet, are solutions of a wave equation. Depending on the wave equation, the wave packet's profile may remain constant (no dispersion, see figure) or it may change (dispersion) while propagating.

---

## *Body*
### 1. Requirement
 - Problem 6.6., 6.12., or 6.16..


### 2. Ideas
 - For the propagation of waves, we have: <br> ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2y%7D%7B%5Cpartial%20t%5E2%7D%3Dc%5Cfrac%7B%5Cpartial%5E2y%7D%7B%5Cpartial%20x%5E2%7D)
 - We suppose a disturbance of the type: <br> ![](http://latex.codecogs.com/gif.latex?y_%7B0%7D%28x%29%3D%5Cexp%5B-k%28x-x_%7B0%7D%29%5E%7B2%7D%5D)
 - We apply two disturbance of the kind above at somewhere on the string, and use the program to simulate their propagation.
 - We can fetch arbitrary points to apply disturbance with arbitrary amplitudes on the string, in order to verify that two waves propagate independently.


### 3. Programs
 - [Ex14.py](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Chapter-6/Exercise-14/Ex14.py)


### 4. Results
 - We run the program, and yield the course of propagation for these to waves with disparate parameters: 
    1. `wxp_1=0`, `wxp_2=1`, and `Amp=1`: <br> ![Ex14-1.gif](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-6/Exercise-14/Ex14-1.gif) 
    2. `wxp_1=0.1`, `wxp_2=0.9`, and `Amp=0.5`: <br> ![Ex14-2.gif](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-6/Exercise-14/Ex14-2.gif) 
    3. `wxp_1=0.2`, `wxp_2=0.7`, and `Amp=1.2`: <br> ![Ex14-3.gif](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Chapter-6/Exercise-14/Ex14-3.gif) 
 
---

## *Conclusion*
 - As we can conclude from these examples, for any two waves, they propagate independently, and would not affect the propagation of the other.
 - Thee linearity is confirmed in the program that two Gaussian waves propagates independently with their speed and shape unruffled.

---

## *Acknowledgment*
   The program part is based on the program of [2013301020142](https://github.com/wuyuqiao/computationalphysics_N2013301020142/blob/master/Ex-14/gauss1.py).

> Written with [StackEdit](https://stackedit.io/).
