# **The Third Homework**



## *Abstract*
    We use Python to design the programs, which can realize the purpose of this assignment. 
    English letters are expressed in pattern composed of '#'. 
    Different letters are organized to display names and so on.
    This article deals with the ideas for these problems, the programs ,and the results.

---

## *Introduction*
 - Since we are required to print our names in English letters on the screen, we need to express each letter in a figure composed of '#' with a size of 8 in width and 7 in height, so that we can print the letters clearly without occupying too much space.
 - And we can use the effect of persistence of vision, which is also the principle of movie, to enable the image to move: Clear the last image, and then display the next image, and so on. If this procedure is carried out fast enough, human would view these images as if they are moving.

---

## *Body*
### 1. Requirement
 - L1: Print your name in English letters on screen using '#';
 - L2: Print arbitrary names in any order in the same way;
 - L3: Print anything you like in a 80*80 dot square (and realize move, rotate).


### 2. Ideas
 - Actually, L1 is only a specific case of L2, so we first focus on the realization of L2. It is naturally to think that we can establish a virtual screen using `Canvas`. Then we can define the properties of this screen, including `width`, `height`, `tupMatrix`, and so on.
 - We create a 2D array (x,y) as coordinates, define right as the direction of x-axis, and down as that of y-axis.
 - Create a function `draw()` which cover all the points in the square, use a variable `tmp_str = ""` to save the strings, which print '#' or nothing for each point, and then print the whole virtual screen.
 - List out the 26 letters in the form of '#' dots.
 - Add the parameter `angle` and define function `rotate` in order to rotate images. We determine the width and height of the image to calculate the center point of the image. Then, we compute the coordinates of each dot according to the center after rotation.
 - Also, we must clear the screen before print the next image, a new parameter `REFRESH_RATE` is set to control the frequency of blinking.


### 3. Programs
 - [MiniGUI.py](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Exercise-3/MiniGUI.py)
 - [Ex03.py](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Exercise-3/Ex03.py)


### 4. Results
 - L1:
 ![Ex3-L1.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Exercise-3/Ex3-L1.png)
 - L2:
 ![Ex3-L2.png](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Exercise-3/Ex3-L2.png)
 - L3:
 ![Ex3-L3.gif](https://raw.githubusercontent.com/2013301020135/computationalphysics_N2013301020135/master/Exercise-3/Ex3-L3.gif)


---

## *Conclusion*
 - All the requirement L1, L2, L3 are completed.
 - Since each "pixel" --- '#' is quite large, the number of "pixel" is rather limited. As a consequence, the English letters are not so smooth or pretty.
 - The effect of rotation is not so desirable, due to the same reason above.

---

## *Acknowledgment*
   The program part is based on the program of [2013301020085](https://github.com/whuCanon/computationalphysics_N2013301020085/blob/master/homework_3/README.md).


> Written with [StackEdit](https://stackedit.io/).
