---
title: "Unit 6: MATHS"
date: "March 2018"
author: "Hasan Balable"
geometry: margin=2.54cm
---

Basic Algebra
-------------
Under this very broad subheading, I will give some examples of how to rearrange mathematical statements, that you can use to simplify expressions and solve equations for unknowns.

#### Simplifying

We can collect like terms in equations to make them simpler to express.

$$4x+2y-8x+y$$

Here, 2 terms, $4x$ and $-8x$, are a product of $x$. Together they are equal to $(4-8)x=-4x$. If we do the same for the y terms and take the sum the result we get a totally simplified expression, $3y-4x$.

$$\frac{4x}{y}+\frac{3x}{2}-\frac{2y}{2}+2x$$

Here we can have 3 factor that we cannot simplify, $x$, $y$ and $x/y$. Using the same method as above, we take the 2 $x$ terms and substitute them for their the sum of the two. 

$$\frac{3x}{2}+2x=\frac{3x}{2}+\frac{4x}{2}=\frac{7x}{2}$$

Now to simplify $2y/2$:

$$\frac{2y}{2}=\frac{2}{2}\times y=1 \times y = y$$

So, the simplified expression:

$$\frac{4x}{y}+\frac{7x}{2}-y$$

#### Rearranging Equations

An equations is a statement in which two mathematical expressions are equal to each other. There is really just one rule that, so long as it is followed, makes rearranging equations simple.

>You can perform mathematical operations on each "side" of the equation, so long as you perform equal operations to all sides.

Let's start with this example:

$$x+\sqrt{4y}=5+x$$

Here, if we wanted to solve for $y$, we could subtract $x$ from each side and we are left with $\sqrt{4y}=5$. Next, we need to get rid of the square root. We can do this by taking a square of both sides. This involves multiplying both sides of the equation with an equal expression, so it still very much follows our one rule. After simplifying $\sqrt{4y}^2=5^2$, we have $4y=25$. Lastly, we can divide all sides by 4, which would leave us with $y=25/4=6.25$.

This was a simple example but the same methodology is used when solving more complex equations such as polynomials. However, unknowns in many equations can not be described by a single value, and instead are be described as an expression which describe a range of possible values. You can craft equations with these which define shapes and curves.

#### The Quadratic Equation

$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$

Where:

$$ax^2+bx+c=0$$

When solving quadratics, this equation can be used to solve for $x$. The $\pm$ symbol means that the equation is true for both a $+$ and a $-$, as most quadratics have 2 solutions.

Trigonometry
-------------
Trigonometry encompasses the studies of ratios including side lengths and angles of triangles. I will cover how to solve a triangle side or angle using trigonometry.

![trig triangle](../images/trig_triangle.png)

There is two trig equations we will be using: the Sine rule and Pythagorus's equation.

##### Pythagoras' Theorem

Pythagoras' theorem states that, with a triangle with sides labeled $a$, $b$ and $c$, where $c$ is that triangles hypotenuse:

$$a^2+b^2=c^2$$

We can use Pythagoras' theorem to calculate the length of a side of a triangle if we have the lengths of the 2 other sides. Let's try it in practice:

> I have a triangle whose opposite side is 13cm,  whose hypotenuse is 21cm  and whose adjacent side is $x$cm. Calculate $x$.

So we can substitute 13cm and 21cm for $a$ ($b$ would be equally as valid) and $c$ respectively. We now have:

$$13^2\mathrm{cm}+b^2=21^2\mathrm{cm}$$

If we subtract $13^2\mathrm{cm}$, we get $b^2=21^2\mathrm{cm}-13^2\mathrm{cm}$. Next step is to take the square root of each side, and evaluate:

$$b=\sqrt{21^2\mathrm{cm}-13^2\mathrm{cm}}=16.492$$

##### The Sine Rule

$$\frac{sin(A)}{a}=\frac{sin(B)}{b}=\frac{sin(C)}{c}$$

We can use rule to calculate lengths and angles of any triangle.
($a$, $A$), ($b$, $B$) and ($c$, $C$) refer to length and angle pairs opposite each other, as displayed in the diagram earlier in this section.

Let's use this rule to solve for x in this triangle.

![trig triangle](../images/trig_triangle_2.png)

###### Substituting known values

First step is to substitute our known values into this rule. It is useful to note that $sin(90)=1$.

$$\frac{1}{15\mathrm{cm}}=\frac{sin(38\degree)}{x\mathrm{cm}}$$

###### Taking the reciprocal

Next, we can take the reciprocal (flip the fraction) of each side. This still fits our one rule as it is the same as raising the expression on each side by a power of $-1$.

i.e. 
>$x^{-1}=\frac{1}{x}$
> 
>$\frac{4}{x}^{-1}=\frac{1}{x}\times4=\frac{4}{x}$

###### Move known terms to one side

$$15\mathrm{cm}=\frac{x\mathrm{cm}}{sin(38\degree)}$$

We can do this by multiplying each side by $sin(38\degree)$, leaving us with a single expression, $15sin(38\degree)$, which, when evaluated, is equal to $x$.

$$15sin(38\degree)=x\mathrm{cm}=9.235\mathrm{cm}$$

###### Using the inverse sine function

When solving for an angle using the sine rule you are left with an unknown in the sine function, after using the standard operators. Here is an example:

$$\frac{sin(90)}{5}=\frac{sin(x)}{4}$$
$$\frac{4}{5}=sin(x)$$

Here we can use the inverse sin function ($sin^{-1}()$) to solve for x:

$$sin^{-1}\left(\frac{4}{5}\right)=53.130\degree$$


Vectors
-------------

A vector is a quantity with more than 1 dimension. It has both a direction and a magnitude. In 2D space, we can use vectors to describe the difference between 2 points. For example, if we had 2 points, $a(13.6,\space4.2)$ and $b(-3,\space1.1)$, we could find the vector betweem them by finding the difference between the $x$ and $y$ components of the points. We can describe the vector from $a$ to $b$ as $\vec{ab}$.

$$\vec{ab}=\begin{pmatrix}
-3-13.6\\1.1-4.2
\end{pmatrix}=
\begin{pmatrix}
+16.6\\-3.1
\end{pmatrix}$$

We can now manupulate this vector the similarly to how we would scalar quantities (one-dimensional quantities). 

Adding and subtracting vectors is easy. Let me show you an algebraic example with my two 3-dimentional vectors: $\vec{p}$ and $\vec{q}$

$$
\vec{p}=\begin{pmatrix}
x_{1}\\y_{1}\\z_{1}
\end{pmatrix},\space
\vec{q}=\begin{pmatrix}
x_{2}\\y_{2}\\z_{2}
\end{pmatrix}
$$
$$
\vec{p}+\vec{q}=\begin{pmatrix}
x_{1}+x_{2}\\y_{1}+y_{2}\\z_{1}+z_{2}
\end{pmatrix},\space\vec{p}-\vec{q}=\begin{pmatrix}
x_{1}-x_{2}\\y_{1}-y_{2}\\z_{1}-z_{2}
\end{pmatrix}
$$

Matrices
-------------

#### Addition

Adding and subtracting matrices from other matrices is only possible for matrices with the same dimentions. Here we will add two 2 by 2 matrices together. It is as simple as just finding the sum of each corresponding value.

$$\begin{pmatrix}3&7\\-9&8\end{pmatrix}+\begin{pmatrix}-1&-3\\5&6\end{pmatrix}=\begin{pmatrix}3-1&7-3\\-9+5&8+6\end{pmatrix}=\begin{pmatrix}2&4\\-4&14\end{pmatrix}$$

#### Multiplication

Multiplication is a little more difficult. The number of rows in  matrix 1 must match the number of columns in the second matrix. You solve them each row/column pair at a time.

$$\begin{pmatrix}4&2&-1\\3&-5&2\\\end{pmatrix}\times
\begin{pmatrix}2&6\\1&8\\1&2\end{pmatrix}=$$
$$
\begin{pmatrix}
    \begin{pmatrix}4&2&-1\end{pmatrix}\times
    \begin{pmatrix}2\\1\\1\end{pmatrix}
&
    \begin{pmatrix}4&2&-1\end{pmatrix}\times
    \begin{pmatrix}6\\8\\2\end{pmatrix}
\\
    \begin{pmatrix}3&-5&2\end{pmatrix}\times
    \begin{pmatrix}2\\1\\1\end{pmatrix}
&
    \begin{pmatrix}3&-5&2\end{pmatrix}\times
    \begin{pmatrix}6\\8\\2\end{pmatrix}
&\end{pmatrix}
$$

Let's first try to solve the first value of our new matrix. To do this we need to know how to multiply a row by a column. We just multiply each value from starting from the left of the row, to its corresponding value in the column, counting starting from the top.

$$\begin{pmatrix}4&2&-1\end{pmatrix}\times
\begin{pmatrix}2\\1\\1\end{pmatrix}=
(4\times2)+(2\times1)+(-1\times1)=9$$

Now we just do that for each other row & column pair, and then we have our result.

$$\begin{pmatrix}4&2&-1\end{pmatrix}\times
\begin{pmatrix}6\\8\\2\end{pmatrix}=
(4\times6)+(2\times8)+(-1\times2)=38$$

$$\begin{pmatrix}3&-5&2\end{pmatrix}\times
\begin{pmatrix}2\\1\\1\end{pmatrix}=
(3\times2)+(-5\times1)+(2\times1)=3$$

$$\begin{pmatrix}3&-5&2\end{pmatrix}\times
\begin{pmatrix}6\\8\\2\end{pmatrix}=
(3\times6)+(-5\times8)+(2\times2)=-18$$

###### The result:

$$\begin{pmatrix}4&2&-1\\3&-5&2\\\end{pmatrix}\times
\begin{pmatrix}2&6\\1&8\\1&2\end{pmatrix}=\begin{pmatrix}9&38\\3&-18\end{pmatrix}$$



Mechanics
-------------

##### Equations of motion

$v=at+u$
$s=ut+\frac{1}{2}at^2$
$s=\frac{1}{2}(v+u)t$
$v^2=u^2+2as$
$s=vt-\frac{1}{2}at^2$

These equations of motion, usually called SUVAT equations, can be used to model motion under constant acceleration. The letters $s$, $u$, $v$, $a$ & $t$ are used to form these equations (hence SUVAT). This is what each letter means:

- **s**: Displacement.
- **u**: Initial velocity.
- **v**: Final velocity.
- **a**: Acceleration.
- **t**: Time.

If we have a scenario in which we have a number of these elements, we can substitute them into one of these equations in an attempt to solve an unknown. For example, take this problem:

>A man throws a football, which leaves his hand at .3m/s, 140cm from the ground. Assuming that his hand was in line with his front foot as the ball left his hand, how far from the man is the position of the ball as it first touches the ground?

Assuming that the force of gravity on his planet is equal to $-9.81\mathrm{m/s}^2$, here is the information we know, for each component in $x$ and $y$.

###### $x$ component

- $s_{x}=$ ? (What we need to find)
- $u_{x}=$ $0.3\mathrm{m/s}$
- $v_{x}=$ $0.3\mathrm{m/s}$
- $a_{x}=$ $0\mathrm{m/s}^2$
- $t=$ ?

###### $y$ component

- $s_{y}=$ $1.4\mathrm{m}$
- $u_{y}=$ $0\mathrm{m/s}$
- $v_{y}=$ ?
- $a_{y}=$ $-9.81\mathrm{m/s}^2$
- $t=$ ?


If we solve for the time ($t$) using the y component, we can then use it to find $s_{x}$. We can use the second equation for this: $s=ut+\frac{1}{2}at^2$. First let's rearrange for $t$.

First we will multiply each side by 2, for nicer numbers:
$$2s=2u_{y}t+a_{y}t^2$$

Then we can subtract $2s_{y}$ from each side, to create a quadratic:
$$a_{y}t^2+2u_{y}t-2s_{y}=0$$

Then solve for $t$ using the quadratic equation:

>$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$

$$a=a_{y},\space b=2u_{y},\space c=2s_{y}$$

$$t=\frac{-2u_{y}\pm\sqrt{2u_{y}^2-4a_{y}2s_{y}}}{2a_{y}}$$

Now we can substitute in our values:
$$t=\frac{-0\pm\sqrt{0^2-4(-9.81)(2*1.4)}}{2(-9.81)}$$
And simplify:
$$t=\frac{\pm\sqrt{-4(-9.81)(2.8)}}{2(-9.81)}=
\frac{\pm\sqrt{109.872}}{-19.62}=\pm0.534$$

We'll discard the negative value as it doesn't really make sense in our scenario. Now we know how long it took for the ball to hit the floor ($t$). We can use it to solve for $s_{x}$ and find the solution to this problem. This next equation seems right for solving the x component:

$$s=\frac{1}{2}(v+u)t$$

We just need to substitute in our values:

$$s_{x}=\frac{1}{2}(0.3\mathrm{m/s}+0.3\mathrm{m/s})\times0.534\mathrm{m}=0.3\mathrm{m/s}\times0.534\mathrm{m}$$
$$s_{x}=0.160\mathrm{m}=16\mathrm{cm}$$

And there is our result. Clearly he isn't a very good throw.

Mechanics is important in everyday work for many visual effects artists, namely artists in the FX department. Something that makes digital performances seem so believeable on screen is the way objects move and are interacted with in a physically realistic way.  Simulations of particles, fluids, cloth, hair and others are all based on how dynamics in the real world behave. This was just a very basic example.