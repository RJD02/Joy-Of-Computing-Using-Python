# Question:
Assuming that num is always a 2-digit number, what is the output of the following code?
* Code:
num = int(input())
temp - num
x = len(str(num))
z = 0
while temp > 0:
	y = temp % 10
	z += y ** x
	temp //= 10
if num == z:
	print(num)
	
1. Prints the number if the sum of squares of its digits is the number itself
2. Prints the number if the sum its digits is the number itself
3. Prints the number if the product of its digits is the number itself
4. Prints nothing (**Correct)
Why?
Let's see the given question more closely..
It says that given integer is 2 digit number(say x, y)
Now if you look at the code it is taking individula digit of num, adding the squares of it.
Since there are 90 numbers which have 2 digits in it, we cannot possibly count all of them by hand.

Mathematical Proof: No 2 digit number has sum of square it's individual numbers equal to the number.
We can define a set such that S = {(x, y) : x and y are two digit numbers | x * x + y * y == xy}
So let's prove:
	Proof by contradiction.
	Let's assume that there does exist such a two digit number that when squared with it's individual numbers
	i.e. x * x + y * y = xy
	Now put x = y
	Therefore, the expression becomes,
	2 * (x ^ 2) = x ^ 2
	=> x ^ 2 = 0
	=> x = 0 * CONTRADICTION!
	Since x = 0, y = 0
	But xy = 00 is not a valid two digit number.
	Thus proved that there exists no valid two digit number whose sum of individual squares is equal to the number itself! :)