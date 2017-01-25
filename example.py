import kthcolors.kthcolors as ktc
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
_SIZE = 1e3
_NUM = int(np.sqrt(len(ktc.kthcolors)))
_counter = 0

for color in ktc.kthcolors.keys():
    plt.scatter(_counter%_NUM, _counter//_NUM, color=color, label=color, s=_SIZE)
    _counter += 1
plt.gca().legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
plt.grid(True)
plt.ylim((-1.0,2*_NUM))
plt.savefig('example.png')
plt.show()
