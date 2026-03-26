import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

Vin = 5.0
R = 1000.0
L = 0.01
T = L/R #Time constant

t_int = np.linspace(0, 5*T, 1000)

t = sp.symbols('t')
i = sp.Function('i')(t)
s = sp.symbols('s')

#Inputting the differential equation
de = sp.Eq(L*(sp.diff(i, t)) + R*i , Vin)

#Converting the equation to Laplace Transform
l_lhs = sp.laplace_transform(de.lhs, t, s, noconds = True)
l_rhs = sp.laplace_transform(de.rhs, t, s, noconds = True)

l_eq = sp.Eq(l_lhs, l_rhs)

#Initial Conditions for solving
initial_conditions = {i.subs(t, 0): 0}
l_eq_subbed = l_eq.subs(initial_conditions)

#Solving the s-domain equation
I_s = sp.laplace_transform(i, t, s, noconds=True)
I_s_solution = sp.solve(l_eq_subbed, I_s)[0]

# sp.pprint(I_s_solution)

#Getting the time-domain solution
i_t_sp = sp.inverse_laplace_transform(I_s_solution, s, t)

i_t = sp.lambdify(t, i_t_sp, modules=['numpy'])
i_vals = i_t(t_int)

Vr = R*i_vals
Vl = Vin - Vr

plt.plot(t_int, Vr, color = 'red', label = "Ch1")
plt.plot(t_int, -Vl, color = 'blue', label = "Ch2")
plt.axhline(y=5.0, color='gray', linestyle='--')

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
plt.legend(loc='best')

plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.6', color='gray')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray')


plt.savefig("../Figs/laplace.png")
plt.show()


