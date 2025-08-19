import numpy as np
import matplotlib.pyplot as plt

# پارامترها
hbar = 1
m = 1
V0 = 0.6
a = 1.0  # پهنای سد
E = 0.4  # انرژی انتخابی (کمتر از سد)

x = np.linspace(-3, 3, 1000)

# عدد موج در مناطق مختلف
k = np.sqrt(2*m*E)/hbar
kappa = np.sqrt(2*m*(V0 - E))/hbar

# موج‌ها (ایده‌آل: فقط برای دید ساده)
psi = np.piecewise(
    x,
    [x < -a/2, (x >= -a/2) & (x <= a/2), x > a/2],
    [
        lambda x: np.cos(k*(x+1.5)),                  # چپ
        lambda x: np.exp(-kappa*(x+a/2)),             # داخل سد (کاهشی)
        lambda x: 0.3*np.cos(k*(x-1.5))               # راست (خروج ضعیف)
    ]
)

# رسم
plt.figure(figsize=(8,5))
plt.plot(x, psi**2, 'b', label=r"$|\psi(x)|^2$")
plt.axvspan(-a/2, a/2, color='red', alpha=0.2, label="سد پتانسیل")
plt.axhline(0, color='black', lw=0.5)
plt.title(f"تونل‌زنی برای E = {E} < V0 = {V0}")
plt.xlabel("x")
plt.ylabel(r"$|\psi(x)|^2$")
plt.legend()
plt.grid()
plt.show()
plt.savefig("fig.png")