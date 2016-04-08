# **The Third Homework**



## *Abstract*
    We use Python to design the programs, which can realize the purpose of this assignment. 
    This article deals with the ideas for these problems, the programs, and the results.

---

## *Introduction*
 - Since we are required to print our names in English letters on the screen, we need to express each letter in a figure composed of '#' with a size of 8 in width and 7 in height, so that we can print the letters clearly without occupying too much space.
 - And we can use the effect of persistence of vision, which is also the principle of movie, to enable the image to move: Clear the last image, and then display the next image, and so on. If this procedure is carried out fast enough, human would view these images as if they are moving.

---

## *Body*
### 1. Requirement

 - L1: Print your name in English letters on screen using '#';
 - L2: Print arbitrary names in any order in the same way;
 - L3: Print anything you like in a 80*80 dot square (and realize move, rotate)

### 2. Ideas

 - Actually, L1 is only a specific case of L2, so we first focus on the realization of L2. It is naturally to think that we can establish a virtual screen using `Canvas`. Then we can define the properties of this screen, including `width`, `height`, `tupMatrix`, and so on.
 - We create a 2D array (x,y) as coordinates, define right as the direction of x-axis, and down as that of y-axis.

### 3. Programs

### 4. Results

---

## Conclusion

---

## Acknowledgment



> Written with [StackEdit](https://stackedit.io/).
