# Pi estimator
Estimates the value of PI using uniform random number generator

##The Approach: 
The steps of the algorithm are given as follows: 

1. Create a unit circle centered at origin. Consider the portion of the circle in the first quadrant. 
2. Create a unit square with corners at `(0, 0)` and `(1, 1)`.
3. Generate x, y points with Unifrom random generator. 
4. PI is given as: 
`PI = 4* points_inside_circle/points_inside_square`

Note: To check if a point lies inside circle, simply check `x^2+y^2<=1 ? inside: outside`


## Result
![Pi estimation figure](Figure_1.png)

`Estimated PI = 3.14`
