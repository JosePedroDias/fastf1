import csv
import numpy as np
import matplotlib.pyplot as plt

# https://matplotlib.org/stable/gallery/mplot3d/index.html

ax = plt.figure().add_subplot(projection='3d')

SKIP_N = 10000
SCALE = 0.1
X = []
Y = []
Z = []
with open('2022_20_quali_pos_1.csv', newline='') as f:
    reader = csv.reader(f)
    next(reader)
    for i in range(SKIP_N):
        next(reader)
    for row in reader:
        [_, x, y, z] = map(lambda v: SCALE * float(v), row) 
        X.append(x)
        Y.append(y)
        Z.append(z)

lim_x = [min(X), max(X)]
lim_y = [min(Y), max(Y)]
lim_z = [min(Z), max(Z)]

avg_x = 0.5 * (lim_x[0] + lim_x[1])
avg_y = 0.5 * (lim_y[0] + lim_y[1])
avg_z = 0.5 * (lim_z[0] + lim_z[1])

X = list( map(lambda x: x - avg_x, X) )
Y = list( map(lambda x: x - avg_y, Y) )
Z = list( map(lambda x: x - avg_z, Z) )

lim_x = [min(X), max(X)]
lim_y = [min(Y), max(Y)]
lim_z = [min(Z), max(Z)]

print('DX', lim_x[1] - lim_x[0])
print('DY', lim_y[1] - lim_y[0])
print('DZ', lim_z[1] - lim_z[0])

lim = [
    min([ lim_x[0], lim_y[0], lim_z[0] ]),
    max([ lim_x[1], lim_y[1], lim_z[1] ])
]

z_min = lim_z[0] - 50

#xx, yy = np.meshgrid(range(10), range(10))
#ax.plot_surface(xx, yy, z_min, alpha=0.2)

ax.plot(X, Y, zs=z_min, c='#AAAAAA', label='shadow')
ax.plot(X, Y, Z, c='r', label='trajectory')


# Make legend, set axes limits and labels
ax.set_xlim(lim[0], lim[1])
ax.set_ylim(lim[0], lim[1])
ax.set_zlim(lim[0], lim[1])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Customize the view angle so it's easier to see that the scatter points lie
# on the plane y=0
#ax.view_init(elev=20., azim=-35, roll=0)

plt.savefig('circuit.pdf', dpi=300)
plt.show()
