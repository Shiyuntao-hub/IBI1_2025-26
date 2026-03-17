import matplotlib.pyplot as plt
import numpy as np
#Heart rate datas
Heart_rate = [72,60,126,85,90,59,76,131,88,121,64]  

#Basic statistics
total=len(Heart_rate)
mean_heart_rate = np.mean(Heart_rate)
print(f"Total patients: {total}")
print(f"Mean heart rate: {mean_heart_rate:.1f} bpm")

#Category statistics
low=0
normal=0   
high=0

for rate in Heart_rate:
    if rate < 60:
        low += 1
    elif 60 <= rate <= 120:
        normal += 1
    else:
        high += 1
print(f"Low heart rate (<60 bpm): {low} patients")
print(f"Normal heart rate (60-120 bpm): {normal} patients")
print(f"High heart rate (>120 bpm): {high} patients")

#Find the max category
categories = {'Low': low, 'Normal': normal, 'High': high}
Largest = max(categories, key=categories.get)
print(f"\nLargest category: {Largest}")

#Draw a pie chart to visualize the heart rate distribution
plt.figure(figsize=(8, 8))
labels = ["Low (<60 bpm)", "Normal (60-120 bpm)", "High (>120 bpm)"]
sizes = [low, normal, high]
colors = ["lightblue", "lightgreen", "salmon"]
plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%")
plt.title("Heart Rate Distribution of Patients")
plt.axis("equal")  # Equal aspect ratio ensures that pie chart is circular
plt.show()
