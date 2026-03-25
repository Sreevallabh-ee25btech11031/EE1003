import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline

# 1. Input the data points
x = np.array([-2, -1, 0, 1, 2, 3])
y = np.array([-58, -21, -12, -13, -6, 27])

#Finding the polynomial using lagrange's method
poly_lagrange = lagrange(x, y)

final_coeffs = [c for c in poly_lagrange.coeffs if abs(c) > 1e-10] #microscopic values introduced in place of 0 while computation. This removes them. 

#getting the curve with the final coeffs only; removing the noise

clean_poly = np.poly1d(final_coeffs)
true_degree = clean_poly.order

#Using Cubic Splines
poly_spline = CubicSpline(x,y)


x_smooth = np.linspace(-3, 4, 100) 

plt.plot(x_smooth, clean_poly(x_smooth), color='blue', linewidth=3, alpha=0.5, 
         label=f'Lagrange')

plt.plot(x_smooth, poly_spline(x_smooth), color='orange', linestyle='--', linewidth=2, 
         label='Cubic Spline')

# Plot the original data points on top
plt.scatter(x, y, color='red', s=50, zorder=5, label='Data Points')

# Formatting the Graph
#plt.title('Lagrange vs. Cubic Spline Interpolation')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.8) # Draws the x-axis
plt.axvline(0, color='black', linewidth=0.8) # Draws the y-axis
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()

# Display the graph
plt.savefig("../Figs/plot.png")
plt.show()

