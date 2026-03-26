# 1. Define variables a/b/c for Scotland's population in 2004/2014/2024 (unit: million)
# 2. Calculate population change 2004-2014: d = b - a
# 3. Calculate population change 2014-2024: e = c - b (typo 2025 corrected to 2024)
# 4. Compare d and e to determine growth trend (accelerating/decelerating)
# 5. Define boolean variables X=True, Y=False, compute W=X or Y
# 6. Write truth table for W and add comments

#population of scotland in 2004(million)
a=5.08
#population of scotland in 2014(million)
b=5.33 
#population of scotland in 2024(million)
c=5.55 
#population change from 2004 to 2014
d=round(b-a, 2)
#population change from 2014 to 2024
e=round(c-b, 2)#Computers represent floating-point numbers in binary,so the result of a calculation may not be exact due to precision limitations. 
#Rounding to 2 decimal places can help mitigate this issue and provide a more accurate representation of the population change.

#Print the population changes
print(f"Population change 2004-2014 (d) = {d} million")
print(f"Population change 2014-2024 (e) = {e} million")
#Compare d and e to determine growth trend
if d>e:
    print("Conclusion: The population is decelerating in scotland.")
else:
    print("Conclusion: The population is accelerating in scotland.")

#Define boolean variables X and Y
X=True
Y=False
#Compute W=X or Y
W=X or Y
#Print the value of W
print(f"X={X}, Y={Y} → W=X or Y = {W}")

#Truth table for W=X or Y
#X	Y	W
#T  T	T
#T	F	T
#F	T	T
#F	F	F