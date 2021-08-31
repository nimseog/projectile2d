import numpy as np
import matplotlib.pyplot as plt

def calculate_path(v0_mag, v0_ang):
    u0 = np.array([0., 0.])
    g = 9.81
    a = np.array([0, -g])
    v0_ang_rad = np.radians(v0_ang)
    v0 = v0_mag * np.array([np.cos(v0_ang_rad), np.sin(v0_ang_rad)])
    t_end = -2 * v0[1] / a[1]
    t = np.linspace(0., t_end, 300)
    u = v0[:,np.newaxis] * t[np.newaxis,:] + 0.5 * a[:,np.newaxis] * (t**2)[np.newaxis,:]
    return u

v0_mags_angs = np.array([
[12., 45.],
[12., 30.],
[12., 77.],
[12., 26.],
[12., 58.],
[12., 88.],
[12., 12.]
])

umaxs = [] 
for v0_pair in v0_mags_angs:
    u = calculate_path(v0_pair[0], v0_pair[1])
    umaxs.append(np.max(u))
    plt.plot(u[0], u[1], label='v0=%g, ang=%g' % (v0_pair[0], v0_pair[1]))

umax = max(umaxs)
plt.xlim(0., umax)
plt.ylim(0., umax)
plt.legend()
plt.show()