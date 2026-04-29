import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.path import Path

# ---------- NACA Generator ----------
def generate_naca(user_input, n_points=200):
    m = float(user_input[0]) / 100.0
    p = float(user_input[1]) / 10
    t = float(user_input[2:]) / 100.0

    x = np.linspace(0, 1, n_points)
    yt = 5 * t * (0.2969 * np.sqrt(x)
                 - 0.1260 * x
                 - 0.3516 * x**2
                 + 0.2843 * x**3
                 - 0.1015 * x**4)

    yc = np.zeros_like(x)
    for i in range(len(x)):
        if x[i] < p:
            yc[i] = (m / p**2) * (2*p*x[i] - x[i]**2)
        else:
            yc[i] = (m / (1 - p)**2) * ((1 - 2*p) + 2*p*x[i] - x[i]**2)

    xu = x
    yu = yc + yt
    xl = x
    yl = yc - yt
    return xu, yu, xl, yl

# ---------- Generate Airfoil ----------
xu, yu, xl, yl = generate_naca("2412")

# Apply small angle of attack (rotate airfoil by 5°)
alpha = np.deg2rad(-20)
xu_rot = xu*np.cos(alpha) - yu*np.sin(alpha)
yu_rot = xu*np.sin(alpha) + yu*np.cos(alpha)
xl_rot = xl*np.cos(alpha) - yl*np.sin(alpha)
yl_rot = xl*np.sin(alpha) + yl*np.cos(alpha)

# ---------- Flow Grid ----------
x = np.linspace(-1, 2, 300)
y = np.linspace(-1, 1, 200)
X, Y = np.meshgrid(x, y)

# ---------- Uniform Flow ----------
U = 140.0  # test speed in m/s
u = U * np.ones_like(X)
v = np.zeros_like(Y)

# ---------- Controlled Circulation ----------
Gamma = -1.5
x0, y0 = 0.25, 0.0
r2 = (X - x0)**2 + (Y - y0)**2 + 1e-3
u += -Gamma * (Y - y0) / (2 * np.pi * r2)
v +=  Gamma * (X - x0) / (2 * np.pi * r2)

# ---------- Velocity Magnitude & Cp ----------
V = np.sqrt(u**2 + v**2)
Cp = 1 - (V / U)**2

# ---------- Mask Airfoil ----------
airfoil_x = np.concatenate([xu_rot, xl_rot[::-1]])
airfoil_y = np.concatenate([yu_rot, yl_rot[::-1]])
airfoil_path = Path(np.vstack((airfoil_x, airfoil_y)).T)
points = np.vstack((X.flatten(), Y.flatten())).T
mask = airfoil_path.contains_points(points).reshape(X.shape)
Cp[mask] = np.nan
u[mask] = np.nan
v[mask] = np.nan

# ---------- Animate Streamlines with Cp ----------
fig, ax = plt.subplots(figsize=(10,5))
seed_y = np.linspace(-0.8, 0.8, 25)
seed_x = -1 * np.ones_like(seed_y)

def update(frame):
    ax.clear()
    # Cp background
    cp_plot = ax.contourf(X, Y, Cp, levels=50, cmap='coolwarm')
    # moving seeds
    seeds = np.array([seed_x + 0.01*frame, seed_y]).T
    ax.streamplot(X, Y, u, v, start_points=seeds,
                  density=2.5, linewidth=1, arrowsize=1.2, color='black')
    # airfoil outline
    ax.plot(xu_rot, yu_rot, 'k')
    ax.plot(xl_rot, yl_rot, 'k')
    ax.set_xlim(-1, 2)
    ax.set_ylim(-1, 1)
    ax.set_title("Animated Streamlines + Cp Around NACA 2412")
    return cp_plot

ani = animation.FuncAnimation(fig, update, frames=200, interval=30)
plt.show()

