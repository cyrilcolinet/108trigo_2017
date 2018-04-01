# 108trigo - Further Fiddling with Fancy Fundamental Functions

[![Build Status](https://travis-ci.org/mrlizzard/108trigo_2017.svg?branch=master)](https://travis-ci.org/mrlizzard/108trigo_2017)

- **Binary name:** 108trigo
- **Repository name:** 109trigo_2017
- **Repository rigths:** ramassage-tek
- **Language:** Python 3

# Subject

As you may know (or not), the exponential function you know so well can be written as the sum of a power series (how beautiful...)

So does many other functions, like trigonomertic and hyperbolic functions.

These power series are extremely handy when it comes to fast approximations of all those functions. But they can also be used to exponentiate (for instance) mathematical objects (as far as they can be elevated to integer powers).
One could for example compute the cosine of a function, the exponentiate of a graph, the hyperbolic tangent of a rotation or the sine of a square matrix (what you will do)...

Given a matrix and the name of a function, your programm will apply the latter to the former, and print the result.

> :bulb: Matrices are given as arguments line by line.

> :exclamation: Obviously, matrix-managing libraries are not allowed. Hopefully, you already wrote efficient functions to compute matrix powers !

```
∼/B-MAT-200> ./108trigo -h
USAGE
	./108trigo fun a0 a1 a2....

DESCRIPTION
	fun	function to be applied, among at least "EXP", "COS", "SIN", "COSH" and "SINH"
	ai	coeficients of the matrix
```

> :exclamation: Your program output has to be strictly identical to the one below

```
∼/B-MAT-200> ./108trigo COS 4 5 9 3 3 5 0 1 9
0.70 -0.43 -1.94
-0.16 0.67 -1.23
-0.06 –0.15 0.07
```

```
∼/B-MAT-200> ./108trigo EXP 1 2 3 4
51.97 74.74
112.10 164.07
```

```
∼/B-MAT-200> ./108trigo SINH 1 0 2 0
1.18 0.00
2.35 0.00
```

> :bulb: Coefficients are split by tabulations
