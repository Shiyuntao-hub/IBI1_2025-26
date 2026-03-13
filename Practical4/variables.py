# 1. Define variables a/b/c for Scotland's population in 2004/2014/2024 (unit: million)
# 2. Calculate population change 2004-2014: d = b - a
# 3. Calculate population change 2014-2024: e = c - b (typo 2025 corrected to 2024)
# 4. Compare d and e to determine growth trend (accelerating/decelerating)
# 5. Define boolean variables X=True, Y=False, compute W=X or Y
# 6. Write truth table for W and add comments

a=5.08*(10**6)
 #population of scotland in 2004
b=5.33*(10**6) 
#population of scotland in 2014
c=5.55*(10**6) 
#population of scotland in 2024
d=b-a
#population growth from 2004 to 2014
e=c-b 
#population growth from 2014 to 2024

#Print the population changes
print(f"Population change 2004-2014 (d) = {d:.2f} million")
print(f"Population change 2014-2024 (e) = {e:.2f} million")
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