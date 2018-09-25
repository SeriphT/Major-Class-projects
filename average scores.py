import math

def Average(lst): 
    return sum(lst) / len(lst) 
  
# scores of tests 
scores = [78, 56, 29, 90,100,67,34]
average = Average(scores) 
  
# Printing average of the list 
print("Average of the list =", round(average, 2))




