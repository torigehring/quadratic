import math
import sys

# Set to 1 for debugging
debug = 0

# Get inputs from user
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

bsq = math.pow(b,2)
fac = 4*a*c

# Imaginary number check
if bsq < fac:
    print("imaginary answer")
    sys.exit(1)

sqrt = math.sqrt(bsq - fac)
num = -b + sqrt
dem = 2*a
x_pos = num/dem
num_neg = -b - sqrt
x_neg = num_neg/dem

# Debug
if debug == 1:
    print("bsq = %f" % bsq)
    print("fac = %f" % fac)
    print("sqrt = %f" % sqrt)
    print("num = %f" % num)
    print("dem = %f" %dem)
    print("num_neg = %f" % num_neg)

# Print out the answer
print("x_pos = %f" %x_pos)
print("x_neg = %f" %x_neg)
