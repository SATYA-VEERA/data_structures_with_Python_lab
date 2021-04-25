""" Python Script to find GCD and LCM of 3 numbers """

# Write your code from here

import math

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

gcd_xyz = math.gcd(math.gcd(x, y), z)
gcd_xy = math.gcd(x, y)
gcd_xz = math.gcd(x, z)
gcd_yz = math.gcd(y, z)

lcm_xyz = int((x*y*z*gcd_xyz)/(gcd_xy*gcd_yz*gcd_xz))

print("gcd and lcm of ",x, ",", y, ",", z, " are ", gcd_xyz, ",", lcm_xyz, "respectively")
