import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rv_continuous
import sympy as sp

#Using SymPy to get the functions
x_sym = sp.Symbol('x')
t = sp.Symbol('t')

pdf_expr = sp.Rational(3, 14) * (5*x_sym - 2*x_sym**2)
cdf_expr = sp.integrate(pdf_expr.subs(x_sym, t), (t, 0, x_sym))

# Convert to fast numerical functions
pdf_num = sp.lambdify(x_sym, pdf_expr, 'numpy')
cdf_num = sp.lambdify(x_sym, cdf_expr, 'numpy')

#SciPy
class CustomDist(rv_continuous):
    def _pdf(self, x):
        return pdf_num(x)
    
    def _cdf(self, x):
        return cdf_num(x)

my_dist = CustomDist(a=0, b=2, name='fully_automated')
x_vals = np.linspace(-0.5, 3, 500)
x_shade = np.linspace(1, 2, 100)

#Plotting pdf
plt.plot(x_vals, my_dist.pdf(x_vals), color='blue', lw=2, label='$f(x)$')
plt.fill_between(x_shade, my_dist.pdf(x_shade), color='skyblue', alpha=0.5, label='P(X > 1)')
plt.axvline(1, color='red', linestyle='--', alpha=0.5)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("../Figs/pdf.png")
plt.show()

#Plotting CDF for verification
plt.plot(x_vals, my_dist.cdf(x_vals), color='green', lw=2, label='CDF')

p_le_1 = my_dist.cdf(1)
plt.scatter([1], [p_le_1], color='red', zorder=5)

plt.annotate(f'P(X \u2264 1) = {p_le_1:.4f}\n(11/28)', 
             (1, p_le_1), textcoords="offset points", xytext=(-40,15), ha='center',
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", lw=1))

plt.axvline(1, color='red', linestyle='--', alpha=0.5)
plt.axhline(p_le_1, color='red', linestyle='--', alpha=0.5)

plt.xlabel('x')
plt.ylabel('F(x)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("../Figs/cdf.png")
plt.show()