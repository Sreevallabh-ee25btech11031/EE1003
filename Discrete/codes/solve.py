import numpy as np

#x values equally spaced, so not necessary during computation
y = np.array([-58, -21, -12, -13, -6, 27])

# Loop through possible degrees (from 1 up to the number of data points)
for n in range(1, len(y)):
    
    # Calculate the n-th difference
    current_diff = np.diff(y, n=n)
    print(f"{n} - Difference: {current_diff}")
    
    # np.all() checks if every element equals the very first element
    if np.all(current_diff == current_diff[0]):
        print(f"The smallest degree of the polynomial is: {n}")
        break