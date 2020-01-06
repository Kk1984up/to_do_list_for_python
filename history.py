ax1.plot(time,encoder,'r--',time,encoder1,'bo',time,encoder2,'y^')
ax1.set(xlabel='time(min)',ylabel='encoder(counts)',title='1.8pump')
fig1.savefig('d:python/1.8代泵基础量精度误差.jpg')
fig2,ax2=plt.subplots(122)
ax2.bar(sn,infusion_error)
fig2.savefig('d:python/infusion_error.jpg')
plt.show()
runfile('C:/Users/libozhang/.spyder-py3/Simple Plot.py', wdir='C:/Users/libozhang/.spyder-py3')
runfile('C:/Users/libozhang/.spyder-py3/plt_Guide.py', wdir='C:/Users/libozhang/.spyder-py3')
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import numpy as np

plt.figure(figsize=(8, 3))
ax1 = plt.subplot(131)
ax1.imshow([[1, 2], [2, 3]])
txt = ax1.annotate("test", (1., 1.), (0., 0),
                   arrowprops=dict(arrowstyle="->",
                                   connectionstyle="angle3", lw=2),
                   size=20, ha="center",
                   path_effects=[PathEffects.withStroke(linewidth=3,
                                                        foreground="w")])
txt.arrow_patch.set_path_effects([
    PathEffects.Stroke(linewidth=5, foreground="w"),
    PathEffects.Normal()])

pe = [PathEffects.withStroke(linewidth=3,
                             foreground="w")]
ax1.grid(True, linestyle="-", path_effects=pe)

ax2 = plt.subplot(132)
arr = np.arange(25).reshape((5, 5))
ax2.imshow(arr)
cntr = ax2.contour(arr, colors="k")

plt.setp(cntr.collections, path_effects=[
    PathEffects.withStroke(linewidth=3, foreground="w")])

clbls = ax2.clabel(cntr, fmt="%2.0f", use_clabeltext=True)
plt.setp(clbls, path_effects=[
    PathEffects.withStroke(linewidth=3, foreground="w")])

# shadow as a path effect
ax3 = plt.subplot(133)
p1, = ax3.plot([0, 1], [0, 1])
leg = ax3.legend([p1], ["Line 1"], fancybox=True, loc='upper left')
leg.legendPatch.set_path_effects([PathEffects.withSimplePatchShadow()])

plt.show()
runfile('C:/Users/libozhang/.spyder-py3/plt_Guide.py', wdir='C:/Users/libozhang/.spyder-py3')

## ---(Wed Oct 30 08:35:47 2019)---
runfile('C:/Users/libozhang/.spyder-py3/plt_Guide.py', wdir='C:/Users/libozhang/.spyder-py3')
runfile('C:/Users/libozhang/.spyder-py3/Simple Plot.py', wdir='C:/Users/libozhang/.spyder-py3')
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# sphinx_gallery_thumbnail_number = 2

vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
              "potato", "wheat", "barley"]
farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
           "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]

harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])


fig, ax = plt.subplots()
im = ax.imshow(harvest)

# We want to show all ticks...
ax.set_xticks(np.arange(len(farmers)))
ax.set_yticks(np.arange(len(vegetables)))
# ... and label them with the respective list entries
ax.set_xticklabels(farmers)
ax.set_yticklabels(vegetables)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(vegetables)):
    for j in range(len(farmers)):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="w")


ax.set_title("Harvest of local farmers (in tons/year)")
fig.tight_layout()
plt.show()
runfile('C:/Users/libozhang/.spyder-py3/numpy_some.test.py', wdir='C:/Users/libozhang/.spyder-py3')

## ---(Wed Oct 30 14:54:14 2019)---
runfile('C:/Users/libozhang/.spyder-py3/Simple Plot.py', wdir='C:/Users/libozhang/.spyder-py3')