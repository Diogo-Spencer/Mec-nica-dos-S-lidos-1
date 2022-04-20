"""
Program created to calculate the values needed to desing a chain sprocket.
Author: Ricardo Cutileiro
Nova Univesity School of Science and Technology
"""
import math

print("Sprocket Equation Solver:")
print("U will have to insert your chain dimenions.")
print()
print("Warning: Be sure to have the right dimensions inserted (standard dimensions):")
Unit=input("Units(mm or in):")
P= float(input("P (Chain Pitch): "))
print("If the number of teeth is a parameter your looking for insert 0.")
N= float(input("N (Number of Teeth): "))
Dr= float(input("Dr (Roller Diameter): "))

if (N==0):
    PD= float(input("PD (Sprocket Diameter): "))
    N = math.pi / (math.asin(P/PD))
    N = round(N)

if(Unit == "mm"):
    P= P / 25.4
    Dr= Dr / 25.4

Ds= 1.0005* Dr + 0.003
R= Ds/2
A= 35 + (60/N)
B= 18 - (56/N)
ac= 0.8 * Dr
M= ac * math.cos(math.radians(A))
T= ac * math.sin(math.radians(A))
E= 1.3025*Dr + 0.0015
yz= Dr*((1.4*math.sin(math.radians(17 - (64/N))))-(0.8*math.sin(math.radians(B))))
ab= 1.4*Dr
W= ab*math.cos(math.pi/N)
V= ab*math.sin(math.pi/N)
F= Dr*((0.8*math.cos(math.radians(B)))+(1.4*math.cos(math.radians(17 - (64/N))))-1.3025)-0.0015
H= math.sqrt((F**2)-(1.4*Dr-(P/2))**2)
S= (P/2)*math.cos(math.pi/N)+H*math.sin(math.pi/N)
PD= P/math.sin(math.pi/N)

PD= PD * 25.4
R= R * 25.4
M= M * 25.4
T= T * 25.4
#A is an angle
#B is an angle
E= E * 25.4
W= W * 25.4
V= V * 25.4
F= F * 25.4

print("Values in mm (or degree):")
print("PD: ", PD)
print("N: ", N, " teeth")
print("R: ",R)
print("M: ",M)
print("T: ",T)
print("A: ",A," deg")
print("B: ",B, " deg")
print("E: ",E)
print("W: ",W)
print("V: ",V)
print("F: ",F)