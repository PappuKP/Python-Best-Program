"""
This program is created to display simple numerical tower.
"""
def simple_digit_triangle(num) -> int:
    """
    This function prints nummerical triangle with given n-1 height
    Input: Positive integer N
    return: numerical triangle of height N-1
    """
    for i in range(1, num):
        print((10**(i)//9)*i)

# function call
N = 10
print("Numerical Triangle for height N-1:")
simple_digit_triangle(N)
